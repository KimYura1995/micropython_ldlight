import uasyncio as asyncio
import machine
import neopixel


neo_pixel = neopixel.NeoPixel(machine.Pin(4), 30)


async def breath_mode(num_leds, led_status, min_brightness,
                      max_brightness, breath_step, red_color,
                      green_color, blue_color):
    try:
        for j in range(min_brightness, max_brightness, breath_step):
            r = int(red_color * j / 100 * led_status)
            g = int(green_color * j / 100 * led_status)
            b = int(blue_color * j / 100 * led_status)
            for i in range(num_leds):
                neo_pixel[i] = (r, g, b)
            neo_pixel.write()
            await asyncio.sleep_ms(50)
    except ValueError:
        pass

    try:
        for j in range(max_brightness, min_brightness, -breath_step):
            r = int(red_color * j / 100 * led_status)
            g = int(green_color * j / 100 * led_status)
            b = int(blue_color * j / 100 * led_status)
            for i in range(num_leds):
                neo_pixel[i] = (r, g, b)
            neo_pixel.write()
            await asyncio.sleep_ms(50)
    except ValueError:
        pass
