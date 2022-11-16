echo off
python -m pip install pyjosa
python -m pip install flask
python -m pip install request
python -m pip install render_template
python -m pip install jsonify
color 0a
cls
start cmd.exe @cmd /k "python web.py"
cd templates
start http://localhost:5000