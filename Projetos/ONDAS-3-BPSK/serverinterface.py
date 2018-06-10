from Tkinter import *
import Tkinter as tk
import server
import threading

class Janela_Principal():

	def __init__(self):
		self.window = tk.Tk()
		self.messages = Text(self.window)
		self.messages.pack()

		self.input_user = StringVar()
		self.input_field = Entry(self.window, text=self.input_user)
		self.input_field.pack(side=BOTTOM, fill=X)
		self.frame = Frame(self.window)  # , width=300, height=300)
		self.frame.pack()

		self.receive()





	def iniciar(self):
		self.window.mainloop()

	def receive(self):
		self.server = server.Server()
		self.server.connectSocket()
		self.start_thread()

	def thread(self):
		while True:
			texto = self.server.receberTexto()
			self.messages.insert(INSERT, '%s' %  texto)

	def start_thread(self):
		print("iniciado")
		self.thread = threading.Thread(target=self.thread, args=())
		self.thread.start()




app = Janela_Principal()
app.iniciar()	
