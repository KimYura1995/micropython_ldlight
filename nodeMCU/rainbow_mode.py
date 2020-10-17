import uasyncio as asyncio
import machine
import neopixel


neo_pixel = neopixel.NeoPixel(machine.Pin(4), 30)


async def wheel(pos):
    if pos < 0 or pos > 255:
        return 0, 0, 0
    if pos < 85:
        return 255 - pos * 3, pos * 3, 0
    if pos < 170:
        pos -= 85
        return 0, 255 - pos * 3, pos * 3
    pos -= 170
    return pos * 3, 0, 255 - pos * 3


async def rainbow_mode(num_leds, led_brightness, led_status, rainbow_step):
    for j in range(0, 255, rainbow_step):
        for i in range(num_leds):
            rc_index = (i * 256 // num_leds) + j
            r, g, b = await wheel(rc_index & 255)
            r = int(r * led_brightness / 100 * led_status)
            g = int(g * led_brightness / 100 * led_status)
            b = int(b * led_brightness / 100 * led_status)
            neo_pixel[i] = (r, g, b)
        neo_pixel.write()
        await asyncio.sleep_ms(50)
