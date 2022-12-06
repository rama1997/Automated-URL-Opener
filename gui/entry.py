import customtkinter

class Entry(customtkinter.CTkFrame):
	def __init__(self, *args, header_name, name, placeholder, **kwargs):
		super().__init__(*args, **kwargs)

		self.label = customtkinter.CTkLabel(master=self, text=name+":", width=20)
		self.label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

		self.entry = customtkinter.CTkEntry(master=self, placeholder_text=placeholder, width=500)
		self.entry.grid(row=0, column=1,padx=2, pady=10)

	def get_value(self):
		""" returns selected value as a string, returns an empty string if nothing selected """
		return self.entry.get()

	def reset(self):
		self.entry.delete(0, len(self.get_value()))

	def set_value(self,text):
		self.entry.insert(0,text)

