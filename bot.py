import os
import telebot

API_TOKEN = os.environ['7617615026:AAHnyXsANriey2OSH_PPRacZTbQ8wbxUk4o']
CHANNEL_ID = -1003117189518
GROUP_ID = -1003390626638

bot = telebot.TeleBot(API_TOKEN)

movies = {
    1: 123, 2: 124, 3: 125, # ... تا 50
}

@bot.message_handler(func=lambda m: m.text and m.text.startswith("فیلم "))
def forward_movie(msg):
    try:
        n = int(msg.text.split()[1])
        if n not in movies:
            bot.reply_to(msg, "این فیلم تو لیست نیست!")
            return
        bot.forward_message(GROUP_ID, CHANNEL_ID, movies[n])
    except:
        bot.reply_to(msg, "فرمت صحیح نیست.")

bot.polling()
