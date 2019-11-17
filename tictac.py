import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,\
        CallbackQueryHandler, ConversationHandler

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,\
    ReplyKeyboardRemove

import settings

from keyboards import my_keyboard, tictac_keyb, inline_keys,\
        text_x, text_o, error_keyboard

from game_logic import game, start_game

'''This is telegram bot created for playing tictactoe'''

subscribers = set()


#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

logging.info('bot started')

logger = logging.getLogger(__name__)




def start(update, context):
    text = '''Вас приветствует новый бот! /start
Нажмите /subscribe для подписки
Нажмите /unsubscribe если хотите отписаться
Нажмите /alarm чтобы установить будильник'''
    logging.info('/start')

    update.message.reply_text(text, reply_markup=my_keyboard())


# subscribe for user means to get "annoing message" every 5 seconds
def subscribe(update, context):
    chat_id = update.message.chat_id
    # write chat_id in set 'subscribers'
    subscribers.add(chat_id)
    update.message.reply_text('subscribe is done')

# unsubscribe from "annoing message"
def unsubscribe(update, context):
    chat_id = update.message.chat_id
    bot = context.bot
    if chat_id in subscribers:
        subscribers.remove(chat_id)
        bot.send_message(chat_id=chat_id, text='unsubscribe is complete')
    else :
        bot.send_message(chat_id=chat_id, text='you have not subscribed yet. Click /subscribe')

# this func send "annoing message" to user if subscribe is done
def send_updates(context):
    bot = context.bot
    for chat_id in subscribers:
        bot.send_message(chat_id=chat_id, text='annoying message')

# this function sets alarm
def set_alarm(update, context):
    job_queue = context.job_queue
    args = context.args
    try:
        seconds = abs(int(args[0]))
        job_queue.run_once(alarm, seconds, context=update.message.chat_id)
    except(IndexError, ValueError):
        update.message.reply_text('Введите число секунтд после команды /alarm')

# send alarm message was set 'set_alarm' function
def alarm(context):
    job = context.job
    context.bot.send_message(chat_id=job.context, text='Сработал будильник')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)






# main function that starts bot
def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=settings.PROXY)



    mybot.job_queue.run_repeating(send_updates, interval=5)
    


    dp = mybot.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('subscribe', subscribe))
    dp.add_handler(CommandHandler('unsubscribe', unsubscribe))
    dp.add_handler(CommandHandler('alarm', set_alarm, pass_job_queue=True, pass_args=True))

    game_handler = ConversationHandler(
            entry_points=[MessageHandler(Filters.regex('^(Play TicTacToe)$'), start_game)],
            states={
                'GAME' : [CallbackQueryHandler(game)]
            },
            fallbacks=[MessageHandler(Filters.regex('^(Play TicTacToe)$'), start_game),
            CommandHandler('start', start)]
            )
    dp.add_handler(game_handler)


    # dp.add_handler(MessageHandler(Filters.regex('^(Play TicTacToe)$'), start_game))


    # this handler catches signal when inline keyboard button is pressed
    # dp.add_handler(CallbackQueryHandler(inline_button_pressed))


    dp.add_error_handler(error)
    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

