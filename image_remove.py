import os

def image_remove(date, host_id):
    os.remove(date+host_id+'.png')