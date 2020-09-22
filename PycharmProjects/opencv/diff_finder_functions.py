from skimage.measure import compare_ssim
import cv2


def diff_finder(img01, img02):
    """
    find the difference between the two different images
    :param img01: file path of the first image
    :param img02: file path of the second image
    :return: address of the result file
    """
    # load the two input images
    image01 = cv2.imread(img01)
    image02 = cv2.imread(img02)

    # convert the images to grayscale
    gray01 = cv2.cvtColor(image01, cv2.COLOR_BGR2GRAY)
    gray02 = cv2.cvtColor(image02, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two images
    (score, diff) = compare_ssim(gray01, gray02, full=True)

    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type in the range [0,1]
    # so we must convert the array to 8-bit unsigned integers in the range
    # [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    for c in contours:
        # calculate the area of the contours for the further filter
        area = cv2.contourArea(c)
        if area > 40:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image01, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("result", image01)
    cv2.imwrite("result.png", image01)
