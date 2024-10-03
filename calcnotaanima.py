import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PySide6.QtGui import QIcon

class NotasApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cálculo de Notas")

        # Definir um ícone para a janela
        self.setWindowIcon(QIcon('E:\programming\calcnotaanima\Calcular_nota_anima\icon.ico'))  # Coloque o caminho correto para seu ícone

        # Layout da interface
        layout = QVBoxLayout()

        # Campos de entrada para as notas
        self.nota1_input = QLineEdit(self)
        self.nota1_input.setPlaceholderText("Insira a Nota 1")

        self.nota2_input = QLineEdit(self)
        self.nota2_input.setPlaceholderText("Insira a Nota 2")

        self.nota3_input = QLineEdit(self)
        self.nota3_input.setPlaceholderText("Insira a Nota 3")

        # Botão para calcular
        calcular_button = QPushButton("Calcular", self)
        calcular_button.clicked.connect(self.calcular_media)

        # Label para exibir o resultado
        self.result_label = QLabel("Resultado das suas notas.", self)

        # Adicionar widgets ao layout
        layout.addWidget(QLabel("Insira suas notas:"))
        layout.addWidget(self.nota1_input)
        layout.addWidget(self.nota2_input)
        layout.addWidget(self.nota3_input)
        layout.addWidget(calcular_button)
        layout.addWidget(self.result_label)  # Exibir o resultado abaixo do botão

        # Definir layout na janela
        self.setLayout(layout)

    def calcular_media(self):
        try:
            # Obter as notas inseridas
            nota1 = float(self.nota1_input.text()) * 0.3
            nota2 = float(self.nota2_input.text()) * 0.3
            nota3 = float(self.nota3_input.text()) * 0.4

            # Calcular a média
            media = round(nota1 + nota2 + nota3, 2)

            # Verificar se foi aprovado ou reprovado
            if media < 70:
                resultado = f"Média: {media} - Reprovado"
            else:
                resultado = f"Média: {media} - Aprovado"

            # Exibir o resultado no QLabel abaixo do botão
            self.result_label.setText(resultado)

        except ValueError:
            # Se houver um erro de entrada, mostrar uma mensagem
            QMessageBox.warning(self, "Erro", "Por favor, insira valores válidos para as notas.")

# Rodar a aplicação
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = NotasApp()
    janela.show()
    sys.exit(app.exec())
