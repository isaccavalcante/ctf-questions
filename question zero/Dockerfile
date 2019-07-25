FROM ubuntu:18.04

RUN apt update && apt install -y \
    build-essential python3-dev python3-pip \
    python3-setuptools python3-wheel python3-cffi \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

ADD . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN [ "python3", "add_users.py" ]

ENTRYPOINT [ "python3", "app.py" ]