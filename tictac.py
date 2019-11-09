import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

logging.info('bot started')

logger = logging.getLogger(__name__)



def start(update, context):
    text = 'Вас приветствует новый бот! /start'

    logging.info('/start')

    update.message.reply_text(text)



def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start))




    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

