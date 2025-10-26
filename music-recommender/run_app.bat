@echo off
echo Starting Music Recommender App...
echo.
cd /d "%~dp0"
C:\Users\Mayank\AppData\Local\Programs\Python\Python39\python.exe -m streamlit run src\app.py
pause
