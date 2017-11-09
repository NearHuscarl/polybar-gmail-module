#!/usr/bin/env python

"""
follow the instruction here: https://developers.google.com/gmail/api/quickstart/python
to generate client_secret.json and put it in $(pwd)/gmail/
Dependencies: google-api-python-client
"""

import argparse
import os
import httplib2

from apiclient import discovery, errors
from oauth2client.file import Storage
from oauth2client import client
from oauth2client import tools

parser = argparse.ArgumentParser(description='Display gmail unread count on polybar')
parser.add_argument('-pe', '--prefix-error', default='', nargs='?',
		help='prefix when an error occurs')
parser.add_argument('-p', '--prefix', default='', nargs='?',
		help='module prefix, preferably an icon')
parser.add_argument('-ec', '--icon-error-color', default='#E74C3C', nargs='?',
		help='foreground color for error icon')
parser.add_argument('-ic', '--icon-color', default='#16A085', nargs='?',
		help='foreground color for mail icon')
parser.add_argument('-tc', '--text-color', default='#ECF0F1', nargs='?',
		help='foreground color for text')

arg = parser.parse_args()

def get_credentials():
	"""
	Gets valid user credentials from storage.

	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns: Credentials, the obtained credential.
	"""

	credentials_dir = os.path.dirname(os.path.realpath(__file__))

	credentials_path = os.path.join(credentials_dir, 'credentials.json')
	credentials_store = Storage(credentials_path)
	credentials = credentials_store.get()

	if not credentials or credentials.invalid:
		SCOPE = 'https://www.googleapis.com/auth/gmail.readonly'
		CLIENT_SECRET_FILE = os.path.join(credentials_dir, 'client_secret.json')
		APPLICATION_NAME = 'Gmail Notification - Polybar'

		flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPE)
		flow.user_agent = APPLICATION_NAME
		credentials = tools.run_flow(flow, credentials_store)
	return credentials

def update_unread_gmail_count():
	""" Update unread mails in gmail and display on polybar """

	try:
		credentials = get_credentials()
		http = credentials.authorize(httplib2.Http())
		gmail = discovery.build('gmail', 'v1', http=http)

		result = gmail.users().messages().list(userId='me', q='in:inbox is:unread').execute()
		unread_count = result['resultSizeEstimate']

		prefix = color_text(arg.prefix, arg.icon_color)
		count = color_text(str(unread_count), arg.text_color)

		print(prefix + ' ' + count)

	except (errors.HttpError, httplib2.ServerNotFoundError) as error:
		prefix = color_text(arg.prefix_error, arg.icon_error_color)
		error = color_text(str(error), arg.text_color)

		print(prefix + ' ' + error)

	except client.AccessTokenRefreshError:
		prefix = color_text(arg.prefix_error, arg.icon_error_color)
		error = color_text('[credential expire]', arg.text_color)

		print(prefix + ' ' + error)

def color_text(string, color):
	"""
	color output in polybar format
	"""

	color_begin = '%{F' + color +  '}'
	color_end = '%{F-}'
	return color_begin + string + color_end

update_unread_gmail_count()

# vim: nofoldenable
