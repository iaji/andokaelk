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

RUN mkdir /usr/share/elasticsearch
RUN wget -P /usr/share/elasticsearch https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.2.0/elasticsearch-2.2.0.tar.gz
RUN tar zxvf /usr/share/elasticsearch/elasticsearch-2.2.0.tar.gz -C /usr/share/elasticsearch
RUN rm /usr/share/elasticsearch/elasticsearch-2.2.0.tar.gz
RUN /usr/share/elasticsearch/elasticsearch-2.2.0/bin/plugin install lmenezes/elasticsearch-kopf/v2.1.1

RUN mkdir /tmp/elasticsearch/
RUN groupadd -r elasticsearch && useradd -r -g elasticsearch elasticsearch

CMD chown -R elasticsearch /usr/share/elasticsearch/elasticsearch-2.2.0/config && chown -R elasticsearch /tmp && su -c /usr/share/elasticsearch/elasticsearch-2.2.0/bin/elasticsearch elasticsearch