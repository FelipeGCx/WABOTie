
import random


commands = {
    'hola':{
        'responses':{
            '01':'Hola, ¿en qué puedo ayudarte?',
            '02':'Hola!, ¿en qué puedo ayudarte?',
            '03':'Buen dia, ¿en qué puedo ayudarte?',
            '04':'Buen dia!, ¿puedo ayudarte?',
        }
    },
    'adios':{
        'responses':{
            '01':'Hasta luego',
            '02':'Hasta pronto',
            '03':'Buen dia',
            '04':'Adios',
        }
}
}

def get_response(cmd):
    try:
        response = commands[cmd]['responses']
        return response.get(random.choice(list(response.keys())))
    except:
        return 'No te entiendo'