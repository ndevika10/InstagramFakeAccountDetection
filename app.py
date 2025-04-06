from flask import Flask, render_template, request
import pickle
import numpy as np
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Load trained model and scaler
with open("xgboost_model.pkl", "rb") as f:
    xgb_model, scaler = pickle.load(f)

def get_instagram_profile_info(username):
    url = f'https://www.instagram.com/{username}/'
    response = requests.get(url)

    if response.status_code != 200:
        return {"exists": False}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract profile picture
    profile_pic = soup.find('meta', property='og:image')
    profile_pic_url = profile_pic['content'] if profile_pic else None

    # Extract bio information
    bio_meta = soup.find('meta', property='og:description')
    bio = bio_meta['content'].split('-')[0].strip() if bio_meta else None

    if not bio:
        return {"exists": False}  # No bio means invalid username

    return {
        "exists": True,
        "profile_picture": profile_pic_url,
        "bio": bio
    }

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", result=None)

@app.route("/check_profile", methods=["POST"])
def check_profile():
    username = request.form.get("username", "").strip()
    result = get_instagram_profile_info(username) if username else {"exists": False}

    return render_template("index.html", result=result, username=username)

@app.route("/analyze", methods=["POST"])
def analyze():
    username = request.form.get("username", "")
    profile_picture = request.form.get("profile_picture", "")

    return render_template("analyze.html", username=username, profile_picture=profile_picture)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        username = request.form.get("username", "")
        nmedia = int(request.form.get("nmedia", 0))
        nfollower = int(request.form.get("nfollower", 0))
        nfollowing = int(request.form.get("nfollowing", 0))
        pic = int(request.form.get("pic", 0))  # 1 = Yes, 0 = No

        # Additional features from form
        followrel = request.form.get("followrel", "")
        acHighlight = request.form.get("acHighlight", "")
        avgtime = request.form.get("avgtime", "")
        newTag = request.form.get("newTag", "")

        # Prepare data for XGBoost prediction
        input_features = np.array([[nmedia, nfollower, nfollowing, pic]])
        input_features = scaler.transform(input_features)  # Normalize

       # Initial prediction using XGBoost
        initial_prediction = xgb_model.predict(input_features)[0]

        # Reanalysis step using predefined conditions
        if followrel == "yes" and acHighlight == "yes" and avgtime == "yes" and newTag == "no":
            final_result = "Real"
        elif followrel == "no" and acHighlight == "no" and avgtime == "no" and newTag == "no":
            final_result = "Fake"
        elif followrel == "yes" and acHighlight == "no" and avgtime == "no" and newTag == "no":
            final_result = "Fake"
        elif followrel == "no" and acHighlight == "no" and avgtime == "no" and newTag == "yes":
            final_result = "Real"
        elif followrel == "yes" and acHighlight == "no" and avgtime == "no" and newTag == "yes":
            final_result = "Real"
        else:
            final_result = "Fake"  # Default case

        return render_template("result.html", username=username, prediction=final_result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
