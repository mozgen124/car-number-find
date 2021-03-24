from imutils import contours
import cv2
import pytesseract

spisok_nomer = "ABEKMHOPCTYX0123456789"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image = cv2.imread("boh.jpg")

height, width, _ = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = contours.sort_contours(cnts[0])

for c in cnts:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    if area > 5000:
        img = image[y:y+h, x:x+w]
        result = pytesseract.image_to_string(img, lang="eng")
        if len(result) > 7:
            for i in result:
                if i in spisok_nomer:
                    print(i, end=' ')
            #print(result)
