FROM ubuntu:20.04

RUN apt-get update --yes && apt-get install --yes;
RUN apt install wget --yes;
RUN apt install curl gnupg2 ca-certificates lsb-release --yes;
RUN echo "deb http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | tee /etc/apt/sources.list.d/nginx.list;
RUN curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add -;
RUN apt install nginx --yes;
RUN apt install git --yes;
RUN apt update --yes;

ENV HOME /home/apka

WORKDIR ${HOME}

ENV DEBIAN_FRONTEND=noninteractive 

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
   && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list;

RUN apt-get update && apt-get -y install google-chrome-stable

RUN apt install python3-pip --yes

RUN pip3 install selenium

COPY . ${HOME}/fastmail-daemon/fastmail-app/

WORKDIR ${HOME}/fastmail-daemon/fastmail-app/

RUN chmod -R 777 ${HOME}/fastmail-daemon

COPY default /etc/nginx/sites-enabled/

EXPOSE 80

CMD ./wrapper_script.sh

