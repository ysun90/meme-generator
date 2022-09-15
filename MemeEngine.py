"""Meme Engine Module manipulates and draws text onto images."""

from PIL import Image, ImageDraw, ImageFont

from QuoteEngine import QuoteModel


class MemeEngine:
    """A MemeEngine class."""

    def __init__(self, output_dir):
        """Instantiate the class.

        param output_dir: location to put the putput picture
        return: None
        """
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
        try:
            img = Image.open(img_path)
        except Exception as e:
            print("Cannot open the file exception.")

        # Picture with most width 500
        if width > 500:
            width = 500

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            quote_model = QuoteModel(text, author)
            draw.text((10, 30), quote_model.quote(), font=font, fill='white')

        img.save(self.output_dir)

        return self.output_dir
