FROM continuumio/miniconda3
WORKDIR /app

# copy the environment file to the container
COPY ./environment.yml /app/environment.yml

# create conda environment
RUN conda env create -f environment.yml

# activate conda environment
SHELL ["conda", "run", "-n", "rl", "/bin/bash", "-c"]

ENV FLASK_APP=src/app.py

# expose the port
EXPOSE 5000

# run the flask application
CMD ["conda", "run", "-n", "rl", "flask", "run", "--host=0.0.0.0"]