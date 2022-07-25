from dataclasses import dataclass
from urllib import response
import requests
import json
import os
from commands import get_response
from dotenv import load_dotenv
load_dotenv()

class ChatBot:
    def __init__(self):
        global URL, HEADERS
        # set the URL and HEADERS constants
        URL = f'https://graph.facebook.com/{os.getenv("API_VERSION")}/{os.getenv("FROM_PHONE_NUMBER_ID")}/messages'
        HEADERS = {'Content-Type': 'application/json', 'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}
    
    def proccess_message(self,sender_phone,message,data):
        response = get_response(message.lower())
        # self.mark_as_read(data['messages'][0]['id'])
        # to type text
        if response['type'] == 'text':
            self.send_message_text(sender_phone,response['response'])
        # to type text with url
        if response['type'] == 'text/url':
            self.send_message_text(sender_phone,response['response'])
            if response['media'] != None:
                self.send_message_url(sender_phone,response['media'])
        # to type url, this send only a url message
        if response['type'] == 'url':
            if response['media'] != None:
                self.send_message_url(sender_phone,response['media'])
        # to type buttons
        if response['type'] == 'buttons':
            self.send_message_buttons(sender_phone,response['response'])
        # to type text with image
        if response['type'] == 'text/image':
            self.send_message_text(sender_phone,response['response'])
            if response['media'] != None:
                self.send_message_image(sender_phone,response['media'])
        # to type image in url
        if response['type'] == 'image':
            if response['media'] != None:
                self.send_message_image(sender_phone,response['media'])
        if response['type'] == 'sticker':
            if response['media'] != None:
                self.send_message_sticker(sender_phone,response['media'])
        if response['type'] == 'document':
            if response['media'] != None:
                self.send_message_document(sender_phone,response['media'],response['title'])
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
        response = requests.post(url=URL,headers=HEADERS, data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def send_message_url(self,sender_phone,message):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "text",
            "text":{
                "preview_url": True,
                "body": message
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
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
        response = requests.post(url=URL, headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def send_message_image(self,sender_phone,media):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "image",
            "image":{
                "link": media
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)

    def send_message_audio(self,sender_phone,media):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "audio",
            "audio":{
                "link": media
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def send_message_video(self,sender_phone,media):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "video",
            "video":{
                "link": media
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def send_message_document(self,sender_phone,media,title):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "document",
            "document":{
                "link": media,
                "filename": title,
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def send_message_sticker(self,sender_phone,media):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "sticker",
            "sticker":{
                "link": media
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def send_message_template(self,sender_phone,media):
        data = {
            "messaging_product": "whatsapp",
            "to": sender_phone,
            "type": "image",
            "image":{
                "link": media
            }
            }
        data = json.dumps(data)
        response = requests.post(url=URL,headers=HEADERS,data=data)
        # here you can send the content of response.text to your API and track logs
        print(response.text)
        
    def mark_as_read(self,id):
        data = {
            "status": "read",
        }
        data = json.dumps(data)
        response = requests.put(url=f'{URL}/{id}',headers=HEADERS,data=data)
        self.send_message_text('573023521590',response.text)
        
    def proccess_response_btn(self,data):
        self.send_message_text('573023521590',str(data))