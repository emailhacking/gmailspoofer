def alter_message_id(raw_message, ip):
    msg = ''
    for line in raw_message.split('\n'):
        if 'Message-ID' in line:
            msg += f'Message-ID: {generate_message_id(ip)}\n'
        msg += f'{line}\n'
    return msg
