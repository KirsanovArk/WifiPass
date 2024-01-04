import subprocess #для возможности запуска процессов программ и передачи аргументов из них в мой проект


#бэкэенд программы
def passw():
    try:
        data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
        wifi=[i.split(':')[1][1:-1]for i in data if 'Все профили пользователей' in i]
        passwifi = '' #переменная для сохранения полученных данных
        for i in wifi:
            result = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('cp866').split('\n')
            for k in result:
                if "Содержимое ключа" in k:
                            passwifi += f'{i}--{k.split(':')[1][1:-1]}\n'
                            print(passwifi)
    except Exception as ex: print(f'Ошибка: {ex}')
    password_label.config(text='WiFi&Passwords:\n'+str(passwifi))

from tkinter import *
app= Tk()

app.title('PassWifi')
app.geometry('300x400')

button=Button(app,text='Нажать чтобы начать',font=40,command=passw)
button.pack(side=BOTTOM,pady=40)

password_label= Label(app,text='WiFi&Passwords:\n-',font=35)
password_label.pack(pady=(50,0))

app.mainloop()



