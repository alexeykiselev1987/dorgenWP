from time import sleep
import webbrowser
import os
import time
import pyautogui, sys
import shutil
logins=open("C:\\doorways\\logins.txt", "r", encoding="utf-8")#логины
passwords=open("C:\\doorways\\passwords.txt", "r", encoding="utf-8")#пароли
x=0
print("Введите количество аккаунтов")
y=int(input())
city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
while x<y:
    if y>1:
        aa=open("C:\doorways\\1.txt", "a+", encoding="utf-8")
        z=str((logins.readline())[0:-1])
        z1=str((passwords.readline())[0:-1])
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        city1=str(city.readline()[0:-1])
        #открытие браузера
        pyautogui.click(x=514, y=1057, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #вход на beget.ru
        pyautogui.click(x=165, y=50, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("https://cp.beget.com/cms",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.press("enter")
        pyautogui.pause=2.5
        time.sleep(5)
        #ввод логина
        pyautogui.click(x=909, y=427, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.typewrite(z,interval=0.1 )
        pyautogui.PAUSE = 2.5
        #ввод пароля
        pyautogui.click(x=930, y=484, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite(z1,interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=946, y=578, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #установка cms
        pyautogui.click(x=1096, y=391, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1000, y=664, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksey",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=989, y=722, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("longuspenisbasisvita",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=991, y=779, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksey.kiselev49631@gmail.com",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=955, y=869, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=951, y=634, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1263, y=393, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1111, y=526, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=550, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=858, y=404, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksey",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1390, y=500, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=850, y=482, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("longuspenisbasisvita",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1063, y=535, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=53, y=426, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=342, y=134, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        #установка плагинов
        pyautogui.click(x=1635, y=195, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("All-in-One WP Migration",interval=0.1 )
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=670, y=306, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(30)
        pyautogui.click(x=654, y=303, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(30)
        #импорт шаблона,обновление
        pyautogui.click(x=72, y=567, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=38, y=542, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=858, y=332, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=786, y=363, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=680, y=42, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("C:\\doorways", interval=0.1 )#настроить
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=412, y=477, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("landings.wpress",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=777, y=505, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(100)
        pyautogui.click(x=1094, y=635, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(30)
        pyautogui.click(x=1067, y=624, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=84, y=45, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        #вход в админку
        pyautogui.click(x=744, y=405, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=653, y=346, clicks=1, interval=1, button='left')
        #ввод логина
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=858, y=404, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksanderkon0waloff",interval=0.1 )
        pyautogui.PAUSE = 2.5
        #ввод пароля
        pyautogui.click(x=1390, y=500, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=850, y=482, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("longuspenisbasisvita",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1063, y=535, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=77, y=242, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=266, y=424, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #вторая часть
        pyautogui.click(x=1593, y=159, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.mouseDown(button = 'left', x=1433, y=216)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=191, y=215)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=191, y=215)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.hotkey("Shift","Alt")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        while w<words:#тайтл
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                words=words-1
        pyautogui.scroll(-1100)
        pyautogui.PAUSE =2.5
        pyautogui.click(x=100, y=718, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.scroll(-1100)
        pyautogui.PAUSE =2.5
        pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.mouseDown(button = 'left', x=681, y=422)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=53, y=422)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=53, y=422)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=2
        while w<words:#сниппет 1
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.PAUSE =2.5
                words=words-1
        pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.mouseDown(button = 'left', x=681, y=609)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=53, y=609)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=53, y=609)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        while w<words:#сниппет 2
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
        pyautogui.click(x=1759, y=98, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1759, y=98, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(15)
        pyautogui.click(x=29, y=96, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(10)
        pyautogui.click(x=84, y=83, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(10)
        pyautogui.click(x=367, y=87, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(5)
        pyautogui.click(x=39, y=394, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(5)
        pyautogui.click(x=48, y=224, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(5)
        pyautogui.scroll(-1100)
        pyautogui.mouseDown(button = 'left', x=320, y=755)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=15, y=755)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=15, y=755)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=15, y=755, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        while w<words:#шапка 1
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1+" ")
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE =2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                words=words-1
        pyautogui.mouseDown(button = 'left', x=320, y=934)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=15, y=934)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=15, y=934)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=15, y=934, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        while w<words:#шапка2
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1+" ")
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1+" ")
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                words=words-1
        pyautogui.click(x=256, y=91, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=470, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=230, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.hotkey("Shift","Alt")
        pyautogui.PAUSE =2.5
        time.sleep(10)
        pyautogui.click(x=514, y=1057, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #вход на beget.ru
        pyautogui.click(x=165, y=50, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("https://cp.beget.com/cms",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.press("enter")
        #подгрузка гугл файла
        pyautogui.click(x=434, y=266, clicks=1, interval=1, button='left')#меню бегет
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=454, y=311, clicks=1, interval=1, button='left')#файловый менеджер
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=230, y=15, clicks=1, interval=1, button='left')#закрытие первой вкладки
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=700, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1015, y=342, clicks=2, interval=0.5, button='left')#папка
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=1000, y=288, clicks=2, interval=0.5, button='left')#public html
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=600, y=132, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=664, y=364, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=464, y=46, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("C:\\doorways", interval=0.1 )#настроить подгрузку файла
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=412, y=477, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("googleeb143e78b63c030f",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=777, y=505, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=1167, y=787, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=1255, y=780, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=469, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #внесение sitemap
        pyautogui.click(x=1263, y=393, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1111, y=526, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=41, y=704, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=333, y=320, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=304, y=787, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=630, y=817, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #регистрация в гугле
        #вход на google.com
        pyautogui.click(x=400, y=51, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("google search console",interval=0.1 )
        pyautogui.PAUSE =2.5
        pyautogui.press("Enter")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=240, y=280, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=373, y=759, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=260, y=165, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=100, y=680, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1045, y=650, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("http://"+z+".beget.tech",interval=0.1 )#!настроить
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1133, y=748, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1168, y=675, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=113, y=440, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("post-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("page-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("categori-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("author-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=400, y=51, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("https://cp.beget.com/cms",interval=0.1 )
        pyautogui.PAUSE =2.5
        pyautogui.press("Enter")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=1512, y=118, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=230, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        y=y-1
        time.sleep(10)
    elif y==1:
        z=str((logins.readline()))
        z1=str((passwords.readline()))
        city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        city1=str(city.readline()[0:-1])
        #открытие браузера
        pyautogui.click(x=514, y=1057, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #вход на beget.ru
        pyautogui.click(x=165, y=50, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("https://cp.beget.com/cms",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.press("enter")
        #ввод логина
        pyautogui.click(x=1251, y=228, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=953, y=238, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite(z,interval=0.1 )
        pyautogui.PAUSE = 2.5
        #ввод пароля
        pyautogui.click(x=969, y=293, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite(z1,interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=842, y=374, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #установка cms
        pyautogui.click(x=1096, y=391, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1000, y=664, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksey",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=989, y=722, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("longuspenisbasisvita",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=991, y=779, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksey.kiselev49631@gmail.com",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=955, y=869, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=951, y=634, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1263, y=393, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1111, y=526, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=550, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=858, y=404, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksey",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1390, y=500, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=850, y=482, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("longuspenisbasisvita",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1063, y=535, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=53, y=426, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=342, y=134, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        #установка плагинов
        pyautogui.click(x=1635, y=195, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("All-in-One WP Migration",interval=0.1 )
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=670, y=306, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(30)
        pyautogui.click(x=654, y=303, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(30)
        #импорт шаблона,обновление
        pyautogui.click(x=72, y=567, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=38, y=542, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=858, y=332, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=786, y=363, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=680, y=42, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("C:\\doorways", interval=0.1 )#настроить
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=412, y=477, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("landings.wpress",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=777, y=505, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(100)
        pyautogui.click(x=1094, y=635, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(30)
        pyautogui.click(x=1067, y=624, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=84, y=45, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        #вход в админку
        pyautogui.click(x=744, y=405, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=653, y=346, clicks=1, interval=1, button='left')
        #ввод логина
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=858, y=404, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("aleksanderkon0waloff",interval=0.1 )
        pyautogui.PAUSE = 2.5
        #ввод пароля
        pyautogui.click(x=1390, y=500, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=850, y=482, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("longuspenisbasisvita",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1063, y=535, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=77, y=242, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=266, y=424, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #вторая часть
        pyautogui.click(x=1593, y=159, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.mouseDown(button = 'left', x=1433, y=216)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=191, y=215)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=191, y=215)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.hotkey("Shift","Alt")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        city1=str(city.readline()[0:-1])
        while w<words:#тайтл
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=1433, y=216, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                words=words-1
        pyautogui.scroll(-1100)
        pyautogui.PAUSE =2.5
        pyautogui.click(x=100, y=718, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.scroll(-1100)
        pyautogui.PAUSE =2.5
        pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.mouseDown(button = 'left', x=681, y=422)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=53, y=422)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=53, y=422)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=2
        city1=str(city.readline()[0:-1])
        while w<words:#сниппет 1
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.click(x=681, y=422, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.PAUSE =2.5
                words=words-1
        pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.mouseDown(button = 'left', x=681, y=609)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=53, y=609)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=53, y=609)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        city1=str(city.readline()[0:-1])
        while w<words:#сниппет 2
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.typewrite(", ", interval=0.1)
                pyautogui.PAUSE= 2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                pyautogui.hotkey("Shift","Alt")
                pyautogui.PAUSE =2.5
                pyautogui.click(x=682, y=609, clicks=1, interval=1, button='left')
                pyautogui.PAUSE = 2.5
                words=words-1
        pyautogui.click(x=1759, y=98, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1759, y=98, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(15)
        pyautogui.click(x=29, y=96, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(10)
        pyautogui.click(x=84, y=83, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(10)
        pyautogui.click(x=367, y=87, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(5)
        pyautogui.click(x=39, y=394, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(5)
        pyautogui.click(x=48, y=224, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5 
        time.sleep(5)
        pyautogui.scroll(-1100)
        pyautogui.mouseDown(button = 'left', x=320, y=755)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=15, y=755)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=15, y=755)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=15, y=755, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        city1=str(city.readline()[0:-1])
        while w<words:#шапка 1
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1+" ")
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE =2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1)
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                words=words-1
        pyautogui.mouseDown(button = 'left', x=320, y=934)
        pyautogui.PAUSE = 2.5
        pyautogui.moveTo(x=15, y=934)
        pyautogui.PAUSE = 2.5
        pyautogui.mouseUp(button = 'left', x=15, y=934)
        pyautogui.PAUSE =2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=15, y=934, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        city=open("C:\\doorways\\города.txt", "r", encoding="utf-8")#подгрузка городов
        keywords=open("C:\\doorways\\keywords.txt", "r", encoding="utf-8")#подгрузка ключевиков
        w=0
        words=3
        city1=str(city.readline()[0:-1])
        while w<words:#шапка2
            if words>1:
                keywords1=str(keywords.readline()[0:-1])
                kc=str(keywords1+" "+city1+" ")
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                words=words-1
            elif words==1:
                keywords1=str(keywords.readline())
                kc=str(keywords1+" "+city1+" ")
                pyautogui.typewrite(kc, interval=0.1)
                pyautogui.PAUSE= 2.5
                words=words-1
        pyautogui.click(x=256, y=91, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=470, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=230, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.hotkey("Shift","Alt")
        pyautogui.PAUSE =2.5
        time.sleep(10)
        pyautogui.click(x=514, y=1057, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #вход на beget.ru
        pyautogui.click(x=165, y=50, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("https://cp.beget.com/cms",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.press("enter")
        #подгрузка гугл файла
        pyautogui.click(x=434, y=266, clicks=1, interval=1, button='left')#меню бегет
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=454, y=311, clicks=1, interval=1, button='left')#файловый менеджер
        pyautogui.PAUSE = 2.5
        time.sleep(10)
        pyautogui.click(x=230, y=15, clicks=1, interval=1, button='left')#закрытие первой вкладки
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=700, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1015, y=342, clicks=2, interval=1, button='left')#папка
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=1000, y=288, clicks=2, interval=1, button='left')#public html
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=600, y=132, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=664, y=364, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=464, y=46, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("C:\\doorways", interval=0.1 )#настроить подгрузку файла
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=412, y=477, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("googleeb143e78b63c030f",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=777, y=505, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=1167, y=787, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        time.sleep(5)
        pyautogui.click(x=1255, y=780, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=469, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #внесение sitemap
        pyautogui.click(x=1263, y=393, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1111, y=526, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=41, y=704, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=333, y=320, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=304, y=787, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=630, y=817, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        #регистрация в гугле
        #вход на google.com
        pyautogui.click(x=400, y=51, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("google search console",interval=0.1 )
        pyautogui.PAUSE =2.5
        pyautogui.press("Enter")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=240, y=280, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=373, y=759, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=260, y=165, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=100, y=680, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1045, y=650, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("http://"+z+".beget.tech",interval=0.1 )#!настроить
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1133, y=748, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1168, y=675, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=113, y=440, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("post-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("page-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("categori-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.typewrite("author-sitemap.xml",interval=0.1 )
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1500, y=300, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=1200, y=648, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=892, y=309, clicks=2, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=400, y=51, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.press("Backspace")
        pyautogui.PAUSE =2.5
        pyautogui.typewrite("https://cp.beget.com/cms",interval=0.1 )
        pyautogui.PAUSE =2.5
        pyautogui.press("Enter")
        pyautogui.PAUSE =2.5
        pyautogui.click(x=1512, y=118, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        pyautogui.click(x=230, y=15, clicks=1, interval=1, button='left')
        pyautogui.PAUSE = 2.5
        y=y-1
        time.sleep(10)
