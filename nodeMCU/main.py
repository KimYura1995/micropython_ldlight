import uasyncio as asyncio
import ure
import ujson

from static_mode import static_mode
from rainbow_mode import rainbow_mode
from breath_mode import breath_mode


SETTINGS = {
    'num_leds': 30,
    'led_status': 0,
    'led_brightness': 0,
    'current_mode': 'static_mode',
    'mode': {
        'static_mode': {
            'red_color': 0,
            'green_color': 0,
            'blue_color': 0,
        },
        'rainbow_mode': {
            'rainbow_step': 1,
        },
        'breath_mode': {
            'min_brightness': 0,
            'max_brightness': 0,
            'breath_step': 0,
            'red_color': 0,
            'green_color': 0,
            'blue_color': 0,
        },
    },
}


def read_initial_settings():
    global SETTINGS
    with open('settings.json', 'r') as file:
        SETTINGS = ujson.load(file)


def save_initial_settings():
    global SETTINGS
    with open('settings.json', 'w') as file:
        ujson.dump(SETTINGS, file)


async def handle_request(request):
    global SETTINGS
    response = ''

    if "GET /?main_settings=get" in request:
        response = ujson.dumps({
            'led_status': SETTINGS['led_status'],
            'led_brightness': SETTINGS['led_brightness'],
            })

    if "GET /?static_mode=get" in request:
        response = ujson.dumps({
            'led_status': SETTINGS['led_status'],
            'led_brightness': SETTINGS['led_brightness'],
            'red_color': SETTINGS['mode']['static_mode']['red_color'],
            'green_color': SETTINGS['mode']['static_mode']['green_color'],
            'blue_color': SETTINGS['mode']['static_mode']['blue_color'],
            })
        SETTINGS['current_mode'] = 'static_mode'

    if "GET /?rainbow_mode=get" in request:
        response = ujson.dumps({
            'led_status': SETTINGS['led_status'],
            'led_brightness': SETTINGS['led_brightness'],
            'rainbow_step': SETTINGS['mode']['rainbow_mode']['rainbow_step'],
        })
        SETTINGS['current_mode'] = 'rainbow_mode'

    if "GET /?breath_mode=get" in request:
        response = ujson.dumps({
            'led_status': SETTINGS['led_status'],
            'led_brightness': SETTINGS['led_brightness'],
            'min_brightness': SETTINGS['mode']['breath_mode']['min_brightness'],
            'max_brightness': SETTINGS['mode']['breath_mode']['max_brightness'],
            'breath_step': SETTINGS['mode']['breath_mode']['breath_step'],
            'red_color': SETTINGS['mode']['breath_mode']['red_color'],
            'green_color': SETTINGS['mode']['breath_mode']['green_color'],
            'blue_color': SETTINGS['mode']['breath_mode']['blue_color'],
            })
        SETTINGS['current_mode'] = 'breath_mode'

    if "GET /?save=save" in request:
        save_initial_settings()

    if "GET /?led_status=" in request:
        match_led_status = ure.search(r'led_status=(\d)', request)
        SETTINGS['led_status'] = int(match_led_status.group(1))

    if "GET /?led_brightness=" in request:
        match_led_brightness = ure.search(r'led_brightness=(\d+)', request)
        SETTINGS['led_brightness'] = int(match_led_brightness.group(1))

    # static mode
    if "GET /?red_range=" in request:
        match_red_color = ure.search(r'red_range=(\d+)', request)
        SETTINGS['mode']['static_mode']['red_color'] = int(match_red_color.group(1))

    if "GET /?blue_range=" in request:
        match_blue_color = ure.search(r'blue_range=(\d+)', request)
        SETTINGS['mode']['static_mode']['blue_color'] = int(match_blue_color.group(1))

    if "GET /?green_range=" in request:
        match_green_color = ure.search(r'green_range=(\d+)', request)
        SETTINGS['mode']['static_mode']['green_color'] = int(match_green_color.group(1))

    # rainbow mode
    if "GET /?rainbow_step=" in request:
        match_rainbow_step = ure.search(r'rainbow_step=(\d+)', request)
        SETTINGS['mode']['rainbow_mode']['rainbow_step'] = int(match_rainbow_step.group(1))

    # breath mode
    if "GET /?min_brightness_range=" in request:
        match_min_brightness = ure.search(r'min_brightness_range=(\d+)', request)
        SETTINGS['mode']['breath_mode']['min_brightness'] = int(match_min_brightness.group(1))

    if "GET /?max_brightness_range=" in request:
        match_max_brightness = ure.search(r'max_brightness_range=(\d+)', request)
        SETTINGS['mode']['breath_mode']['max_brightness'] = int(match_max_brightness.group(1))

    if "GET /?breath_step=" in request:
        match_breath_step = ure.search(r'breath_step=(\d+)', request)
        SETTINGS['mode']['breath_mode']['breath_step'] = int(match_breath_step.group(1))

    if "GET /?breath_red_range=" in request:
        match_breath_red_color = ure.search(r'breath_red_range=(\d+)', request)
        SETTINGS['mode']['breath_mode']['red_color'] = int(match_breath_red_color.group(1))

    if "GET /?breath_green_range=" in request:
        match_green_color = ure.search(r'breath_green_range=(\d+)', request)
        SETTINGS['mode']['breath_mode']['green_color'] = int(match_green_color.group(1))

    if "GET /?breath_blue_range=" in request:
        match_blue_color = ure.search(r'breath_blue_range=(\d+)', request)
        SETTINGS['mode']['breath_mode']['blue_color'] = int(match_blue_color.group(1))

    return response


async def web_handler(reader, writer):
    try:
        request = str(await reader.read(1024))
        response = await handle_request(request)
        header = """HTTP/1.1 200 OK\nConnection: close\n\n"""
        await writer.awrite(header)
        await writer.awrite(response)
        await writer.aclose()
        print("Finished processing request")
    except Exception as e:
        print(e)


async def led_handler():
    while True:
        if SETTINGS['current_mode'] == 'static_mode':
            await static_mode(
                SETTINGS['num_leds'],
                SETTINGS['mode']['static_mode']['red_color'],
                SETTINGS['mode']['static_mode']['green_color'],
                SETTINGS['mode']['static_mode']['blue_color'],
                SETTINGS['led_brightness'],
                SETTINGS['led_status'],
            )
        elif SETTINGS['current_mode'] == 'rainbow_mode':
            await rainbow_mode(
                SETTINGS['num_leds'],
                SETTINGS['led_brightness'],
                SETTINGS['led_status'],
                SETTINGS['mode']['rainbow_mode']['rainbow_step'],
                )
        elif SETTINGS['current_mode'] == 'breath_mode':
            await breath_mode(
                SETTINGS['num_leds'],
                SETTINGS['led_status'],
                SETTINGS['mode']['breath_mode']['min_brightness'],
                SETTINGS['mode']['breath_mode']['max_brightness'],
                SETTINGS['mode']['breath_mode']['breath_step'],
                SETTINGS['mode']['breath_mode']['red_color'],
                SETTINGS['mode']['breath_mode']['green_color'],
                SETTINGS['mode']['breath_mode']['blue_color'],
            )
        await asyncio.sleep_ms(50)


async def tcp_server(host, port):
    await asyncio.start_server(web_handler, host, port)


read_initial_settings()
loop = asyncio.get_event_loop()
loop.create_task(tcp_server('0.0.0.0', 80))
loop.create_task(led_handler())
loop.run_forever()
