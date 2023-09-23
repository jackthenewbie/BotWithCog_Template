FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
COPY . /usr/src/
WORKDIR /usr/src/bot
RUN apt-get update -y && \
    apt-get install -y `cat /usr/src/dependencies`
RUN pip3 install -r requirements.txt
ENTRYPOINT  ["python3"]
CMD ["main.py"]
