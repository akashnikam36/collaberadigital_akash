FROM python:3.9-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV AUTH0_DOMAIN=dev-8rxv0ifihijphc75.us.auth0.com
ENV AUTH0_CLIENT_ID=Vcw87egL0WEIyjGcEO0p0PI9zYSyNfMI
ENV AUTH0_CLIENT_SECRET=l7Li0vnP8LtEio_uKsATma8SYqIr2kgRfX1UscbtoEkhg7Q9BnXLC1WfgfJSxJQL
ENV AUTH0_CONNECTION=Username-Password-Authentication
ENV AUTH0_AUDIENCE=https://dev-8rxv0ifihijphc75.us.auth0.com/api/v2/

CMD ["python", "app.py"]