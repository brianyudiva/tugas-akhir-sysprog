# Server Printer

## Member:
- Brian Athallah Yudiva
- Muhammad Zuhdi Zamrud
- Mushaffa Huda

## Techstack
- Shell
- Django
- CUPS

## Setup

1. Install python, pip, and cups in linux system

```shell
sudo apt install python3, pip, cups
```

For the CUPS configuration, go to CUPS configuration header

2. Make sure printer is connected to the system

```shell
lsmod | grep usblp
```
**NOTE** : if command return usblp, then printer exist, if not, check your VM settings

4. Install django dependacies

```shell
pip install -r requirements.txt
```

5. Run Django WebServer

Go to the Django project directory then

```shell
python3 manage.py runserver
```

6. Your WebServer is now running!

## CUPS Configuration

1. Edit /etc/cups/cupsd.conf

[See this website for this part](https://www.suse.com/support/kb/doc/?id=000017214)

2. Run CUPS in process

```shell
systemctl enable cups
systemctl start cups
```

3. Check if printer exist

```shell
lpstat -p
```

4. Make printer default

```shell
lpoptions -d PRINTER_NAME
```

5. Then you can use the lp command to print file

