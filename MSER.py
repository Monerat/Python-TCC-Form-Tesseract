import cv2
import numpy as np

def aplica_MSER(n):
    #Criar um objeto MSER
    mser = cv2.MSER_create()

    #Detectar as regioes na img em escala de cinza
    regions, _ = mser.detectRegions(n)

    #envultoria convexa
    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

    mask = np.zeros((n.shape[0], n.shape[1], 1), dtype=np.uint8)

    for contour in hulls:
        cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

    #this is used to find only text regions, remaining are ignored
    text_only = cv2.bitwise_and(n, n, mask=mask)

    cv2.imshow("text only", text_only)

    cv2.waitKey(0)
    return text_only
