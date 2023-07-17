# flickr_dl

This python script is to help you download images from [Flickr](https://www.flickr.com/), which is an image hosting website.

## Installation
Please clone this repo or download zip package to use this script.

## Usage
### Set configuration
Primarily, you must set your Flick `API_KEY` and `SECRET` in [*config.yaml*](./config.yaml). If you haven't acquired a API_KEY, you can get one from [here](https://www.flickr.com/services/api/keys/). 

```yaml
api_key: YOUR_API_KEY
secret: YOUR_SECRET
```

### Execute command
This script provides a command-line interface. Typing `python ./main.py --help` for showing help messages.
```
usage: Flickr Images Downloader [-h] [-c CFG] [-d SAVE_DIR] [-s START_PAGE] [-p PAGE_NUM] [-t INTERVAL] [--resize] [--width WIDTH] [--height HEIGHT] keyword

positional arguments:
  keyword               keyword

options:
  -h, --help            show this help message and exit
  -c CFG, --cfg CFG     path to config file
  -d SAVE_DIR, --save_dir SAVE_DIR
                        directory for images to be saved
  -s START_PAGE, --start_page START_PAGE
                        start page
  -p PAGE_NUM, --page_num PAGE_NUM
                        how many pages do you want to download
  -t INTERVAL, --interval INTERVAL
                        interval between downloading two images
  --resize              whether to resize images
  --width WIDTH         width for reszing
  --height HEIGHT       height for reszing
```

The images downloaded from Flickr are stored at `./images/<keyword>`, please open this folder to check them.

## Acknowledgement

- [Flickr](https://www.flickr.com/)
- [flickapi](https://github.com/sybrenstuvel/flickrapi/)