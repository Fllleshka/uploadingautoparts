import os
import time
import pyautogui
import datetime
import pyautogui

# Включение паузы 1.5 секунды между действиями
pyautogui.PAUSE = 1

# Функция перемещения мышки и кликов
def movemouse(massx, massy, numberbutton):
    for elem in range(0, len(massx)):
        print(f'{elem + 1}\t\t[{massx[elem]}]\t[{massy[elem]}]')
        pyautogui.moveTo(massx[elem], massy[elem], duration=0.25)
        # Тип скриншота кнопка
        if elem == numberbutton:
            pyautogui.leftClick()
            # reg = (100-20, 270-10, 60, 20)
            reg = (0, 0, 1920, 1080)
            takeascreenshot("Button", "screenshots/proofofwork/", reg)
        else:
            pyautogui.leftClick()

# Функция скриншота
def takeascreenshot(name, path, reg):
    # Время сейчас
    today = datetime.datetime.today()
    todaytime = today.strftime("%d.%m.%Y.%H.%M.%S")
    path = path + name + " " + todaytime + ".png"
    screen = pyautogui.screenshot(path, region = reg)

# Функция выбора действия от времени
def switcher(argument):
    match argument:
        # Время сканирования папки
        # "Проставить остатки"
        case times.putDownBalances:
            # [0] Перемещение к свёрнотому рабочему столу
            # [1] Перемещение к вкладке "Проставить остатки"
            # [2] Перемещение к кнопке "Сформировать"
            # [3] # Перемещение к сворачиванию удалённого рабочего стола
            massx = [260, 960, 200, 100, 1160]
            massy = [1060, 540, 1005, 270, 10]
            try:
                movemouse(massx, massy, 3)
            except Exception:
                print(f"Программа [Проставить остатки] завершилась с ошибкой: \n{Exception}\n")
            else:
                print(f"Проставка остатков прошла успешно")
            time.sleep(60)
        # "Выгрузка товаров на сайт"
        case times.uploadingpricetoweb:
            # [0] Перемещение к свёрнотому рабочему столу
            # [1] Перемещение к вкладке "Выгрузка товаров на сайт"
            # [2] Перемещение к кнопке "Сформировать"
            # [3] # Перемещение к сворачиванию удалённого рабочего стола
            massx = [260, 960, 400, 100, 1160]
            massy = [1060, 540, 1005, 300, 10]
            try:
                movemouse(massx, massy, 3)
            except Exception:
                print(f"Программа [Выгрузка товаров на сайт] завершилась с ошибкой: \n{Exception}\n")
            else:
                print(f"Выгрузка товаров на сайт прошла успешно")
            time.sleep(60)
        # Подтверждение новой даты
        case times.acceptnewday:
            # [0] Перемещение к свёрнотому рабочему столу
            # [1] Перемещение к кнопке "Сменить рабочую дату"
            # [2] # Перемещение к сворачиванию удалённого рабочего стола
            massx = [260, 960, 920, 1160]
            massy = [1060, 540, 570, 10]
            try:
                movemouse(massx, massy, 1)
            except Exception:
                print(f"Программа [Сменить рабочую дату] завершилась с ошибкой: \n{Exception}\n")
            else:
                print(f"Смена рабочей даты прошла успешно")
            time.sleep(60)
        # Закрытие таблицы с проставлением остатков
        case times.closetable:
            # [0] Перемещение к свёрнотому рабочему столу
            # [1] Перемещение к вкладке "Сформировать2"
            # [2] Перемещение к закрытию таблицы
            # [3] # Перемещение к сворачиванию удалённого рабочего стола
            massx = [260, 960, 800, 1910, 1160]
            massy = [1060, 540, 1005, 25, 10]
            try:
                movemouse(massx, massy, 3)
            except Exception:
                print(f"Программа [Закрытия проставления остатков] завершилась с ошибкой: \n{Exception}\n")
            else:
                print(f"Закрытие проставления остатков прошло успешно")
            time.sleep(60)
        case default:
            return print("Время сейчас:\t", argument)

# Класс времён
class times:
    # Время сейчас
    today = datetime.datetime.today()
    todaytime = today.strftime("%H:%M:%S")
    # Время для срабатывания скрипта "Проставить остатки"
    #putDownBalances = today.time().strftime("%H:%M")
    #putDownBalances = (today + datetime.timedelta(minutes=30)).strftime("%H:%M")
    putDownBalances = datetime.time(22, 0).strftime("%H:%M")
    # Время для срабатывания скрипта "Выгрузка товаров на сайт"
    #uploadingpricetoweb = today.time().strftime("%H:%M")
    #uploadingpricetoweb = (today + datetime.timedelta(minutes=60)).strftime("%H:%M")
    uploadingpricetoweb = datetime.time(22, 20).strftime("%H:%M")
    # Время для закрытия таблицы с проставлением остатков
    #closetable = today.time().strftime("%H:%M")
    closetable = datetime.time(23, 0).strftime("%H:%M")
    # Время для подтверждения новой даты
    #acceptnewday = today.time().strftime("%H:%M")
    acceptnewday = datetime.time(7, 0).strftime("%H:%M")

# Вечный цикл с таймером 0.5 секунд
while True:
    # Время сейчас
    today = datetime.datetime.today()
    todaytime = today.strftime("%H:%M")
    # Запускаем функцию обработки времени
    switcher(todaytime)
    # Засыпаем функцию
    time.sleep(60)