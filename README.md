# MicroredUCSC


This a monitor system for non-conventional renewable energy in the Catholic University of the Most Holy Conception, departament engeenery electric.

```bash

user: microred username: sbc password: z79j@arfKb
```

Database Postgres User: microred database: dbmicroreducsc password: M*MDx8IjHe


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
