import urllib
import re
import os.path

addList = ["https://en.wikipedia.org/wiki/Hello_%28Adele_song%29"]
def getLinks():
	address = addList.pop(0)
	if(len(address) > 150):
		return
	print "Working on  "+address
	try:
		fname = address.split("://")[1]
		fname = fname.replace("/","_sl_")
		fname = fname.replace(":","_cl_")
		f = open("data/"+fname+".txt","w")
		value = urllib.urlopen(address).read()
		value = re.sub(">.*?<","><",value);
		value = re.sub("</.*?>"," ",value); 
		links = value.split(">");
		for i in  links:
			if "<a" in i and "href" in i and "http" in i :
			  	i =re.sub(".*<a.*?href.*?=","",i);
			      	i = i.replace("\"","");
			      	i = i.replace("\'","");  
				f.write("<a href=\""+i+"></a>\n")
			      	addList.append(i)
		f.close()
	except:
		print "error crawling"
def crawlChunk():
	for i in range(50):
		getLinks()
		print str(i+1)+" : Crawled " + str(len(set(addList))) + " pages"
	f2 = open("queue.txt","w")
	for i in addList:
		f2.write(i+" ")
	f2.close()

if os.path.isfile("queue.txt") :
	f1 = open("queue.txt")
	addList = f1.read().split(" ")
while(1):
	crawlChunk()
