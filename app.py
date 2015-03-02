#coding=utf-8
import json
import timeit
import threading
import random
import requests
from requests.exceptions import HTTPError
from itertools import product
from string import ascii_lowercase

headers = {
	'X-Parse-Application-Id': '',
	'X-Parse-REST-API-Key': '',
	'content-type': 'application/json'
}

def checkForName(username, network):
	if network == 'instagram': url = "https://www.instagram.com/" + username
	elif network == 'twitter': url = "https://www.twitter.com/" + username
	elif network == 'github': url = "https://www.github.com/" + username
	elif network == 'facebook': url = "https://www.facebook.com/" + username
	elif network == 'pinterest': url = "https://www.pinterest.com/" + username
	elif network == 'tumblr': url = "https://" + username + ".tumblr.com"
	else: url = ''
	# exit with error "Please enter a supported network!"

	try:
	    r = requests.get(url)
	    r.raise_for_status()
	except HTTPError:
		print network + ': ' + username
		return True
	else: return False

def iterateNames(network, x):
	keywords = [''.join(i) for i in product(ascii_lowercase, repeat = x)]
	matches = []
	for i in keywords:
		if checkForName(i, network) == True: r = requests.post('https://api.parse.com/1/classes/ZSSUsername', data=json.dumps({'username': i,'network': network, 'available': True}), headers = headers)
		else: r = requests.post('https://api.parse.com/1/classes/ZSSUsername', data=json.dumps({'username': i,'network': network, 'available': False}), headers = headers)

def startUp(net):
	for x in range(4, 5):
		iterateNames(net, x)
	time = random.randint(1,10)
	threading.Timer(time, startUp).start()

while (True):
	networks = ['instagram', 'twitter', 'github', 'facebook', 'pinterest', 'tumblr']
	for network in networks:
		startUp(network)