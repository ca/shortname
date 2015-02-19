#coding=utf-8
import json
import timeit
import threading
import random
# import urllib2
import requests
from flask import Flask, url_for, render_template
from requests.exceptions import HTTPError
from itertools import product
from string import ascii_lowercase
app = Flask(__name__)

headers = {
	'X-Parse-Application-Id': 'JmLQy3H9D7arbVcofNY2AVLhMpj2Xt1RxTSjeMhY',
	'X-Parse-REST-API-Key': 'Uwcbhq8CyO9fIDUJtHt1R5z4GbfpzCbBcYSq3SCc',
	'content-type': 'application/json'
}

def checkForName(username, network):
	if network == 'twitter': url = "https://www.twitter.com/" + username
	elif network == 'github': url = "https://www.github.com/" + username
	elif network == 'facebook': url = "https://www.facebook.com/" + username
	# elif network == 'tumblr': url = "https://" + username + ".tumblr.com"
	else: url = ''
	# exit with error "Please enter a supported network!"

	try:
	    r = requests.get(url)
	    r.raise_for_status()
	except HTTPError: return True
	else: return False

@app.route('/search/<username>')
def search(username=None):
	networks = ['twitter', 'github', 'facebook']#, 'tumblr']
	for network in networks:
		print network
		if checkForName(username, network) == True: r = requests.post('https://api.parse.com/1/classes/ZSSUsername', data=json.dumps({'username': username,'network': network}), headers = headers)
	return "processed successfully you asshole"


# @app.route('/list/<network>')
# def list(network=''):
# 	startUp(network)
# 	return "listed"

def iterateNames(network, x):
	keywords = [''.join(i) for i in product(ascii_lowercase, repeat = x)]
	matches = []
	for i in keywords:
		if checkForName(i, network) == True: r = requests.post('https://api.parse.com/1/classes/ZSSUsername', data=json.dumps({'username': i,'network': network}), headers = headers)

def startUp(net):
	for x in range(1, 4):
		iterateNames(net, x)
	time = random.randint(1,10)
	threading.Timer(time, startUp).start()

if __name__ == '__main__':
	app.run()
    # app.run(host='0.0.0.0', port=80)