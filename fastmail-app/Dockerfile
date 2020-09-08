FROM ubuntu:20.04

RUN apt-get update --yes && apt-get install --yes;
RUN apt install wget --yes;
RUN apt install curl gnupg2 ca-certificates lsb-release --yes;
RUN echo "deb http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | tee /etc/apt/sources.list.d/nginx.list;
RUN apt install git --yes;
RUN curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add -;
RUN apt update --yes;
RUN apt install nginx --yes;


ENV HOME /root

WORKDIR ${HOME}

#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 

#RUN apt install ./google-chrome-stable_current_amd64.deb --yes

#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -;

#RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list;

#RUN apt-get update && apt-get -f install google-chrome-stable --yes;

# Install Chrome
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

ENV DEBIAN_FRONTEND=noninteractive 
# Set the Chrome repo.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Install Chrome.
RUN apt-get update && apt-get -y install google-chrome-stable



RUN git clone https://github.com/darkfurby/fastmail-daemon.git 

WORKDIR ${HOME}/fastmail-daemon/bin/

RUN source activate

