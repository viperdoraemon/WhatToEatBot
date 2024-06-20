from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage)

import openai
import requests

# Azure OpenAI configurations
openai.api_type = "azure"
openai.api_key = "YOUR_AZURE_API_KEY"
openai.api_base = "https://YOUR_AZURE_OPENAI_ENDPOINT"
openai.api_version = "2023-05-15"  # Example version, please check the latest version in Azure documentation

# Model deployment name in Azure
deployment_name = "text-davinci-003"

channel_secret = "xxx"
channel_access_token = "xxx"

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)

    prompt_text = text

    response = openai.Completion.create(
        engine=deployment_name,  # Use 'engine' instead of 'model'
        prompt=prompt_text,  
        max_tokens=1024
    )

    text_out = response.choices[0].text.strip()
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=text_out))

if __name__ == "__main__":          
    app.run()
