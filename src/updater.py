import requests


url = 'https://github.com/RilexBTW/youtube/archive/refs/heads/master.zip'

def fetch():
    r = requests.get(url, allow_redirects=True)
    print(r.status_code)
    print(r.encoding)
    print(r.headers['content-type'])
    open('youtube-master.zip', 'wb').write(r.content)


fetch()
