import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class NotasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cálculo de Notas")
        
        # Setting the window icon
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, 'icon.ico')
        
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Aviso: Arquivo de ícone não encontrado em {icon_path}")

        layout = QVBoxLayout()

        # Input fields for notes
        self.nota1_input = QLineEdit(self)
        self.nota1_input.setPlaceholderText("Insira a Nota 1")
        self.nota2_input = QLineEdit(self)
        self.nota2_input.setPlaceholderText("Insira a Nota 2")
        self.nota3_input = QLineEdit(self)
        self.nota3_input.setPlaceholderText("Insira a Nota 3")

        # Button to calculate the result
        self.calcular_button = QPushButton("Calcular", self)
        self.calcular_button.clicked.connect(self.calcular_media)

        # Label to display result
        self.result_label = QLabel("Resultado das suas notas.", self)

        layout.addWidget(QLabel("Insira suas notas:"))
        layout.addWidget(self.nota1_input)
        layout.addWidget(self.nota2_input)
        layout.addWidget(self.nota3_input)
        layout.addWidget(self.calcular_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Setting minimum window size
        self.setMinimumSize(300, 200)

        self.focusable_widgets = [self.nota1_input, self.nota2_input, self.nota3_input, self.calcular_button]
        for widget in self.focusable_widgets:
            widget.setFocusPolicy(Qt.StrongFocus)

        self.nota1_input.setFocus()

    def keyPressEvent(self, event):
        key = event.key()
        current_widget = self.focusWidget()
        
        if key in (Qt.Key_Enter, Qt.Key_Return):
            if current_widget == self.calcular_button:
                self.calcular_media()
            else:
                self.focusNextChild()
        elif key == Qt.Key_Up:
            self.focusPreviousChild()
        elif key == Qt.Key_Down:
            self.focusNextChild()
        elif key == Qt.Key_Tab:
            self.focusNextChild()
        elif key == Qt.Key_Backtab:
            self.focusPreviousChild()
        else:
            super().keyPressEvent(event)

    def focusInEvent(self, event):
        widget = self.focusWidget()
        if isinstance(widget, QLineEdit):
            widget.selectAll()
        super().focusInEvent(event)

    def calcular_media(self):
        try:
            nota1 = float(self.nota1_input.text()) * 0.3
            nota2 = float(self.nota2_input.text()) * 0.3
            nota3 = float(self.nota3_input.text()) * 0.4

            media = round(nota1 + nota2 + nota3, 0)

            if media < 70:
                resultado = f"Média: {media} - Reprovado"
            else:
                resultado = f"Média: {media} - Aprovado"

            self.result_label.setText(resultado)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos para as notas.")
            self.nota1_input.clear()
            self.nota2_input.clear()
            self.nota3_input.clear()
            self.nota1_input.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = NotasApp()
    janela.show()
    sys.exit(app.exec())
