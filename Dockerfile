FROM python:3.8

COPY . /app

WORKDIR /app

RUN rm -rf app/search/data/faiss.index
RUN pip install -r r.txt
RUN python protobuf/gen_python_code.py
RUN python use/gen_use_model.py

CMD ["python", "server.py"]