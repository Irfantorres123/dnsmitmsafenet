FROM python:3.9

WORKDIR /usr/src/proxy

COPY requirements.txt ./
COPY entrypoint.sh ./
RUN pip3 install -r requirements.txt &&\
    chmod +x ./entrypoint.sh
EXPOSE 80 443
COPY . .
ENTRYPOINT [ "./entrypoint.sh" ]