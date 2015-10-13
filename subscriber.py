#!/usr/bin/python3.4

import sys
import requests
from flask import Flask, request

# config
client = {
	'id': 'YOUR APP ID',
	'secret': 'YOUR APP SECRET KEY',
	'uri': 'REDIRECT URI'
}

api_url = 'https://api.instagram.com/v1/subscriptions/'

try:

	# start 
	if sys.argv[1] == 'start':

		handler = Flask(__name__)

		@handler.route("/", methods=['GET', 'POST'])
		def main():
		    if request.args.get('hub.challenge') != None:
		    	return request.args.get('hub.challenge'), 200
		    else:

		    	return '', 200

		if __name__ == "__main__":
		    handler.run(port=8888, debug=True)

    # subscribe
	elif sys.argv[1] == 'subscribe':

		if sys.argv[2] == 'tag' && sys.argv[3] !== None:

			query = {
				'client_id': client['id'],
				'client_secret': client['secret'],
				'aspect': 'media',
				'object': 'tag',
				'object_id': 'javascript',
				'callback_url': client['uri']
			}

			response = requests.post(api_url, data=query)
			print(response.json())

		else:
			print('Only tag subscription avilable')

	elif sys.argv[1] == 'unsubscribe':
		query = {
			'client_secret': client['secret'],
			'client_id': client['id'],
			'object': 'all'
		}
		response = requests.delete(api_url, params=query)
		print(response.json())

	elif sys.argv[1] == 'list':
		query = {
			'client_secret': client['secret'],
			'client_id': client['id']
		}
		response = requests.get(api_url, params=query)
		print(response.json())

	else:
		print('Instruction with name "'+sys.argv[1]+'" not found!')

except (IndexError):
	print('ARGV was empty!')
