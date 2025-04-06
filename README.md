Abstract:
    With the rise of social media, fake accounts have become a major concern, leading to privacy threats and misinformation. 
    This project introduces an Instagram Fake Account Detection System using Machine Learning (XGBoost) and rule-based validation. 
    Profile data is extracted via web scraping (BeautifulSoup) and classified based on user activity metrics. 
    The hybrid approach enhances accuracy by combining model predictions with manual reanalysis rules. 
    A Flask-based web application enables users to check Instagram profiles in real time.

Introduction:
    The growing presence of fake Instagram accounts contributes to spam, fraud, and misinformation, making detection essential. 
    This project integrates machine learning and rule-based validation to enhance detection accuracy. 
    The system extracts profile data, analyzes engagement metrics, and applies an XGBoost model for classification. 
    The Flask web application offers an interactive way to analyze Instagram profiles in real time.
    As fake accounts become more sophisticated, traditional detection methods fall short. 
    This project’s hybrid approach leverages automated ML predictions with rule-based verification, ensuring a scalable and reliable solution. 
    By providing real-time analysis, the system enhances social media security and helps users identify fake profiles, scams, and misinformation effectively.

[image](https://github.com/user-attachments/assets/5f682c5a-9052-48e7-a487-e27d5da2dd05)

Data Preprocessing:
Clean data by handling missing values.
Select relevant features and normalize them for better model performance.

Model Training:
Initialize the XGBoost model with key parameters (like learning rate, max depth, number of trees).
Train the model using the training dataset, where each tree corrects the errors of the previous one.

Model Evaluation:
Evaluate the model's performance using metrics like accuracy and precision.
Make predictions on test data to assess how well the model generalizes.

Hyperparameter Tuning:
Optimize the model's parameters (e.g., learning rate, tree depth) for better accuracy.
Use techniques like grid search to find the best hyperparameters.

Prediction and Post-Processing:
Use the trained model to make predictions.
Apply any additional rules for final decision-making (e.g., verifying the account's authenticity).

Implementing WebScrapping:
    I used BeautifulSoup for web scraping to retrieve Instagram profile details such as the profile picture, number of posts, number of followers, and number of followings because it allows easy extraction of structured data from web pages. 
    BeautifulSoup efficiently parses HTML and XML documents, helping me locate and extract the required data from Instagram's profile page. 
    This approach is useful when an API is unavailable or has restrictions, making web scraping a valuable alternative for gathering public profile information.


       







