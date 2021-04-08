import uasyncio as asyncio
import machine
import neopixel
import settings


neo_pixel = neopixel.NeoPixel(machine.Pin(4), settings.SETTINGS['num_leds'])


class ColorLoopMode:

    def __init__(self):
        self.set_settings()
        self.mode = 'color_loop_mode'

    async def run(self):
        try:
            rgb = [255, 0, 0]
            for dC in range(0, 3, 1):
                iC = 0 if dC == 2 else dC + 1
                for i in range(0, 255, self.loop_step):
                    rgb[dC] -= self.loop_step
                    rgb[iC] += self.loop_step
                    for a in range(0, self.num_leds, 1):
                        neo_pixel[a] = (
                            self.calc_color(rgb[0]),
                            self.calc_color(rgb[1]),
                            self.calc_color(rgb[2]),
                        )
                    neo_pixel.write()
                    self.change_settings()
                    await asyncio.sleep_ms(30)
        except Exception:
            return

    def change_settings(self):
        self.set_settings()
        if settings.SETTINGS['current_mode'] is not self.mode:
            raise ValueError('Change Mode')

    def set_settings(self):
        self.loop_step = settings.SETTINGS['mode']['color_loop_mode']['loop_step']
        self.led_brightness = settings.SETTINGS['led_brightness']
        self.num_leds = settings.SETTINGS['num_leds']
        self.led_status = settings.SETTINGS['led_status']

    def calc_color(self, color):
        return int(color * self.led_status * self.led_brightness / 100)











