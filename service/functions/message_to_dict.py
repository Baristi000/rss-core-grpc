from google.protobuf.json_format import MessageToDict


def convert_list(data: list):
    result = []
    for i in range(len(data)):
        result.append(MessageToDict(data[i]))
    return result


def convert_obj(data):
    return MessageToDict(data)
