from telegram.ext import Updater

from keyboards import tictac_keyb, error_keyboard, inline_keys,\
    text_x


# starts the game 
def start_game(update, context):
    update.message.reply_text(text='TicTacToe. Press button for X',
                         reply_markup=tictac_keyb(*inline_keys()))

# catch if inline keyboard button is pressed
def inline_button_pressed(update, context):
    query = update.callback_query


    button = [' ', ' ', ' ', 
              ' ', ' ', ' ',
              ' ', ' ', ' ']

    try:
        user_choice = int(query.data)
        button[user_choice-1] = text_x
        keyboard = tictac_keyb(*button)

    except TypeError:
        keyboard = error_keyboard

    context.bot.edit_message_text(text='Your turn', chat_id=query.message.chat_id, 
                message_id=query.message.message_id,
                reply_markup=keyboard)
