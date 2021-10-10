Aug/21
The idea "Quick response to corporates and people who wishes to contact CIG-IITR"
'''
Suppose some delegates of a corporation wishes to contact CIG-IITR. So they will fill the form
given ... It will go to the database and an automated no-reply chat bot type mail /message will be sent 
on one hand on other hand CIG quick response team will be alerted start working on proper communication channels
Quick response Time with automation will be beneficial to both delegates and CIG team as it will 
save time and effort.
'''
Major Implementation:
The contact us form would be linked to the a googlesheet/DBMS which will scanned on hourly basis
by a python script. If a new delegate is found it will contact CIG response team and
also send an automated reply to the delegates.

comm.csv # demo table/db
name,mail,timestamp,reason,connection
timestamp is unix epoch timestamp (in seconds)

Toschedule a python script in linux use cron. (see schedule_cron.txt)

Using python 3.8.10
Sept/2021
modules :

>> main
datetime
smtplib
pandas
tabulate

>> googlesheet
gspread
google-api-python-client 
oauth2client

Readcsv.py v0
v0
-basic skeleton is done.
v0p1 (sept/21)
- added a feature that subsets only for last 3 hours data from all DBMS
+ (to be done) make a suitable python script task scheduler (currently using cron)
+ (") make it more secure
+ (") add auto schedule to run it every 3 hours.

readGsheets.py v0 (oct/21)
v0 
- uses an online googlesheets instead of csv as input dataframe.
-use following data structure : 
    name:"",    
    corporation:"",
    mail:"",    
    Phone:"",   
    msg:"",
    deliver_lec:false,
    start_proj:false,
    conduct_workshop:false,
    others:false,
    (see comm2.csv)




