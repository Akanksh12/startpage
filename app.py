from flask import Flask, render_template, request, make_response
from os import mkdir
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    wallpaper_id = request.args.get("id")
    if wallpaper_id == None:
        return render_template('settings.html')
    try:
        mkdir(f'themes/{wallpaper_id}')
    except FileExistsError:
        pass
    req = requests.get(f'https://wallhaven.cc/api/v1/w/{wallpaper_id}')
    req = req.json()
    with open(f'themes/{wallpaper_id}/info.json', 'w+') as file:
        json.dump(req, file)
    wallpaper = requests.get(req['data']['path'])
    with open(f'themes/{wallpaper_id}/wallpaper.png', 'wb') as file:
        file.write(wallpaper.content)
    return render_template('settings.html')