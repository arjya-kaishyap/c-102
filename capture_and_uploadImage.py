from os import access
import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    VideoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = VideoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
    return img_name
    print("SnapShot has taken...")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BH9BqYz-HjQjOtDpRfktjXLxU6qyEGm90HNhDVHTzERRsw68Gxn5CsCHwsePTDa_DbExBwb4_hGgSb9jFi7QE7FsSa5Cvn5WIvaBveiYNbhW49XWfYWjdwp_vqeo6_K9KdFvlPg"
    file = img_name
    file_from = file
    file_to = "/newFolder1" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print(" File uploaded... ")

def main():
    while(True):
        if((time.time()-start_time)>= 30):
            name = take_snapshot()
            upload_file(name)

main()
