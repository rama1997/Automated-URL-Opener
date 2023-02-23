import customtkinter
import tkinter as tk
from gui import add_job_frame, record_frame
import cron
import database as db
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		self.geometry("605x310")
		self.title("URL Task Scheduler")
		self.minsize(605,310)
		self.maxsize(605,310)
		self.configure(fg_color = "#271a38")

		self.new_job_frame = add_job_frame.add_job_frame(self, header_name="add_job_frame",fg_color="#271a38")
		self.new_job_frame.grid(row=0, column=0, padx=0, pady=0, sticky="W")

		self.get_button = customtkinter.CTkButton(self, text="Show All Scheduled Jobs", command=self.show_records, width = 40, fg_color="green")
		self.get_button.grid(row=1, column=0, padx=10, pady=10)

		if not os.path.exists(db.database_path):
			db.create_db()

	def show_records(self):
		self.window = customtkinter.CTkToplevel(self)
		self.window.geometry("600x430")
		width = 510
		height = 500
		self.window.minsize(width, height)
		self.window.maxsize(width, height)
		self.window.grid_columnconfigure(4, weight=1)
		self.window.title("Existing Jobs")
		records = db.query_all()

		# Create a frame for the canvas with non-zero row&column weights
		frame_canvas = tk.Frame(self.window)
		frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
		frame_canvas.grid_rowconfigure(0, weight=1)
		frame_canvas.grid_columnconfigure(0, weight=1)
		# Set grid_propagate to False to allow resizing later
		frame_canvas.grid_propagate(False)

		# Add a canvas in that frame
		canvas = tk.Canvas(frame_canvas)
		canvas.grid(row=0, column=0, sticky="news")

		# Link a scrollbar to the canvas
		vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
		vsb.grid(row=0, column=1, sticky='ns')
		canvas.configure(yscrollcommand=vsb.set)

		# Create a frame to contain the record
		frame_records = tk.Frame(canvas)
		canvas.create_window((0, 0), window=frame_records, anchor='nw')

		# Add records to the frame
		rows = 3
		columns = 3
		k = 0
		for i in range(0, rows):
			for j in range(0, columns):
				if k < len(records):
					record = records[k]
					record_display = record_frame.record_frame(frame_records, record_window= self.window, header_name=str(record[8]) + "_frame", job_id=record[8], title=record[0], url=record[1], frequency=record[2], dow=record[3], date=record[4], hour=record[5], minute=record[6], am_pm=record[7])
					record_display.grid(row=i, column=j, padx=5, pady=5, sticky="news")
					k+=1
				else:
					break

		# Update buttons frames idle tasks to let tkinter calculate buttons sizes
		frame_records.update_idletasks()

		# Resize the canvas frame
		frame_canvas.config(width=width-10,height=height)

		# Set the canvas scrolling region
		canvas.config(scrollregion=canvas.bbox("all"))


if __name__ == "__main__":
	app = App()
	app.mainloop()