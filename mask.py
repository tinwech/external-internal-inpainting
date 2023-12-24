import numpy as np
import cv2 as cv
import argparse

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
color = (255, 255, 255)
img = None
mask = None


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), color, -1)
                cv.rectangle(mask, (ix, iy), (x, y), color, -1)
            else:
                cv.circle(img, (x, y), 10, color, -1)
                cv.circle(mask, (x, y), 10, color, -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), color, -1)
            cv.rectangle(mask, (ix, iy), (x, y), color, -1)
        else:
            cv.circle(img, (x, y), 10, color, -1)
            cv.circle(mask, (x, y), 10, color, -1)


def main(img_path):
    global img, mask, mode
    img = cv.imread(img_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    mask = np.zeros(img.shape, np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw)
    while (1):
        cv.imshow('image', img)
        k = cv.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == ord('q'):
            cv.imwrite("images/input3.jpg", img)
            cv.imwrite("images/gray3.jpg", gray)
            cv.imwrite("images/mask3.jpg", mask)
            break
        elif k == 27:
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, default="test.jpg")
    args = parser.parse_args()
    main(args.image)
