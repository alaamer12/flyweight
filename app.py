class Font:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def render(self, text):
        print(f"Rendering '{text}' with font '{self.name}', size {self.size}, color {self.color}")


class FontFactory:
    _fonts = {}

    @staticmethod
    def get_font(name, size, color):
        key = (name, size, color)
        if key not in FontFactory._fonts:
            FontFactory._fonts[key] = Font(name, size, color)
        return FontFactory._fonts[key]


class Text:
    def __init__(self, content, font):
        self.content = content
        self.font = font

    def draw(self):
        self.font.render(self.content)


if __name__ == "__main__":
    # Create text objects with different fonts
    text1 = Text("Hello", FontFactory.get_font("Arial", 12, "Black"))
    text2 = Text("World", FontFactory.get_font("Arial", 12, "Black"))
    text3 = Text("Python", FontFactory.get_font("Times New Roman", 14, "Red"))
    text4 = Text("Programming", FontFactory.get_font("Arial", 12, "Black"))

    # Draw the text
    text1.draw()
    text2.draw()
    text3.draw()
    text4.draw()

    # Check if fonts are shared
    print(text1.font is text2.font)  # Output: True
    print(text1.font is text4.font)  # Output: True
    print(text2.font is text4.font)  # Output: True
    print(text1.font is text3.font)  # Output: False
