@echo off
echo Starting Music Recommender Model Training...
echo This will take 5-10 minutes. Please wait...
echo.
cd /d "%~dp0"
C:\Users\Mayank\AppData\Local\Programs\Python\Python39\python.exe src\model\train.py
pause
