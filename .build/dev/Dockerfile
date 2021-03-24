FROM python:3

# https://github.com/aws/amazon-sagemaker-examples/issues/319
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD tail -f /dev/null