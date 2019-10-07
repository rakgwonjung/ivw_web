FROM ubuntu:18.04

MAINTAINER ivw

# lib install
RUN apt-get update
RUN apt-get install -y nginx gcc g++ zlib1g-dev openssl libssl-dev \
sqlite3 libsqlite3-dev wget tree make sudo vim git curl \
libmysqlclient-dev python-mysqldb mysql-client systemd

# ENV
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# nginx port change(8080)
RUN sed -i 's/80/8081/' /etc/nginx/sites-available/default

# nginx link
RUN ["ln", "-sf", "/etc/nginx/sites-available/default", "/etc/nginx/sites-enabled/default"]

# NGINX
#ENTRYPOINT ["/usr/sbin/nginx"]
#WORKDIR /etc/nginx

#CMD ["nginx", "-g", "deamon off;"]

# Python3.6 install
WORKDIR /tmp/python-install

RUN wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6rc1.tgz

#CMD ["tar", "-zxvf", "Python3.6.6rcl.tgz"]
RUN tar -zxvf Python-3.6.6rc1.tgz
WORKDIR /tmp/python-install/Python-3.6.6rc1
RUN ./configure --enable-optimizations
RUN make altinstall

# Symlinks
WORKDIR /usr/local/bin
RUN ln -s python3.6 python3
RUN ln -s pip3.6 pip3
RUN pip3 install --upgrade pip

# rm Python3.6 install file
RUN rm -rf /tmp/python-install

WORKDIR /ivw

#RUN pip3 install -r /ivw_web/requirements.txt

RUN pip3 install django djangorestframework
RUN pip3 install serializers
RUN pip3 install gunicorn
RUN pip3 install markdown
RUN pip3 install django-suit
RUN pip3 install mysql-python
RUN pip3 install mysqlclient
#RUN pip3 install filter


# nginx start
#WORKDIR /etc/nginx
#CMD ["nginx", "-g", "daemon off;"]

#COPY nginx-app.conf /etc/nginx/sites-available/default
#COPY supervisor-app-staging.conf /etc/supervisor/conf.d/
EXPOSE 8001
EXPOSE 8081
EXPOSE 433
