#!python
# downloadHuaban.py - download picture from http://huaban.com/favorite/beauty/

import requests, os, re

url = "http://huaban.com/favorite/beauty/"
os.makedirs('huaban', exist_ok=True)
print('Fetching waterfall...')
res = requests.get(url)
res.raise_for_status()

pin_id_match = re.compile('"pin_id":(\d+)')
pin_id_list = pin_id_match.findall(res.text)

for pin_id in pin_id_list:
    url = 'http://huaban.com/pins/' + pin_id
    res = requests.get(url)
    res.raise_for_status()

    image_key_match = re.compile('"pin":{"pin_id":' + pin_id + ',\s.+?"key":"(.+?)",')
    image_key = image_key_match.findall(res.text)
    url = 'http://img.hb.aicdn.com/' + image_key[0]
    res = requests.get(url)
    res.raise_for_status()

    print('downloading %s.jpg...' % pin_id)
    image = open('huaban/' + pin_id + '.jpg', 'wb')
    for chunk in res.iter_content(100000):
        image.write(chunk)
    image.close()