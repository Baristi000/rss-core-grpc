import tensorflow_hub as hub
import faiss
from elasticsearch import Elasticsearch
import multiprocessing


class Setting():
    def __init__(self) -> None:
        self.max_workers = multiprocessing.cpu_count()
        self.host = "0.0.0.0:9090"
        self.encode = hub.load("use/model/use_v4")
        self.FEATURE_SIZE = 512
        self.BATCH_SIZE = 32
        self.index_dir = "search/data/faiss.index"
        try:
            self.faiss_index = faiss.read_index(self.index_dir)
        except:
            self.faiss_index = faiss.IndexFlatL2(self.FEATURE_SIZE)
            print("No index file found")
        self.index = "news"
        self.es = Elasticsearch("http://elastic-tt.ddns.net:80")
        self.fake_news_base_url = "http://ai.ttst.asia:8001"


settings = Setting()
