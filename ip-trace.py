import requests
import telebot

bot = telebot.TeleBot('6076887774:AAH0gCaGi8059K4Ji5e0T3_Y-eiJw4G_PIY')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome to the Ip-Tracking Bot.")

@bot.message_handler(commands=['ip'])
def send_ip_info(message):
    try:
        ip = message.text.split()[1] # Extract the IP address from the message
        url = "http://ip-api.com/json/"+ip
        data = requests.get(url).json()
        response = "SIM: {}\nCity: {}\nCountry: {}\nLongitude: {}\nLatitude: {}\nTimeZone: {}\nZipCode: {}".format(
        data['org'], data['city'], data['country'], data['lon'], data['lat'], data['timezone'], data['zip'])
    except:
        response = "Check the input!"
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['author'])
def send_hello(message):
    bot.send_message(message.chat.id, "Instagram: https://instagram.com/response.200")
    bot.send_message(message.chat.id, "Website: https://lone1177.blogspot.com/")
    bot.send_message(message.chat.id, "Telegram Group: https://t.me/lonemods")

print("STARTED!")
bot.polling(none_stop=True)

