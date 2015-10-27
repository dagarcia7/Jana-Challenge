import requests

##Setting up the these variables with the values of the parameters that
##I'm going to use when I make the GET request
endpoint = 'https://api.emailhunter.co/v1/search'
api_key = '6117a312004920f3beb37693e122892f38957b24'
email_type = 'generic'

emails_found = []

##Ask the user to input a domain name to acquire the emails from
domain = raw_input("Enter domain name: ")

##Construct the params that will be passed with the GET request
payload = {'domain': domain, 'api_key': api_key, 'type': email_type}

response = requests.get(endpoint, params=payload)

##Dig through the request for the emails returned
for email in response.json()['emails']:
    email_value = email['value']
    emails_found.append(email_value)

print "Found these email addresses: "

##Print results
for email in emails_found:
    print email

