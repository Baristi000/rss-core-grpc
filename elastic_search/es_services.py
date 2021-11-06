from setting import settings


def ImportData(data):
    response = settings.es.index(
        index=settings.index,
        id=data["link"],
        body=data
    )
    if response["result"] == "created":
        return True
    return False


def GetData(place: int = None):
    response = settings.es.search(
        index=settings.index,
        body={
            "query": {
                "match": {
                    "position": place
                },
            },
            "size": 1
        }
    )
    return(response["hits"]["hits"][0]["_source"])


def is_id_exist(id: str):
    try:
        settings.es.search(
            index=settings.index,
            body={
                "query": {
                    "match": {
                        "_id": id
                    },
                },
                "size": 1
            }
        )["hits"]["hits"][0]["_source"]
        return True
    except:
        return False


def ImportAfterCrawl(datas: list):
    for data in datas:
        if not ImportData(data):
            url = data["link"]
            print(f"\tCan not import data from {url} to Elasticsearch server")
