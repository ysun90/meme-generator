
from PIL import Image, ImageDraw, ImageFont

from QuoteEngine import QuoteModel

class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme With a Text and an author.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- text attached on the image
            author {str} -- author of the text
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        img = Image.open(img_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if test and author:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(size=20)
            quote_model = QuoteModel(text, author)
            draw.text((10, 30), quote_model.quote(), font=font, fill='white')

        img.save(self.output_dir)
        return self.output_dir
