                                                                                   			 AI Customer Support Bot
                                                                                       (for a e-commerce website)
This project is a functional simulation of an AI-powered customer support chatbot. 
It is designed to handle frequently asked questions, maintain conversational context, and intelligently escalate issues to a human agent when necessary.
The application is built with a Python Flask backend, a simple vanilla JavaScript frontend, and integrates with an LLM (in this case, via the OpenAI API) for generating intelligent responses.

===>>>Features :

    LLM-Powered Responses: Utilizes a Large Language Model to understand user intent and provide natural-sounding answers.

    Contextual Memory: Tracks conversation history for each session to answer follow-up questions accurately.

    FAQ-Based Knowledge: The bot's knowledge is strictly limited to a provided faqs.txt file to prevent hallucination and ensure factual accuracy.

    Escalation to Human Agent: Recognizes when a user wants to speak to a person and simulates an escalation, complete with a conversation summary for the agent.

    REST API Backend: A clean backend with endpoints for session management and chat interaction.

===>>>Tech Stack

    Backend: Python, Flask

    LLM: OpenAI API (gpt-3.5-turbo)

    Database: SQLite for session and message storage

    Frontend: HTML, CSS, JavaScript (via index.html)

===>>>Setup and Installation

Follow these steps to run the project locally.

1. Clone the Repository

git clone https://github.com/your-username/ai-customer-support-bot.git
cd ai-customer-support-bot

2. Create and Activate a Virtual Environment

On Windows:
python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies
Create a requirements.txt file and install the necessary packages.
pip install Flask openai python-dotenv
pip freeze > requirements.txt

4. Create the .env File
Create a file named .env in the root of the project and add your Gemini API key:
GEMINI_API_KEY='sk-YourSecretKeyGoesHere'

5. Run the Application
python app.py
