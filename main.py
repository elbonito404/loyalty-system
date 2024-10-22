import telebot
from telebot import types
token='7498093097:AAE32K9KmXlZID8V1E2GcKWndUEcIlw4EY4'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'ZOOOOOOOV')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=PUAMmEgOEyM&list=RDcFVMiTnGn6w&index=27")
bot.infinity_polling()