config = {
    'destination' : 'gmail.com', # This should always stay static
    'mail_from' : 'YOUR_EMAIL@YOUR_SERVER.COM', # Original sender from OUR domain (never gmail)
    'subscriber_email' : 'DESTINATION@gmail.com ', # Destination email, regardless of raw_email header
    'server' : {
        'ip' : 'YOUR_SERVER_IP_OR_DOMAIN', # IP or Domain of sending mail server
        'port' : 25, 
        'starttls': True,
    },
    'raw_email': """ YOUR RAW EMAIL FROM A GMAIL ACCOUNT YOU OWN """,
}
