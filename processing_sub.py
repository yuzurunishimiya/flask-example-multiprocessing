from connection import session

import requests
import json


def doMultiProcessing(args):
    print("[+] Do Multiprocessing ...")
    r = requests.get("http://localhost:5000/get-context")
    print(r.status_code)
    if r.status_code == 200:
        session.set(args, json.dumps(r.text), ex=60)
    print("[+] Selesai ...!")
    return
