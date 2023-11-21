import sys
import re
from ui_form import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btnPwd.clicked.connect(self.analizador_lexicografico)
        self.emoji_dict = {
            ":)": "feliz.png",
            ":(": "triste.png",
            ":D": "entusiasta.png",
            ";)": "guino.png",
            ":P": "lengua.png",
            ":p": "lengua.png",
            "xD": "risa.png",
            "XD": "risa.png",
            ":-)": "feliz.png",
            ":-(": "triste.png",
            "(y)": "like.png",
            "(n)": "dislike.png",
            "<3": "corazon.png",
            "\m/": "rock.png",
            ":-O": "sorpresa.png",
            ":O": "sorpresa.png",
            ":-|": "preocuparse.png",
            "^^": "entusiasta.png",
            ":-]": "entusiasta.png",
            ":3": "perro.png",
            "owo": "gato.png",
            "shit": "shit.png",
            "fuck": "insulto.png",
            ":9": "lengua.png",
            "xd": "risa.png",
            ":0": "sorpresa.png",
            ":|": "preocuparse.png",
            "m:m": "abrazar.png",
            "'-'": "preocuparse.png",
            "°^°": "gato.png"
        }

    def analizador_lexicografico(self):
        texto = self.ui.TXTpWD.text()

        for emoticon, ruta_imagen in self.emoji_dict.items():
            if emoticon in texto:
                imagen = QPixmap(ruta_imagen)
                self.mostrar_imagen(emoticon, imagen)

        cantEmoji = sum(texto.count(emoticon) for emoticon in self.emoji_dict.keys())
        palabras_ignoradas = set(self.emoji_dict.keys())
        cantPalabrasEspanol = sum(1 for palabra in re.findall(r'\b(?:[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+)\b(?<!:)\b|', texto.lower())
                                  if palabra not in palabras_ignoradas)
        self.ui.lblSalida.setText(f"Se reconocieron {cantEmoji} emoji(s) en el texto y {cantPalabrasEspanol} palabra(s)")
        self.ui.lblEmoji.setText(f"Texto modificado: {texto}")

    def mostrar_imagen(self, emoticon, imagen):
        label = getattr(self.ui, f"lbl{emoticon}")
        label.setPixmap(imagen.scaled(50, 50, aspectRatioMode=QtCore.Qt.KeepAspectRatio))
        if imagen.isNull():
            print(f"ERROR: No se ha podido cargar la imagen: {imagen}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
