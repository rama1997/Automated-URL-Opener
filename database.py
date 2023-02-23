import sqlite3

database_path = "/Users/ray/Documents/CS/Scripts/Automated-URL-Opener/db/database.db"

def create_db():
	# Create a database automatically or connect to existing one
	conn = sqlite3.connect(database_path)

	# Create cursor; something that will do actions for us
	cursor = conn.cursor()

	# Create Table - only needs to be ran once
	cursor.execute("""CREATE TABLE urls (
		title text,
		url text,
		frequency text,
		dow text,
		date_month text,
		hour text,
		minute text,
		am_pm text
		)""")

	# Commit Changes
	conn.commit()

	# Close connection
	conn.close()

def add(title,url,frequency):
	conn = sqlite3.connect(database_path)
	cursor = conn.cursor()

	cursor.execute("INSERT INTO urls VALUES (:title, :url, :frequency, :dow, :date_month, :hour, :minute, :am_pm) ",
			{
				'title': title,
				'url': url,
				'frequency': frequency["Frequency"],
				'dow': frequency["Day"],
				'date_month': frequency["Date"],
				'hour': frequency["Hour"],
				'minute': frequency["Minute"],
				'am_pm': frequency["am_pm"]
			})

	recent_id = cursor.lastrowid
	conn.commit()
	conn.close()
	return recent_id

def delete(id):
	conn = sqlite3.connect(database_path)
	cursor = conn.cursor()

	cursor.execute("DELETE from urls WHERE oid = " + str(id))

	conn.commit()
	conn.close()

def update(job_id, title, url, frequency):
	conn = sqlite3.connect(database_path)
	cursor = conn.cursor()

	cursor.execute("""UPDATE urls SET
		title = :title,
		url = :url,
		frequency = :frequency,
		dow = :dow,
		date_month = :date_month,
		hour = :hour,
		minute = :minute,
		am_pm = :am_pm

		WHERE oid = :oid""",
		{
			'title': title,
			'url': url,
			'frequency': frequency["Frequency"],
			'dow': frequency["Day"],
			'date_month': frequency["Date"],
			'hour': frequency["Hour"],
			'minute': frequency["Minute"],
			'am_pm': frequency["am_pm"],
			'oid': job_id
		})

	conn.commit()
	conn.close()

def query_all():
	conn = sqlite3.connect(database_path)
	cursor = conn.cursor()

	cursor.execute("SELECT *, oid FROM urls")
	records = cursor.fetchall()

	conn.commit()
	conn.close()
	return records

def query_id(job_id):
	conn = sqlite3.connect(database_path)
	cursor = conn.cursor()

	cursor.execute("SELECT * FROM urls WHERE oid = " + str(job_id))
	record = cursor.fetchall()

	conn.commit()
	conn.close()
	return record