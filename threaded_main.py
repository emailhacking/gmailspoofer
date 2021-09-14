from lib.mail_sender import MailSender
from lib.utils import alter_message_id
from config import config

from functools import partial
from pebble import ProcessPool
from concurrent.futures import TimeoutError

def send(config, rcpt_to):
    email_data = config['raw_email']
    email_data = alter_message_id(email_data, config['server']['ip'])

    mail_sender = MailSender()
    mail_sender.set_param((config['server']['ip'], config['server']['port']), 
                          helo=config['destination'].encode(), 
                          mail_from=f"<{config['mail_from']}>".encode(), 
                          rcpt_to=f"<{rcpt_to}>".encode(), 
                          email_data=email_data.encode(), 
                          starttls=config['server']['starttls'])
    mail_sender.send_email()

def task_done(future):
    try:
        result = future.result()  # blocks until results are ready
    except TimeoutError as error:
        print("Function took longer than %d seconds" % error.args[1])
    except Exception as error:
        print("Function raised %s" % error)
        print(error.traceback)  # traceback of the function

def main():

    f = open('list.txt', 'r')
    rcpts = f.readlines()
    f.close()

    i = 0
    total = len(rcpts)
    with ProcessPool(max_workers=25) as pool:
        for rcpt_to in rcpts:
            i+=1
            print(f'Processing: {i}/{total}')
            future = pool.schedule(send, args=[config, rcpt_to.strip()])
            future.add_done_callback(task_done)

if __name__=='__main__':
    main()
