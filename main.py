class Character:
    def __init__(self, char):
        self.char = char

    def print_character(self, font_size):
        print(f"Character: {self.char}, Font Size: {font_size}")


class CharacterFactory:
    def __init__(self):
        self.characters = {}

    def get_character(self, char):
        if char not in self.characters:
            self.characters[char] = Character(char)
        return self.characters[char]


class TextEditor:
    def __init__(self, character_factory):
        self.characters = []
        self.character_factory = character_factory

    def insert_character(self, char, font_size):
        character = self.character_factory.get_character(char)
        character.print_character(font_size)
        self.characters.append(character)

    def print_text(self, font_size):
        for character in self.characters:
            character.print_character(font_size)

if __name__ == "__main__":
    character_factory = CharacterFactory()
    text_editor = TextEditor(character_factory)

    text_editor.insert_character('H', 12)
    text_editor.insert_character('e', 12)
    text_editor.insert_character('l', 12)
    text_editor.insert_character('l', 12)
    text_editor.insert_character('o', 12)

    text_editor.print_text(12)
