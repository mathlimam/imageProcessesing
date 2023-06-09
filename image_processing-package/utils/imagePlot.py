import cv2

class Plot:

    def plot(image):
        cv2.imwrite("image", image)
        cv2.imshow()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

