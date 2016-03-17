FROM ubuntu:14.04
MAINTAINER Lingxiao Xia <s1006595991@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common
RUN apt-get install -y python-software-properties
RUN apt-get install -y wget

RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
RUN echo "export LC_ALL=en_US.utf8" >> ~/.bashrc
RUN echo "export LANG=en_US.utf8" >> ~/.bashrc
RUN echo "export LANGUAGE=en_US.utf8" >> ~/.bashrc

RUN mkdir /usr/share/kibana
RUN wget -P /usr/share/kibana "https://download.elastic.co/kibana/kibana/kibana-4.4.1-linux-x64.tar.gz"
RUN tar zxvf /usr/share/kibana/kibana-4.4.1-linux-x64.tar.gz -C /usr/share/kibana
RUN rm /usr/share/kibana/kibana-4.4.1-linux-x64.tar.gz

RUN mkdir /tmp/kibana/

ENTRYPOINT ["/usr/share/kibana/kibana-4.4.1-linux-x64/bin/kibana"]
CMD [ "-c","/tmp/kibana/config/kibana.yaml" ]
