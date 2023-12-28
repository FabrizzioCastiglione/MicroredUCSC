# MicroredUCSC


This a monitor system for non-conventional renewable energy in the Catholic University of the Most Holy Conception, departament engeenery electric.

```bash

user: microred
username: sbc
password: z79j@arfKb


Database Postgres
User: microred
database: dbmicroreducsc
password: M*MDx8IjHe
```




```bash
sudo nano daphne.service
```

```bash
[Unit]
Description=WebSocket Daphne Service
After=network.target

[Service]
User=microred
Group=www-data
WorkingDirectory=/home/microred/microreducsc
Environment=DJANGO_SETTINGS_MODULE=microreducsc.settings
ExecStart=/home/microred/env/bin/python /home/microred/env/bin/daphne -b 0.0.0.0 -p 8001 microreducsc.asgi:application

[Install]
WantedBy=multi-user.target
```


Uwsgi with daphne for socket.
/etc/nginx/sites-availables

```bash
# the upstream component nginx needs to connect to
upstream django {
        server unix:///home/microred/microreducsc/microreducsc.sock;
}
# configuration of the server
server {
    listen      80;
    server_name localhost;
    charset     utf-8;
    # max upload size
    client_max_body_size 75M;
    # Django media and static files
    location /media  {
        alias /home/microred/microreducsc/media;
    }
    location /static {
        alias /home/microred/microreducsc/static;
    }
    # Send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include     /home/microred/microreducsc/uwsgi_params;
    }
    location /ws/ {
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_redirect off;
        proxy_pass http://127.0.0.1:8001;
    }
}

```
