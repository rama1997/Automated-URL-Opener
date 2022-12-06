import customtkinter
from . import frequency_option_menu
from . import entry
import cron
import database

class add_job_frame(customtkinter.CTkFrame):
	def __init__(self, *args, header_name, **kwargs):
		super().__init__(*args, **kwargs)

		self.title_entry = entry.Entry(self, header_name="Title_Entry", name = "Title", placeholder="Enter Title", fg_color="#271a38")
		self.title_entry.grid(row=0, column=0, padx=20, pady=2, sticky="ew")

		self.url_entry = entry.Entry(self, header_name="URL_Entry", name = "URL", placeholder="Enter URL", fg_color="#271a38")
		self.url_entry.grid(row=1, column=0, padx=20, pady=2, sticky="ew")

		self.frequency_option_menu= frequency_option_menu.Frequency_Option_Menu(self, header_name="Frequency_Option_Menu", default="Select Frequency", fg_color="#271a38")
		self.frequency_option_menu.grid(row=2, column=0, padx=20, pady=2, sticky="ew")

		self.add_button = customtkinter.CTkButton(self, text="Add", command=self.add_link, width = 40)
		self.add_button.grid(row=3, column=0, padx=10, pady=10)

	def add_link(self):
		# Get values from input
		title = self.title_entry.get_value()
		url = self.url_entry.get_value()
		frequency = self.frequency_option_menu.get_value()

		# Add to database, returns the job id for newly added job
		job_id = database.add(title,url,frequency)

		# Add to crontab
		cron.schedule(job_id,title,url, frequency)

		# Reset form
		self.title_entry.reset()
		self.url_entry.reset()
		self.frequency_option_menu.reset()

