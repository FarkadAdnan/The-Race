from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import threading, webbrowser, urllib.request
ROOT = Path(__file__).resolve().parent
PORT = 5510
URL = f'http://127.0.0.1:{PORT}/'
if __name__ == '__main__':
    try:
        server = ThreadingHTTPServer(('127.0.0.1',PORT),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
    except OSError:
        try:
            with urllib.request.urlopen(URL, timeout=3) as response:
                if b'eng.dr.farkadadnan' not in response.read(): raise RuntimeError('Port is used by another app')
            webbrowser.open(URL)
        except Exception as error:
            print('Unable to start:', error)
            input('Press Enter to close...')
    else:
        print('Racing:',URL)
        threading.Timer(1,lambda:webbrowser.open(URL)).start()
        server.serve_forever()
