"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

from ast import While
from tkinter import W

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} 

def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
      try:
       questions = input("Ваш вопрос?")
      except KeyboardInterrupt:
        print("Пока!")
        break

      if questions in questions_and_answers:
        print(questions_and_answers[questions])
      else:
        print ("не знаю как ответить...")
    
if __name__ == "__main__":
    hello_user()
