import random
from unittest.mock import DEFAULT

commands = [
    {
        "keywords":  [
            "hola",
            "hola!",
            "ola",
            "ole",
            "buenos días",
            "buenos dias"
            "buenas tardes",
            "buenas noches",
            "me dieron este número",
            "me dieron este numero",
            "venden a crédito",
            "quisiera saber si venden",
            "necesito saber",
            "buen día",
            "buen dia",
        ],
        "key": "CMD_KEY_1"
    },
]

responses = {
    "DEFAULT":{
        "response":"No te entiendo",
        "media":None,
        "trigger":None
    },
    "CMD_KEY_1":{
        "response":"Hola! soy WABOTie un CHATBOT de Whatsapp 🤖, \nlo primero que necesitas saber es que estoy en desarrollo, \npor lo tanto no puedo responderte mucho aún. \nPero si quieres saber que puedo hacer, pon **comados**",
        "media":None,
        "trigger":None,
    }
}

def get_response(cmd):
    cmd_key = get_cmd_key(cmd)
    if cmd_key in responses:
        response = responses[cmd_key]['response']
    else:
        response = responses['DEFAULT']['response']
    return response
    
def get_cmd_key(cmd):
    for i in commands:
        for j in i['keywords']:
            if cmd in j:
                return i['key']