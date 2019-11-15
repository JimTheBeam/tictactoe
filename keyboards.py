from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,\
    ReplyKeyboardRemove




# keyboard:
def my_keyboard():
    keyboard = ReplyKeyboardMarkup([['Play TicTacToe']], resize_keyboard=True)
    return keyboard


# inline keyboards:
# buttons:
text_none = ' '
text_o = 'O'
text_x = 'X'

button_text = text_none

# def button1(button_text):
#     button = {'button1' : {'text' : button_text, 'callback_data' : '1'}}
#     return button

# def button2(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button3(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button4(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button5(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button6(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button7(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button8(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button

# def button9(button_text):
#     button = InlineKeyboardButton(button_text, callback_data='1')
#     return button


def inline_keys():
    buttons = ['button1', 'button2', 'button3', 
                      'button4', 'button5', 'button6',
                      'button7', 'button8', 'button9']
    return buttons

def inline_keys2():
    buttons = ['1', '2', '3', 
                      '4', '5', '6',
                      '7', '8', '9']
    return buttons

def tictac_keyb(*args):
    button1 = InlineKeyboardButton(args[0], callback_data='1')
    button2 = InlineKeyboardButton(args[1], callback_data='2')
    button3 = InlineKeyboardButton(args[2], callback_data='3')
    button4 = InlineKeyboardButton(args[3], callback_data='4')
    button5 = InlineKeyboardButton(args[4], callback_data='5')
    button6 = InlineKeyboardButton(args[5], callback_data='6')
    button7 = InlineKeyboardButton(args[6], callback_data='7')
    button8 = InlineKeyboardButton(args[7], callback_data='8')
    button9 = InlineKeyboardButton(args[8], callback_data='9')
    
    buttons = [[button1, button2, button3], 
                    [button4, button5, button6],
                    [button7, button8, button9]]

    keyboard = InlineKeyboardMarkup(buttons)
    return keyboard



