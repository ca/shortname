#coding=utf-8
import threading
import random
import urllib2
import requests
from requests.exceptions import HTTPError
from itertools import product
from string import ascii_lowercase

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def checkTwitter(username):
	print "checking for username: " + bcolors.OKBLUE + username + bcolors.ENDC + "..."
	url = "https://www.twitter.com/" + username

	try:
	    r = requests.get(url)
	    r.raise_for_status()
	except HTTPError:
	    print bcolors.OKGREEN + 'GET THAT USERNAME' + bcolors.ENDC
	else:
	    print bcolors.FAIL + 'Not available.' + bcolors.ENDC

def threeLetterCombos():
	for i in keywords:
		checkTwitter(i)
	time = random.randint(1,100000)
	threading.Timer(time, threeLetterCombos).start()