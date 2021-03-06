"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(string_analysis(True,0))
    print(string_analysis('Андрей','Андрей'))
    print(string_analysis('Андрей1','Андрей'))
    print(string_analysis('lear','learn'))
    
def string_analysis(str1,str2):

  if not (isinstance(str1, str) or isinstance(str2, str)):
    return 0
  elif str1 == str2:
    return 1
  elif len(str1) > len(str2):
    return 2
  elif str2 == 'learn':
    return 3 
  else:
    return -1

if __name__ == "__main__":
    main()
