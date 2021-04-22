from .imageprocessing import ImageProcessor
from .textprocessing import TextProcessor

class DataProcessing:
    def __init__(self):
        pass

    def process_data(self):
        # detect cells from the image
        imageprocessor = ImageProcessor()
        img_cells = imageprocessor.get_cells()

        # detect text from the img_cells
        textprocessor = TextProcessor()
        text_cells = textprocessor.get_cells()

        return text_cells
