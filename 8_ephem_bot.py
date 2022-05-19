"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import settings
import ephem
from datetime import date


logging.basicConfig(filename='bot.log', level=logging.INFO)



def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text("Привет, пользователь! Ты вызвал команду /start")

def where_planet(name_planet):
    current_date = str(date.today()).replace('-','/')
  
    try:
        if name_planet.upper() == 'MARS':
            return ephem.constellation(ephem.Mars(current_date))
        elif name_planet.lower() == 'earth':
            return ephem.constellation(ephem.Earth(current_date))
        else:
            return 'Не обрабатываем такую планету'
    except:
        return "Не могу определить планету"

def planet_user(update, context):
    name_planet = update.message.text.split()[1]
    update.message.reply_text(where_planet(name_planet))

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():

    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал')

    mybot.start_polling()

    mybot.idle()

if __name__ == "__main__":
    main()