from lib.mail_sender import MailSender
from lib.utils import alter_message_id
from config import config

def main():

    email_data = config['raw_email']
    email_data = alter_message_id(email_data, config['server']['ip'])

    print(email_data)

    mail_sender = MailSender()
    mail_sender.set_param((config['server']['ip'], config['server']['port']), 
                          helo=config['destination'].encode(), 
                          mail_from=f"<{config['mail_from']}>".encode(), 
                          rcpt_to=f"<{config['subscriber_email']}>".encode(), 
                          email_data=email_data.encode(), 
                          starttls=config['server']['starttls'])
    mail_sender.send_email()
if __name__=='__main__':
    main()
