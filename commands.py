def get_response(cmd):
    cmd_key = get_cmd_key(cmd)
    if cmd_key in responses:
        response = responses[cmd_key]
    else:
        response = responses['DEFAULT']
    return response
    
def get_cmd_key(cmd):
    for i in commands:
        for j in i['keywords']:
            if j in cmd:
                return i['key']
            
def get_cmds():
    cmds = []
    for i in commands:
        string = f"\n • ```{i['keywords'][0]}```"
        cmds.append(string)
    return ' '.join(cmds)

commands = [
    {
        'keywords':  [
            'hola',
            'hola!',
            'ola',
            'buenas',
            'buen día',
            'buen dia',
            'buenos días',
            'buenos dias'
            'buenas tardes',
            'buenas noches',
            'quisiera saber si venden',
            'me dieron este número',
            'me dieron este numero'
        ],
        'key': 'CMD_KEY_1'
    },
    {
        'keywords':  [
            'comandos',
            'commands',
            'cmds',
            'comando',
        ],
        'key': 'CMD_KEY_2'
    },
    {
        'keywords':  [
            'creador',
            'creator',
        ],
        'key': 'CMD_KEY_3'
    },
]

responses = {
    'DEFAULT':{
        'response':'No te entiendo',
        'type':'text',
        'media':None,
        'trigger':None
    },
    'CMD_KEY_1':{
        'response':'Hola! soy WABOTie un CHATBOT de Whatsapp 🤖 \nlo primero que necesitas saber es que estoy en desarrollo, por lo tanto no puedo responderte mucho aún. \nPero si quieres saber que puedo hacer, pon *comados*',
        'type':'text',
        'media':None,
        'trigger':None,
    },
    'CMD_KEY_2':{
        'response':f'Esta es mi lista de comandos:{get_cmds()}',
        'type':'text',
        'media':None,
        'trigger':None,
    },
    'CMD_KEY_3':{
        'response':'Mi creador es FelipeGCx\naquí tienes su github:',
        'type':'url',
        'media':'https://github.com/FelipeGCx',
        'trigger':None,
    },
}
    
    