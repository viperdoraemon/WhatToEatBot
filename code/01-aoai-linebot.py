from flask import Flask, request, abort, jsonify
from flask_ngrok import run_with_ngrok
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from linebot.exceptions import (InvalidSignatureError)
from dotenv import load_dotenv

import os
import openai
import requests
import json
import logging, ngrok

load_dotenv("../.env")
line_channel_secret = os.getenv("LINE_CHANNEL_SECRET")
line_channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
ngrok_auth_token = os.getenv("NGROK_AUTH_TOKEN")

# Initialize Line Bot API and Webhook Handler with the provided tokens
line_bot_api = LineBotApi(line_channel_access_token)
handler = WebhookHandler(line_channel_secret)

# Initialize Flask app
app = Flask(__name__)
run_with_ngrok(app)

# Route for home page, handling both GET and POST methods
@app.route("/", methods=["GET", "POST"])
def home():
    try:
        # Get the X-Line-Signature header value
        signature = request.headers["X-Line-Signature"]
        
        # Get request body as text
        body = request.get_data(as_text=True)
        
        # Handle the request with the Line webhook handler
        handler.handle(body, signature)
    except Exception as e:
        # Print any errors that occur
        print(f"Error: {e}")
    
    return "Hello Line Chatbot"

# Handler for receiving text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # Get the text from the message
    text = event.message.text
    print(text)

    # Set the prompt for the GPT model
    prompt_text = text

    # Get the response from the OpenAI GPT model
    response = openai.Completion.create(
        engine=azure_openai_deployment_name,  # Use 'engine' instead of 'model'
        prompt=prompt_text,  
        max_tokens=1024
    )

    # Extract the text from the response
    text_out = response.choices[0].text.strip()
    
    # Reply to the user with the generated text
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

if __name__ == "__main__":
    # Run the Flask app
    app.run()