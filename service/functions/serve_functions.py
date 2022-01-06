import json

from search import faiss
from protobuf import serve_pb2, train_pb2
from elastic_search import es_services as es
from fake_news_module.fake_news_services import predict


def create_response(status, message, raw_datas):
    predict_result = predict(message)
    
    status_data = train_pb2.StatusCode(status=status, message="succeed")
    
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

    search_body = serve_pb2.SearchBody(
        datas = input_data,
        percent=predict_result["percent"], 
        status=predict_result["status"]
    )
    return serve_pb2.SearchResult(statuscode=status_data, body=search_body)


def search(query, result_numbers):
    indexs = faiss.search(query, result_numbers)
    data = []
    for index in indexs:
        data.append(es.GetData(index))
    res = create_response(200, query, data)
    return res
