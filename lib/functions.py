import telegram as telegram

def get_username(user: telegram.User) -> str:
    if user.username == 'None' or user.username == '':
        username = f"{user.last_name} {user.first_name}"
    else:
        username = f"@{user.username}"
    return(username)

def strip_string(input: str, expressions = []) -> str:
    for s in expressions:
        input = input.replace(s,'')
    input = input.strip()
    return(input)

def message_chat(update: telegram.Update, context: telegram.ext.CallbackContext, message: str):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def start(update: telegram.Update, context: telegram.ext.CallbackContext):
    user = get_username(update.effective_user)
    msg = f"{user}, vigyázz, mert csúnyán beszélek!"
    message_chat(update,context,msg)

def helper(update: telegram.Update, context: telegram.ext.CallbackContext):    
    user = get_username(update.effective_user)
    msg=f"{user}, ha nem tudod kitalálni mire jó ez a bot, nem tudok rajtad segíteni."
    message_chat(update,context,msg)