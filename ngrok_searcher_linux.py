import requests
import random
import colorama
import sys
file = open('workings_sites_ngrok.txt', 'a')
g = str("qwertyuiopasdfghjklzxcvbnm1234567890")

def gen():
	global g
	i = str("http://" + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + random.choice(g) + ".ngrok.io")
	check(i)
def check(url):
	r = requests.get(url)
	print("\033[33m" + url)
	if r.status_code == 404:
		print("\033[31mСайт не рабочий! | Site not working!")
	else:
		print("\033[32mСайт рабочий!| Site is working!")
		file.write('\n' + url)
	gen()
sys.setrecursionlimit(999999999)
gen()
