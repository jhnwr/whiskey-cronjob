# Commands and Links from Video

## Links:

Digital Ocean (Affiliate Link) - https://m.do.co/c/c7c90f161ff6
Crontab Guru - https://crontab.guru/#0_8_*_*_*

## Commands used:

I use the windows terminal app from the windowns 10 store (mine is themed). I am using Powershell for this video.

### Create a Droplet

* apt udpate
* apt upgrade
* python3
* apt install python3-pip
* cd ..
* cd /home
* pip install requests beautifulsoup3 pandas
* git clone <repo URL>

DONT FORGET DO NOT UPLOAD PASSWORDS TO GITHUB

I use a separate .py file and import it into my code

* nano creds.py

### Cronjobs

* crontab -e
* select nano [1]

This runs every minute our test.py file that is in the home directory
* * * * * /usr/bin/python3 /home/test.py >> /home/cron.log

this runs everyday at 8 AM
0 8 * * * /usr/bin/python3 /home/<path to your script>

