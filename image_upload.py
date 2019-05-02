def image_upload(filedata, date, host_id):
    with open(date+host_id+'.png', 'wb') as my_img:
        data = filedata.data
        my_img.write(data)
        my_img.close()
        return True

