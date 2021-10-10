# -*- coding: utf-8 -*-
#!/usr/bin/python

#t1 uses api to connect to google sheets

import os
from datetime import datetime,timedelta
import pandas as pd

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

import smtplib
from tabulate import tabulate

import tabulate
tabulate.PRESERVE_WHITESPACE = True

from dotenv import load_dotenv
load_dotenv()# look for a file named .env in the current directory and will add all the var

# gmail account n password for mailing
g_user = os.environ['USER']
g_password = os.getenv('PASSWORD')
#g_password = os.environ['PASSWORD']

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account (sorry cannot share gsheet-secret-keys.json)
creds = ServiceAccountCredentials.from_json_keyfile_name('gsheet-secret-keys.json', scope) 

# authorize the clientsheet 
client = gspread.authorize(creds)

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

    #df = pd.read_csv ('comm2.csv')
    # get the instance of the Spreadsheet
    sheet = client.open('DAmailer2021')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)
    all_data = sheet_instance.get_all_records()
    df = pd.DataFrame.from_dict(all_data)
    #print (df.head())
    if  df.empty:
        exit()
    else:
        mailCIG(df)
        pass

    #print(df)
    # name,corporation,mail,Phone,msg,deliver_lec,start_proj,conduct_workshop,others,time,
    for ind in df.index:
         print(ind,df['name'][ind], df['mail'][ind])
         #ts = datetime.utcfromtimestamp(df['timestamp'][ind]).strftime('%Y-%m-%d %H:%M:%S')
         ct = datetime.now() - timedelta(hours=3)
         ts3 = ct.timestamp()
         if (ts3< df['time'][ind]):
            mailGuest(df['mail'][ind])



if __name__ == "__main__":
    main()