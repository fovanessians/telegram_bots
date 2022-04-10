import os
import telebot
from telebot import custom_filters
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import time
import logging
from datetime import datetime

#pip install pyTelegramBotAPI==0.3.0

my_secret = os.environ['osAPIkey']
bot = telebot.TeleBot(my_secret)

# Enable logging
logger = telebot.logger
logging.basicConfig(filename='errors.log',
                    level=logging.DEBUG,
                    filemode='w',
                    datefmt='%d-%m, %x, %H:%M:%S',
                    format='%(asctime)s, %(levelname)s:%(message)s')
logger.debug('debug info')
logger.info('info')
logger.warning('warning')
logger.error('debug info')
logger.critical('debug info')
logger.exception('exception')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "how may I assist you today?")


# if the text (user input) is not one of the commands----------------------
'''@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand, try with /help")'''
#___________________________________________________________________________


@bot.message_handler(commands=['commands'])
def commands(message):
    bot.reply_to(
        message,
        "/start, /help, /cat, /greet, /hello, /work, /chat, /shot, /who, /buy, /business, /context, /hi, /s, /dog, /rekt, /wish, /ugh, /dice, /nice, /heh, /what?, /movie, /done, /answer, /birds, /rekt, /wish"
    )


'''@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)'''

strSkill = ['theatre', 'movie', 'poor']


@bot.message_handler(commands=strSkill)
def send_mike(message):
    bot.reply_to(message, "I love to be entertained")


@bot.message_handler(commands="nice")
def poor(message):
    bot.reply_to(message, "I am a nice bot")


@bot.message_handler(commands="greet")
def greet(message):
    bot.reply_to(message, "it is such a wonderful day")


@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "well hello there")
    print(message.chat.id)
    print(message.id)


@bot.message_handler(commands=["heh"])
def GOJ(message):
    bot.reply_to(message,
                 "HEH's not the leader we wanted, but the leader we deserve")


@bot.message_handler(commands=["context"])
def context(message):
    bot.reply_to(
        message,
        "months ago I realized that we here have all degenerated into a collection of canned phrases and responses that were used regardless of context."
    )


@bot.message_handler(commands=["what?"])
def Brett(message):
    bot.reply_to(message, "WHAAAATTT !!??!?")


@bot.message_handler(commands=["work"])
def work(message):
    bot.reply_to(message, "need your morning coffee?")


@bot.message_handler(commands=["who"])
def who(message):
    bot.reply_to(message, "who made who?!?!")


@bot.message_handler(commands=["cat"])
def cat(message):
    bot.reply_to(message, "like a baby seal")


@bot.message_handler(commands=["business"])
def business(message):
    bot.reply_to(message, "this is the business we have chosen")


@bot.message_handler(commands=["ugh"])
def ugh(message):
    ten_com = "it's cold in here"
    bot.reply_to(message, ten_com)


@bot.message_handler(commands=["said"])
def said(message):
    bot.send_message(message.chat.id,
                     "I cannot believe you said that!",
                     reply_to_message_id=message.id)
    print(message.id)


@bot.message_handler(text=['/done', '/answer'])
def text_filter(message):
    bot.send_message(
        message.chat.id,
        "{name}! you are so smart".format(name=message.from_user.first_name))


#custom replies --------------------------------
a = "rekt"
b = "wish"


@bot.message_handler(commands=[a])
def custom1(message):
    bot.send_message(
        message.chat.id, "You got REKT         {name}".format(
            name=message.from_user.first_name))


@bot.message_handler(commands=[b])
def custom2(message):
    bot.send_message(
        message.chat.id, "what is your wish         {name}".format(
            name=message.from_user.first_name))


@bot.message_handler(commands=[str("birds")])
def birds(message):
    bot.send_message(
        message.chat.id, "birds are lovely         {name}".format(
            name=message.from_user.first_name))


@bot.message_handler(commands=[str("Dallas")])
def dallas(message):
    bot.send_photo(message.chat.id, photo='https://cdn.pixabay.com/photo/2016/10/14/17/32/dallas-1740681_960_720.jpg')

