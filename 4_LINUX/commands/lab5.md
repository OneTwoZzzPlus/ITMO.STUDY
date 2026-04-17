# Часть 1. Получение информацию о времени загрузки

1. Общее время загрузки системы

```systemd-analyze time```

2. Список сервисов по времени загрузки

```systemd-analyze blame | head -n 20```

3. Цепочка зависимостей для sshd

```systemd-analyze critical-chain sshd.service```

4. Создание графического отчета в формате SVG

```systemd-analyze plot > boot_report.svg```

```scp ivan@otz.duckdns.org:~/boot_report.svg ./```

# Часть 2. Управление юнитами

1. Список всех запущенных юнитов сервисов

```systemctl list-units --type=service --state=running | head -n 20```

2. Перечень сервисов с настроенной автозагрузкой

```systemctl list-unit-files --type=service --state=enabled | head -n 20```

3. Определение зависимостей для sshd, nginx и postgresql

```
systemctl list-dependencies sshd.service
systemctl list-dependencies nginx.service
systemctl list-dependencies postgresql.service
```

# Часть 3. Создание пробного сервиса

```sudo useradd -r -s /usr/sbin/nologin mymsguser```

`/etc/systemd/system/mymsg.service`

```Ini, TOML
[Unit]
Description=mymsg service
After=network.target
Requires=network.target

[Service]
Type=oneshot
User=mymsguser
ExecStart=/usr/bin/logger "mymsg: $(date)"
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

```bash
systemd-analyze verify /etc/systemd/system/mymsg.service
sudo systemctl daemon-reload
sudo systemctl enable mymsg.service
sudo systemctl start mymsg.service
systemctl status mymsg.service
```

# Часть 4. Работа с системным журналом

1. Просмотр сообщений системного журнала

```sudo journalctl --no-pager | head -n 20```

2. Просмотр сообщений системного журнала, касающихся сервиса mymsg 

```sudo journalctl -u mtmsg```

3. Выведите на экран все сообщения об ошибках в журнале.

```sudo journalctl -p err```

4. Определение размера журнала.

```sudo journalctl --disk-usage```

# Часть 5

## Кастомный юнит для nginx

```bash
sudo cp /lib/systemd/system/nginx.service /etc/systemd/system/nginx-custom.service
sudo nano /etc/systemd/system/nginx-custom.service
sudo systemctl disable nginx.service
sudo systemctl stop nginx.service
systemd-analyze verify /etc/systemd/system/nginx-custom.service
sudo systemctl daemon-reload
sudo systemctl enable nginx-custom
sudo systemctl start nginx-custom
```

## Ограничение памяти для nginx через slice

```bash
sudo nano /etc/systemd/system/nginx.slice
sudo nano /etc/systemd/system/nginx-custom.service
sudo systemctl daemon-reload
sudo systemctl restart nginx-custom
systemctl show nginx-custom -p Slice
systemctl show nginx.slice -p MemoryMax
```

## Юнит для бэкенда (три процесса node‑бэкенда)

```bash
sudo useradd -r -s /usr/sbin/nologin speedtestuser
sudo nano /etc/systemd/system/speedtest@.service
sudo systemctl daemon-reload
sudo systemctl restart speedtest@8888 speedtest@8889 speedtest@8890
sudo systemctl status 'speedtest@*'
```

```bash
sudo nano /etc/systemd/system/librespeed.target
sudo systemctl enable librespeed.target
```

## Порядок запуска сервисов

```bash
systemctl list-units --type=service | grep -i postgres
sudo nano /etc/systemd/system/nginx-custom.service
sudo systemctl daemon-reload
systemctl list-dependencies nginx-custom
```

## Таймер для резервного копирования PostgreSQL

```bash
sudo cp ~/db/backuper.sh /usr/local/bin/postgres-backup.sh
sudo chmod +x /usr/local/bin/postgres-backup.sh

sudo nano /etc/systemd/system/postgres-backup.service
sudo nano /etc/systemd/system/postgres-backup.timer

sudo systemctl daemon-reload
sudo systemctl enable postgres-backup.timer
sudo systemctl start postgres-backup.timer

sudo systemctl status postgres-backup.timer
sudo systemctl list-timers --all | grep postgres
```

## Таймер для отправки логов Nginx в S3

```bash
sudo cp ~/rotor/uploader.sh /usr/local/bin/nginx-logs.sh
sudo chmod +x /usr/local/bin/nginx-logs.sh

sudo nano /etc/systemd/system/nginx-logs.service
sudo nano /etc/systemd/system/nginx-logs.timer

sudo systemctl daemon-reload
sudo systemctl enable nginx-logs.timer
sudo systemctl start nginx-logs.timer

sudo systemctl status nginx-logs.timer
sudo systemctl list-timers --all
```

## Общий юнит приложения

```bash
sudo nano /etc/systemd/system/myapp.target
sudo systemctl daemon-reload
sudo systemctl enable myapp.target
sudo systemctl start myapp.target
sudo systemctl status myapp.target

# [Unit] PartOf=myapp.target
```