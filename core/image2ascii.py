from typing import List
import cv2
import numpy as np
import math

from util import exception_log, get_logger

DENSITY = "@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-`"


def get_density(density: str, value: float):
    # Since we don't have 255 characters, we have to use percentages
    charValue = math.floor(len(DENSITY) / 255.0 * value)
    charValue = max(charValue, 0)
    charValue = min(charValue, len(DENSITY) - 1)
    return density[charValue]

@exception_log
def toascii(image_path: str, 
            max_width = 80, 
            max_height = 40,
            force_resize = False,
            density = DENSITY) -> str:
    logger = get_logger(LOG_NAME='toascii')
    img = cv2.imread(image_path)
    height, width = img.shape[:2]
    logger.info(f'Image -> width: {width}, height: {height}, force_resize: {force_resize}')
        
    if force_resize:
        print('Resizing image')
        img = cv2.resize(img, (max_width, max_height), interpolation=cv2.INTER_AREA)
    
    else:    
    # only shrink if img is bigger than required
        if max_height < height or max_width < width:
            # get scaling factor
            scaling_factor = max_height / float(height)
            logger.info(f'Scaling factor: {scaling_factor}')
            if max_width/float(width) < scaling_factor:
                scaling_factor = max_width / float(width)
                logger.info(f'Scaling factor (max_width): {scaling_factor}')
            # resize image
            img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    # convert to hsl
    hsl = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    # increse saturation
    hsl[:,:,1] = hsl[:,:,1] * 1
    # convert back to rgb
    img = cv2.cvtColor(hsl, cv2.COLOR_HLS2BGR)
    

    brightness = np.empty((img.shape[0], img.shape[1]))
    ascii_image = []
    for x in range(len(img)):
        for y in range(len(img[x])):
            pixel = img[x][y]
            avg  = (pixel[0] + pixel[1] + pixel[2]) / 3
            brightness[x][y] = avg
    for x in range(len(brightness)):
        line = []
        for y in range(len(brightness[x])):
            line.append(get_density(density,brightness[x][y]))
        ascii_image.append(''.join(line))
    ascii_img_txt = '\n'.join(ascii_image)
    return ascii_img_txt