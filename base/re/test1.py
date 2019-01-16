import re

print(re.match('www', 'www.google.com.cn').span())

line = "Cat are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I )

if matchObj:
    print("group()", matchObj.group())
    print("group(0)", matchObj.group(0))
    print("group  ", matchObj)
    print("group(1)", matchObj.group(1))
    print("group(2)", matchObj.group(2))
    # print("group(3) error", matchObj.group(3))
else:
    print("no match")
