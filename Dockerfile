## Dockerfile for backend of krisenheldinnen, #WeVsVirus Hackathon 2020
##
## created: 2020-03-21
## updated: 2020-03-22
##
## authors: jsommer

FROM makinacorpus/geodjango:bionic-3.7

LABEL maintainer="Johannes Sommer <js@sommergis.de>"
RUN apt-get update -y && apt-get install -y ca-certificates \
    nginx && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*


COPY requirements.txt /

## Install packages to Python3
RUN pip3 install -r requirements.txt

# nginx config
COPY config/nginx.conf /etc/nginx/sites-enabled/default

# uwsgi config
COPY config/uwsgi.ini /etc/uwsgi/krisenheldinnen.ini 

# deploy app
COPY app /var/www/app

# permissions
RUN chown -R www-data:www-data /var/www/app

# work directory for app
WORKDIR /var/www/app

CMD service nginx start && uwsgi -c /etc/uwsgi/krisenheldinnen.ini