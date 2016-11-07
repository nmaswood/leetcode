import re
myLine="This is;;;;;;;;;a-line,with pieces"
res = re.split("[ ;\-,]",myLine)

print (res)