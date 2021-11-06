from .utils import *
from setting import settings

def feed_data(data:list):
    data = {"data":data}
    url = settings.fake_news_base_url + "/FakenewsDetection/train"
    try:
        res = perform_post(url, data)
        if res["status"] == 200:
            print("\tFeed data to fake news succeeded")
        else:
            print("\tFeed data to fake news falsed")
    except:
        print("\tServer error")

def predict(sentence: str):
    data = {"message": sentence}
    url = settings.fake_news_base_url + "/FakenewsDetection/predict"
    try:
        res = perform_post(url, data)
        if res["status"] == 200:
            return res["data"]
        else:
            print("\tFeed data to fake news falsed")
    except:
        print("\tServer error")