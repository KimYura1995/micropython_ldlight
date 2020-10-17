import uasyncio as asyncio
import machine
import neopixel


neo_pixel = neopixel.NeoPixel(machine.Pin(4), 30)


async def static_mode(num_leds, red_color, green_color,
                      blue_color, led_brightness, led_status):
    red = int(red_color * led_brightness / 100 * led_status)
    green = int(green_color * led_brightness / 100 * led_status)
    blue = int(blue_color * led_brightness / 100 * led_status)

    for led in range(num_leds):
        neo_pixel[led] = (red, green, blue)
        neo_pixel.write()
