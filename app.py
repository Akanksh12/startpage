from flask import Flask, render_template, request
from os import mkdir

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    wallpaper_id = request.args.get("id")
    if wallpaper_id != '':
        mkdir(f'themes/{wallpaper_id}')
    print(wallpaper_id)
    return render_template('settings.html')