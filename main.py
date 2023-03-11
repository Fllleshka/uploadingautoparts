import time
import pyautogui
import datetime

# Включение паузы 1.5 секунды между действиями
pyautogui.PAUSE = 1

# Функция перемещения мышки и кликов
def movemouse(massx, massy):
    for elem in range(0, len(massx)):
        print(f'{elem + 1}\t\t[{massx[elem]}]\t[{massy[elem]}]')
        pyautogui.moveTo(massx[elem], massy[elem], duration=0.25)
        pyautogui.leftClick()

# Функция выбора действия от времени
def switcher(argument):
    match argument:
        # Время сканирования папки
        case times.putDownBalances:
            # [0] Перемещение к свёрнотому рабочему столу
            # [1] Перемещение к вкладке "Проставить остатки"
            # [2] Перемещение к кнопке "Сформировать"
            # [3] # Перемещение к сворачиванию удалённого рабочего стола
            massx = [260, 960, 200, 100, 1160]
            massy = [1060, 540, 1005, 270, 10]
            movemouse(massx, massy)
            # Средующее время выполения операции
            times.putDownBalances = datetime.time(22, 0).strftime("%H:%M")
        case times.uploadingpricetoweb:
            # [0] Перемещение к свёрнотому рабочему столу
            # [1] Перемещение к вкладке "Выгрузка товаров на сайт"
            # [2] Перемещение к кнопке "Сформировать"
            # [3] # Перемещение к сворачиванию удалённого рабочего стола
            massx = [260, 960, 400, 100, 1160]
            massy = [1060, 540, 1005, 300, 10]
            movemouse(massx, massy)
            times.uploadingpricetoweb = datetime.time(22, 20).strftime("%H:%M")
        # Время которое не выбрано для события
        case default:
            return print("Время сейчас:\t",argument)

# Класс времён
class times:
    # Время сейчас
    today = datetime.datetime.today()
    todaytime = today.strftime("%H:%M:%S")
    # Время для срабатывания скрипта "Проставить остатки"
    putDownBalances = today.time().strftime("%H:%M")
    #putDownBalances = (today + datetime.timedelta(minutes=1)).strftime("%H:%M")
    # Время для срабатывания скрипта "Выгрузка товаров на сайт"
    uploadingpricetoweb = (today + datetime.timedelta(minutes=5)).strftime("%H:%M")

# Вечный цикл с таймером 0.5 секунд
while True:
    # Время сейчас
    today = datetime.datetime.today()
    todaytime = today.strftime("%H:%M")
    # Запускаем функцию обработки времени
    switcher(todaytime)
    # Засыпаем функцию
    time.sleep(60)