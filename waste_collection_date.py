import datetime
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

with open('/home/zhangyao/mypython/apps/waste_collection_date/waste_collection_date.txt', 'r') as f:
    for date0 in f.readlines():
        date0 = date0.strip('\n')
        year, mon, day = date0.split('-')
        date1 = datetime.date(int(year), int(mon), int(day))
        day_delta = date1 - datetime.date.today()

        if day_delta == datetime.timedelta(days=1):

            # Send email
            print('Sending email...')
            mail_host = 'smtp.126.com'
            mail_username = 'zy_onlooker@126.com'
            with open('/home/zhangyao/mypython/apps/waste_collection_date/email_pwd.txt', 'r') as pwd:
                mail_auth_password = pwd.read().strip('\n')

            sender = 'zy_onlooker@126.com'
            receivers = 'zy_onlooker@126.com, 819357683@qq.com'
            #receivers = 'zy_onlooker@126.com'

            message = MIMEText('Waste in GREY BIN and RECYCLING BOXES will be collected tomorrow!\n\n------尧之助', 'plain', 'utf-8')
            #message = MIMEText('Waste in GREY BIN and RECYCLING BOXES will be collected today!\n\n------尧之助', 'plain', 'utf-8')
            message['From'] = sender
            message['To'] =  receivers
            message['Subject'] = "Waste Collection Reminder."

            try:
                smtpObj = smtplib.SMTP_SSL(mail_host, 465)
                smtpObj.ehlo()
                smtpObj.login(mail_username, mail_auth_password)
                smtpObj.sendmail(sender, receivers.split(','), message.as_string())
                print ("Email has been sent successfully.")
            except smtplib.SMTPException:
                print ("Error: Failed to send email.")


            # Send text message
            print('Sending SMS...')
            with open('/home/zhangyao/mypython/apps/waste_collection_date/sms_pwd.txt', 'r') as f:
                pwd = f.read().strip('\n')
                pwd = eval(pwd)
                account_sid = pwd['sid']
                auth_token = pwd['token']
            client = Client(account_sid, auth_token)
            message = client.messages \
                            .create(
                                body="Waste in GREY BIN and RECYCLING BOXES will be collected tomorrow!\n\n------尧之助.",
                                #body="Waste in GREY BIN and RECYCLING BOXES will be collected today!\n\n------尧之助.",
                                from_='+17607480468',
                                to='+447729884941'
                      )
            message = client.messages \
                            .create(
                                body="Waste in GREY BIN and RECYCLING BOXES will be collected tomorrow!\n\n------尧之助.",
                                #body="Waste in GREY BIN and RECYCLING BOXES will be collected today!\n\n------尧之助.",
                                from_='+17607480468',
                                to='+447561558467'
                      )
            print('SMS has been sent successfully.')
            break

print(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
print('Waste collection date has been checked.\n\n')

