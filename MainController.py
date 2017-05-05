from PySide import QtGui

class MainController(object):

    def __init__(self,model):
        self.model = model

    def change_mode(self,mode_name):
        self.model.mode = mode
        self.model.update()

    def stop_running(self):
        self.model.mode.stop_modus()

    def start_running(self):
        self.model.mode.running=True
        self.model.mode.start_mode()
        self.model.update()

    def preview(self):
        self.model.mode.preview()
