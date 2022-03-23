import os
import telebot
from telebot import custom_filters
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton



my_secret = os.environ['osAPIkey']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "You need my help?")

@bot.message_handler(commands=['commands'])
def commands(message):
	bot.reply_to(message, "/start, /help, /garage, /greet, /hello, /work, /chat")

'''@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)'''

strSkilly = ['cat']

@bot.message_handler(commands = "movie" )
def send_mike(message):
	bot.reply_to(message, "your favorite movie?)
  
@bot.message_handler(commands = "poor" )
def poor(message):
	bot.reply_to(message, "spent all my life savings to visit Manhattan")  

@bot.message_handler(commands=["greet"])
def greet(message):
  bot.reply_to(message, "Hi !")


@bot.message_handler(commands=["business"])
def business(message):
  bot.reply_to(message, "this is the business we have chosen")


@bot.message_handler(commands=["tasks"])
def dick(message):
    bot.reply_to(message, "Looks like you are calling admin....")

@bot.message_handler(text=['/hi','/you'])
def text_filter(message):
    bot.send_message(message.chat.id, "{name}! you are the best".format(name=message.from_user.first_name))

@bot.message_handler(text=['/friend'])
def text_filter2(message):
    bot.send_message(message.chat.id, "{name}! is a friend".format(name=message.from_user.first_name))


# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("I buy your contract out", callback_data="buyout"),InlineKeyboardButton("The top bot is here", callback_data="thedonhere"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "buyout":
        bot.answer_callback_query(call.id, "I have to straighten you out")
    elif call.data == "thedonhere":
        bot.answer_callback_query(call.id, "that's unbelievable!")

@bot.message_handler(commands=["buy"])
def message_handler(message):
    bot.send_message(message.chat.id, "/buy", reply_markup=gen_markup())




bot.polling()