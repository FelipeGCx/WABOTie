import requests
import json
import os
from commands import get_response
from dotenv import load_dotenv
load_dotenv()

class ChatBot:
    
    def proccess_message(self,sender_phone,message):
        response = get_response(message.lower())
        if response['type'] == 'text':
            self.send_message_text(sender_phone,response['response'])
        if response['type'] == 'url':
            self.send_message_text(sender_phone,response['response'])
            if response['media'] != None:
                self.send_message_text(sender_phone,response['media'])
            
    
    def send_message_text(self,sender_phone,message):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "text",
            "text":{
                "body": message
            }
            }
        data = json.dumps(data)
        url = f'https://graph.facebook.com/{os.getenv("API_VERSION")}/{os.getenv("FROM_PHONE_NUMBER_ID")}/messages'
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}
        response = requests.post(url=url, data=data, headers=headers,)
        print(response.text)
        