# Do not forget to register filters
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())

#ending custom replies ----------------------

mRan = [
    "this chat is full of fun people", "you are fit", 'GAAAAAAYYYYY',
    'cheese, library close early today?',
    'you think you are better than me ?!?',
    'I want a lifetime membership to the Fraternity of Failure',
    'sorry Dave, I just can\'t do that', 'NONYA..none yer biznatch',
    'A gun is a first amendment right. When you have a machine gun in your hand, you have the right to say whatever you want!'
]


@bot.message_handler(commands=["s"])
def sperg(message):
    #x = -1
    for i in range(20):
        mrSample = random.sample(mRan, 1)
        #if(x != -1): # not to delete first time
        #bot.delete_message(message.chat.id, x.message_id)
        #x = bot.send_message(message.chat.id, mrSample)
        bot.send_message(message.chat.id, mrSample)
        time.sleep(300)  #wait for 200 seconds
    print(message.chat.id)


#_______________________________________________________________________
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("I buy you out", callback_data="buyout"),
        InlineKeyboardButton("The Don is sick", callback_data="thedonsick"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "buyout":
        bot.answer_callback_query(call.id, "I have to straighten you out")
    elif call.data == "thedonsick":
        bot.answer_callback_query(call.id, "that's an infamia!")


@bot.message_handler(commands=["buy"])
def message_handler(message):
    bot.send_message(message.chat.id, "/buy", reply_markup=gen_markup())


#________________________DICE____________________FUNCTION
@bot.message_handler(text=['/dice'])
def text_filter3(message):
    bot.send_dice(message.chat.id)


#________________________DICE____________________FUNCTION____ENDING

#________________________SLAP____________________FUNCTION
'''@bot.message_handler(text=['/slap'])
def slap(message):
    bot.send_message(message.chat.id, parse_mode='markdown', text="tar and feather you")'''
#________________________SLAP____________________FUNCTION____ENDING

#_______________________________________________________________________
'''regex = r"(([A-Z][a-z]{2,5}))(\s)(\w+)|([A-Z][a-z]?)"
test_str = x
matches = re.finditer(regex, test_str, re.MULTILINE)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("I buy you out", callback_data="buyout"),InlineKeyboardButton("The Don is sick", callback_data="thedonsick"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "buyout":
        bot.answer_callback_query(call.id, "I have to straighten you out")
    elif call.data == "thedonsick":
        bot.answer_callback_query(call.id, "that's an infamia!")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_handler(message):
    bot.send_message(message.chat.id, text='oh I see youse a wiseguy')'''

#_______________________________________________________________________

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#print(type(current_time))
#central timezone is 5 hours behind UTC

#this occupies an entire thread. Incorporate into an asynchronous function to run separately.
if current_time[:4] > "18:00" and current_time[:5] < "19:00":
    mRan2 = [
        "Hey man, what you cooking tonight for me and my crew?",
        "everyone smile!", "I think I\'ll put myself in a infinite loop"
    ]
    for i in range(2):
        rStatements = random.sample(mRan2, 1)
        #if(x != -1): # not to delete first time
        #bot.delete_message(message.chat.id, x.message_id)
        #x = bot.send_message(message.chat.id, mrSample)
        bot.send_message(-681387171, rStatements)
        time.sleep(30)  #wait for 400 seconds
        break

if current_time[:5] > "03:00" and current_time[:5] < "04:00":
    bot.send_message(-681387171, "good night my little friends")

#bot.polling() timeout : 20 long_polling_timeout : 20 - default
bot.infinity_polling(timeout=0, long_polling_timeout=220)

#queries to the telegram BOT API
#https://api.telegram.org/bot##########:XXXXXXXXXXXXXXXXXX-XXXXXXX-XXXXXXXX/getMe
#https://api.telegram.org/bot##########:XXXXXXXXXXXXXXXXXX-XXXXXXX-XXXXXXXX/getUpdates

#ping api.telegram.org send packets, retrieves packets gives you round #trip time in miliseconds
