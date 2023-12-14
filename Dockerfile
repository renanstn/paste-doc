FROM python:3

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src /app
RUN chmod +x run.sh
CMD [ "sh", "run.sh" ]
