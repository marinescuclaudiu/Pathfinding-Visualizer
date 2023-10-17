class Color:
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'orange': (255, 117, 24),
        'pink': (255, 192, 203),
        'cyan': (0, 255, 255),
        'gray': (128, 128, 128),
        'brown': (165, 42, 42),
        'lime': (0, 255, 0),
        'turquoise': (64, 224, 208),
        'gold': (255, 215, 0),
        'indigo': (75, 0, 130),
        'maroon': (128, 0, 0),
        'navy': (0, 0, 128),
        'teal': (0, 128, 128),
        'coral': (255, 127, 80),
        'lavender': (230, 230, 250),
        'juniper': (84, 135, 107)
    }

    @classmethod
    def get_color(cls, color_name):
        return cls.colors.get(color_name.lower(), None)
