FROM ubuntu:18.04

RUN apt update && apt install -y \
    build-essential python3-dev python3-pip \
    python3-setuptools python3-wheel python3-cffi \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

ADD . .

RUN python3 -m pip install -r requirements.txt

RUN apt-get install -y locales

EXPOSE 5000

RUN locale-gen en_US.UTF-8
ENV LANG=en_GB.UTF-8
ENV LC_CTYPE="en_US.UTF-8"
ENV LC_NUMERIC="en_GB.UTF-8"
ENV LC_TIME="en_GB.UTF-8"
ENV LC_COLLATE="en_GB.UTF-8"
ENV LC_MONETARY="en_GB.UTF-8"
ENV LC_MESSAGES="en_GB.UTF-8"
ENV LC_ALL=

RUN [ "python3", "add_users.py" ]

ENTRYPOINT [ "python3", "app.py" ]