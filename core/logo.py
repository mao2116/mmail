acl='\033[1;30m'
rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
pcl = '\033[1;35m'
ccl='\033[1;36m' 
wcl='\033[1;37m'
mcl = '\033[1;94m'
ncl='\033[0;00m'
rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
pcl = '\033[1;35m'
ccl='\033[1;36m' 
wcl='\033[1;37m'
mcl = '\033[1;94m'
ncl='\033[0;00m'
loginpromt="""
{acl} __  _V1.2{ycl}__  __    _    ___ _
{acl}|  \/  | {ycl}|  \/  |  / \  |_ _| |
{acl}| |\/| | {ycl}| |\/| | / _ \  | || |
{acl}| |  | | {ycl}| |  | |/ ___ \ | || |___
{acl}|_|  |_| {ycl}|_|  |_/_/   \_\___|_____|{ncl}
        
        {acl}[ {bcl}CODER {acl}] {pcl}MAO2116
        {acl}[ {bcl}GITHUB {acl}]{pcl} MAO2116    
        {acl}[ {bcl}THANKS TO {acl}]{pcl} ALLAH !
        
        {acl}[{gcl} !{acl} ] {rcl}ANALYSING  DATA{acl}[{gcl} !{acl} ]{ncl}
""".format(acl=acl,ncl=ncl,pcl=pcl,ycl=ycl,bcl=bcl,gcl=gcl,rcl=rcl)
manuhome="""
{acl} __  __V1.2{ycl}_  __    _    ___ _
{acl}|  \/  | {ycl}|  \/  |  / \  |_ _| |
{acl}| |\/| | {ycl}| |\/| | / _ \  | || |
{acl}| |  | | {ycl}| |  | |/ ___ \ | || |___
{acl}|_|  |_| {ycl}|_|  |_/_/   \_\___|_____|{ncl}
        
        {acl}[ {bcl}CODER {acl}] {pcl}MAO2116
        {acl}[ {bcl}GITHUB {acl}]{pcl} MAO2116    
        {acl}[ {bcl}THANKS TO {acl}]{pcl} ALLAH !
        
        {acl}[{gcl} !{acl} ] {rcl}MANU {acl}[{gcl} !{acl} ]{ncl}
""".format(acl=acl,ncl=ncl,pcl=pcl,ycl=ycl,bcl=bcl,gcl=gcl,rcl=rcl)
def inboxlogo(currentemail):
  inboxlogo_="""
{acl} __  _V1.2{ycl}__  __    _    ___ _
{acl}|  \/  | {ycl}|  \/  |  / \  |_ _| |
{acl}| |\/| | {ycl}| |\/| | / _ \  | || |
{acl}| |  | | {ycl}| |  | |/ ___ \ | || |___
{acl}|_|  |_| {ycl}|_|  |_/_/   \_\___|_____|{ncl}
        
        {acl}[ {bcl}CODER {acl}] {pcl}MAO2116
        {acl}[ {bcl}GITHUB {acl}]{pcl} MAO2116    
        {acl}[ {bcl}THANKS TO {acl}]{pcl} ALLAH !
        
{acl}[{bcl} PRESS{gcl} CTRL+C {acl}]{ycl} TO OPEN MAIN MANU   

{acl}[ {gcl}CURRENT{acl}_{mcl}MAIL {acl}] {ycl}{currentemail}

        {acl}[{gcl} !{acl} ] {rcl}INBOX {acl}[{gcl} !{acl} ]{ncl}
""".format(mcl=mcl,acl=acl,ncl=ncl,pcl=pcl,ycl=ycl,bcl=bcl,gcl=gcl,rcl=rcl,currentemail=currentemail)
  print(inboxlogo_)
