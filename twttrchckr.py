#coding=utf-8
import timeit
import threading
import random
import urllib2
import requests
from requests.exceptions import HTTPError
from itertools import product
from string import ascii_lowercase
from twilio.rest import TwilioRestClient

account_sid = ""
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)

x = 3 # here's where you want that user input or the flags or something
numbers = [''.join(i) for i in product(['1','2','3','4','5','6','7','8','9','0'], repeat = x)]
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = x)]

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
	elif network == 'github':
		url = "https://www.github.com/" + username
	elif network == 'facebook':
		url = "https://www.facebook.com/" + username
	else:
		url = ''
		# exit with error "Please enter a supported network!"

	try:
	    r = requests.get(url)
	    r.raise_for_status()
	except HTTPError:
		client.messages.create(
			to="",
			from_="",
			body="Username available on " + network + "!: " + username
		)
		print bcolors.OKGREEN + 'GET THAT USERNAME' + bcolors.ENDC
	else:
	    print bcolors.FAIL + 'Not available.' + bcolors.ENDC

def iterateNames(network):
	for i in keywords:
		checkForName(i, network)
	time = random.randint(1,100000)
	# threading.Timer(time, threeLetterCombos).start()

# execute on -3 or some other ones on flags
iterateNames('twitter')
# checkForName('fdsjlflkdlsjfdlskf','twitter')
# ask for input of a username