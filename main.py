import shutil
from bing_image_downloader import downloader
from city import *
import sqlite3


def main():
    city = get_city()
    shutil.rmtree('./image')
    downloader.download(f'{city[0]}', limit=1, output_dir='image', verbose=True)


main()
