from cloudscraper import CloudScraper as Session
from proxyscrape import generate_random_ip
import re

def run_nano_bot(link, proxy=None, headless=None):
    s=Session()
    s.proxies=dict(http=proxy, https=proxy)
    r1=s.get(link, headers={'Referer': 'https://thekisscartoon.com/'}, allow_redirects=False)
    loc = r1.headers.get('Location')
    if loc is None:
        raise Exception('Error in nano links. Location is None')
    print('Nano Links:', loc)
    


if __name__=='__main__':
    from all_links import random_nanolinks
    run_nano_bot(random_nanolinks, headless=False)


