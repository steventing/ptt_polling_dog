import requests
from bs4 import BeautifulSoup
import re, time, sys
import signal
#import sys
#res=requests.get('https://www.ptt.cc/bbs/HatePolitics/index.html')
glo = False

def signal_handler(signal, frame):
	print('Ctrl + C evnet')
	global glo
	glo = True

signal.signal(signal.SIGINT, signal_handler)
while True:
	url = 'https://www.ptt.cc/bbs/BuyTogether/index.html'
	res=requests.get(url=url, cookies={'over18': '1'})
	#res=requests.get('https://www.ptt.cc/bbs/BuyTogether/index.html')
	#  print res.text.encode('utf-8')

	soup=BeautifulSoup(res.text.encode('utf-8'), "html.parser")

	#print(soup)
	for pp in soup.select('.r-ent'):
		#print (pp.select('.title')[0].text)
		sech = pp.select('.title')[0].text
		if 'spotify' in sech.lower():
			if '截止'.encode('utf-8') not in sech.lower().encode('utf-8'):
				print (sech)
		#print (sech.lower())
		#if 'spotify' in search.lower()
		#print(pp)
		#sys.stdout.buffer.write(outbuf)
		#print pp.select('.date')[0].text.encode('utf-8'),pp.select('.author')[0].text.encode('utf-8')
	#print (glo)
	time.sleep(3)
	if glo == True:
		print('Bye Bye')
		break


