# Table of Contents
- [Cài Docker trên Ubuntu](#step1)
- [Docker <commit, load>](#step2)
- [Share data](#step3)
- [Netword](#step4)
## 1. Cài Docker trên Ubuntu <a name="step1"></a>
Chạy các lệnh để cài đặt:
```sh
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
```
Sau khi cài đặt, bạn có thể cho user hiện tại thuộc group docker, để khi gõ lệnh không cần xin quyền sudo
```sh 
sudo usermod -aG docker $USER
```
Ngoài ra khi sử dụng đến thành phần docker-compose thì bạn cài thêm
``` sh 
sudo apt install docker-compose
```
 **Tóm tắt các lệnh làm quen**
``` sh 
#kiểm tra phiên bản
docker --version
# Hoặc lệnh thông tin chi tiết hơn:
docker --info
#liệt kê các image
docker images -a

#xóa một image (phải không container nào đang dùng)
docker images rm imageid

#tải về một image (imagename) từ hub.docker.com
docker pull imagename

#liệt kê các container
docker container ls -a
docker container ls --all

#xóa container
docker container rm containerid

#tạo mới một container
docker run -it imageid 

#thoát termial vẫn giữ container đang chạy
CTRL +P, CTRL + Q

#Vào termial container đang chạy
docker container attach containerid

#Chạy container đang dừng
docker container start -i containerid

#Chạy một lệnh trên container đang chạy
docker exec -it containerid command
```
Các container bạn đã tạo, liệt kê ra hãy chú ý mấy thứ

    - CONTAINER ID một con số (mã hash) gán cho container, bạn dùng mã này để quản lý container này, như xóa bỏ, khởi động, dừng lại ...
    - IMAGE cho biết container sinh ra từ image nào.
    - COMMAND cho biết lệnh, ứng dụng chạy khi container chạy (/bin/bash là terminate)
    - STATUS cho biết trạng thái, (exit - đang dừng)

## 2. Docker commit, load 