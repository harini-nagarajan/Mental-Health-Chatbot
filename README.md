## Mental Health Chatbot

## Introduction
The Mental Health Chatbot is an intelligent conversational agent designed to provide mental health support and guidance to users. It leverages deep learning techniques to understand user queries and generate contextually relevant responses, aiming to assist individuals dealing with various mental health issues.

## Features
- **Data-driven Responses**: Utilizes a vast dataset of mental health topics and user conversations to provide accurate and empathetic responses.
- **LSTM Model**: Implements a Long Short-Term Memory (LSTM) neural network for sequence prediction and context understanding.
- **Student-Focused Topics**: Includes a specialized dataset focusing on mental health issues faced by students, addressing topics such as academic pressure, loneliness, and exam stress.
- **Voice Input**: Supports voice input for user queries, enhancing accessibility and user experience.
- **Meditation Audio**: Provides a meditation audio track within the chatbot interface to promote relaxation and stress relief.
- **Web-Based Interface**: Deployed as a web application using Flask, HTML, and CSS, allowing users to access the chatbot from any device with a web browser.

## Technologies Used
- Python
- Flask
- TensorFlow/Keras
- HTML/CSS
- JavaScript
- Render (for cloud deployment)

## Installation and Setup
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your_username/mental-health-chatbot.git
   ```
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application locally:
   ``'
   python app.py
   ```
4. Access the chatbot interface in your web browser at `http://localhost:5000`.

## Usage
- Enter your message in the chat input field and press "Send" to receive a response from the chatbot.
- Click on the "Meditation Audio" button to listen to a meditation track for relaxation.
- Alternatively, use voice input by clicking on the microphone icon and speaking your query.

## Deployment
The chatbot can be deployed on a cloud platform such as Render for public access. Follow the deployment instructions in the `deployment` part given below for detailed steps.

# Deployment Instructions

## Deploying the Mental Health Chatbot on Render

### Step 1: Create a Render Account
1. Sign up for a Render account at [https://render.com](https://render.com).
2. Follow the instructions to set up your account and create a new Render project.

### Step 2: Configure the Environment
1. Navigate to your Render dashboard and create a new web service.
2. Configure the web service settings, including the repository URL (e.g., GitHub repository), deployment branch, environment variables, etc.
3. Specify the build command (`python app.py`) and the start command (`python app.py` or `gunicorn -b :$PORT app:app`) in the Render dashboard.

### Step 3: Deploy the Application
1. Connect your GitHub repository to Render or manually upload your project files.
2. Trigger a deployment by pushing changes to the deployment branch or manually initiating a deploy in the Render dashboard.
3. Monitor the deployment process and wait for the application to be deployed successfully.

### Step 4: Access the Deployed Chatbot
1. Once the deployment is complete, access your deployed chatbot application using the provided URL from Render.
2. Test the chatbot functionality, including message input, voice input, and meditation audio playback.
3. Ensure that the chatbot is working as expected in the deployed environment.

## Additional Deployment Options
- You can also deploy the chatbot application on other cloud platforms like Heroku, AWS, or Google Cloud Platform by following their respective deployment guides and configurations.
- Customize the deployment settings as per your requirements, such as scaling options, domain settings, SSL certificates, etc.
----
## Future Enhancements
- Implement sentiment analysis to better understand user emotions and provide personalized responses.
- Integrate natural language processing (NLP) techniques for improved conversation flow and comprehension.
- Enhance the user interface with more interactive elements and accessibility features.
- Expand the dataset to include a wider range of mental health topics and user scenarios.

## Contributors
- Harini K N (@harini-nagarajan - https://github.com/harini-nagarajan)
- Dhanalakshmi G (@Dhanalakshmi2003 - https://github.com/Dhanalakshmi2003)
---

