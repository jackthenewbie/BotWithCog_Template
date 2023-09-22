FROM python3
WORKDIR /usr/src/bot
COPY setup.py .
RUN pip install -e /usr/src
ENTRYPOINT  ["python3"]
CMD ["main.py"]
