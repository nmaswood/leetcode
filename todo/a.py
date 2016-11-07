import re
myLine="This is;a-line,with pieces"
for p in re.split("[ ;\-,]",myLine):
    print("piece="+p)