import requests



name="sumit"
location=""
url="https://api.github.com/search/users?q=\""+name+"\"in:fullname+location:\""+location+"\"&per_page=100&page=1"
res=requests.get(url,auth=('shubham51297','9f9894c24f91f96376099437e75798eced357fd2'))

print(res.links.keys())
