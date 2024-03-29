from all_links import *
# from adrinolinks import run_adrino_bot
from nanolinks import run_nano_bot
# from telegramlinks import run_telegram_bot
# from teraboxlinks import run_terabox_bot
# from link2cash import run_link2cash_bot
# from zagl import run_zagl_bot
from random import randint
import urllib3, threading
Thread=threading.Thread

d={'e':''}

def excepthook(l):
    d['e']+=str(l.exc_value) + '\n\n'

threading.excepthook=excepthook

def main(proxy=None, **kw):
    t=[]
    # t.append(Thread(target=lambda: run_adrino_bot(random_adrino, proxy, **kw)))
    t.append(Thread(target=lambda: run_nano_bot(random_nanolinks, proxy, **kw)))
    # t.append(Thread(target=lambda: run_telegram_bot(random_telegramlinks, proxy, **kw)))
    # t.append(Thread(target=lambda: run_terabox_bot(random_teraboxlinks, proxy, **kw)))
    # t.append(Thread(target=lambda: run_link2cash_bot(random_link2cash, proxy, **kw)))
    # t.append(Thread(target=lambda: run_zagl_bot(random_zagl, proxy, **kw)))

    for v in t:
        v.start()
    for v in t:
        v.join()
        
    if d['e']!='':
        raise Exception(d['e'])
    
    # Slow earning speed
    from time import sleep
    sleep(60)



if __name__ == '__main__':
    main()
