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
currenteversion="v1.0"
def logop(z):
  for word in z + '\n':
     sys.stdout.write(word)
     sys.stdout.flush()
     time.sleep(0.1)
def maogit():
  os.system("xdg-open https://github.com/mao2116/")
def inboxlogo(currentemail):
  inboxlogo_="""
{acl} __  __  {ycl} __  __    _    ___ _
{acl}|  \/  | {ycl}|  \/  |  / \  |_ _| |
{acl}| |\/| | {ycl}| |\/| | / _ \  | || |
{acl}| |  | | {ycl}| |  | |/ ___ \ | || |___
{acl}|_|  |_| {ycl}|_|  |_/_/   \_\___|_____|{ncl}
        
        {acl}[ {bcl}CODER {acl}] {pcl}MAO2116
        {acl}[ {bcl}GITHUB {acl}]{pcl} MAO2116    
        {acl}[ {bcl}THANKS TO {acl}]{pcl} ALLAH
        
{acl}[{bcl} PRESS{gcl} CTRL+C {acl}]{ycl} TO OPEN MAIN MANU   

{acl}[ {gcl}CURRENT{acl}_{mcl}MAIL {acl}] {ycl}{currentemail}

        {acl}[{gcl} !{acl} ] {rcl}INBOX {acl}[{gcl} !{acl} ]{ncl}
""".format(mcl=mcl,acl=acl,ncl=ncl,pcl=pcl,ycl=ycl,bcl=bcl,gcl=gcl,rcl=rcl,currentemail=currentemail)
  print(inboxlogo_)
def ext():
  exit(f"\n{acl}[{rcl} !{acl} ] {gcl}THANKS FOR USING {acl}[{rcl} !{acl} ]\n")
def viewmail():
  if os.path.exists("domain.txt"):
    with open("domain.txt","r") as cmmail:
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
      print(f"{acl}[{gcl} !{acl} ] {ycl}SUCCESSFULLY CREATE A NEW EMAIL {acl}[{gcl} !{acl} ]")
      logop("{acl}[{gcl} !{acl} ]{gcl} CREATED EMAIL {acl}:{ycl} {newemail}".format(newemail=(json.loads(domainr.text))["email"],acl=acl,gcl=gcl,ycl=ycl))

    with open("all_domain.json","r+") as alldr:
      filesdata=alldr.read()
      domall=int(len(filesdata))-2
      domanadd=filesdata[:domall]
      addingmail=domanadd+','+makedic(emailcoustom,mailtoken,(str(digite)))+']}'
     
    with open("all_domain.json","w") as alldr:
      alldr.write(str(addingmail))
    with open("domain.txt","w") as currend:
      currend.write(emailcoustom)
    inboxchkdef()  
  else:
    print("{acl}[{rcl} !{acl} ]{rcl} SELECTED DOMAIN NOT FOUNDED {acl}[{rcl} !{acl} ]")
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
  in__=int(input(f"\n{bcl}>>>> {ycl}"))
  if num+1 >= in__:
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
    
    with open("domain.txt","w") as currend:
      currend.write(login)
      currend.close()
  
    if login == historymail["email"]:
      logop(f"{acl}[{gcl} !{acl} ]{ycl} MAIL SUCCESSFULLY ADDED {acl}[{gcl} !{acl} ]")
      inboxchkdef()
    else:
      logop("{acl}[{rcl} !{acl} ] { gcl}YOUR MAIL{ycl} : {log}".format(log=login,acl=acl,rcl=rcl,ycl=ycl,gcl=gcl))
      exit()

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
  with open("domain.txt","w") as currend:
      currend.write(randommail)
      currend.close()
  inboxchkdef()
  
  

def filchk(mao):
  return os.path.exists(mao)
  
  
