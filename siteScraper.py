import urllib
import os
import os.path
import re

q = ["http://hadoop.apache.org/docs/current/index.html"]
base = '/home/srijan/crawl/hadoop/'
rt = 'http://hadoop.apache.org/'

def getPage():
	if len(q) is 0:
		print "Finished"
		return
	url = q.pop(0)
	print url
	try:
		if ".html" not in url and ".pdf" not in url :
			print "Not useful"
			return
		fname = url.split("//")[1].split("/")[-1]
		p= url.split("//")[1].split("/")
		cur = ""
		if len(p) > 1:
			pt = ('/').join(p[1:-1])
			path = base  + pt
			if not os.path.exists(path):
				cp = base
				for i in p[1:-1]:
					cp = cp + '/' + i
					if not os.path.exists(cp):
						os.mkdir(cp)
			fname = path + '/'+fname
			cur = pt + "/"
		else:
			fname = base + fname
		page = urllib.urlopen(url).read()
		if not os.path.isfile(fname) :
			f = open(fname,"w")
			f.write(page)
			f.close()
		value = re.sub(">.*?<","><",page)
		value = re.sub("</.*?>"," ",value)
		links = value.split(">");
		for i in  links:
			if "<a" in i and "href" in i :
			  	i =re.sub(".*<a.*?href.*?=","",i)
			      	i = i.replace("\"","")
			      	i = i.replace("\'","")
			      	i = i.replace("\n","")
			      	if "http" not in i and "#" not in i:
			      		q.append(rt + cur + i)
			      	elif rt in i:
			      		q.append(i)
	except:
		print "Error occured"

while(1):
	getPage()
	q = list(set(q))
	      	

	
