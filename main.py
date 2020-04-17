from GLWidget import GLWidget
from PyQt5 import QtWidgets

import sys

from PythonUI.MainUI import Ui_main_window


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()

        self.ui.setupUi(self)

        self.glGeometry = self.ui.opengl_widget.geometry()
        self.glObjectName = self.ui.opengl_widget.objectName()
        self.glWidget = GLWidget(self.ui.centralwidget)
        self.glWidget.setGeometry(self.glGeometry)
        self.glWidget.setObjectName(self.glObjectName)

        self.ui.box_button.clicked.connect(lambda: self.glWidget.setObject('box'))
        self.ui.sphere_button.clicked.connect(lambda: self.glWidget.setObject('sphere', r=1, step=100))
        self.ui.pyramid_button.clicked.connect(lambda: self.glWidget.setObject('pyramid'))
        self.ui.thor_button.clicked.connect(lambda: self.glWidget.setObject('thor', ir=0.5, step=100))
        self.ui.cylinder_button.clicked.connect(lambda: self.glWidget.setObject('cylinder', r=1, h=0.5, step=100))
        self.ui.csg_button.clicked.connect(lambda: self.glWidget.setObject('csg', operation='a_or_b'))
        self.ui.reset_button.clicked.connect(self.glWidget.resetPosition)

        self.ui.mouse_wheel_check_box.clicked.connect(
            lambda: self.glWidget.setMouseWheelInvertion(self.ui.mouse_wheel_check_box.isChecked()))
        self.ui.mouse_wheel_slider.sliderReleased.connect(
            lambda: self.glWidget.setMouseWheelSensitivity(10 - (self.ui.mouse_wheel_slider.value()) // 10))
        self.ui.rotation_slider.sliderReleased.connect(
            lambda: self.glWidget.setRotationSensitivity(10 - (self.ui.rotation_slider.value()) // 10))
        self.ui.lighting_checkbox.clicked.connect(
            lambda: self.glWidget.setGLlighting(self.ui.lighting_checkbox.isChecked()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
