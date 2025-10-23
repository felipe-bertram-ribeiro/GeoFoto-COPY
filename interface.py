from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout, QHBoxLayout, QMessageBox
import os
import shutil

class CopiarFotosWindow(QWidget):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setWindowTitle("Copiar Fotos de Placas")
        self.resize(400, 200)

        self.label_origem = QLabel("Pasta de Origem:")
        self.input_origem = QLineEdit()
        self.btn_origem = QPushButton("Selecionar")

        self.label_destino = QLabel("Pasta de Destino:")
        self.input_destino = QLineEdit()
        self.btn_destino = QPushButton("Selecionar")

        self.btn_iniciar = QPushButton("Iniciar Cópia")

        layout = QVBoxLayout()

        origem_layout = QHBoxLayout()
        origem_layout.addWidget(self.input_origem)
        origem_layout.addWidget(self.btn_origem)

        destino_layout = QHBoxLayout()
        destino_layout.addWidget(self.input_destino)
        destino_layout.addWidget(self.btn_destino)

        layout.addWidget(self.label_origem)
        layout.addLayout(origem_layout)
        layout.addWidget(self.label_destino)
        layout.addLayout(destino_layout)
        layout.addWidget(self.btn_iniciar)

        self.setLayout(layout)

        self.btn_origem.clicked.connect(self.selecionar_origem)
        self.btn_destino.clicked.connect(self.selecionar_destino)
        self.btn_iniciar.clicked.connect(self.iniciar_copia)

    def selecionar_origem(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecionar Pasta de Origem")
        if pasta:
            self.input_origem.setText(pasta)

    def selecionar_destino(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecionar Pasta de Destino")
        if pasta:
            self.input_destino.setText(pasta)

    def iniciar_copia(self):
        origem = self.input_origem.text()
        destino = self.input_destino.text()

        if not origem or not destino:
            QMessageBox.warning(self, "Erro", "Preencha os dois caminhos!")
            return

        if not os.path.exists(destino):
            os.makedirs(destino)

        layer = self.iface.activeLayer()
        if not layer:
            QMessageBox.warning(self, "Erro", "Nenhuma camada ativa.")
            return

        copiados = 0
        for feat in layer.selectedFeatures():
            nome = feat['Name']
            caminho = os.path.join(origem, nome)
            if os.path.exists(caminho):
                shutil.copy(caminho, destino)
                copiados += 1
            else:
                print(f"⚠️ Não encontrado: {nome}")

        QMessageBox.information(self, "Concluído", f"{copiados} fotos copiadas!")
