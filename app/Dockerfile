FROM python:3.8.3-alpine

RUN adduser -D app
USER app

WORKDIR /home/app

ENV PATH="/home/webserver/.local/bin:${PATH}"
RUN /usr/local/bin/python -m pip install --upgrade pip

ENV PATH="/usr/local/bin/python:${PATH}"
RUN pip install flask==2.3.0 --user --no-cache-dir

COPY --chown=app:app webserver.py /home/app/

EXPOSE 5000

CMD [ "python", "/home/app/webserver.py" ]