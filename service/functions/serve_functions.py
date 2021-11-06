import json

from search import faiss
from protobuf import serve_pb2, train_pb2
from elastic_search import es_services as es


def create_response(status, message, raw_datas):
    status_data = train_pb2.StatusCode(status=status, message=message)
    input_datas = []
    for data in raw_datas:
        item = train_pb2.Block(
            title=data["title"],
            description=data["description"],
            link=data["link"],
            blog_title=data["blogTitle"],
            blog_link=data["blogLink"],
            authors=data["authors"],
            time_published=data["timePublished"]
        )
        input_datas.append(item)
    input_data = train_pb2.InputData(block=input_datas)
    return serve_pb2.SearchResult(statuscode=status_data, data=input_data)


def search(query, result_numbers):
    indexs = faiss.search(query, result_numbers)
    data = []
    for index in indexs:
        data.append(es.GetData(index))
    return create_response(200, "succeed", data)
