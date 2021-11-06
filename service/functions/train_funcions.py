from search import faiss
from elastic_search import es_services as es
from protobuf import train_pb2
from setting import settings

from service.functions.message_to_dict import convert_list


def create_response(status, message):
    return train_pb2.StatusCode(status=status, message=message)


def train(datas: list):
    data = convert_list(datas)
    for block in data:
        block = dict(block)
        if settings.faiss_index.ntotal == 0 or not es.is_id_exist(block["link"]):
            block.update({"position": int(settings.faiss_index.ntotal)})
            es.ImportData(block)
            title = block["title"]
            faiss.build_index(title)
        else:
            url = block["link"]
            print(f"\tCan not import data from {url} to Elasticsearch server")
    return create_response(200, "succeed")
