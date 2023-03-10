class ColorBuilder():
    def __init__(self):
        self.mod = '0'
        self.color_mode = '0'
        self.color = '39'
        self.background = '49'
        self.rgb_back = None
        self.rgb_foreground = None

    def build(self, text):
        colors = ""
        if self.rgb_back is not None:
            colors += f"48;5;{self.rgb_back};"
        if self.rgb_foreground is not None:
            colors += f"38;5;{self.rgb_foreground};"
        if self.color != '39' and self.rgb_foreground is None:
            colors += f"{self.color};"
        if self.background != '49' and self.rgb_back is None:
            colors += f"{self.background};"
        if self.color_mode == '0':
            return f"\x1b[{self.mod};{colors[:-1]}m{text}\x1b[0m"
        elif self.mod == '0':
            return f"\x1b[{self.color_mode};{colors[:-1]}m{text}\x1b[0m"
        else:
            return f"\x1b[{self.mod};{self.color_mode};{colors[:-1]}m{text}\x1b[0m"

    def red_color(self):
        self.color = '31'
        return self
    
    def black_color(self):
        self.color = '30'
        return self
    
    def green_color(self):
        self.color = '32'
        return self
    
    def yellow_color(self):
        self.color = '33'
        return self
    
    def blue_color(self):
        self.color = '34'
        return self
    
    def magenta_color(self):
        self.color = '35'
        return self
    
    def cyan_color(self):
        self.color = '36'
        return self
    
    def white_color(self):
        self.color = '37'
        return self
    
    def red_background(self):
        self.background = '41'
        return self
    
    def black_background(self):
        self.background = '40'
        return self
    
    def green_background(self):
        self.background = '42'
        return self
    
    def yellow_background(self):
        self.background = '44'
        return self
    
    def blue_background(self):
        self.background = '44'
        return self
    
    def magenta_background(self):
        self.background = '45'
        return self
    
    def cyan_background(self):
        self.background = '46'
        return self
    
    def white_background(self):
        self.background = '47'
        return self
    
    def light_color(self):
        self.color_mode = '1'
        return self
    
    def dark_color(self):
        self.color_mode = '2'
        return self
    
    def italic_mode(self):
        self.mod = '3'
        return self
    
    def underline_mode(self):
        self.mod = '4'
        return self
    
    def blinking_mode(self):
        self.mod = '5'
        return self
    
    def strikethrough_mode(self):
        self.mod = '9'
        return self
    
    def rgb_color(self, color):
        """
        RGB Color has an advantage over other colors
        """
        self.rgb_foreground = str(color)
        return self

    def light_background(self):
        """
        Dark color mode not change background
        """
        self.background = f"10{self.background[-1]}"
        return self

    def rgb_background(self, color):
        """
        RGB Background has an advantage over other backgrounds
        """
        self.rgb_back = str(color)
        return self

    @staticmethod
    def print_all_colors_by_mode():
        for i in range(0, 3):
            for j in range(30, 40):
                for c in range(40, 50):
                        print(f"\x1b[{i};{j};{c}mTest\x1b[0m", end=' ')
                print()
            print()
    
    @staticmethod
    def print_all_color_by_rgb():
        for i in range(0, 256):
            for j in range(0, 256):
                print(f"\x1b[48;5;{i};38;5;{j}m{i} {j}\x1b[0m", end=' ')
