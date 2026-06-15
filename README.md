# BetterTalos by koalas

# Roster

- Alexandru Cimpoiesu (PM)
- Shafin Kazi
- Mustafa Abdullah
- Jalen Chen

# Description
Better Talos is to help inform Stuy students inform themselves on their classes (e.g. course rigor, course requirements, teacher evaluation, etc) and engage in public forums to discuss all things Stuy. Users can login and register accounts. Users can navigate to pages for certain classes which include details like the teacher(s), course description, and user submitted anecdotes on the class. They can build a schedule for their 4 years at Stuy and see a graph of all the prerequisites for courses.

#### Visit our live site at [koalas.me](https://koalas.me)

### Install Guide:
Pre-Requisites:
  - python3 installed
  - git installed

1. Clone the repository:
```
git clone git@github.com:acimpoiesu/koalas.git
```
2. Navigate into directory:
```
cd koalas
```
3. Create virtual environment:
```
python3 -m venv venv
```
4. Activate virutal environment:

macOS/Linux:
```
. venv/bin/activate
```
Windows:
```
venv/Scripts/activate
```
5. Install dependencies:
```
pip install -r requirements.txt
```

### Launch Codes:
1. Build the database
```
python3 app/build_db.py
```
2. Run the app
```
python3 app/__init__.py
```
