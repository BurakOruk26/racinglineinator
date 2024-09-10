FROM ubuntu:24.04
WORKDIR /app
COPY ./environment.yml /app

# install miniconda
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda-installer.sh && \
    bash /opt/miniconda-installer.sh -b -p /opt/miniconda && \
    rm /opt/miniconda-installer.sh

# update PATH
ENV PATH="/opt/miniconda/bin:${PATH}"

# create conda environment
RUN conda env create --name rl --file environment.yml

# activate conda environment
RUN echo "conda activate rl" >> ~/.bashrc

WORKDIR /app/src
COPY ./racinglineinator.py /app/src
ENTRYPOINT [ "python3", "racinglineinator.py" ]