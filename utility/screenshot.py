from numpy import array
from cv2 import cvtColor,imwrite,COLOR_RGB2BGR
from pyautogui import screenshot

#path where you want to store screenshots
path="C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\utility\\screenshots\\"

def takeScreenshot(filename="image"):
    # take screenshot using pyautogui 
    image = screenshot() 
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk 
    image = cvtColor(array(image), 
                        COLOR_RGB2BGR) 
    # writing it to the disk using opencv 
    imwrite(path+filename+".png", image) 

if __name__ == "__main__":
    takeScreenshot()