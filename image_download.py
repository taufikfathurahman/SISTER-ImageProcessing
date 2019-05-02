import xmlrpc.client

def image_download(date, host_id):
    handle = open(date+host_id+'.png', 'rb')
    return xmlrpc.client.Binary(handle.read())
    handle.close() 