FROM python:3.6.8-stretch

ENV PYTHONUNBUFFERED=1

#RUN echo -e \
#    "http://nl.alpinelinux.org/alpine/v3.5/main\nhttp://nl.alpinelinux.org/alpine/v3.5/community" > \
#    /etc/apk/repositories

RUN apt-get update

RUN apt-get install -y bash postgresql-client gcc libpq-dev musl-dev

RUN rm -rf /choco_reddit
WORKDIR /choco_reddit
COPY . /choco_reddit
RUN pip install --upgrade pip
RUN pip install -U -r requirements.txt

RUN chmod +x entrypoint.sh
