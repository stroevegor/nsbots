 # -*- coding: utf-8 -*-
import telebot
import configuration
import random

from telebot import types
 
bot = telebot.TeleBot(configuration.TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    send = bot.send_message(message.from_user.id, "Введите пароль и подождите пару секунд:")
    bot.register_next_step_handler(send, hello)
def hello(message) :
    if message.text == "shardakova55":

        photo = open('/Users/egor/Desktop/NS/welcomephoto.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Для зала".decode("utf-8"))
        user_markup.row("Для дома".decode("utf-8"))
        user_markup.row("Питание".decode("utf-8"))
        send = bot.send_message(message.from_user.id, "👋 Привет, {0.first_name}! Я бот созданный чтобы ты могла тренироваться всегда и везде! \n\n Выбери тип тренировки и приступай к упражнениям!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, menu)
    

    else: bot.send_message(message.chat.id, "Неверный пароль, снова нажмите start и введите верный пароль") 
     


def menu(message):
    
    if message.text == "Для зала".decode("utf-8"):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, one_time_keyboard=False)
        user_markup.row("Спина")
        user_markup.row("Ноги")
        user_markup.row("Попа")
        user_markup.row("Главное меню")
        send = bot.send_message(message.from_user.id, "{0.first_name}, хорошей тренировки в зале! Что сегодня тренируем? Есть упражнения для попы, ног или спины".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, forGym)
        

    elif message.text == "Для дома".decode("utf-8"):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, one_time_keyboard=False)
        user_markup.row("Ягодицы")
        user_markup.row("Грудь")
        user_markup.row("Главное меню")
        send = bot.send_message(message.from_user.id, "{0.first_name}, плохая погода? Для домашней тренировки у меня тоже есть упражнения. Например, для попы, ног или спины".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, forHome)
    
    elif message.text == "Питание".decode("utf-8"):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, one_time_keyboard=False)
        user_markup.row("90кг")
        user_markup.row("70кг")
        user_markup.row("Главное меню")
        send = bot.send_message(message.from_user.id, "{0.first_name}, питание - очень важная часть спорта, питайся правильно".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, eatDocuments)


def forGym(message):
 
    
    if message.text == "Спина".decode("utf-8"):
        
        send = bot.send_message(message.from_user.id, "{0.first_name}, вот упражнение для спины: https://www.youtube.com/watch?v=T8OS3B6jPGw".format(message.from_user, bot.get_me()),
                parse_mode='html')
        bot.register_next_step_handler(send, forGym)

    elif message.text == "Ноги".decode("utf-8"):
        
        send = bot.send_message(message.from_user.id, "{0.first_name}, вот упражнение для ног: https://www.youtube.com/watch?v=C1unNjiLcfU".format(message.from_user, bot.get_me()),
                parse_mode='html')
        bot.register_next_step_handler(send, forGym)


    elif message.text == "Попа".decode("utf-8"):
        
       send = bot.send_message(message.from_user.id, "{0.first_name}, вот упражнение для попы: https://www.youtube.com/watch?v=BFaYipEsivI".format(message.from_user, bot.get_me()),
                parse_mode='html')
       bot.register_next_step_handler(send, forGym)

    elif message.text == "Главное меню".decode("utf-8"):
        
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Для зала".decode("utf-8"))
        user_markup.row("Для дома".decode("utf-8"))
        user_markup.row("Питание".decode("utf-8"))
        send = bot.send_message(message.from_user.id, "👋 Привет, {0.first_name}! Я бот созданный чтобы ты могла тренироваться всегда и везде! \n\n Выбери тип тренировки и приступай к упражнениям!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, menu)

    


def forHome(message):

    if message.text == "Ягодицы".decode("utf-8"):
        
        send = bot.send_message(message.from_user.id, "{0.first_name}, вот упражнение для крутого ореха: https://www.youtube.com/watch?v=t8fUlq53Z8s".format(message.from_user, bot.get_me()),
                parse_mode='html')
        bot.register_next_step_handler(send, forHome)

    elif message.text == "Грудь".decode("utf-8"):
        
        send = bot.send_message(message.from_user.id, "{0.first_name}, вот упражнение для упругой груди: https://www.youtube.com/watch?v=JXuvYfUhF9o".format(message.from_user, bot.get_me()),
                parse_mode='html')
        bot.register_next_step_handler(send, forHome)

    elif message.text == "Главное меню".decode("utf-8"):
        
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Для зала".decode("utf-8"))
        user_markup.row("Для дома".decode("utf-8"))
        user_markup.row("Питание".decode("utf-8"))
        send = bot.send_message(message.from_user.id, "👋 Привет, {0.first_name}! Я бот созданный чтобы ты могла тренироваться всегда и везде! \n\n Выбери тип тренировки и приступай к упражнениям!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, menu)






def eatDocuments(message):

    if message.text == "90кг".decode("utf-8"):
        
        send = bot.send_message(message.from_user.id, "{0.first_name}, вот питание для 90кг: https://docs.google.com/document/d/1tSnpaK1i_w3Tv01vLtlpR0JuDxGJKuERbOlly5FIvZw/edit?usp=sharing".format(message.from_user, bot.get_me()),
                parse_mode='html')
        bot.register_next_step_handler(send, eatDocuments)

    elif message.text == "70кг".decode("utf-8"):
        
        send = bot.send_message(message.from_user.id, "{0.first_name}, вот питание для 70кг: https://docs.google.com/document/d/1tSnpaK1i_w3Tv01vLtlpR0JuDxGJKuERbOlly5FIvZw/edit?usp=sharing".format(message.from_user, bot.get_me()),
                parse_mode='html')
        bot.register_next_step_handler(send, eatDocuments)

    elif message.text == "Главное меню".decode("utf-8"):
        
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Для зала".decode("utf-8"))
        user_markup.row("Для дома".decode("utf-8"))
        user_markup.row("Питание".decode("utf-8"))
        send = bot.send_message(message.from_user.id, "👋 Привет, {0.first_name}! Я бот созданный чтобы ты могла тренироваться всегда и везде! \n\n Выбери тип тренировки и приступай к упражнениям!".format(message.from_user, bot.get_me()),
                parse_mode='html', reply_markup=user_markup)
        bot.register_next_step_handler(send, menu)

   






        





       







        

        

 
                        


    
	


        

             	
	
	   
# RUN
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0, timeout=20)