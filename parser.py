

# goal of the program: apply specified modifications, and add some random ones too if desired
"""
will not treat:
vertical alignment
horizontal alignment
"""

# for colors: color names / hex tags / RGB(A) values




class Block:
    
    def __init__ (self, text: str, **kwargs):
        self.text = text

        self.font_color = kwargs.get('font_color', 'black')  # to change
        self.font_color_start = kwargs.get('font_color_start', self.font_color)
        self.font_color_end = kwargs.get('font_color_end', self.font_color_start)

        self.background_color = kwargs.get('background_color', 'white')  # to change
        self.background_color_start = kwargs.get('background_color_start', self.background_color)
        self.background_color_end = kwargs.get('background_color_end', self.background_color_start)

        self.font_size = kwargs.get('font_size', 12)  # to change
        # process whether function / array / value

        self.style_underlined = kwargs.get('underlined', False)
        self.style_italicised = kwargs.get('italicised', False)
        self.style_bold = kwargs.get('bold', False)
        self.style_strikethrough = kwargs.get('strikethrough', False)

        self.font = kwargs.get('font', None) # to change

        # Generate
        self.html = self.__generate()


    def __generate (self):

        html = ''
        return html
    

    





class Paragraph:

    def __init__ (self, text: str):
        self.text = text

        self.parse = self.__parse()
        self.html = self.__generate()
    
    def __parse (self):
        # linear read? or multi split?
        #\b{}  or \bold\

        # multi split along all markers like \b, \bold, … and then determine arguments and ranges
        pass

    def __generate (self):
        pass


        