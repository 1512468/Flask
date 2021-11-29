File docker-compose.yml gần giống ý nghĩa với file Dockerfile đã tìm hiểu trong Sử dụng Dockerfile, là một file text, viết với định dạng YAML (Ain’t Markup Language, đọc nhanh định dạng Định dạng YML) là cấu hình để tử đó lệnh docker compose sinh ra và quản lý các service (container), các network, các ổ đĩa ... cho một ứng dụng hoàn chỉnh.

**Lệnh docker-compose**

- Về nội dung bên trong file docker-compose.yml sẽ tìm hiểu phía sau, giờ giả sử đang có file này, từ thư mục chứa file này gõ lệnh docker-compose với tham số phù hợp để thi hành những tác vụ như:

- Tạo và chạy các thành phần định nghĩa trong docker-compose.yml (các dịch vụ, image, container, mạng, đĩa ...).
    ```docker-compose up```
- Dừng và xóa: image, container, mạng, đĩa tạo ra bởi docker-compose up
    ```docker-compose down```
- Theo dõi Logs từ các dịch vụ
    ```docker-compose logs [SERVICES]```
Ngoài ra còn có các lệnh nhỏ khác như ```exec ps restart``` ... sẽ tìm hiều dần khi cần dùng đến.

#### Biên tập docker-compose.yml
``` sh
# VIẾT THEO CÚ PHÁP YAML, CHÚ Ý CHÍNH XÁC KHOẢNG TRẮNG ĐẦU CÁC DÒNG

version: "3"                      # chọn viết theo bản 3 docs.docker.com/compose/compose-file/

services:                         # CÁC DỊCH VỤ (CONTAINER) NĂM TRONG services
  pro-memcached:                  # (((1))) BẮT ĐẦU TẠO DỊCH VỤ THỨ NHẤT
    image: "memcached:latest"     # Image tạo ra dịch vụ
    container_name: c-memcached01 # Tên container khi chạy
    restart: always
    hostname: memcached
    networks:
      - my-network                # nối vào mạng my-network (tạo mạng này ở dưới)
    command:
      - "--conn-limit=2048"       # Giới hạn kết nối là 2048
      - "--memory-limit=2048"     # Giới hạn cho phép dùng tới 4096 MB bộ nhớ làm cache
  xtlab-apache:                   # (((2))) TẠO DỊCH VỤ HTTPD
    image: "httpd:version2"       # sử dụng image custome lại ở trên để tạo container
    container_name: c-httpd01     # tên khi chạy container HTTPD
    restart: always
    hostname: httpd01
    networks:
      - my-network
    ports:
      - "8080:80"                 # Mở cổng 8080 public, ánh xạ vào 80
      - "443:443"

    volumes:                      # Ánh xạ thự mục vào container
      - dir-site:/home/sites/     # Bind ổ đĩa - dir-site
  xtlab-mysql:                      # (((3))) TẠO DỊCH VỤ MYSQL
    image: "mysql:latest"
    container_name: mysql-product
    restart: always
    hostname: mysql01
    networks:
      - my-network
    environment:
      MYSQL_ROOT_PASSWORD: abc123   #Thiết lập password
    volumes:
      - /mycode/db:/var/lib/mysql  # thư mục lưu DB
      - /mycode/db/my.cnf:/etc/mysql/my.cnf  # ánh xạ file cấu hình
  xtlab-php:                         # (((4))) TẠO DỊCH VỤ PHP
    image: "php:version2"
    container_name: php-product      # tên container
    hostname: php01
    restart: always
    networks:
      - my-network
    volumes:
      - dir-site:/home/sites/        # Bind ổ đĩa - dir-site

networks:                             # TẠO NETWORK
  my-network:
    driver: bridge
volumes:                              # TẠO Ổ ĐĨA
  dir-site:                           # ổ đĩa này lưu dữ liệu ở /mycode/
    driver_opts:
      device: /mycode/                # Hãy đảm bảo có thư mục /mycode/default
      o: bind
```