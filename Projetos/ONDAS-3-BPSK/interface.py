from Tkinter import *
import Tkinter as tk
import client

class Janela_Principal():



	def __init__(self):
		self.window = tk.Tk()
		self.messages = Text(self.window)
		self.messages.pack()

		self.input_user = StringVar()
		self.input_field = Entry(self.window, text=self.input_user)
		self.input_field.pack(side=BOTTOM, fill=X)
		self.frame = Frame(self.window)  # , width=300, height=300)
		self.input_field.bind("<Return>", self.Enter_pressed)
		self.frame.pack()

	def Enter_pressed(self, event):
	    input_get = self.input_field.get()
	    #print(input_get)
	    self.messages.insert(INSERT, '%s\n' % input_get)
	    self.send(input_get)
	    # label = Label(window, text=input_get)
	    # label.pack()
	    return "break"

	def iniciar(self):
		self.window.mainloop()

	def send(self, message):
		self.client = client.Client()
		self.client.main(message)


app = Janela_Principal()
app.iniciar()	