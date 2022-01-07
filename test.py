import telebot
token = '5055886821:AAGZWhoPa6J8_I0bxzAEFCleOptO-Bb_zSY'
bot = telebot.TeleBot(token)

@bot.message_handler()
def start_message(message):
    your_variable = message.from_user.id

bot.send_message(message.from_user.id, text='ghbt')


bot.polling()