from telegram import Update
from telegram.ext import CallbackContext
import requests
from random import randint

def get_username(user: User) -> str:
    if user.username == 'None' or len(user.username) == 0:
        username = f"{user.last_name} {user.first_name}"
    else:
        username = f"@{user.username}"
    return(username)

def get_random_insult() -> str:
    f = open('./dirty.json', 'r')
    json_data = json.loads(f.read())
    max_n = len(json_data['DirtyWords'])
    n = randint(0, max_n-1)

    return(json_data['DirtyWords'][n].lower())

def strip_input(input: str, expressions = []) -> str:
    for s in expressions:
        input = input.replace(s,'')
    input = input.strip()
    return(input)

def download_image(url, file_name):
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }
    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        return 1

def message_chat(update: Update, context: CallbackContext, message: str):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def send_image(update: Update, context: CallbackContext, image_path: str):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(image_path, 'rb'))

def start(update: Update, context: CallbackContext):
    user = get_username(update.effective_user)
    msg = f"{user}, vigyázz, mert csúnyán beszélek!"
    message_chat(update,context,msg)

def helper(update: Update, context: CallbackContext):    
    user = get_username(update.effective_user)
    msg=f"{user}, ha nem tudod kitalálni mire jó ez a bot, nem tudok rajtad segíteni."
    message_chat(update,context,msg)