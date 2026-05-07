
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

#### roster:


| Name | Email | Primary Role | Secondary Role |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

---


# Summary
{Keep it tight. Concise. 1 sentence. Really need more? 3 max.}

## Problem Being Solved


## Target Users

Who will use this system?

- ____________________________________
- ____________________________________


## Why This Project Matters


---

# Minimum Viable Product (MVP) Scope

## Core Features (Required for Final Submission)
Features that **must** be completed:
1.
1.
1.

## Stretch Features (Only if MVP is Complete)
1.
1.
1.

## Explicit Non-Goals

Features intentionally excluded:
-
-

---

# Technology Stack

| Layer | Selected Tool |
|---|---|
| Backend Framework | Flask / Node.js (choose one) |
| Frontend Framework | none / bootstrap / foundation / tailwind / other? (seek clearance) |
| Database | SQLite / MongoDB |
| Authentication | Flask sessions unless you have good reason/need to deviate |
| ORM / DB Library | optionally SQLAlchemy; initiate clearance protocol if interested |

## Why This Stack Was Chosen
{your summary/recap of team discussions here}

---

# Team Ownership Plan

Each member must own meaningful deliverables.

| Team Member | Primary Ownership | Secondary Ownership | Specific Deliverables |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

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
