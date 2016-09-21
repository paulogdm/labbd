from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition


from dbapi import DBApi
 

class MainApp(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
        self.manager.get_screen('login').disconnect()

