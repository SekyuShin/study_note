Nas setup
Created at : 2025-10-11 00:40

# Install Docker
1. docker 설치 shell 파일 다운로드
```shell
curl -fsSL https://get.docker.com -o get-docker.sh
```
2. 권한 수정
```shell
sudo chmod +777 get-docker.sh
```
3. shell 실행
```shell
sh get-docker.sh
```
4. 우분투 계정 권한 변경
```shell
sudo usermod -aG docker skyle
sudo systemctl daemon-reload
sudo systemctl enable docker
sudo systemctl restart docker
sudo reboot
```
