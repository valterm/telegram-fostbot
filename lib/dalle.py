import requests
import openai
from .functions import *
from .insult import *
from .globals import *
from telegram import Update,User
from telegram.ext import CallbackContext
from random import randrange


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
        if prompt in ["the most handsome man", "the best waterpolo player ever", "the handsomest man ever", "the biggest stud", "the man every man wants to be and every woman wants"]:
            urls = ['https://i.imgur.com/6TwuNCc.jpeg','https://i.imgur.com/Jzu6gPC.jpeg','https://i.imgur.com/2XXJHvG.jpeg','https://i.imgur.com/llRXYmS.jpeg','https://i.imgur.com/00oHQ1D.jpeg']
            index = randrange(5)
            image_url = urls[index]
        else:
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
        msg = f'There was a problem with your request ({prompt}):\n{e}'
        message_chat(update,context,msg)
    
    except Exception as e:
        e=str(e)
        if len(e) > 240:
            msg = f'There was an unknown error trying to process your prompt ({prompt})\n\nDetails:\n{e}'
        else:
            msg = f'There was an unknown error trying to process your prompt ({prompt})'

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