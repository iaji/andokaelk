FROM ubuntu:14.04
MAINTAINER Lingxiao Xia <s1006595991@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install -y default-jdk

RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
RUN echo "export LC_ALL=en_US.utf8" >> ~/.bashrc
RUN echo "export LANG=en_US.utf8" >> ~/.bashrc
RUN echo "export LANGUAGE=en_US.utf8" >> ~/.bashrc

RUN mkdir /usr/share/logstash
RUN wget -P /usr/share/logstash https://download.elastic.co/logstash/logstash/logstash-2.2.0.tar.gz
RUN tar zxvf /usr/share/logstash/logstash-2.2.0.tar.gz -C /usr/share/logstash
RUN rm /usr/share/logstash/logstash-2.2.0.tar.gz
RUN wget -P /usr/share/logstash/logstash-2.2.0 http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
RUN gunzip /usr/share/logstash/logstash-2.2.0/GeoLiteCity.dat.gz
RUN /usr/share/logstash/logstash-2.2.0/bin/plugin install logstash-filter-elasticsearch

RUN mkdir /tmp/logstash

CMD ["/usr/share/logstash/logstash-2.2.0/bin/logstash","-f","/tmp/logstash/config/logstash.conf"]
