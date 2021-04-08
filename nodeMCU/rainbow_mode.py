import uasyncio as asyncio
import machine
import neopixel
import settings


neo_pixel = neopixel.NeoPixel(machine.Pin(4), settings.SETTINGS['num_leds'])


class RainbowMode:

    def __init__(self):
        self.set_settings()
        self.mode = 'rainbow_mode'

    def wheel(self, pos):
        if pos < 0 or pos > 255:
            return 0, 0, 0
        if pos < 85:
            return 255 - pos * 3, pos * 3, 0
        if pos < 170:
            pos -= 85
            return 0, 255 - pos * 3, pos * 3
        pos -= 170
        return pos * 3, 0, 255 - pos * 3

    async def run(self):
        try:
            for j in range(0, 255, self.rainbow_step):
                for i in range(self.num_leds):
                    rc_index = (i * 256 // self.num_leds) + j
                    r, g, b = self.wheel(rc_index & 255)
                    r = self.calc_color(r)
                    g = self.calc_color(g)
                    b = self.calc_color(b)
                    neo_pixel[i] = (r, g, b)
                    self.change_settings()
                neo_pixel.write()
                await asyncio.sleep_ms(5)
        except Exception:
            return

    def change_settings(self):
        self.set_settings()
        if settings.SETTINGS['current_mode'] is not self.mode:
            raise ValueError('Change Mode')

    def set_settings(self):
        self.rainbow_step = settings.SETTINGS['mode']['rainbow_mode']['rainbow_step']
        self.led_brightness = settings.SETTINGS['led_brightness']
        self.num_leds = settings.SETTINGS['num_leds']
        self.led_status = settings.SETTINGS['led_status']

    def calc_color(self, color):
        return int(color * self.led_brightness * self.led_status / 100)