def inboxchkdef():
  os.system("clear")
  
  with open("mailchk.mao","w") as faka:
    faka.write(" ")
    faka.close()
  with open("domain.txt","r") as currentemail:
    currentemail=currentemail.read()
    
  currentemail=currentemail
  inboxchk="https://api.internal.temp-mail.io/api/v3/email/{crmail}/messages".format(crmail=currentemail)
  inboxlogo(currentemail)    

  while True:
    try:
      with open("mailchk.mao","r") as maochk:  
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
            mailmes=f"{acl}[{rcl} !{acl} ] {ycl}YOUR MAIL IS EXPIRED {acl}[{rcl} !{acl} ]"
            os.system("clear;")
            print(mailmes)
            time.sleep(2)
            main2()
            break
          else:
            exit(inboxget["message"])
        else:
          with open("mailchk.mao","w") as maochk:
            
            inboxget=json.loads((inboxget1).text)
            maochk.write(str(inboxget))
          for filse,emailtext in enumerate(inboxget):
            if emailtext==[]:
              pass
            else:
             
              print(f"{acl}----------{ycl} INBOX {acl}-----------\n")
              logop("{acl}>>>>   {gcl}EMAIL : {ycl}{filse}\n\n".format(filse=(1+filse), acl=acl,gcl=gcl,ycl=ycl))
              print("{acl}>>> {gcl}FROM {acl}:{ycl} {From}\n".format(From=emailtext['from'],gcl=gcl,acl=acl,ycl=ycl))
              
              print("{acl}>>> {gcl}TO{acl} :{ycl} {To}".format(To=emailtext["to"],acl=acl,gcl=gcl,ycl=ycl))
              print("{acl}>>> {gcl}CC {acl}: {rcl}{cc}".format(cc=emailtext["cc"],acl=acl,gcl=gcl,rcl=rcl))
              print("{acl}>>> {gcl}SUBJECT{acl} :{ycl} {subject}" .format(subject=emailtext["subject"],acl=acl,gcl=gcl,ycl=ycl))
              print("\n{acl}>>> \033[1;0mBODY : {body}".format(body=emailtext["body_text"],acl=acl))
              if emailtext["attachments"] == []:
                pass
              else:
                for num,ia in enumerate(emailtext["attachments"]):
                  print("\n{acl}>>>{gcl} ATTACHMENT NO. {acl}:{ycl} {ia}\n".format(ia=num+1,acl=acl,gcl=gcl,ycl=ycl))
                  print(f"{acl}>>>{gcl} VIEW ATTACHMENT {acl}:{ycl} https://api.internal.temp-mail.io:443/api/v3/attachment/"+(str(ia["id"]))+"?preview=1\n")
                  print(f"{acl}>>>{gcl} DOWNLOAD ATTACHMENT{acl} :{ycl} https://api.internal.temp-mail.io:443/api/v3/attachment/"+(str(ia["id"]))+"?download=1\n")
                  print(f"{acl}>>>{gcl} ATTACHMENT NAME {acl}:{ycl}"+(str(ia["name"]))+"\n")
                  print(f"{acl}>>>{gcl} ATTACHMENT SIZE {acl}:{ycl} "+(str(ia["size"]))+f"{bcl} BYTES\n")
                  
    except Exception as mao:
      exit(mao)
    except  KeyboardInterrupt:
      main2()
      break
def more():
  logo=f"""
  
  {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
  {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
  {acl}[{gcl} 3{bcl}.{acl} ]{ycl} SEE ALL EMAIL {acl}[{bcl} YOU CREATED {acl}]
  {acl}[{gcl} 4{bcl}.{acl} ]{ycl} VIEW CUREENT MAIL {acl}[ {ccl}ALL MAILS {acl}]
  {acl}[{gcl} 5{bcl}.{acl} ]{ycl} EMAILS HISTORY {acl}[ {bcl}YOU CAN LOG IN {acl}]
  {acl}[{gcl} 6{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
  {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT {acl}[{bcl} ×××{acl} ]
  """
  while True:
    os.system("clear")
    print(manuhome)
    print(logo)
    manuin=input(f"{acl}>>>{ycl} ")
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
def main2():
  logo=f"""
  
  {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
  {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
  {acl}[{gcl} 3{bcl}.{acl} ]{ycl} MORE FEATURES {acl}[ {bcl}... {acl}]
  {acl}[{gcl} 4{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
  {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT{acl} [{rcl} ××× {acl}]
  """
  while True:
    
    os.system("clear")
    print(manuhome)
    print(logo)
    manuin=input(f"{acl}>>>{ycl} ")
    if manuin=="1":
      randomemail()
      break
    elif manuin=="2":
      coustomnewdomains()
      break
    elif manuin=="3":
      more()
      break
    elif manuin =="4":
      maogit()
      break
    elif manuin=="0":
      ext()
      break
    else:
      print(f"{acl}[{rcl} !{acl} ]{rcl} INVALID SELECTION {acl}[{rcl} !{acl} ]")
      time.sleep(2)
def main():
  logo=f"""
  
  {acl}[{gcl} 1{bcl}.{acl} ]{ycl} CREATE NEW MAIL{acl} [{ccl} RANDOM {acl}] 
  {acl}[{gcl} 2{bcl}.{acl} ]{ycl} CREAT NEW MAIL{acl} [{bcl} CREAT YOUR SELF {acl}]
  {acl}[{gcl} 3{bcl}.{acl} ]{ycl} MORE FEATURES {acl}[ {bcl}... {acl}]
  {acl}[{gcl} 4{bcl}.{acl} ]{ycl} GITHUB {acl}[{bcl} MAO2116 {acl}]
  {acl}[{rcl} 0{bcl}.{acl} ]{rcl} EXIT{acl} [{rcl} ××× {acl}]
  """
  while True:
    if filchk("domain.txt"):
      inboxchkdef()
      break
    else:
      os.system("clear")
      print(manuhome)
      print(logo)
      manuin=input(f"{acl}>>>{ycl} ")
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
        break
      elif manuin=="0":
        ext()
      else:
        print(f"{acl}[{rcl} !{acl} ]{rcl} INVALID SELECTION {acl}[{rcl} !{acl} ]")
        time.sleep(2)
def __init__():
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
        
#main()
__init__()
