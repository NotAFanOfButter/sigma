import time
from PIL import ImageGrab, ImageChops, Image
from pynput.mouse import Controller, Button

dir = "C:/Users/seblf/Documents/Python/Sigma/"

notebooks = {
    "button": {
        "png":dir+"screen/nb-button.png",
        "coords":(10,120,20,130)
    },
    "all": {
        "png":dir+"screen/notebooks.png",
        "coords":(90,120,100,140)
    },
    "english": {
        "png":[dir+"screen/onenote/english.png", dir+"screen/onenote/english-new.png"],
        "coords":(140,400,150,440)
    }
}

mouse = Controller()
def onenote():
    time.sleep(5)
    mouse.click(Button.left)
    # open notebooks dialogue
    if checkPic(notebooks["button"]["coords"],notebooks["button"]["png"]):
        mouse.position = notebooks["button"]["coords"][:2] + (5,5)
        mouse.click(Button.left)
        time.sleep(1)
    #
    print(checkPic(notebooks["all"]["coords"],notebooks["all"]["png"]))
    #
    #open all notebooks
    if not checkPic(notebooks["all"]["coords"],notebooks["all"]["png"]):
        mouse.position = notebooks["all"]["coords"][:2] + (5,5)
        #
        print(mouse.position,notebooks["all"]["coords"][:2])
        #
        mouse.click(Button.left)
def checkPic(bbox, path):
    sc = ImageGrab.grab(bbox)
    return False if ImageChops.difference(sc,Image.open(path)).getbbox() else True