import urllib.request
import os


def retrieve_image(url_address, image_name, upload_directory='news/news_images/'):
    file_type = str(url_address)[-4:]
    if not os.path.isdir(upload_directory):
        os.makedirs(upload_directory)
    urllib.request.urlretrieve(str(url_address), upload_directory + image_name + file_type)