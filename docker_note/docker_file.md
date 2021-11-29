# Sử dụng Dockerfile
Dockerfile là một file text, trong đó chứa các dòng chỉ thị để Docker đọc và chạy theo chỉ thị đó để cuối cùng bạn có một image mới theo nhu cầu. Khi đang có một Dockerfile giả sử có tên là Dockerfile để ra lệnh cho Docker chạy nó bạn có thể gõ:
```sh 
# Dấu . ở cuối lệnh docker build ở trên, có nghĩa tìm file có tên Dockerfile ở thư mục hiện tại.
# -t nameimage:version là đặt tên và tag được gán cho image mới tạo ra.
docker build -t nameimage:version --force-rm -f Dockerfile .
```