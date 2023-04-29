from telegram import Update,User
from telegram.ext import CallbackContext
from .functions import *
from .globals import *

def insult(update: Update, context: CallbackContext):
    insult = get_random_insult()
    user = get_username(update.effective_user)
    msg=f"{user}, te {insult}."
    message_chat(update,context,msg)

def fuckyou(update: Update, context: CallbackContext):
    insult = get_random_insult()
    target = update.message.text
    user = get_username(update.effective_user)

    tags = ['/fuckyou',f'@{bot_username}']
    target = strip_input(str(target), tags)

    if len(target) == 0:
        msg=f"{user}, ennyire nem lehetsz ostoba. Adj meg egy nevet, te {insult}."
        message_chat(update,context,msg)
        return 0

    msg=f"Kedves {target}, {user} szeretné kifejezni az igaz érzéseit irántad: \n{target}, te {insult}."
    message_chat(update,context,msg)   
