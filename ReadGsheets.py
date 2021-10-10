# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
from datetime import datetime,timedelta
import pandas as pd
import smtplib
from tabulate import tabulate

import tabulate
tabulate.PRESERVE_WHITESPACE = True

g_user = os.environ['USER']
g_password = os.environ['PASSWORD']

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(g_user, g_password)
except:
    print ('Something went wrong...')


def mailCIG(df1):
    
    sent_from = 'aaurfanalyst@gmail.com'
    #to = 'teamCIG@iitr.ac.in'
    to = 'a09.abhishek@gmail.com'
    subject = "Alert! CIG response team you have a Guest"
    body = df1.to_string()
    body = tabulate.tabulate(df1, headers='keys', tablefmt='psql',colalign=("right",)) 
    print (body,'\n',type(body))
    emailTxt = 'From: %s\r\n' % sent_from +'To: %s\r\n'% (to)+'Subject: %s \n\n the following guest wishes to contact u \n %s  \n '% (subject,body)

    #print (emailTxt)

    try:
    
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(g_user, g_password)
        server.sendmail(sent_from, to, emailTxt)
        #server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')


def mailGuest(mailID):
    
    sent_from = 'aaurfanalyst@gmail.com'
    to = mailID
    print (type(to))
    subject = "IITR CIG will be with you in a moment"
    eText = open("email2Guest.txt","r")
    body = eText.read()
    eText.close()
    emailTxt = 'From: %s\r\n' % sent_from +'To: %s\r\n'% (to)+'Subject: %s \n \n %s  \n '% (subject,body)

    #print(emailTxt)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(g_user, g_password)
        server.sendmail(sent_from, to, emailTxt)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')


def main():

    df = pd.read_csv ('comm.csv')
    if  df.empty:
        exit()
    else:
        mailCIG(df)
        pass

    #print(df)
    # Name,mail,timestamp,reason,connection
    for ind in df.index:
         print(ind,df['Name'][ind], df['mail'][ind])
         #ts = datetime.utcfromtimestamp(df['timestamp'][ind]).strftime('%Y-%m-%d %H:%M:%S')
         ct = datetime.now() - timedelta(hours=3)
         ts3 = ct.timestamp()
         if (ts3< df['timestamp'][ind]):
            mailGuest(df['mail'][ind])



if __name__ == "__main__":
    main()