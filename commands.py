import code


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
        string = f"\n 📌 ```{i['keywords'][0]}```"
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
            'hello'
        ],
        'key': 'CMD_KEY_1'
    },
    {
        'keywords':  [
            'comandos',
            'comando',
            'cmds',
            'commands',
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
    {
        'keywords':  [
            'servicios',
            'services',
        ],
        'key': 'CMD_KEY_4'
    },
    {
        'keywords':  [
            'imagen',
            'image',
            'foto',
            'img',
        ],
        'key': 'CMD_KEY_5'
    },
    {
        'keywords':  [
            'sticker',
        ],
        'key': 'CMD_KEY_6'
    },
    {
        'keywords':  [
            'documento',
            'document',
        ],
        'key': 'CMD_KEY_7'
    },
    {
        'keywords':  [
            'audio',
        ],
        'key': 'CMD_KEY_8'
    },
    {
        'keywords':  [
            'video',
        ],
        'key': 'CMD_KEY_9'
    },
    {
        'keywords':  [
            'template',
        ],
        'key': 'CMD_KEY_10'    
    },
    {
        'keywords':  [
            'adios',
            'adiós',
            'chao',
            'hasta luego',
            'bye',
        ],
        'key': 'CMD_KEY_100'
    }
]

responses = {
    'DEFAULT':{
        'response':'No te entiendo',
        'type':'text',
        'media':None,
        'trigger':None
    },
    'CMD_KEY_1':{
        'response':'Hola! soy WABOTie un CHATBOT 🤖 de Whatsapp\nlo primero que necesitas saber es que estoy en desarrollo, por lo tanto no puedo responderte mucho aún ☹️. Pero si quieres saber que puedo hacer, escribe ⌨️ *comados*',
        'type':'text',
        'media':None,
        'trigger':None,
    },
    'CMD_KEY_2':{
        'response':f'Esta es mi lista 📝 de comandos:{get_cmds()}',
        'type':'text',
        'media':None,
        'trigger':None,
    },
    'CMD_KEY_3':{
        'response':'Mi creador es FelipeGCx\naquí tienes su github:',
        'type':'text/url',
        'media':'https://github.com/FelipeGCx',
        'trigger':None,
    },
    'CMD_KEY_4':{
        'response': {
            'title':'ELIGE UN SERVICIO',
            'content':'🤖 Elige una de las siguientes opciones:',
            'footer':'elige solo una opción',
            'buttons':[
               {
                "type": "reply",
                "reply": {
                    "id": "btn1",
                    "title": "Servicio 1",
                    }
                },
               {
                "type": "reply",
                "reply": {
                    "id": "btn2",
                    "title": "Servicio 2",
                    }
                },
            ],
        },
        'type':'buttons',
        'media':None,
        'trigger':None,
    },
    'CMD_KEY_5':{
        'response':None,
        'type':'image',
        'media':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNna-6wP9XJRHYzJbgtft0IqHcejRRxcN44XKiBRoTB-ZMBQqb08tP1itkp4ucuUCuyQA&usqp=CAU',
        'trigger':None,
    },
    'CMD_KEY_6':{
        'response':None,
        'type':'sticker',
        'media':'https://i.ibb.co/TkZfGZQ/WS202207231681038355.webp',
        'trigger':None,
    },
    'CMD_KEY_7':{
        'response':None,
        'type':'document',
        'media':'https://sigloxxieditores.com.ar/wp-content/uploads/2021/12/reimpr.-Galeano.-Los-hijos-de-los-días-baja.pdf',
        'title': 'Los hijos de los días',
        'trigger':None,
    },
    'CMD_KEY_8':{
        'response':None,
        'type':'audio',
        'media':'https://mp3teca.app/-/aac/96/100966_96.m4a',
        'trigger':None,    
    },
    'CMD_KEY_9':{
        'response':None,
        'type':'video',
        'media':'https://media.istockphoto.com/videos/technologic-earth-4k-video-id523063952',
        'trigger':None,    
    },
    'CMD_KEY_10':{
        'response':None,
        'type':'template',
        'media':None,
        'template':{
            "name": "hello_world", 
            "language":{
                "code":"en_US",
            } 
        },
        'trigger':None,    
    },
    'CMD_KEY_100':{
        'response':'Adiós! 👋 fue un gusto ayudarte 🤗',
        'type':'text',
        'media':None,
        'trigger':None,
    }
}
    
    