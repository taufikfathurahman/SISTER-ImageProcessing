from xmlrpc.server import SimpleXMLRPCServer
from image_upload import image_upload
from image_download import image_download
from image_smoothing import image_smoothing
from image_remove import image_remove
from object_detection import object_detection
from canny_edge_detection import canny_ed
from image_rgbtohsv import rgb2hsv_main
from image_rgbtograyscale import rgb2grayscale_main
from image_rgbtocmy import rgb2cmy_main
from image_rgbtoycrcb import rgb2ycrcb_main

server = SimpleXMLRPCServer(('172.20.10.3', 8000), allow_none=True)
print('Listening on port 8000')

server.register_function(rgb2ycrcb_main, 'rgb2ycrcb_main')
server.register_function(image_upload, 'image_upload')
server.register_function(image_smoothing, 'image_smoothing')
server.register_function(image_download, 'image_download')
server.register_function(image_remove, 'image_remove')
server.register_function(object_detection, 'object_detection')
server.register_function(canny_ed, 'canny_ed')
server.register_function(rgb2hsv_main, 'rgb2hsv_main')
server.register_function(rgb2grayscale_main, 'rgb2grayscale_main')
server.register_function(rgb2cmy_main, 'rgb2cmy_main')

server.serve_forever()