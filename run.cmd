echo off
pip install pyjosa
color 0a
cls
start cmd.exe @cmd /k "python web.py"
cd templates
start http://localhost:5000