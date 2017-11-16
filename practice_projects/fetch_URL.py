#!python3
# fetch_URL.py - Fetch all the link started at URL.

import sys
import os
import requests
import bs4

achieve = set()


def back_to_parent(url):
    while url[-1] != '/':
        url = url[:-1]
    return url


def find_all_url(origin_url):
    res = requests.get(origin_url)
    if res.status_code == 404:
        print("%s is 404..." % origin_url)
        return
    res.raise_for_status()

    prev = back_to_parent(origin_url)
    if origin_url is not sys.argv[1]:
        achieve.add(origin_url.split('/')[-1])

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        url = link.get('href')
        if not url.startswith('http:') and not url.startswith('https:'):
            if url is '#':
                continue
            elif url.startswith('../'):
                url = back_to_parent(prev[:-1]) + url[3:]
            else:
                url = prev + url
        filename = url.split('/')[-1]
        if filename in achieve:
            continue
        if not url.endswith('.html'):
            res = requests.get(url)
            if res.status_code == 404:
                continue
            res.raise_for_status()
            print('downloading %s...' % filename)
            page = open('psi/' + filename, 'wb')
            for chunk in res.iter_content(100000):
                page.write(chunk)
            page.close()
            achieve.add(filename)
        else:
            print('opening %s...' % url)
            find_all_url(url)


if len(sys.argv) != 2:
    print('Usage: python fetch_URL.py [URL]')
    sys.exit()

os.makedirs('psi', exist_ok=True)
find_all_url(sys.argv[1])
