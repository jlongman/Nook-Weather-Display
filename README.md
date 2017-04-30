<image align="right" height="400" src="https://cloud.githubusercontent.com/assets/1051995/25560794/0e9f7ad2-2d2b-11e7-815d-523507578a61.png"/>

# Nook-Weather-Display
- based on <br/>https://github.com/mrfunkyland/Nook-Weather-Display

- which was based on Kindle Weather Display by Matt Petroff<br/>
https://github.com/mpetroff/kindle-weather-display

# features
- use openweather to get four days of forecast
  - requires owm key
- access google calendar
  - requires google app, keys

# changes from original versions
- removed goodreads
- use openweather, requires pyowm
- isolate drawing code
- add rotate code, requires python-pil (pillow)

# requirements
Raspberry Pi setup:
(NB: much more is required, I forget and lost bash history, will take PRs!)
- `pip install pyowm`
- `apt-get install python-googleapiclient`
- `apt-get install python-pil` (for rotate)
- `apt-get install pngcrush` - reduces image size, optional
- install https://github.com/andreafabrizi/Dropbox-Uploader.git 
- get a copy of the DropSync v1.68 app and install on Nook
- DO NOT USE 2FA on DropBox
- openweather api key
- google app keys

# execution script
Add this to your crontab:

```
#!/bin/bash
####################################
# generate weather
# clean up
# upload to dropbox
####################################
# use with ramdisk: 
# echo "tmpfs /var/tmp tmpfs nodev,nosuid,size=1M 0 0" >> /var/fstab # as root
# sudo mount -a

HOME_PATH=/home/pi/work
NOOK=$HOME_PATH/Nook-Weather-Display
cp $NOOK/weather-script-preprocess.svg  $NOOK/data.json  /var/tmp
cd /var/tmp
pwd
python $NOOK/weather-script.py
cairosvg -d 172 -f png -o weather.png weather-script-output.svg
# rotate png? optional
python $NOOK/rotate-png.py weather.png
/usr/bin/pngcrush  -reduce -m 7 weather.png weather2.png
$HOME_PATH/Dropbox-Uploader/dropbox_uploader.sh  upload weather2.png weather.png
```

