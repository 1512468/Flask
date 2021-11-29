FROM ubuntu:latest

# Cập nhật các gói và cài vào đó HTTPD, HTOP, VIM
RUN apt update -y
RUN apt install httpd httpd-tools -y
RUN apt install epel-release -y \
    && apt update -y \
    && apt install htop -y \
    && apt install vim -y

#Thiết lập thư mục hiện tại
WORKDIR /var/www/html
# Copy tất cả các file trong thư mục hiện tại (.)  vào WORKDIR
ADD . /var/www/html

#Thiết lập khi tạo container từ image sẽ mở cổng 80
# ở mạng mà container nối vào
EXPOSE 80

# Khi chạy container tự động chạy ngay httpd
ENTRYPOINT ["/usr/sbin/httpd"]

#chạy terminate
CMD ["-D", "FOREGROUND"]