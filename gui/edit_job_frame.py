import customtkinter
from . import frequency_option_menu
from . import entry
import cron
import database

class edit_job_frame(customtkinter.CTkFrame):
	def __init__(self, edit_window, *args, header_name, job_id, title, url, frequency, dow, date, hour, minute, am_pm, **kwargs):
		super().__init__(*args, **kwargs)
		self.configure(fg_color = "#271a38")
		self.edit_window = edit_window
		self.job_id = job_id
		self.title_entry = entry.Entry(self, header_name="Title_Entry", name = "Title", placeholder="", fg_color="#271a38")
		self.title_entry.set_value(title)
		self.title_entry.grid(row=0, column=0, padx=20, pady=2, sticky="ew")

		self.url_entry = entry.Entry(self, header_name="URL_Entry", name = "URL", placeholder= "", fg_color="#271a38")
		self.url_entry.set_value(url)
		self.url_entry.grid(row=1, column=0, padx=20, pady=2, sticky="ew")

		self.frequency_option_menu= frequency_option_menu.Frequency_Option_Menu(self, header_name="Frequency_Option_Menu", default="Select Frequency",fg_color="#271a38")
		self.frequency_option_menu.set_value(frequency, dow, date, hour, minute, am_pm)
		self.frequency_option_menu.grid(row=2, column=0, padx=20, pady=2, sticky="ew")

		self.add_button = customtkinter.CTkButton(self, text="Save", command=self.save, width = 40)
		self.add_button.grid(row=3, column=0, padx=10, pady=10)

	def save(self):
		title = self.title_entry.get_value()
		url = self.url_entry.get_value()
		frequency = self.frequency_option_menu.get_value()
		database.update(self.job_id, title, url, frequency)
		self.edit_window.destroy()
		cron.edit_job(self.job_id, url, frequency)
