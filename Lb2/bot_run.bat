@echo off
call %~dp0venv\Scripts\activate
cd .

set TOKEN = 5881834952:AAFGhZRozjHOBHsfAfO7wN5CRgvlegTWWTw

python bot_telegram.py

pause