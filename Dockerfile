FROM python:3.11

COPY . /onnet_web_app
WORKDIR /onnet_web_app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "run:app", "-k", "gevent", "-b", "0.0.0.0", "--worker-connections", "1000", "-w", "1"]
