import urllib.request as req

fh = req.urlopen("http://data.pr4e.org/romeo.txt")

for line in fh:
   print(line.decode().strip())
