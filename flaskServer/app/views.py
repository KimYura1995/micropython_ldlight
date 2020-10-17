import requests
import json
from flask import render_template, request

from app import app


MAIN_INITIAL_SETTINGS = {
    'led_brightness': 0,
    'led_status': 0,
}

STATIC_MODE_SETTINGS = {
    'red_color': 0,
    'green_color': 0,
    'blue_color': 0,
}
STATIC_MODE_SETTINGS.update(MAIN_INITIAL_SETTINGS)

RAINBOW_MODE_SETTINGS = {
    'rainbow_step': 0,
}
STATIC_MODE_SETTINGS.update(MAIN_INITIAL_SETTINGS)

BREATH_MODE_SETTINGS = {
    'min_brightness': 0,
    'max_brightness': 0,
    'breath_step': 0,
    'red_color': 0,
    'green_color': 0,
    'blue_color': 0,
}
BREATH_MODE_SETTINGS.update(MAIN_INITIAL_SETTINGS)


@app.route('/', methods=['GET', 'POST'])
def index():
    global MAIN_INITIAL_SETTINGS

    if request.method == 'POST':
        params = {}
        main_switch = request.form.get('main_switch')
        brightness = request.form.get('brightness')
        save = request.form.get('save')

        # main switch
        if main_switch:
            if main_switch == 'on':
                status = 1
            else:
                status = 0
            params = {'led_status': status}

        # brightness
        if brightness:
            params = {'led_brightness': brightness}

        if save:
            params = {'save': 'save'}

        # GET request to NodeMCU
        requests.get('http://192.168.0.146/', params=params)

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    if request.method == 'GET':
        try:
            response = requests.get('http://192.168.0.146/', params={'main_settings': 'get'}, timeout=10)
            if response:
                try:
                    MAIN_INITIAL_SETTINGS = response.json()
                except json.decoder.JSONDecodeError:
                    pass
        except requests.exceptions.ReadTimeout:
            pass
        return render_template('base.html', **MAIN_INITIAL_SETTINGS)


@app.route('/static-mode/', methods=['GET', 'POST'])
def static_mode():
    global STATIC_MODE_SETTINGS

    if request.method == 'POST':
        params = {}
        static_red = request.form.get('static_red')
        static_green = request.form.get('static_green')
        static_blue = request.form.get('static_blue')

        # static red color
        if static_red:
            params = {'red_range': static_red}

        # static green color
        if static_green:
            params = {'green_range': static_green}

        # static blue color
        if static_blue:
            params = {'blue_range': static_blue}

        # GET request to NodeMCU
        requests.get('http://192.168.0.146/', params=params)

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    if request.method == 'GET':
        try:
            response = requests.get('http://192.168.0.146/', params={'static_mode': 'get'}, timeout=10)
            if response:
                try:
                    STATIC_MODE_SETTINGS = response.json()
                except json.decoder.JSONDecodeError:
                    pass
        except requests.exceptions.ReadTimeout:
            pass

        return render_template('static_mode.html', **STATIC_MODE_SETTINGS)


@app.route('/rainbow-mode/', methods=['GET', 'POST'])
def rainbow_mode():
    global RAINBOW_MODE_SETTINGS

    if request.method == 'POST':
        params = {}
        rainbow_step = request.form.get('rainbow_step')

        # rainbow step
        if rainbow_step:
            params = {'rainbow_step': rainbow_step}

        # GET request to NodeMCU
        requests.get('http://192.168.0.146/', params=params)

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    if request.method == 'GET':
        try:
            response = requests.get('http://192.168.0.146/', params={'rainbow_mode': 'get'}, timeout=10)
            if response:
                try:
                    RAINBOW_MODE_SETTINGS = response.json()
                except json.decoder.JSONDecodeError:
                    pass
        except requests.exceptions.ReadTimeout:
            pass

        return render_template('rainbow_mode.html', **RAINBOW_MODE_SETTINGS)


@app.route('/breath-mode/', methods=['GET', 'POST'])
def breath_mode():
    global BREATH_MODE_SETTINGS

    if request.method == 'POST':
        params = {}
        min_bright = request.form.get('min_bright')
        max_bright = request.form.get('max_bright')
        breath_step = request.form.get('breath_step')
        breath_red = request.form.get('breath_red')
        breath_green = request.form.get('breath_green')
        breath_blue = request.form.get('breath_blue')

        # breath min brightness
        if min_bright:
            params = {'min_brightness_range': min_bright}

        # breath max brightness
        if max_bright:
            params = {'max_brightness_range': max_bright}

        # breath step
        if breath_step:
            params = {'breath_step': breath_step}

        # breath red
        if breath_red:
            params = {'breath_red_range': breath_red}
            print(breath_red)

        # breath green
        if breath_green:
            params = {'breath_green_range': breath_green}
            print(breath_green)

        # breath blue
        if breath_blue:
            params = {'breath_blue_range': breath_blue}
            print(breath_blue)

        # GET request to NodeMCU
        requests.get('http://192.168.0.146/', params=params)

        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    if request.method == 'GET':
        try:
            response = requests.get('http://192.168.0.146/', params={'breath_mode': 'get'}, timeout=10)
            if response:
                try:
                    BREATH_MODE_SETTINGS = response.json()
                    print(BREATH_MODE_SETTINGS)
                except json.decoder.JSONDecodeError:
                    pass
        except requests.exceptions.ReadTimeout:
            pass

        return render_template('breath_mode.html', **BREATH_MODE_SETTINGS)
