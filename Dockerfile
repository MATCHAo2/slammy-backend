FROM python:3.10

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
RUN mkdir /usr/src/app/static
RUN mkdir /usr/src/app/images

RUN pip install --upgrade pip
COPY ./.env /usr/src/app/.env
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh
RUN pip install -r requirements.txt
RUN mkdir -p /var/run/gunicorn

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
