import requests
import openai
from .functions import *
from .insult import *
from .globals import *
from telegram import Update,User
from telegram.ext import CallbackContext


openai.api_key=openai_token


def picme(update: Update, context: CallbackContext):
    tags = ['/picme', f'@{bot_username}']
    user = get_username(update.effective_user)

    prompt = update.message.text
    prompt = strip_input(prompt,tags)

    if len(prompt) == 0:
        insult = get_random_insult()
        msg = f'{user}, you must provide a prompt.'
        message_chat(update,context,msg)
        return 0
    
    try:
        r = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
        )
        image_url = r['data'][0]['url']
        download_image(image_url, './tmp.png')
        sending_image(update,context)
        send_image(update,context,'./tmp.png')

    except openai.error.InvalidRequestError as e:
        e=str(e)
        msg = f'There was an error with your request:\n{e}'
        message_chat(update,context,msg)

def dickpic(update: Update, context: CallbackContext):
    
    r = openai.Image.create(
    prompt='Closeup of large thick flesh coloured bald worm with a mushroom shaped head on top of two eggs on a white background',
    n=1,
    size="256x256"
    )
    sending_image(update,context)
    image_url = r['data'][0]['url']
    download_image(image_url, './tmp.png')
    send_image(update,context,'./tmp.png')