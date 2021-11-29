# 1. Sử dụng Dockerfile
Dockerfile là một file text, trong đó chứa các dòng chỉ thị để Docker đọc và chạy theo chỉ thị đó để cuối cùng bạn có một image mới theo nhu cầu. Khi đang có một Dockerfile giả sử có tên là Dockerfile để ra lệnh cho Docker chạy nó bạn có thể gõ:
```sh 
# Dấu . ở cuối lệnh docker build ở trên, có nghĩa tìm file có tên Dockerfile ở thư mục hiện tại.
# -t nameimage:version là đặt tên và tag được gán cho image mới tạo ra.
docker build -t nameimage:version --force-rm -f Dockerfile .
```

# 2. Các chỉ thị Dockerfile
Phần này tìm hiểu các chỉ thị cơ bản:
```sh
- FROM : mọi Docker file đều có chỉ thị này, chỉ định image cơ sở
- COPY ADD : sao chép dữ liệu
- ENV : thiết lập biến môi trường
- RUN : chạy các lệnh.
- VOLUME : gắn ổ đĩa, thư mục
- USER : user
- WORKDIR : thư mục làm việc
- EXPOSE : thiết lập cổng
```

[link] (https://xuanthulab.net/su-dung-dockerfile-de-tu-dong-tao-cac-image-trong-docker.html)

Trong Dockerfile có bao nhiêu chỉ thị RUN thì có bấy nhiêu layer được tạo ra, tương tự là ADD, ENTRYPOINT, CMD ... Nên muốn ít layer thì cần viết sao cho ít chỉ thị nhất. Ở ví dụ trên thay vì có 3 chỉ thị RUN có thể viết thành 1 như vậy 3 layer chỉ còn 1. WORKDIR chưa dùng đến bỏ đi (giảm 1 layer). Tham số ENTRYPOINT có thể viết gộp cùng lệnh này, thay vì phải dùng thêm CMD (giảm 1 layer).