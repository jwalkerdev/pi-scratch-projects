from gpiozero import LED
from time import sleep

# led1 = LED(17)
# led2 = LED(27)
# led3 = LED(22)
# led1.on()
# sleep(5)
# led1.off()

# https://picamera.readthedocs.io/en/release-1.13/api_mmalobj.html
# https://picamera.readthedocs.io/en/release-1.13/fov.html#camera-hardware

from picamera import mmal, mmalobj as mo
camera = mo.MMALCamera()
preview = mo.MMALRenderer()

len(camera.inputs)
# 0
len(camera.outputs)
# 3
len(preview.inputs)
# 1
len(preview.outputs)
# 0

camera.outputs[0]
# <MMALVideoPort "vc.ril.camera:out:0": format=MMAL_FOURCC('I420')
# buffers=1x7680 frames=320x240@0fps>
preview.inputs[0]
# <MMALVideoPort "vc.ril.video_render:in:0" format=MMAL_FOURCC('I420')
# buffers=2x15360 frames=160x64@0fps>

camera.outputs[0].framesize = (640, 480)
camera.outputs[0].framerate = 30
camera.outputs[0].commit()
camera.outputs[0]
# <MMALVideoPort "vc.ril.camera:out:0(I420)": format=MMAL_FOURCC('I420')
# buffers=1x460800 frames=640x480@30fps>

# Connections
preview.inputs[0].connect(camera.outputs[0])
# <MMALConnection "vc.ril.camera:out:0/vc.ril.video_render:in:0">
preview.inputs[0].connection.enable()

camera.outputs[0]
# <MMALVideoPort "vc.ril.camera:out:0(OPQV)": format=MMAL_FOURCC('OPQV')
# buffers=10x128 frames=640x480@30fps>
preview.inputs[0]
# <MMALVideoPort "vc.ril.video_render:in:0(OPQV)": format=MMAL_FOURCC('OPQV')
# buffers=10x128 frames=640x480@30fps>







