FROM ubuntu:14.04
MAINTAINER Lingxiao Xia <s1006595991@gmail.com>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list
RUN apt-get update 
RUN apt-get upgrade -y
RUN apt-get install -y software-properties-common
RUN apt-get install -y python-software-properties
COPY oauth2_proxy /usr/share/oauth2_proxy

RUN mkdir /tmp/oauth2

RUN locale-gen "en_US.UTF-8"
RUN dpkg-reconfigure locales
RUN echo "export LC_ALL=en_US.utf8" >> ~/.bashrc
RUN echo "export LANG=en_US.utf8" >> ~/.bashrc
RUN echo "export LANGUAGE=en_US.utf8" >> ~/.bashrc

ENTRYPOINT ["/usr/share/oauth2_proxy/oauth2_proxy.py"]
CMD ["/usr/share/oauth2_proxy/oauth2_proxy", "/tmp/oauth2/config/oauth2_proxy.cfg", "/tmp/oauth2/output/oauth2_proxy.log"]