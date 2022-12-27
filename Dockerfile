FROM python:3.10.9

ENV FLASK_APP=app

ENV FLAK_DEBUG=$FLAK_DEBUG

ENV JWT_SECRET_KEY='238455349656035893078255666465296948333'

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY . /opt

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT