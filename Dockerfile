FROM debian:bullseye

RUN apt update &&\
    apt install -y python3 python3-pip scapy
    
WORKDIR /app
COPY tcp_scanner.py .

CMD ["python3", "tcp_scanner.py"]  
