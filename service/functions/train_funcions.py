from search import faiss
from elastic_search import es_services as es
from protobuf import train_pb2
from setting import settings

from service.functions.message_to_dict import convert_list
from fake_news_module.fake_news_services import feed_data


def create_response(status, message):
    return train_pb2.StatusCode(status=status, message=message)


def train(datas: list):
    data = convert_list(datas)
    fake_news_data_list = []
    for block in data:
        block = dict(block)
        if settings.faiss_index.ntotal == 0 or not es.is_id_exist(block["link"]):
            block.update({"position": int(settings.faiss_index.ntotal)})
            es.ImportData(block)
            title = block["title"]
            fake_news_data_list.append(title)
            faiss.build_index(title)
        else:
            url = block["link"]
            print(f"\tCan not import data from {url} to Elasticsearch server")
    feed_data(fake_news_data_list)
    return create_response(200, "succeed")
