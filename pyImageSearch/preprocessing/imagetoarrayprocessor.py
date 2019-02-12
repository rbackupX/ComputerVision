
from keras.preprocessing.image import img_to_array


class ImageToArrayProcessor:
    def __init__(self,dataFormat=None):
            self.dataFormat = dataFormat

    def preprocess(self,image):


        return img_to_array(image,dataFormat=self.dataFormat)
        