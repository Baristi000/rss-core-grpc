import tensorflow_hub as hub
import faiss
from elasticsearch import Elasticsearch


class Setting():
    def __init__(self) -> None:
        self.max_workers = 10
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
        self.index = "covid1"
        self.es = Elasticsearch("http://tstsv.ddns.net:80")


settings = Setting()
