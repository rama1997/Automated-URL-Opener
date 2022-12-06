import customtkinter

class Frequency_Option_Menu(customtkinter.CTkFrame):
    def __init__(self, *args, header_name, default, **kwargs):
        super().__init__(*args, **kwargs)

        # Freqeuncy Option Menu
        frequency_options = ["Daily", "Weekly", "Biweekly", "Monthly"]
        self.frequency_label = customtkinter.CTkLabel(master=self, text="Frequency: ", width=20)
        self.frequency_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        frequency_default = customtkinter.StringVar(value=default)  # set initial value
        self.frequency_option_menu = customtkinter.CTkOptionMenu(master=self, values=frequency_options, command=self.frequency_callback, variable=frequency_default)
        self.frequency_option_menu.grid(row=0, column=1,padx=2, pady=10)

        # Date Option Menu
        date_default = customtkinter.StringVar(value="Select Date")
        dates = ["Start of Month", "End of Month"]
        for i in range(1,32):
            dates.append(str(i))
        self.date_label = customtkinter.CTkLabel(master=self, text="Date: ", width=20)
        self.date_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.date_label.grid_forget()
        self.date_option_menu = customtkinter.CTkOptionMenu(master=self, values=dates, variable=date_default)
        self.date_option_menu.grid(row=1, column=1,padx=2, pady=10)
        self.date_option_menu.grid_forget()

        # Days Option Menu
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_default = customtkinter.StringVar(value="Select Day")
        self.day_label = customtkinter.CTkLabel(master=self, text="Day: ", width=20)
        self.day_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.day_label.grid_forget()
        self.day_option_menu = customtkinter.CTkOptionMenu(master=self, values=days, variable=day_default)
        self.day_option_menu.grid(row=2, column=1,padx=2, pady=10)
        self.day_option_menu.grid_forget()

        # Time Option Menu
        self.time_label = customtkinter.CTkLabel(master=self, text="Time: ", width=20)
        self.time_label.grid(row=0, column=3, padx=10, pady=10, sticky="W")
        hour = []
        for i in range(1,13):
            hour.append(str(i))
        hour_default = customtkinter.StringVar(value="12")
        self.hour_option_menu = customtkinter.CTkOptionMenu(master=self, values=hour, variable=hour_default, width = 70)
        self.hour_option_menu.grid(row=0, column=4,padx=2,pady=10,sticky="E")
        minute = ["00", "05"]
        for i in range(10,60,5):
            minute.append(str(i))
        minute_default = customtkinter.StringVar(value="00")
        self.minute_option_menu = customtkinter.CTkOptionMenu(master=self, values=minute, variable=minute_default,width = 70)
        self.minute_option_menu.grid(row=0, column=5,padx=2, pady=10,sticky="W")
        am_pm = ["AM", "PM"]
        am_pm_default = customtkinter.StringVar(value="AM")
        self.am_pm_option_menu = customtkinter.CTkOptionMenu(master=self, values=am_pm, variable=am_pm_default,width = 70)
        self.am_pm_option_menu.grid(row=0, column=6,padx=2, pady=10,sticky="W")

    def frequency_callback(self, choice):
        if choice == "Monthly":
            self.date_option_menu.grid(row=1, column=1,padx=2, pady=10)
            self.date_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
            self.day_option_menu.grid_forget()
            self.day_label.grid_forget()
        elif choice == "Daily":
            self.day_option_menu.grid_forget()
            self.day_label.grid_forget()
            self.date_option_menu.grid_forget()
            self.date_label.grid_forget()
        else:
            self.date_option_menu.grid_forget()
            self.date_label.grid_forget()
            self.day_option_menu.grid(row=2, column=1,padx=2, pady=10)
            self.day_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    def get_value(self):
        """ returns selected values in a dictionary """
        frequency = self.frequency_option_menu.get()
        date = self.date_option_menu.get()
        day = self.day_option_menu.get()
        hour = self.hour_option_menu.get()
        minute = self.minute_option_menu.get()
        am_pm = self.am_pm_option_menu.get()
        return {"Frequency":frequency, "Date":date, "Day":day, "Hour": hour, "Minute": minute, "am_pm":am_pm}

    def reset(self):
        """reset menus to default"""
        self.frequency_option_menu.set("Select Frequency")
        self.day_option_menu.grid_forget()
        self.day_label.grid_forget()
        self.date_option_menu.grid_forget()
        self.date_label.grid_forget()
        self.hour_option_menu.set("12")
        self.minute_option_menu.set("00")
        self.am_pm_option_menu.set("AM")

    def set_value(self, frequency, day, date, hour, minute, am_pm):
        """ selects the corresponding option, selects nothing if no corresponding option"""
        self.frequency_option_menu.set(frequency)
        self.frequency_callback(frequency)
        self.day_option_menu.set(day)
        self.date_option_menu.set(date)
        self.hour_option_menu.set(hour)
        self.minute_option_menu.set(minute)
        self.am_pm_option_menu.set(am_pm)


