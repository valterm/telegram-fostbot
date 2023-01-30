import json
from random import randint
import telegram
from .functions import *

def get_random_insult() -> str:
    f = open('./dirty.json', 'r')
    json_data = json.loads(f.read())
    max_n = len(json_data['DirtyWords'])
    n = randint(0, max_n-1)

    return(json_data['DirtyWords'][n].lower())

def insult(update: telegram.Update, context: telegram.ext.CallbackContext):
    insult = get_random_insult()
    user = get_username(update.effective_user)
    msg=f"{user}, te {insult}."
    message_chat(update,context,msg)

def fuckyou(update: telegram.Update, context: telegram.ext.CallbackContext):
    insult = get_random_insult()
    target = update.message.text
    user = get_username(update.effective_user)

    strip = ['/fuckyou','@kretanyad_bot']
    target = strip_string(str(target), strip)

    if len(target) == 0:
        msg=f"{user}, ennyire nem lehetsz ostoba. Adj meg egy nevet, te {insult}."
        message_chat(update,context,msg)
        return 0

    msg=f"Kedves {target}, {user} szeretné kifejezni az igaz érzéseit irántad: \n{target}, te {insult}."
    message_chat(update,context,msg)   
