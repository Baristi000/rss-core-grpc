import requests
import json


def perform_post(url: str, data: dict):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    req_body = json.dumps(data)
    resp = requests.post(url, headers=headers, data=req_body)
    print(json.dumps(data, indent=2))
    return resp.json()

def perform_get(url:str):
    return requests.get(url).json()
