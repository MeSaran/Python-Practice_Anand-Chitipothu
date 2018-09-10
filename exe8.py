import re
import urllib
url = 'http://checkip.dyndns.org'
request = urllib.urlopen(url).read()
Ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',request)
print(Ip)
