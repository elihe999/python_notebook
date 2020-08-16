from urllib import request, parse

url = 'http://httpbin.org/get'
parms = {
        'name':'value'
}

querystring = parse.urlencode(parms)

u = request.urlopen(url+'?'+querystring)
resp=u.read()
print(resp)

