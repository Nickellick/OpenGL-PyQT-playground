from PyQt5.QtCore import QEvent
from PyQt5.QtGui import (QGuiApplication, QMatrix4x4, QOpenGLContext,
        QOpenGLShader, QOpenGLShaderProgram, QSurfaceFormat, QWindow)

from PythonUI.MainUI import Ui_main_window

if __name__ == '__main__':

    import sys

    app = QGuiApplication(sys.argv)

    format = QSurfaceFormat()
    format.setSamples(4)

    window = Ui_main_window()
    window.setFormat(format)
    window.show()

    window.setAnimating(True)

    sys.exit(app.exec_())