FROM python:3.10

WORKDIR /app2
COPY requirements.txt /app2/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app2/requirements.txt

COPY . /app2

CMD bash -c "while true; do sleep 1; done"