#MAO2116
#coding/bin/python3
#coding=utf-8
from core.headers import *
from core.logo import *
import os
try:
  import requests
except:
  os.system("pip install requests")
import json, requests ,os, random, time, sys
from requests import post as rp
rs=requests.session()
rg=rs.get
maomailex=""
mailmes=""
currenteversion="v1.2"
def logop(z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.01)
def maogit():
  os.system("xdg-open https://github.com/mao2116/")
def ext():
  exit("\n{acl}[{rcl} !{acl} ] {gcl}THANKS FOR USING {acl}[{rcl} !{acl} ]\n".format(acl=acl,rcl=rcl,gcl=gcl))
def viewmail():
  if os.path.exists("core/domain.txt"):
    with open("core/domain.txt","r") as cmmail:
      cmmail = cmmail.read()
    print(f"{acl}>>>{bcl} CUREENT _ MAIL{acl} :{ycl} {cmmail}")  
    x_X=input(f"\n\n{ycl} BACK MAIN MANU {acl}[{gcl}y{ncl}/{rcl}n{acl}] {acl}:{bcl} ")
    if x_X=="y":
      main()
    elif x_X=="n":
      ext()  
  else:
    main()
def coustomnewdomains():
  domain=(json.loads(rg("https://api.internal.temp-mail.io/api/v3/domains",headers=header).text))["domains"]
  email_name=str(input(f"{acl} >>>{gcl} ENTER EMAIL NAME  {acl}:{ycl} "))
  for domainsrow,domains in enumerate(domain):
      print(f"{acl}[{gcl}",domainsrow+1,f"{acl}]{bcl}",domains["name"],f" {gcl}!{ncl}")
  ma=int(input(f"{acl}>>>{gcl} SELECT YOUR DOMAIN {acl}:{ycl} "))
  if domainsrow+1 >= ma:
    inputdomain=ma-1
    print(f"{acl}[ {gcl}>>> {acl}]{gcl} SELECTED DOMAIN {acl}:{ycl}"+domain[inputdomain]["name"])
    coustom_domain=domain[inputdomain]["name"]
    
    coustom={
	"name":email_name,
	"domain":coustom_domain
}
    digite=len(email_name)
    newdomain="https://api.internal.temp-mail.io/api/v3/email/new"
    domainr=rp(newdomain,json=coustom,headers=header)
    emailcoustom=email_name+"@"+coustom_domain
    domaincon=(json.loads(domainr.text))["email"]==emailcoustom
    mailtoken=(json.loads(domainr.text))["token"]
    if domaincon:
      logop(f"{acl}[{gcl} !{acl} ] {ycl}SUCCESSFULLY CREATE A NEW EMAIL {acl}[{gcl} !{acl} ]")
      logop("{acl}[{gcl} !{acl} ]{gcl} CREATED EMAIL {acl}:{ycl} {newemail}".format(newemail=(json.loads(domainr.text))["email"],acl=acl,gcl=gcl,ycl=ycl))

    with open("all_domain.json","r+") as alldr:
      filesdata=alldr.read()
      domall=int(len(filesdata))-2
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(emailcoustom,mailtoken,(str(digite)))+']}'
     
    with open("all_domain.json","w") as alldr:
      alldr.write(str(addingmail))
    with open("core/domain.txt","w") as currend:
      currend.write(emailcoustom)
    inboxchkdef()  
  else:
    print(f"{acl}[{rcl} !{acl} ]{rcl} SELECTED DOMAIN NOT FOUNDED {acl}[{rcl} !{acl} ]")
    
    coustomnewdomains()
def seemail():
  with open("all_domain.json","r") as read:
    read=(json.loads(read.read()))["domains"]
  os.system("clear")
  print(manuhome)
  for num , mail in enumerate(read):
    print("{acl}[{bcl} {mao} {acl}]{ycl} ".format(mao=num+1,acl=acl,bcl=bcl,ycl=ycl)+mail["email"])
  x_X=input(f"\n\n{ycl} BACK MAIN MANU {acl}[{gcl}y{ncl}/{rcl}n{acl}] {acl}:{bcl} ")
  if x_X=="y":
    main()
  elif x_X=="n":
    ext()
