class Pixels:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.red = 0
        self.green = 0
        self.blue = 0

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def set_grayscale(self, red_pixel, green_pixel, blue_pixel):
        self.red = red_pixel
        self.green = green_pixel
        self.blue = blue_pixel
        average = (red_pixel + blue_pixel + green_pixel) / 3

    def print_pixel_info(self):
        pass


def main():
    p = Pixels(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


main()
