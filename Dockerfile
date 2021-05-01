FROM python:3.6
LABEL maintainer "Nicola Bernini <nicola.bernini@gmail.com>"
RUN pip install pyyaml web3 
WORKDIR /root
EXPOSE 8545
