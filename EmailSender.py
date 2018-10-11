#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import argparse


#try:
def get_arguments():
	parser = argparse.ArgumentParser(description='Fake Email Sender Options')
	parser.add_argument("-f", "--from", dest="from_email", help="From Email (sender email)", required=True)

	parser.add_argument("-n", "--name", dest="name",help="Name of From Email", required=True)
	parser.add_argument("-t", "--to", dest="to",help="To Email", required=True)
	parser.add_argument("-s", "--subject", dest="subject", help="Subject of Mail", required=True)
	parser.add_argument("-m", "--message", dest="message", help="Message of Mail", required=True)
	return parser.parse_args()


with open("apikeys.txt", "r") as ins:
    apikey_list = []
    apikey_list = ins.read().splitlines() 
    for line in ins:
        apikey_list.append(line)

try:
		arguments = get_arguments()

		msg = MIMEMultipart()
		msg['From'] = arguments.name + ' ' + '<' + arguments.from_email + '>'
		msg['To'] = arguments.to

		msg['Subject'] = arguments.subject
		message = arguments.message
		msg.attach(MIMEText(message))

		def send_mail(api):
			mailserver = smtplib.SMTP('smtp.sendgrid.net',587)

			mailserver.ehlo()
			mailserver.starttls()
			mailserver.ehlo()

			mailserver.login('apikey', api)

			mailserver.sendmail(arguments.from_email,arguments.to,msg.as_string())

			mailserver.quit()
		
		sendmail()
except Exception:
	for element in apikey_list:
		try:
			send_mail(element)
		except Exception:
			pass;


print("\n\n[***] Please use this tool for Legal and Valid Purposes\n")
print("Thanks for using this tool :)")
