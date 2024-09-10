FROM ubuntu:22.04
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y python3:3.12.4 && \
    pip install -r requirements.txt
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python", "racinglineinator.py" ]