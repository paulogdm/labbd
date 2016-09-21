from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
import cx_Oracle

from app import MainApp
from dbapi import DBApi


class Login(Screen):
	def do_login(self, loginText, passwordText):

		app = App.get_running_app()

		app.username = loginText
		app.password = passwordText

		try:
			self.oracledb = DBApi(app.username, app.password)
		
		except cx_Oracle.DatabaseError as e:
			error, = e.args


		self.manager.transition = SlideTransition(direction="left")
		self.manager.current = 'MainApp'

		app.config.read(app.get_application_config())
		app.config.write()

	def disconnect(self):
		self.oracledb.disconnect()

	def resetForm(self):
		self.ids['login'].text = ""
		self.ids['password'].text = ""

class LoginApp(App):
	username = StringProperty(None)
	password = StringProperty(None)

	def build(self):
		manager = ScreenManager()

		manager.add_widget(Login(name='login'))
		manager.add_widget(MainApp(name='MainApp'))

		return manager

	def get_application_config(self):
		if(not self.username):
			return super(LoginApp, self).get_application_config()

		conf_directory = self.user_data_dir + '/' + self.username

		if(not os.path.exists(conf_directory)):
			os.makedirs(conf_directory)

		return super(LoginApp, self).get_application_config(
			'%s/config.cfg' % (conf_directory)
		)

if __name__ == '__main__':
	LoginApp().run()