from telegram import Update,User
from telegram.ext import Updater,CallbackContext,CommandHandler
import logging
import os
import lib.functions as f
import lib.insult as insult


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def main():

    token = os.environ.get('TELEGRAM_BOT_TOKEN')    

    updater = Updater(token=token)
    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', f.start)
    help_handler = CommandHandler('help', f.helper)
    insult_handler = CommandHandler('insult',insult.insult)
    fuckyou_handler = CommandHandler('fuckyou',insult.fuckyou)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(insult_handler)
    dispatcher.add_handler(fuckyou_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()


