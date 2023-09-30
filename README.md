# Pratice 1:
為了讓測試專案可以在任何地方一鍵執行，只需要有容器 (I.e. Docker, K8S)，不用額外安裝環境就可執行。需要把測試專案，從建設環境到執行測試寫成 DockerFile，用於包裝成 Docker Image。該 DockerFile 應包含：

1. 安裝 Python
2. 安裝 Chrome Driver
3. 執行專案，產出報告，可以的話也發到 Discord 通知