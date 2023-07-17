import argparse
import flickrapi
import urllib.request as req
import yaml
import time
import os
from tqdm import tqdm
from PIL import Image
from io import BytesIO


parser = argparse.ArgumentParser(
    prog='Flickr Images Downloader'
)
parser.add_argument('keyword', type=str, help='keyword')
parser.add_argument('-c', '--cfg', type=str, default='config.yaml', help='path to config file')
parser.add_argument('-d', '--save_dir', type=str, default='images', help='directory for images to be saved')
parser.add_argument('-s', '--start_page', type=int, default=1, help='start page')
parser.add_argument('-p', '--page_num', type=int, default=1, help='how many pages do you want to download')
parser.add_argument('-t', '--interval', type=float, default=1.0, help='interval between downloading two images')
parser.add_argument('--resize', action='store_true', help='whether to resize images')
parser.add_argument('--width', type=int, default=800, help='width for reszing')
parser.add_argument('--height', type=int, default=600, help='height for reszing')
args = parser.parse_args()

with open(args.cfg, 'r') as f:
    cfg = yaml.load(f, yaml.FullLoader)

save_dir = os.path.join(args.save_dir, args.keyword)
os.makedirs(save_dir, exist_ok=True)

flickr = flickrapi.FlickrAPI(cfg['api_key'], cfg['secret'], cache=True, format='parsed-json')

for p in range(args.start_page, args.start_page+args.page_num):
    response = flickr.photos.search(
        text=args.keyword,
        tags=args.keyword,
        page=p,
        tag_mode='all',
        extras='url_c',
        per_page=100,
        sort='relevance'
    )
    if response['stat'] == 'ok':
        if p == args.start_page:
            pages = response['photos']['pages']
            print(f"Get <{pages}> pages!")
        page = response['photos']['page']
        print(f"Start to download page <{page}>...")
        images = response['photos']['photo']
        for image in tqdm(images):
            try:
                img_url = image['url_c']
                img_id = image['id']
                img_ext = img_url.split('.')[-1]
                img_name = f"{img_id}.{img_ext}"
                
                if not args.resize:
                    req.urlretrieve(img_url, os.path.join(save_dir, img_name))
                else:
                    img_data = req.urlopen(img_url)
                    img_pil = Image.open(BytesIO(img_data.read()))
                    img_pil = img_pil.resize((args.width, args.height), resample=Image.Resampling.LANCZOS)
                    img_pil.save(os.path.join(save_dir, img_name))

                time.sleep(args.interval)
            except:
                pass