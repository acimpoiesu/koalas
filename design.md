
**koalas**

> Alexandru Cimpoiesu (PM), Shafin Kazi, Mustafa Abdullah, Jalen Chen

**Ship Date:** 2026-06-15

# Better Talos
The goal of Better Talos is to help inform Stuy students inform themselves on their classes (e.g. course rigor, course requirements, teacher evaluation, etc). Users can interact with the site by logging in with accounts that they can register. If users are not logged in, they still have access to all the data about each course and can read posts on the public forum. If users are logged in, they can input their own data to be given recommended classes, gpa predictor upon new schedules, access to posting on the forum, etc.

**Components**
1. `login.html`
	* allows users to log into their accounts
	* visible link to register page
	* throws error if:
		* account doesn’t exist
		* incorrect password
2. `register.html`
	* allows users to create an account
	* throws error if:
		* username already exists in db
		* password response doesn’t match with confirm password response
3. `auth.py`
	* handles login/register logic












	# System Blueprint (_a.k.a._ "Design Doc")

	## TNPG: koalas
	## project: Better talos
	## Target ship date: {2026-06-15}

	---

	### roster: Alexandru Cimpoiesu, Shafin Kazi, Mustafa Abdullah, Jalen Chen


	| Name | Email | Primary Role | Secondary Role |
	|---|---|---|---|
	|Alexandru Cimpoiesu|alexandruc4@nycstudents.net | | |
	|Shafin Kazi |shafink3@nycstudents.net | | |
	|Mustafa Abdullah|mustafaa80@nycstudents.net | | |
	|Jalen Chen|jalenc60@nycstudents.net | | |
