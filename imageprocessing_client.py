import xmlrpc
import xmlrpc.client
import socket
import datetime
import os

def header(host_id):
    print('| $ Welcome', host_id)
    print('|===================================================|')
    print('|         Big Computational-Image Processing        |')
    print('|                   --Metasplot--                   |')
    print('|===================================================|')

def main_menu():
    os.system('clear')
    print('|___________________________________________________|')
    print('| Menu :                                            |')
    print('|___________________________________________________|')
    print("| 1. | Edge Detection Using Canny Method            |")
    print("| 2. | Image Smoothing                              |")
    print("| 3. | Convert Image to Grayscale                   |")
    print("| 4. | Convert Image to HSV                         |")
    print("| 5. | Convert Image to CMY                         |")
    print("| 6. | Convert Image to ycbcr                       |")
    print("| 7. | Face and Eyes Detection                      |")
    print("| 8. | Change Image to Edit                         |")
    print("| 9. | Download Image                               |")
    print("| 10.| Exit                                         |")
    print('|----|----------------------------------------------|')

    return input('| <> | Choose Menu =>')

def load_image(proxy, date, host_id):
    print('| <> | Please Input Image File Name + Extentions    |')
    filename = input('| <> | => ')
    with open(filename, 'rb') as my_img:
        img_data = xmlrpc.client.Binary(my_img.read())
        my_img.close()
        proxy.image_upload(img_data, date, host_id)

def success_msg():    
    print('|----|----------------------------------------------|')
    print('| <> | $ Function Successfully Executed !           |')
    print('|----|----------------------------------------------|')
    input("Press enter to continue")

def failed_msg():    
    print('|----|----------------------------------------------|')
    print('| <> | $ Function Failed Executed !                 |')
    print('|----|----------------------------------------------|')
    input("Press enter to continue")

if __name__ == "__main__":
    host_id = str(socket.gethostname())
    date = str(datetime.datetime.now().date())
    proxy = xmlrpc.client.ServerProxy("http://172.20.10.2:8000")
    choice = 99
    
    header(host_id)
    load_image(proxy, date, host_id)

    while(choice != "10"):        
        choice = main_menu()
        if (choice == '1'):
            try:
                proxy.canny_ed(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '2'):
            try:
                proxy.image_smoothing(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '3'):
            try:
                proxy.rgb2grayscale_main(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '4'):
            try:
                proxy.rgb2hsv_main(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '5'):
            try:
                proxy.rgb2cmyk_main(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '6'):
            try:
                proxy.rgb2ycrcb_main(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '7'):
            try:
                proxy.object_detection(date, host_id)
                success_msg()
            except:
                failed_msg()
        elif (choice == '8'):
            try:
                proxy.image_remove(date, host_id)
                success_msg()
                os.system('clear')
                load_image(proxy, date, host_id)
            except:
                failed_msg()
        elif (choice == '9'):
            print('| <> | Please Input New Image File Name + Extentions|')
            new_filename = input('| <> | => ')
            try:
                my_img = open(new_filename, "wb")
                my_img.write(proxy.image_download(date, host_id).data)
                my_img.close()
                success_msg()
            except:
                failed_msg()
        elif (choice == '10'):
            
            print('| <> | $ echo \'Terimakasih ~~~ \'                    |')
            print('|___________________________________________________|')
            # Delete files after client exit the program
            try:
                proxy.image_remove(date, host_id)
            except:
                failed_msg()
        else:
            print('| <> | $ Wrong Input !                              |')