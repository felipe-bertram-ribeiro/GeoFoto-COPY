from PyQt5.QtWidgets import QAction, QMessageBox
from .dialog import CopiarFotosDialog

class CopiarFotosPlacasPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction("Copiar Fotos com Placas", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("Copiar Fotos com Placas", self.action)

    def unload(self):
        self.iface.removePluginMenu("Copiar Fotos com Placas", self.action)

    def run(self):
        dlg = CopiarFotosDialog(self.iface)
        dlg.exec_()