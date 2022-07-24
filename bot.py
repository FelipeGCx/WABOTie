import requests
import json
import os
from commands import get_response
from dotenv import load_dotenv
load_dotenv()

class ChatBot:
    
    def proccess_message(self,sender_phone,message,data):
        response = get_response(message.lower())
        if response['type'] == 'text':
            self.send_message_text(sender_phone,response['response'])
        if response['type'] == 'url':
            self.send_message_text(sender_phone,response['response'])
            if response['media'] != None:
                self.send_message_url(sender_phone,response['media'])
        if response['type'] == 'buttons':
            self.send_message_buttons(sender_phone,response['response'])
        self.send_message_text(sender_phone, str(data))
        # in this point, you can send the message and response to your API and save the conversation in a database
            
    
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
        
    def send_message_url(self,sender_phone,message):
        data = {
            "messaging_product": "whatsapp",
            "preview_url": True,
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
        
    def send_message_buttons(self,sender_phone,message):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "interactive",  
            "interactive": {
                    "type": "button",
                    "header": {
                    "type": "text",
                    "text": message['title']
                    },
                    "body": {
                    "text": message['content']
                    },
                    "footer": {
                    "text": message['footer']
                    },
                    "action": {
                    "buttons": message['buttons']
                    }
                }
            }
        data = json.dumps(data)
        url = f'https://graph.facebook.com/{os.getenv("API_VERSION")}/{os.getenv("FROM_PHONE_NUMBER_ID")}/messages'
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}
        response = requests.post(url=url, data=data, headers=headers,)
        print(response.text)
        