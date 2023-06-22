from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.20.10.7', 61518))

class MyKivyApp(App): # Create a class MyKivyApp  
        
    def build(self):   
        layout = BoxLayout(orientation='vertical')

        btn1 = Button(text = "Discord")  
        btn1.bind(on_press=self.discord) 

        layout.add_widget(btn1)

        btn2 = Button(text = "Steam")  
        btn2.bind(on_press=self.steam) 

        layout.add_widget(btn2)

        btn3 = Button(text = "Music")  
        btn3.bind(on_press=self.music) 

        layout.add_widget(btn3)

        return layout
    
    def discord(self, button):
        client.send(('discord').encode('utf-8'))

    def steam(self, button):
        client.send(('steam').encode('utf-8'))

    def music(self, button):
        client.send(('music').encode('utf-8'))


start = MyKivyApp()
start.run()  # Class MyKivyApp is initialized and run () method is called to run the App.  


    
