import requests
import openai
from .functions import *
from .insult import *
from telegram import Update,User
from telegram.ext import CallbackContext
import os


token = os.environ.get('OPENAI_API_TOKEN')
openai.api_key=token


def picme(update: Update, context: CallbackContext):
    tags = ['/dickpic', context.bot.username]
    user = get_username(update.effective_user)

    prompt = update.message.text
    prompt = strip_input(prompt,tags)

    if len(prompt) == 0:
        insult = get_random_insult()
        msg = f"@{user}, te {insult}. \nHogy a picsába generáljak egy fotót, ha nem mondod meg mit akarsz?"
        message_chat(update,context,msg)
    
    r = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256"
    )
    image_url = r['data'][0]['url']

    download_image(image_url, "./tmp.png")

    send_image(update,context,'./tmp.png')

def dickpic(update: Update, context: CallbackContext):
    r = openai.Image.create(
    prompt="A large bald worm wriggiling in brown grass on top of two eggs",
    n=1,
    size="256x256"
    )
    image_url = r['data'][0]['url']

    download_image(image_url, "./tmp.png")

    send_image(update,context,'./tmp.png')