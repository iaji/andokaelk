FROM ubuntu:14.04
MAINTAINER Lingxiao Xia <s1006595991@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget
RUN apt-get install -y default-jdk
RUN apt-get install -y supervisor

RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
RUN echo "export LC_ALL=en_US.utf8" >> ~/.bashrc
RUN echo "export LANG=en_US.utf8" >> ~/.bashrc
RUN echo "export LANGUAGE=en_US.utf8" >> ~/.bashrc

RUN mkdir /usr/share/kafka
RUN wget -P /usr/share/kafka http://apache.communilink.net/kafka/0.9.0.1/kafka_2.11-0.9.0.1.tgz
RUN tar zxvf /usr/share/kafka/kafka_2.11-0.9.0.1.tgz -C /usr/share/kafka/
RUN rm /usr/share/kafka/kafka_2.11-0.9.0.1.tgz
COPY log4j.properties /usr/share/kafka/kafka_2.11-0.9.0.1/config/log4j.properties
COPY test-log4j.properties /usr/share/kafka/kafka_2.11-0.9.0.1/config/test-log4j.properties
COPY connect-log4j.properties /usr/share/kafka/kafka_2.11-0.9.0.1/config/connect-log4j.properties

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
