# Use https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
# hello world demo
FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./main.py /main.py
RUN  chmod +x /main.py
WORKDIR /
USER root
ENTRYPOINT [ "/usr/local/bin/python3","/main.py" ]
