

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
	## project: Better Talos
	## Target ship date: {2026-06-15}

	---

	### roster: Alexandru Cimpoiesu, Shafin Kazi, Mustafa Abdullah, Jalen Chen


	| Name | Email | Primary Role | Secondary Role |
	|---|---|---|---|
	| Alexandru Cimpoiesu|alexandruc4@nycstudents.net | Database organizer/parser | Grade prediction algorithm developer |
	| Shafin Kazi |shafink3@nycstudents.net | Javascript  | (Secondary) frontend designer  |
	| Mustafa Abdullah|mustafaa80@nycstudents.net | API Integration/JS |(Secondary) frontend designer  |
	| Jalen Chen|jalenc60@nycstudents.net | Frontend designer  | Secondary database parser  |

	---


# Summary
Better Talos is to help inform Stuy students inform themselves on their classes (e.g. course rigor, course requirements, teacher evaluation, etc) and engage in public forms to discuss all things Stuy. 

## Problem Being Solved
Talos does not present all of the information that students might need in an easy/meaningful way. Students might have to socialize with others in order to gleam information about courses/teachers and better inform themselves on which classes to take or not to take. 

## Target Users

Who will use this system?

- Current Stuyvesant students 
- Current Stuyvesant administration (guidance counselors, program office)


## Why This Project Matters

The project would help students better map out their academic path over the course of their 4 years at Stuyvesant as opposed to the current rudimentary system of blindly picking courses through Talos.

--- 

# Minimum Viable Product (MVP) Scope

## Core Features (Required for Final Submission)
Features that **must** be completed:
1. Online message board for discussion
2. Information on each course and teacher
3. Prerequisites for each course 

## Stretch Features (Only if MVP is Complete)
1. Class Grade predictor 
2. idk something 

## Explicit Non-Goals

Features intentionally excluded:
- 
-

---

# Technology Stack

| Layer | Selected Tool |
|---|---|
| Backend Framework | Flask |
| Frontend Framework | tailwind |
| Database | SQLite|
| Authentication | Flask sessions |
| ORM / DB Library | N/A |

## Why This Stack Was Chosen
We chose most of these options because they are what we are most comfortable and familiar with. Tailwind offers easy, customizable, and lightweight designing. 

---

# Team Ownership Plan

Each member must own meaningful deliverables.

| Team Member | Primary Ownership | Secondary Ownership | Specific Deliverables |
|---|---|---|---|
| Alexandru | | | |
| Shafin | | | |
| 'Stafa | | | |
| Jalen | | | |

---

# Component map

{Insert your mermaid(or equivalent)-generated diagram here}

# Site map

{Insert your mermaid(or equivalent)-generated diagram here}
eg...
```
Landing Page
   ↓
Login / Register
   ↓
Dashboard
   ├── Feature A
   ├── Feature B
   └── Profile
```

## Key User Stories
### eg0
As a __________, I want to __________ so that...

### eg1
As a __________, I want to __________ so that...

### eg2
As a __________, I want to __________ so that...



# Database Design

{Insert your table/document organizational structure here}


# Testing Plan
{Delineate here your plan for testing each component}

# Timeline
## Week 1 Goals:
## Week 2 Goals:
## Week 3 Goals:
## Internal Deadlines:
{List milestones your team has identified, in the order they must be completed. Set a target completion date for each.}


# Completion Criteria (_a.k.a._ "Definition of 'Done'")
Project is considered complete when all of the following are true:
1.
1.
1.

# Open Questions
{Delineate anything undecided here}

# Appendix
{Any relevant info that is useful but would have interrupted narrative flow above, or cluttered the information portrayed}

# Other
{Put here anything that did not sensibly fit under above headings. This section will inform evolution of SoftDev.}

