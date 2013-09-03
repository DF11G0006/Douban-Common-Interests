import simplejson
import urllib.request
import urllib.parse
import http.cookiejar
import webbrowser
from bs4 import BeautifulSoup

username='xxxxxxxx'
password='xxxxxxxx'
log_file_name='log.txt'
COUNT=100
ALOT=12
start=1000001
stop=80000000

cj = http.cookiejar.LWPCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
login_path = 'http://www.douban.com/accounts/login'
urllib.request.install_opener(opener)
log_page=urllib.request.urlopen(login_path)

data = {"form_email":username,"form_password":password,"remember":"true"}
soup_log=BeautifulSoup(log_page)
if soup_log.find(id='captcha_image'):
        im=soup_log.find(id='captcha_image')
        im_url=im['src']
        cap=soup_log.find(attrs={'name':'captcha-id'})
        cap_id=cap['value']
        webbrowser.open(im_url)
        print('Please input the captcha that is shown in the page:\n')
        captcha=input()
        data['captcha-solution']=captcha
        data['captcha-id']=cap_id


post_data = urllib.parse.urlencode(data)
post_data = post_data.encode('utf-8')
html=urllib.request.urlopen(login_path,post_data)
log_in=BeautifulSoup(html.read())
if log_in.find(id='wrapper'):
        print('Log in successful.\n')


if cj:
        cj.save('cookiefile.txt')

def find_itr(id,log_file):
	url='http://www.douban.com/j/people/'+str(id)+'/common_interest'
	try:
		text=urllib.request.urlopen(url).read().decode('utf-8')
	except urllib.request.HTTPError:
		return -1
	else:
		print('User ID '+str(id)+' exists.\n')
		content=simplejson.loads(text)
		if content['total']>0:
			print('User ID '+str(id)+' shares '+str(content['total'])+' interests with you:\n')
			user={'id':id}
			user['num']=content['total']
			user['items']=[]
			com_soup=BeautifulSoup(content['more_html'])
			aobs=com_soup.findAll('a')
			for i in aobs:
					print(i['title']+'\n')
					user['items'].append(i['title'])
			log_file.write(str(user)+',')
			if content['total']>ALOT:
				webbrowser.open('http://www.douban.com/people/'+str(id))
		return 1

def sort(log_file_name,sorted_file_name,not_compl):
	f=open(log_file_name,'r')
	log=f.read()
	if(not_compl==1):
		log=log[0:len(log)-1]+']'
	data=eval(log)
	data.sort(key=lambda x:x['num'],reverse=True)
	f.close
	f=open(sorted_file_name,'w')
	sorted_log=str(data)
	if(not_compl==1):
		sorted_log=sorted_log[0:len(sorted_log)-1]+','
	f.write(sorted_log)
	f.close


def main():
	common={}
	log_file=open(log_file_name,'a')
	log_file.write('[')
	count=0
	for id in range(start,stop):
		find_itr(id,log_file)
		count=count+1
		if count>COUNT:
			count=0
			log_file.close()
			sort(log_file_name,log_file_name,1)
			log_file=open(log_file_name,'a')
	log_file.write(']')
	log_file.close()
	sort(log_file_name,log_file_name,0)
main()
