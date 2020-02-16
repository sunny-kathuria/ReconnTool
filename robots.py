import urllib.request
import io

def get_robots(url):
    if url.endswith('/'):
        path=url
    else:
        path=url +'/'
    req=urllib.request.urlopen(path+"robots.txt",data=None)
    data=io.TextIOWrapper(req,encoding='utf-8')
    print("Robots.txt Done!")
    return data.read()

#print(get_robots('https://wwww.facebook.com'))