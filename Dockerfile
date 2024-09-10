FROM ubuntu:22.04
WORKDIR /app
COPY ./requirements.txt /app
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y python3:3.12.4 && \
    pip install -r requirements.txt
WORKDIR /app/src
COPY ./racinglineinator.py /app/src
ENTRYPOINT [ "python", "racinglineinator.py" ]