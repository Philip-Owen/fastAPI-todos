FROM python:3.8-slim
COPY . /app
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]