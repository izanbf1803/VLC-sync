import vlc
import argparse
import time
import requests
import json

GLOBALS = {}
TIME_DELTA = 1000

def clean_input(text):
	ans = input(text)
	return ans.strip()

def update():
	global GLOBALS
	r = requests.get(args.server + "/get_globals/")
	print(r.text)
	GLOBALS = json.loads(r.text)

parser = argparse.ArgumentParser(
    prog='client.py',
    description='What the program does',
    epilog='Text at the bottom of help')

parser.add_argument('-c', '--server', required=True)
parser.add_argument('-f', '--file', required=True)
parser.add_argument('-s', '--subs')

args = parser.parse_args()


mp = vlc.MediaPlayer(args.file)

if args.subs is not None:
	mp.video_set_subtitle_file(args.subs)

update()

mp.play()

time.sleep(1)

mp.pause()
mp.set_time(0)

print("Duration:", mp.get_length())

try:
	while True:
		time.sleep(0.5)
		update()
		print(GLOBALS, abs(mp.get_time() - GLOBALS["time"]))
		if abs(mp.get_time() - GLOBALS["time"]) > TIME_DELTA:
			mp.set_time(GLOBALS["time"])
		if int(GLOBALS["play"]) == 1 and not mp.is_playing():
			mp.play()
		if int(GLOBALS["play"]) == 0 and mp.is_playing():
			mp.pause()
except:
	pass
