from crontab import CronTab
import datetime
import os

# Access user's crontab
cron = CronTab(user=True)

cwd = os.getcwd()
current_time = datetime.datetime.now()
current_week = current_time.strftime("%W")
dow = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}
month = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

def add_job(job_id,url,frequency):
	job = cron.new(command='open "{}"'.format(url), comment=str(job_id))
	schedule(job,url,frequency)
	get_jobs(job_id)

def edit_job(job_id, url, frequency):
	iter = cron.find_comment(str(job_id))
	for job in iter:
		job.clear()
		job.set_command('open "{}"'.format(url))
		schedule(job, url, frequency)
		get_jobs(job_id)

def schedule(job,url,frequency):
	if frequency["Frequency"] == "Daily":
		job.every().day()
	elif frequency["Frequency"]== "Weekly":
		job.dow.on(dow[frequency["Day"]])
	elif frequency["Frequency"] == "Biweekly":
		job.dow.on(dow[frequency["Day"]])
		if int(current_week) % 2 == 1:
			job.set_command('test $((10#$(/usr/local/bin/gdate +%W)%2)) -eq 1 && open "{}"'.format(url))
		else:
			job.set_command('test $((10#$(/usr/local/bin/gdate +%W)%2)) -eq 0 && open "{}"'.format(url))
	elif frequency["Frequency"] == "Monthly":
		if frequency["Date"] == "End of Month":
			job.set_command('[ "$(/usr/local/bin/gdate +%d -d tomorrow)" = "01" ] && open "{}"'.format(url))
			job.setall('30 13 28-31 * *')
		elif frequency["Date"] == "Start of Month":
			job.day.on(1)
		else:
			job.day.on(int(frequency["Date"]))

	job.minute.on(int(frequency["Minute"]))

	# Setting hours relative to AM/PM. Handles 12AM as 0, and every hour in PM as +12
	if frequency["am_pm"] == "AM":
		if int(frequency["Hour"]) == 12:
			job.hour.on(0)
		else:
			job.hour.on(int(frequency["Hour"]))
	else:
		if int(frequency["Hour"]) == 12:
			job.hour.on(int(frequency["Hour"]))
		else:
			job.hour.on(int(frequency["Hour"])+12)

	cron.write()

def get_jobs(job_id):
	iter = cron.find_comment(str(job_id))
	for job in iter:
		print(job)

def clear_jobs(job_id):
	cron.remove_all(comment=str(job_id))
	cron.write()

