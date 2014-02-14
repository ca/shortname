#coding=utf-8
import timeit
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

def checkForName(username, network):
	print "checking " + bcolors.WARNING + network + bcolors.ENDC + " for username: " + bcolors.OKBLUE + username + bcolors.ENDC + "..."

	if network == 'twitter':
		url = "https://www.twitter.com/" + username
	else if network == 'github':
		url = "https://www.github.com/" + username
	else:
		url = ''
		# exit with error "Please enter a network!"

	try:
	    r = requests.get(url)
	    r.raise_for_status()
	except HTTPError:
	    print bcolors.OKGREEN + 'GET THAT USERNAME' + bcolors.ENDC
	else:
	    print bcolors.FAIL + 'Not available.' + bcolors.ENDC

def threeLetterCombos(network):
	for i in keywords:
		checkForName(i, network)
	time = random.randint(1,100000)
	threading.Timer(time, threeLetterCombos).start()

# execute on -3 or some other ones on flags
timeit(threeLetterCombos('github'))
# ask for input of a username