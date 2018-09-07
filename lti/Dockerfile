# Dockerfile

# FROM directive instructing base image to build upon
FROM continuumio/miniconda3

RUN mkdir -p /usr/src/app
COPY . /usr/src/app

WORKDIR /usr/src/app

RUN conda env create -f environment.yml
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/surf-share/bin:$PATH

# Collect all statics resources (images, css, etc.)
#RUN python manage.py collectstatic --noinput

# Create and/or migrate simple database
RUN python manage.py migrate

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
