import telebot
import os
from flask import Flask
from threading import Thread

# 1. إعداد سيرفر وهمي عشان Render ما يقفلش البوت
app = Flask('')

@app.route('/')
def home():
    return "البوت شغال بنجاح!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. إعداد البوت (حط التوكن بتاعك هنا)
TOKEN = '7253503140:AAGY6pD5fS6X7_5uW-xY_85e0D0A5p-S6Xw' # استبدله بالتوكن بتاعك لو ده قديم
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً يا حسين! البوت شغال دلوقتي على Render.\nارسل أي نص لتوليد صورة (لو مفعل الميزة) أو استخدم الأوامر.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تم استلام رسالتك! البوت مستقر الآن.")

# 3. تشغيل البوت
if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر في الخلفية
    print("البوت بدأ العمل...")
    bot.infinity_polling()

