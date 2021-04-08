import uasyncio as asyncio
import machine
import neopixel
import settings


neo_pixel = neopixel.NeoPixel(machine.Pin(4), settings.SETTINGS['num_leds'])


class BreathMode:

    def __init__(self):
        self.set_settings()
        self.mode = 'breath_mode'

    async def run(self):
        try:
            for j in range(self.min_brightness, self.max_brightness, self.breath_step):
                r = self.calc_color(self.red_color, j)
                g = self.calc_color(self.green_color, j)
                b = self.calc_color(self.blue_color, j)
                for i in range(self.num_leds):
                    neo_pixel[i] = (r, g, b)
                    self.change_settings()
                neo_pixel.write()
                await asyncio.sleep_ms(20)

            for j in range(self.max_brightness, self.min_brightness, -self.breath_step):
                r = self.calc_color(self.red_color, j)
                g = self.calc_color(self.green_color, j)
                b = self.calc_color(self.blue_color, j)
                for i in range(self.num_leds):
                    neo_pixel[i] = (r, g, b)
                    self.change_settings()
                neo_pixel.write()
                await asyncio.sleep_ms(20)
        except Exception:
            return

    def change_settings(self):
        self.set_settings()
        if settings.SETTINGS['current_mode'] is not self.mode:
            raise ValueError('Change Mode')

    def set_settings(self):
        self.num_leds = settings.SETTINGS['num_leds']
        self.led_status = settings.SETTINGS['led_status']
        self.min_brightness = settings.SETTINGS['mode']['breath_mode']['min_brightness']
        self.max_brightness = settings.SETTINGS['mode']['breath_mode']['max_brightness']
        self.breath_step = settings.SETTINGS['mode']['breath_mode']['breath_step']
        self.red_color = settings.SETTINGS['mode']['breath_mode']['red_color']
        self.green_color = settings.SETTINGS['mode']['breath_mode']['green_color']
        self.blue_color = settings.SETTINGS['mode']['breath_mode']['blue_color']

    def calc_color(self, color, step):
        return int(color * step * self.led_status / 100)
