## 1. Cài đặt OpenSSH Server trên Linux

Cài đặt OpenSSH Server
```sh
# Centos
yum install openssh openssh-server openssh-clients openssl-libs -y

# Ubuntu
sudo apt-get install openssh-server openssh-client
```
Chạy dịch vụ SSH Server, thiết lập chạy ngay khi khởi động
```sh
systemctl start sshd
systemctl enable sshd
```
_Mặc định SSH dùng cổng 22 nên bạn phải mở cổng này nếu có firewall_
```sh
firewall-cmd --add-port=22/tcp --permanent
firewall-cmd --reload
```
**Note:**
File cấu hình của OpenSSH Server tại /etc/ssh/sshd_config, bạn có thể mở và chỉnh sửa nó theo nhu cầu (có thể dùng Vim, Nano để soạn thảo). 

Sau khi sửa Config thì cần khởi động lại SSH Server. 
```sh
systemctl restart sshd
```
Kiểm tra trạng thái SSH Server
```sh
systemctl status sshd
```

## 2. Cài đặt OpenSSH Client
Kiểm tra: Mở terminal (trên Windows dùng cmd hoặc PowerShell) gõ lệnh:
```sh
ssh -V
```

Với Ubuntu Destop, SSH Client cũng có mặc định, nếu không thấy gõ lệnh để cài, cuối cùng là kiểm tra như hình

```sh
sudo apt-get install openssh-client
```
Sử dụng SSH Client cơ bản
```sh
ssh username@remoteserver
Ex: ssh testuser@192.168.1**.52**
```
- Sau khi nhập lệnh, do lần đầu kết nối SSH đến IP này, nên ssh có hỏi về ECDSA key fingerprint- gõ yes, rồi nhập password theo yêu cầu.
- Sau khi nhập password - kết nối thành công tới dòng lệnh của máy Windows (Remote Server)

## 3. Lệnh scp copy file và thư mục từ server về máy local và ngược lại
Cú pháp sử dụng scp
```sh 
TEMPLATE:
scp [OPTION] [user_src@]src_host:]src_file [user@]desk_host:]des_file
    Trong đó:
    [user_src@]src_host:]src_file là file, thư mục nguồn, ví dụ abcuser@192.168.1.55:/home/file1.txt là file /home/file1.txt tại máy abcuser@192.168.1.55, như dấu :, nếu là tại máy local thì không cần chỉ ra user, host tức bỏ đoạn abcuser@192.168.1.55:
    [user@]desk_host:]des_file đường dẫn file, thư mục đích muốn copy - ý nghĩa tương tự như trên
    [OPTIONS] các thiết lập cho thêm vào nếu muốn, như cho thêm tham số -r để đệ quy copy cả thư mục, các file, thư mục con theo đường dẫn.
```
Ví dụ sử dụng scp
```sh
# download - copy một file từ server về local
scp root@192.168.1.99:/home/data/1.txt /mycode/1.txt
# download - copy thư mục về máy local
scp -r root@192.168.1.99:/home/data /mycode/data01
# upload - copy file (thư mục) từ local lên server
scp /mycode/3.txt root@192.168.1.99:/home/data/3.txt
```

## 4. Tạo SSH Key và xác thực kết nối SSH bằng Public/Private key
Cơ chế xác thực bằng SSH Key
Ngoài cơ chế xác thức bằng cách nhập mật khẩu như trên còn có cơ chế sử dụng SSH Key để xác thực. Để tạo nên xác thực này cần có hai file, một file lưu Private Key và môt lưu Public key

-   Public Key khóa chung, là một file text - nó lại lưu ở phía Server SSH, nó dùng để khi Client gửi Private Key (file lưu ở Client) lên để xác thực thì kiểm tra phù hợp giữa Private Key và Public Key này. Nếu phù hợp thì cho kết nối.
- Private Key khóa riêng, là một file text bên trong nó chứa mã riêng để xác thực (xác thực là kiểm tra sự phù hợp của Private Key và Public Key). Máy khách kết nối với máy chủ phải chỉ ra file này khi kết nối SSH thay vì nhập mật khẩu. Hãy lưu file Private key cận thận, bất kỳ ai có file này có thể thực hiện kết nối đến máy chủ của bạn

Tạo SSH Key (Public/Private)
```sh 
ssh-keygen -t rsa
```
Kết quả lệnh trên bạn đã có:

- Private Key chứa trong file ```~/.ssh/id_rsa```, hãy lưu lại cẩn thận, nó được dùng để SSH client (máy local) kết nối đến Server. Mở file này ra, đoạn mã Private Key có dạng
- Public Key chứa trong file ```~/.ssh/id_rsa.pub```, hãy copy nội dung bên trong file - giữ cận thận, Nó được lưu (dùng) ở máy Server để xác thực khi có Private key gửi đến. Nếu mở file này ra, thì nội dung mã Public key nhìn thấy có dạng:
  
## 5. Sử dụng Rsync đồng bộ thư mục trên Linux
Rsync (remote sync) là công cụ đồng bộ file, thư mục của Linux. 
```sh
# TRÊN CENTOS/RED HAT
yum install rsync

# TRÊN UBUNTU
apt-get install rsync
```
Rsync cơ bản
```sh
rsync -a thư_mục_nguồn thư_mục_đích
# Ex:
# rsync -a dir1/ dir2
```
Tham số -a (Archive) cho biết sẽ đồng bộ tất cả các file, thư mục con trong dir1.
Nếu muốn rsync kiểm tra thông tin dir1, dir2 trước khi thi hành thì thêm thiết lập -n, nếu muốn quá trình đồng bộ hiện thị thông tin thêm -v
```sh 
rsync -anv dir1/ dir2
```
Rsync - Đồng bộ giữa 2 máy Linux
```sh 
rsync -anv root@IP:/home/dir1 /home/dir1_backup
```
## 6. Sử dụng GitHub để làm Remote Repo chứa code dự án
Đăng ký tài khoản GitHub, thiết lập truy cập GitHub qua SSH Key, tạo Repo và thiết lập liên kết với Local Repo của Git, thi hành các lệnh Git với GitHub
[https://xuanthulab.net/su-dung-github-de-lam-remote-repo-chua-code-du-an.html#sshgithub]