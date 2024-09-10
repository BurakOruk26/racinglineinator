FROM ubuntu:24.04
WORKDIR /app
COPY ./requirements.txt /app
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt
WORKDIR /app/src
COPY ./racinglineinator.py /app/src
ENTRYPOINT [ "python3", "racinglineinator.py" ]