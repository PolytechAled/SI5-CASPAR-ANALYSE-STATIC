import requests
data = {'foo':'bar'}
proxies = {
        'https': 'https://127.0.0.1:8080',
}
url = 'https://httpbin.org/post'
r = requests.post(url, data=data, proxies=proxies, verify=False)
print(r.content)
