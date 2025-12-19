FROM python:3.12-alpine

# чтобы находился .html шаблон
WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "app1.py" ]
