from use.encoder import encode
import faiss

from setting import settings


def _standardized_input(sentence: str):
    return sentence.replace("\n", "").lower()


def save_index(index):
    faiss.write_index(index, settings.index_dir)


def build_index(data: str):
    clean_data = _standardized_input(data)
    settings.faiss_index.add(encode(clean_data))
    save_index(settings.faiss_index)


def search(query: str, result_numbers: int = 1):
    clean_data = _standardized_input(query)
    vector = encode(clean_data)
    top_n_results = settings.faiss_index.search(vector, result_numbers)
    return [id_ for id_ in top_n_results[1].tolist()[0]]