def historylog():
  url='https://api.internal.temp-mail.io/api/v3/email/new'
  with open("all_domain.json","r") as read:
    read=(json.loads(read.read()))["domains"]
  os.system("clear")
  print(manuhome)
  for num , mail in enumerate(read):
    print("{acl}[ {gcl}{mao} {acl}] {ycl}".format(mao=num+1,acl=acl,gcl=gcl,ycl=ycl)+mail["email"])
  print(f"{acl}[{rcl} 0. {acl}]{pcl} BACK MAIN MANU {acl}[ {gcl}../{acl} ]")  
  in__=int(input(f"\n{bcl}>>>> {ycl}"))
  if num+1 >= in__ and in__ != 0:
    
    index=(in__-1)
    historymail=read[index]
    number=(int((len(historymail["email"]))))-(int(historymail["digit"]))
    number=(int(historymail["digit"]))
    emailmail=(historymail["email"])[:(int(historymail["digit"]))]
    domainn=(historymail["email"])[((int(historymail["digit"]))+1):]
    jsonmao={
	"name":emailmail,
	"token":(historymail["token"]),
	"domain":domainn
}
    login=(json.loads(rp(url,json=jsonmao,headers=header).text))["email"]
    
    with open("core/domain.txt","w") as currend:
      currend.write(login)
      currend.close()
  
    if login == historymail["email"]:
      logop(f"{acl}[{gcl} !{acl} ]{ycl} MAIL SUCCESSFULLY ADDED {acl}[{gcl} !{acl} ]")
      inboxchkdef()
    else:
      logop("{acl}[{rcl} !{acl} ] { gcl}YOUR MAIL{ycl} : {log}".format(log=login,acl=acl,rcl=rcl,ycl=ycl,gcl=gcl))
      exit()
  elif  in__==0:
    #break
    main2()

def makedic(mail,token,digit):
  dic="{\"email\":\""+mail+"\",\"token\":\""+token+"\",\"digit\":\""+digit+"\"}"
  return dic
def randomemail():
  randomtype=random.randint(10,15)
  randomemai_l={
	"min_name_length":randomtype,
	"max_name_length":randomtype
}
  newdomain="https://api.internal.temp-mail.io/api/v3/email/new"
  randomemail=(json.loads((rp(newdomain,json=randomemai_l)).text))
  randommail=randomemail["email"]
  mailtoken=randomemail["token"]
  with open("all_domain.json","r+") as alldr:
      randomtypestr=str(randomtype)
      filesdata=alldr.read()
      domall=int(len(filesdata))-2
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(randommail,mailtoken,randomtypestr)+']}'
      alldr.close()
     
  with open("all_domain.json","w") as alldr:
      alldr.write(str(addingmail))
      alldr.close()
  with open("core/domain.txt","w") as currend:
      currend.write(randommail)
      currend.close()
  logop(f"{acl}[{gcl} !{acl} ] {ycl}SUCCESSFULLY CREATE A NEW EMAIL {acl}[{gcl} !{acl} ]")
  logop("{acl}[{gcl} !{acl} ]{gcl} CREATED EMAIL {acl}:{ycl} {newemail}".format(newemail=randommail,acl=acl,gcl=gcl,ycl=ycl))    
  inboxchkdef()
  
  

def filchk(mao):
  return os.path.exists(mao)
  
  
