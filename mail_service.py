import smtplib

def send_email(name):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('showu2021@gmail.com', 'ush@w2021')
    server.sendmail('showu2021@gmail.com',
                    'parves5405@gmail.com',
                     name)




