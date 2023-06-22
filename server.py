import socket
import webbrowser
import os
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('172.20.10.7', 61518))

server.listen()

while True:
    user, adres = server.accept()

    while True:
        data = user.recv(1024).decode('utf-8').lower()
        print(data)

        match data:
            case 'discord':
                # starts discord app via link
                os.startfile(r"C:\Users\Aspidov Pavel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")
                continue
            case 'steam':
                # starts steam app via link
                os.startfile(r'C:\Users\Aspidov Pavel\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk')
                continue
            case 'music':
                # open tab in browser
                webbrowser.open('https://www.youtube.com/watch?v=Vr-DOV-TP5s&pp=ygUo0YHQtdGA0LXQs9CwINC_0LjRgNCw0YIg0LDQv9C10LvRjNGB0LjQvQ%3D%3D')
                continue