def inboxchkdef():
  os.system("clear")
  
  with open("core/mailchk.mao","w") as faka:
    faka.write(" ")
    faka.close()
  with open('core/maocount.mao','w') as maocount:
    maocount.write("0")
    maocount.close()
  with open("core/domain.txt","r") as currentemail:
    currentemail=currentemail.read()
    
  currentemail=currentemail
  inboxchk="https://api.internal.temp-mail.io/api/v3/email/{crmail}/messages".format(crmail=currentemail)
  inboxlogo(currentemail)    

  while True:
    try:
      with open("core/mailchk.mao","r") as maochk:  
        defaultbox=maochk.read()
        maochk.close()
      time.sleep(1.5)
      inboxget1=  rg(inboxchk,headers=header)
      inboxget=json.loads((inboxget1).text)
      x=str(defaultbox)==str(inboxget)
      if str(defaultbox)==str(inboxget):
        pass
      else:
        if inboxget == []:
          pass
        elif inboxget1.status_code==400:
          inboxget["message"]
          if inboxget["message"]=="Email not found":
            os.system("clear;")
            print("{acl}[{rcl} !{acl} ] {ycl}YOUR MAIL IS EXPIRED {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl,ycl=ycl))
            time.sleep(2)
            main2()
            break
          else:
            exit(inboxget["message"])
        else:
          with open("core/mailchk.mao","w") as maochk:
            
            inboxget=json.loads((inboxget1).text)
            maochk.write(str(inboxget))
         
          for filse,emailtext in enumerate(inboxget):
            if emailtext==[]:
              pass
            else:
        
              if int(open('core/maocount.mao','r').read()) <filse+1:
                
                with open('core/maocount.mao','w') as maocount:
                  
                  maocount.write(str(filse+1))
                  maocount.close()
                
                logop(f"{acl}----------{ycl} INBOX {acl}-----------\n")
                logop("{acl}>>>>   {gcl}EMAIL : {ycl}{filse}\n".format(filse=(1+filse), acl=acl,gcl=gcl,ycl=ycl))
                if 'T' in emailtext["created_at"]:
                  timecr=emailtext["created_at"].replace("T","mao")
                  maotime=timecr.split("mao")
                 
                else:
                  timecr=emailtext["created_at"]
                for num,i in enumerate(maotime):
                  if num==0:
                    date=i
                  elif num == 1:
                    timecr=i.split(":")
                    for num,timeing in enumerate(timecr):
                      if num==0:
                        hour=int(timeing)
                        hour=hour+6 
                        hour=str(hour)
                      elif num==1:
                        minit=timeing
                      elif  num==2:
                        second=timeing[:2]
                    print("{acl}>>> {gcl}Date {acl}:{ycl} {time}".format(time=date+', '+hour+":"+minit+':'+second,acl=acl,ycl=ycl,gcl=gcl))  
                if "<" in emailtext['from']:
                  fromf_ck=emailtext['from']
                  f_cky=fromf_ck.replace(" <"," • ")
                  f_cky=f_cky.replace(">", "")
                  if '"' in f_cky:
                    f_cky=f_cky.replace('"','')
                  else:
                    pass
                else:
                  f_cky=emailtext['from']
                print("{acl}>>> {gcl}FROM {acl}:{ycl} {From}\n".format(From=f_cky,gcl=gcl,acl=acl,ycl=ycl))
                
                print("{acl}>>> {gcl}TO{acl} :{ycl} {To}".format(To=emailtext["to"],acl=acl,gcl=gcl,ycl=ycl))
                if str(emailtext["cc"])== "None":
                  pass
                else:
                  print("{acl}>>> {gcl}CC {acl}: {rcl}{cc}".format(cc=emailtext["cc"],acl=acl,gcl=gcl,rcl=rcl))
                print("{acl}>>> {gcl}SUBJECT{acl} :{ycl} {subject}" .format(subject=emailtext["subject"],acl=acl,gcl=gcl,ycl=ycl))
                print("\n{acl}>>> \033[1;0mBODY : {body}".format(body=emailtext["body_text"],acl=acl))
                
                if emailtext["attachments"] == []:
                  pass
                else:
                  for num,ia in enumerate(emailtext["attachments"]):
                    print("\n{acl}>>>{gcl} ATTACHMENT NO. {acl}:{ycl} {ia}\n".format(ia=num+1,acl=acl,gcl=gcl,ycl=ycl))
                    print(f"{acl}>>>{gcl} VIEW ATTACHMENT {acl}:{ycl} https://api.internal.temp-mail.io/api/v3/attachment/"+(str(ia["id"]))+"?preview=1\n")
                    print(f"{acl}>>>{gcl} DOWNLOAD ATTACHMENT{acl} :{ycl} https://api.internal.temp-mail.io/api/v3/attachment/"+(str(ia["id"]))+"?download=1\n")
                    print(f"{acl}>>>{gcl} ATTACHMENT NAME {acl}:{ycl}"+(str(ia["name"]))+"\n")
                    if 1048576<=int(ia["size"]):
                      mathsize=str((int(ia["size"]))/1048576)
                      sizeofia=mathsize[:4]
                      print(f"{acl}>>>{gcl} ATTACHMENT SIZE {acl}:{ycl} "+str(sizeofia)+f"{bcl} M.B.\n")
                    elif 1048576>=int(ia["size"]) and 1024<=int(ia["size"]):
                      mathsize=str((int(ia["size"]))/1024)
                      sizeofia=mathsize[:4]
                      print(f"{acl}>>>{gcl} ATTACHMENT SIZE {acl}:{ycl} "+str(sizeofia)+f"{bcl} K.B.\n")
                    
                    else:
                      print(f"{acl}>>>{gcl} ATTACHMENT SIZE {acl}:{ycl} "+str(ia["size"])+f"{bcl} BYTES\n")
                      
              else:
                pass
    except Exception as mao:
      exit(mao)
    except  KeyboardInterrupt:
      main2()
      break
def more():
  logo="""
  
  {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
  {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
  {acl}[{gcl} 3{bcl}.{acl} ]{ycl} SEE ALL EMAIL {acl}[{bcl} YOU CREATED {acl}]
  {acl}[{gcl} 4{bcl}.{acl} ]{ycl} VIEW CUREENT MAIL {acl}[ {ccl}ALL MAILS {acl}]
  {acl}[{gcl} 5{bcl}.{acl} ]{ycl} EMAILS HISTORY {acl}[ {bcl}YOU CAN LOG IN {acl}]
  {acl}[{gcl} 6{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
  {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT {acl}[{bcl} ×××{acl} ]
  """.format(acl=acl,bcl=bcl,gcl=gcl,ycl=ycl,rcl=rcl,ccl=ccl)
  try:
    while True:
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{acl}  ~~~>>>{ycl} ")
      if manuin=="1":
        randomemail()
        break
      elif manuin=="2":
        coustomnewdomains()
        break
      elif manuin =="3":
        seemail()
        break
      elif manuin =="4":
        viewmail()
        break
      elif manuin=="5":
        historylog()
        break
      elif manuin=="6":
        maogit()
        break
      elif manuin=="0":
        ext()
        break
      else:
        print("[ ! ] INVALID SELECTION [ ! ]")
        time.sleep(2)
  except KeyboardInterrupt:
    x_X=input(f"\n\n{ycl} BACK MAIN MANU OR TYPE {rcl}n{ycl} TO EXIT {acl}[{gcl}y{ncl}/{rcl}n{acl}] {acl}:{bcl} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()      
def more2():
  logo="""
  
  {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
  {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
  {acl}[{gcl} 3{bcl}.{acl} ]{ycl} INBOX CHECK{acl} [{bcl} ALL MAILS {acl}]
  {acl}[{gcl} 4{bcl}.{acl} ]{ycl} SEE ALL EMAIL {acl}[{bcl} YOU CREATED {acl}]
  {acl}[{gcl} 5{bcl}.{acl} ]{ycl} VIEW CUREENT MAIL {acl}[ {ccl}ALL MAILS {acl}]
  {acl}[{gcl} 6{bcl}.{acl} ]{ycl} EMAILS HISTORY {acl}[ {bcl}YOU CAN LOG IN {acl}]
  {acl}[{gcl} 7{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
  {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT {acl}[{bcl} ×××{acl} ]
  """.format(acl=acl,bcl=bcl,gcl=gcl,ycl=ycl,rcl=rcl,ccl=ccl)
  try:
    
    while True:
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{acl}  ~~~>>>{ycl} ")
      if manuin=="1":
        randomemail()
        break
      elif manuin=="2":
        coustomnewdomains()
        break
      elif manuin=="3":
        inboxchkdef()
        break
      elif manuin =="4":
        seemail()
        break
      elif manuin =="5":
        viewmail()
        break
      elif manuin=="6":
        historylog()
        break
      elif manuin=="7":
        maogit()
        break
      elif manuin=="0":
        ext()
        break
      else:
        print("[ ! ] INVALID SELECTION [ ! ]")
        time.sleep(2)   
  except KeyboardInterrupt:
    x_X=input(f"\n\n{ycl} BACK MAIN MANU OR TYPE {rcl}n{ycl} TO EXIT {acl}[{gcl}y{ncl}/{rcl}n{acl}] {acl}:{bcl} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()      
def main2():
  try:
    logo="""
    
    {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
    {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
    {acl}[{gcl} 3{bcl}.{acl} ]{ycl} INBOX CHECK{acl} [{bcl} ALL MAILS {acl}]
    {acl}[{gcl} 4{bcl}.{acl} ]{ycl} MORE FEATURES {acl}[ {bcl}... {acl}]
    {acl}[{gcl} 5{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
    {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT{acl} [{rcl} ××× {acl}]
    """.format(acl=acl,bcl=bcl,gcl=gcl,ycl=ycl,rcl=rcl,ccl=ccl)
    while True:
      
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{acl}  ~~~>>>{ycl} ")
      if manuin=="1":
        randomemail()
        break
      elif manuin=="2":
        coustomnewdomains()
        break
      elif manuin=="3":
        inboxchkdef()
        break
      elif manuin=="4":
        more2()
        break
      elif manuin =="5":
        maogit()
        break
      elif manuin=="0":
        ext()
        break
      else:
        print("{acl}[{rcl} !{acl} ]{rcl} INVALID SELECTION {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl))
        time.sleep(2)
  except KeyboardInterrupt:
    x_X=input(f"\n\n{ycl} BACK MAIN MANU OR TYPE {rcl}n{ycl} TO EXIT {acl}[{gcl}y{ncl}/{rcl}n{acl}] {acl}:{bcl} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()    
def main():
  try:
    
    logo="""
    
    {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
    {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
    {acl}[{gcl} 3{bcl}.{acl} ]{ycl} MORE FEATURES {acl}[ {bcl}... {acl}]
    {acl}[{gcl} 4{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
    {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT{acl} [{rcl} ××× {acl}]
    """.format(acl=acl,bcl=bcl,gcl=gcl,ycl=ycl,rcl=rcl,ccl=ccl)
    while True:
      if filchk("core/domain.txt"):
        inboxchkdef()
        break
      else:
        os.system("clear")
        print(manuhome)
        print(logo)
        manuin=input(f"{acl}  ~~~>>>{ycl} ")
        if manuin=="1":
          randomemail()
          break
        elif manuin=="2":
          coustomnewdomains()
          break
        elif manuin=="3":
          more()
          break
        elif manuin=="4":
          maogit()
          break
        elif manuin=="0":
          ext()
        else:
          print("{acl}[{rcl} !{acl} ]{rcl} INVALID SELECTION {acl}[{rcl} !{acl} ]".format(acl=acl,rcl=rcl))
          time.sleep(2)
        
  except KeyboardInterrupt:
    x_X=input(f"\n\n{ycl} BACK MAIN MANU OR TYPE {rcl}n{ycl} TO EXIT {acl}[{gcl}y{ncl}/{rcl}n{acl}] {acl}:{bcl} ")
    if x_X=="y":
      main2()
    elif x_X=="n":
      ext()
        
        
        
def __init__():
  try:
    os.system("clear")
    print(loginpromt)
    x=json.loads(rg("https://raw.githubusercontent.com/mao2116/test/main/testpy/mao.json",headers=headergit).text)
    if x["condition"] == "on":
      if x["version"]==currenteversion:
        if x["api"] == "running":
          main()
        else:
          exit("[ ! ] API DOWN [ ! ]")
      else:
        os.system("bash core/up_mmail.sh")
    else:
      exit("[ ! ] TOOL IS OFF [ ! ]")
  except Exception as mm:
    exit(mm)

__init__()
