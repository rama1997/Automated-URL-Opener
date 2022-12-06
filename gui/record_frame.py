import customtkinter
import database
from . import edit_job_frame
import cron

class record_frame(customtkinter.CTkFrame):
	def __init__(self,*args, record_window,header_name, job_id, title, url, frequency, dow, date, hour, minute, am_pm, **kwargs):
		super().__init__(*args, **kwargs)

		self.job_id = job_id
		self.title = title
		self.url = url
		self.frequency = frequency
		self.dow = dow
		self.date = date
		self.hour = hour
		self.minute = minute
		self.am_pm = am_pm
		self.configure(fg_color = "#3c74b5")
		self.record_window = record_window

		self.title_display = customtkinter.CTkLabel(master=self, text="Title: " + title, width=20, wraplength = 140, justify = "left")
		self.title_display.grid(row=0, column=0, padx=5, pady=2, sticky="W")

		self.frequency_display = customtkinter.CTkLabel(master=self, text="Frequency: " + frequency, width=20)
		self.frequency_display.grid(row=1, column=0, padx=5, pady=2, sticky="W")

		if frequency == "Weekly" or frequency == "Biweekly":
			self.day_display = customtkinter.CTkLabel(master=self, text="Day: " + dow, width=20)
			self.day_display.grid(row=2, column=0, padx=5, pady=2, sticky="W")
		elif frequency == "Monthly":
			self.date_display = customtkinter.CTkLabel(master=self, text="Date: " + date, width=20)
			self.date_display.grid(row=2, column=0, padx=5, pady=2, sticky="W")
		else:
			self.date_display = customtkinter.CTkLabel(master=self, text="Date: Everyday", width=20)
			self.date_display.grid(row=2, column=0, padx=5, pady=2, sticky="W")

		self.time_display = customtkinter.CTkLabel(master=self, text="Time: " + hour + ":" + minute + " " + am_pm, width=20)
		self.time_display.grid(row=3, column=0, padx=5, pady=2, sticky="W")

		self.delete_button = customtkinter.CTkButton(self, text="Delete", command=self.delete, fg_color="red")
		self.delete_button.grid(row=5, column=0, padx=5, pady=5,sticky="WN")

		self.edit_button = customtkinter.CTkButton(self, text="Edit", command=self.edit, fg_color="blue")
		self.edit_button.grid(row=4, column=0, padx=5, pady=5,sticky="WN")

	def delete(self):
		database.delete(self.job_id)
		cron.clear_jobs(self.job_id)
		self.record_window.update()
		self.record_window.update_idletasks()
		self.destroy()

	def edit(self):
		window = customtkinter.CTkToplevel(self)
		window.geometry("605x260")
		window.title("Edit " + self.title)
		window.minsize(605,260)
		window.maxsize(605,260)
		window.configure(fg_color = "#271a38")
		window.edit_job_frame = edit_job_frame.edit_job_frame(window, window, header_name="edit_job_frame" , job_id = self.job_id, title=self.title, url=self.url, frequency = self.frequency, dow = self.dow, date=self.date, hour=self.hour, minute=self.minute, am_pm = self.am_pm)
		window.edit_job_frame.grid(row=0, column=0, padx=0, pady=0, sticky="W")
		self.record_window.withdraw()

