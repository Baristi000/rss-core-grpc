FROM python:3.8

COPY elastic_search /app/elastic_search
COPY protobuf /app/protobuf
COPY search/faiss.py /app/search/faiss.py
COPY search/data /app/search/data
COPY service /app/service
COPY use /app/use
COPY r.txt /app/r.txt
COPY server.py /app/server.py
COPY setting.py /app/setting.py

WORKDIR /app

RUN rm -rf app/search/data/faiss.index
RUN pip install -r r.txt
RUN python protobuf/gen_python_code.py
RUN python use/gen_use_model.py

CMD ["python", "server.py"]