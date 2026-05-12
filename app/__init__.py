# Alexandru Cimpoiesu (PM), Shafin Kazi, Mustafa Abdullah, Jalen Chen
# koalas
# SoftDev pd4
# p05
# 2026-06-15


from flask import Flask, render_template, request, session, redirect, url_for, flash
from auth import bp as auth_bp
import sqlite3, os
