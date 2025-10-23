from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar, QTextEdit, QHBoxLayout, QWidget
import os
import shutil
import configparser

class CopiarFotosDialog(QDialog):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setWindowTitle("Copiar Fotos com Placas")
        self.setMinimumWidth(400)
        self.config_file = os.path.join(os.path.dirname(__file__), "config.ini")
        self.initUI()
        self.load_config()

    def initUI(self):
        layout = QVBoxLayout()

        self.origem_btn = QPushButton("Selecionar Pasta de Origem")
        self.origem_btn.clicked.connect(self.set_pasta_origem)
        self.origem_label = QLabel("")
        layout.addWidget(self.origem_btn)
        layout.addWidget(self.origem_label)

        self.destino_btn = QPushButton("Selecionar Pasta de Destino")
        self.destino_btn.clicked.connect(self.set_pasta_destino)
        self.destino_label = QLabel("")
        layout.addWidget(self.destino_btn)
        layout.addWidget(self.destino_label)

        self.placa_input = QLineEdit()
        self.placa_input.setPlaceholderText("Digite o código da placa (ex: R-1)")
        layout.addWidget(QLabel("Classe da Placa:"))
        layout.addWidget(self.placa_input)

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        self.copy_btn = QPushButton("Iniciar Cópia")
        self.copy_btn.clicked.connect(self.iniciar_copia)
        layout.addWidget(self.copy_btn)

        self.setLayout(layout)

    def set_pasta_origem(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecione a pasta de origem")
        if pasta:
            self.pasta_origem = pasta
            self.origem_label.setText(pasta)
            self.save_config()

    def set_pasta_destino(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecione a pasta de destino")
        if pasta:
            self.pasta_destino = pasta
            self.destino_label.setText(pasta)
            self.save_config()

    def iniciar_copia(self):
        try:
            layer = self.iface.activeLayer()
            if not layer:
                raise Exception("Nenhuma camada ativa.")

            selecionadas = layer.selectedFeatures()
            if not selecionadas:
                raise Exception("Nenhuma feição selecionada.")

            campo_foto = 'Name'  # pode ser alterado se o campo tiver outro nome
            nome_placa = self.placa_input.text().strip()
            if not nome_placa:
                raise Exception("Digite o nome da placa (ex: R-1).")

            destino_final = os.path.join(self.pasta_destino, nome_placa)
            os.makedirs(destino_final, exist_ok=True)

            self.progress_bar.setMaximum(len(selecionadas))
            self.progress_bar.setValue(0)
            self.log_box.clear()

            copiados = 0
            for i, feat in enumerate(selecionadas):
                nome_foto = feat[campo_foto]
                caminho_foto = os.path.join(self.pasta_origem, nome_foto)
                if os.path.exists(caminho_foto):
                    shutil.copy(caminho_foto, destino_final)
                    self.log_box.append(f"✅ Copiado: {nome_foto}")
                    copiados += 1
                else:
                    self.log_box.append(f"⚠️ Não encontrado: {nome_foto}")
                self.progress_bar.setValue(i + 1)

            QMessageBox.information(self, "Concluído", f"{copiados} fotos copiadas para {destino_final}")
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    def load_config(self):
        if os.path.exists(self.config_file):
            config = configparser.ConfigParser()
            config.read(self.config_file)
            if 'paths' in config:
                self.pasta_origem = config['paths'].get('origem', '')
                self.pasta_destino = config['paths'].get('destino', '')
                self.origem_label.setText(self.pasta_origem)
                self.destino_label.setText(self.pasta_destino)

    def save_config(self):
        config = configparser.ConfigParser()
        config['paths'] = {
            'origem': getattr(self, 'pasta_origem', ''),
            'destino': getattr(self, 'pasta_destino', '')
        }
        with open(self.config_file, 'w') as f:
            config.write(f)