import machine
import neopixel
import time
import usocket as socket
import ure


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(("", 80))
soc.listen(5)

num_leds = 30
neo_pixel = neopixel.NeoPixel(machine.Pin(4), 30)

red_color = 0
green_color = 0
blue_color = 0
led_brightness = 0
led_status = 0

def web_page():
	with open("index.html", "r") as file:
		page = file.read()
		return page

html = web_page()


while True:
	conn, address = soc.accept()
	request = str(conn.recv(1024))

	if "GET /?led_status=" in request:
		match_led_status = ure.search(r'led_status=(\d)', request)
		led_status = int(match_led_status.group(1))

	if "GET /?led_brightness=" in request:
		match_led_brightness = ure.search(r'led_brightness=(\d+)', request)
		led_brightness = int(match_led_brightness.group(1))

	if "GET /?red_range=" in request:
		match_red_color = ure.search(r'red_range=(\d+)', request)
		red_color = int(match_red_color.group(1))

	if "GET /?blue_range=" in request:
		match_blue_color = ure.search(r'blue_range=(\d+)', request)
		blue_color = int(match_blue_color.group(1))

	if "GET /?green_range=" in request:
		match_green_color = ure.search(r'green_range=(\d+)', request)
		green_color = int(match_green_color.group(1))

	red = int(red_color * led_brightness / 100 * led_status)
	green = int(green_color * led_brightness / 100 * led_status)
	blue = int(blue_color * led_brightness / 100 * led_status)

	for led in range(num_leds):
		neo_pixel[led] = (red, green, blue)
		neo_pixel.write()

	conn.send("HTTP/1.1 200 OK\n")
	conn.send("Content-type: text/html\n")
	conn.send("Connection: close\n\n")
	conn.sendall(html % (led_brightness,
							red_color,
							red_color,
							blue_color,
							blue_color,
							green_color,
							green_color))
	conn.close()
