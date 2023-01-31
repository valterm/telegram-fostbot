from telegram import Update,User
from telegram.ext import Updater,CallbackContext,CommandHandler
import logging
import lib.functions as f
import lib.globals as g
import lib.insult as insult
import lib.dalle as dalle


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():

    token = g.telegram_token

    updater = Updater(token=token)
    
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', f.start)
    help_handler = CommandHandler('help', f.helper)
    insult_handler = CommandHandler('insult',insult.insult)
    fuckyou_handler = CommandHandler('fuckyou',insult.fuckyou)
    image_generator_handler = CommandHandler('picme',dalle.picme)
    dickpic_handler = CommandHandler('dickpic', dalle.dickpic)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(insult_handler)
    dispatcher.add_handler(fuckyou_handler)
    dispatcher.add_handler(image_generator_handler)
    dispatcher.add_handler(dickpic_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()


