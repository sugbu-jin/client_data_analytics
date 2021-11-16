FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && rm -rf /var/lib/apt/lists

RUN mkdir /client_data_analytics

WORKDIR /client_data_analytics

ADD requirements.txt /client_data_analytics/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

ADD . /client_data_analytics/

CMD [ "python", "application.py" ]