import requests

url = 'https://detik.com'
try:
    requests.get(url)
    print('sukses')
except Exception as e:
    print('ada error', e)
print('program ended')