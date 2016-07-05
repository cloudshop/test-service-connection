#!Python.exe
#-*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from email import encoders

from_addr = "yaop@tuyouchina.com"
password = "19849121Yp"
smtp_server = "smtp.mxhichina.com"
to_addr = ['57150877@qq.com','wcyc_yp@126.com']

message=MIMEMultipart()
message['From']=from_addr
message['To'] =  ",".join(to_addr)
subject = '服务运行状态监测报告'
message['Subject'] = Header(subject, 'utf-8')
with open("E:\\apache-jmeter\\report\\html\\LeiFengReport.html",'rb') as q:
	msg=q.read().decode('utf-8')
	#print(msg)
	q.close()
message.attach(MIMEText(msg,'html','utf-8'))
with open('E:\\apache-jmeter\\report\\html\\LeiFengReport.html','rb') as f:
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(f.read())
    att.add_header('Content-Disposition', 'attachment', filename="testReport.html")
    encoders.encode_base64(att)
    message.attach(att)
with open('E:\\apache-jmeter\\report\\html\\expand.png','rb') as o:
    att1 = MIMEBase('application', 'octet-stream')
    att1.set_payload(o.read())
    att1.add_header('Content-Disposition', 'attachment', filename="expand.png")
    encoders.encode_base64(att1)
    message.attach(att1)
with open('E:\\apache-jmeter\\report\\html\\collapse.png','rb') as p:
    att2 = MIMEBase('application', 'octet-stream')
    att2.set_payload(p.read())
    att2.add_header('Content-Disposition', 'attachment', filename="collapse.png")
    encoders.encode_base64(att2)
    message.attach(att2)
t=0
while(1):
    try:
        smtpObj = smtplib.SMTP_SSL(smtp_server,465)
        smtpObj.login(from_addr,password)
        smtpObj.sendmail(from_addr, to_addr, message.as_string())
        smtpObj.quit()
        t=0
        print("send success")
    except smtplib.SMTPException:
        t=1
        print("Error: failed")
    if t!=0:
        continue
    else:
        break