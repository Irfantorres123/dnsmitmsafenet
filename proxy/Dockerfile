FROM python:3.7

WORKDIR /usr/src/proxy

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt &&\
    chmod +x ./entrypoint.sh
EXPOSE 80 443
COPY . .
ENTRYPOINT [ "./entrypoint.sh" ]