import sys
import re
from ui_form import *
from PyQt5.QtWidgets import *


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btnPwd.clicked.connect(self.analizador_lexicografico)
        self.emoji_dict = {
            ":)": "😊",
            ":(": "😔",
            ":D": "😀",
            ";)": "😉",
            ":P": "😛",
            ":p": "😛",
            "xD": "😆",
            "XD": "😆",
            ":-)": "😊",
            ":-(": "😔",
            "(y)": "👍",
            "(n)": "👎",
            "<3": "❤️",
            "\m/": "🤘",
            ":-O": "😮",
            ":O": "😮",
            ":-|": "😐",
            ":*": "😘",
            ">:<": "😠",
            "^^": "😄",
            ":-]": "😃",
            "¬_¬": "😒",
            ":3": "🐶",
            "owo": "😺",
            "7u7": "😏",
            "$)": "🤑",
            "shit": "💩",
            "fuck": "🤬",
            "o-o": "🚗",
            "°v°": "🐧",
            ":9": "😛",
            "xd": "😆",
            "X9": "😝",
            "Y:oY": "😲",
            ":0": "😮",
            ":|": "😐",
            "o o": "😶",
            "):<": "😠",
            "@u@": "🤪",
            "m:m": "🙌😊🙌",
            "°:°": "🐼",
            ":>**": "🦆",
            "°| °|": "👀",
            ":>}}": "🐓",
            ":>YY": "🐥",
            "'-'": "😐",
            "°^°": "🙀"
        }

    def analizador_lexicografico(self):
        texto = self.ui.TXTpWD.text()

        def reemplazar_emoticon(match):
            emoticon = match.group(0)
            emoji = self.emoji_dict.get(emoticon, emoticon)
            return emoji

        patron = re.compile("|".join(map(re.escape, self.emoji_dict.keys())))
        texto_modificado = patron.sub(reemplazar_emoticon, texto)
        cantEmoji = sum(texto.count(emoticon) for emoticon in self.emoji_dict.keys())
        palabras_ignoradas = set(self.emoji_dict.keys())
        # Dividir el texto en palabras y emojis
        palabras_y_emojis = re.findall(r'\b(?:[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+)\b(?<!:)\b|' +
                                       "|".join(map(re.escape, self.emoji_dict.values())), texto_modificado.lower())
        # Contar las palabras que no son emojis
        cantPalabrasEspanol = sum(1 for palabra in palabras_y_emojis if palabra not in self.emoji_dict.values())
        for emoticon, emoji in self.emoji_dict.items():
            texto_modificado = texto_modificado.replace(emoticon, emoji)
        self.ui.lblSalida.setText(
            f"Se reconocieron {cantEmoji} emoji(s) en el texto y {cantPalabrasEspanol} palabra(s)")
        self.ui.lblEmoji.setText(f"Texto modificado: {texto_modificado}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
