from qgis.PyQt.QtWidgets import QAction
from .interface import CopiarFotosWindow

class CopiarFotosPlacas:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.window = None

    def initGui(self):
        self.action = QAction("Copiar Fotos com Placas", self.iface.mainWindow())
        self.action.triggered.connect(self.show_window)
        self.iface.addPluginToMenu("Copiar Fotos", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("Copiar Fotos", self.action)
        self.iface.removeToolBarIcon(self.action)

    def show_window(self):
        self.window = CopiarFotosWindow(self.iface)
        self.window.show()
