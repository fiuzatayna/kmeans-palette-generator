FROM python:3.8-slim

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD streamlit run app.py --server.port 8000
