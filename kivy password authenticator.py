#password checker
import numpy as np
import pandas
import sklearn

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen


def apendder(input):
	data=[]
	data.append(input)
	return data
class passapp(App):
	def build (self):
		self.sm=ScreenManager()
		screen2=Screen(name="next")
		screen3=Screen(name="welcome")
		screen1=Screen()
		self.sm.add_widget(screen1)
		self.sm.add_widget(screen2)
		self.sm.add_widget(screen3)
		box=BoxLayout(orientation="vertical")
		box2=BoxLayout(orientation="vertical")
		screen1.add_widget(box)
		screen2.add_widget(box2)
		dat=np.arange(20).reshape((5,4))
		screen3.add_widget(Label(text=str(dat),font_size="20"))
		self.input=TextInput(font_size="50",password=True,hint_text="please enter password")
		self.input2=TextInput(font_size="50",password=True,hint_text="please enter password")
		grid=GridLayout(cols=2)
		grid2=GridLayout(cols=2)
		grid.add_widget(Label(text="Password",font_size="50"))
		grid.add_widget(self.input)
		box.add_widget(grid)
		box.add_widget(Button(text="signup",font_size="50",on_press=self.change))
		#scrern 2 widgets
		self.labelo=Label(text="",font_size="20")
		box2.add_widget(self.labelo)
		grid2.add_widget(self.input2)
		box2.add_widget(grid2)
		box2.add_widget(Button(text="login",font_size="50",on_press=self.login))
		box2.add_widget(Button(text="clear",font_size="50",on_press=self.clear))
		
		return self.sm
	
	def change (self,obj):
		if self.input.text=="":
			return " "
		else:
			self.sm.current="next"
			global grin
			grin=apendder(self.input.text)

	def clear(self,obj):
		self.labelo.text=""
		self.input2.text=""
				
	def login(self,obj):
		checker=self.input2.text
		if checker =="":
			self.labelo.text="NO INPUT RECOGNIZED"
		elif checker in grin:
			self.sm.current="welcome"
		else:
			self.labelo.text="WRONG PASSWORD"
			
			
		
			
			
			
			
			
		
passapp().run()