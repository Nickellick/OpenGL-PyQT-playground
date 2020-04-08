# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        main_window.setMinimumSize(QtCore.QSize(800, 600))
        main_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.opengl_widget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.opengl_widget.setGeometry(QtCore.QRect(0, 0, 520, 520))
        self.opengl_widget.setObjectName("opengl_widget")
        self.box_button = QtWidgets.QPushButton(self.centralwidget)
        self.box_button.setGeometry(QtCore.QRect(10, 530, 89, 25))
        self.box_button.setObjectName("box_button")
        self.sphere_button = QtWidgets.QPushButton(self.centralwidget)
        self.sphere_button.setGeometry(QtCore.QRect(110, 530, 89, 25))
        self.sphere_button.setObjectName("sphere_button")
        self.pyramid_button = QtWidgets.QPushButton(self.centralwidget)
        self.pyramid_button.setGeometry(QtCore.QRect(210, 530, 89, 25))
        self.pyramid_button.setObjectName("pyramid_button")
        self.thor_button = QtWidgets.QPushButton(self.centralwidget)
        self.thor_button.setGeometry(QtCore.QRect(310, 530, 89, 25))
        self.thor_button.setObjectName("thor_button")
        self.cylinder_button = QtWidgets.QPushButton(self.centralwidget)
        self.cylinder_button.setGeometry(QtCore.QRect(410, 530, 89, 25))
        self.cylinder_button.setObjectName("cylinder_button")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(530, 10, 89, 25))
        self.reset_button.setObjectName("reset_button")
        self.mous_wheel_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.mous_wheel_check_box.setGeometry(QtCore.QRect(630, 10, 171, 23))
        self.mous_wheel_check_box.setObjectName("mous_wheel_check_box")
        self.mouse_wheel_slider = QtWidgets.QSlider(self.centralwidget)
        self.mouse_wheel_slider.setGeometry(QtCore.QRect(530, 70, 261, 16))
        self.mouse_wheel_slider.setMaximum(100)
        self.mouse_wheel_slider.setSingleStep(10)
        self.mouse_wheel_slider.setTracking(True)
        self.mouse_wheel_slider.setOrientation(QtCore.Qt.Horizontal)
        self.mouse_wheel_slider.setObjectName("mouse_wheel_slider")
        self.mouse_wheel_label = QtWidgets.QLabel(self.centralwidget)
        self.mouse_wheel_label.setGeometry(QtCore.QRect(530, 40, 171, 21))
        self.mouse_wheel_label.setObjectName("mouse_wheel_label")
        self.rotation_label = QtWidgets.QLabel(self.centralwidget)
        self.rotation_label.setGeometry(QtCore.QRect(530, 90, 141, 21))
        self.rotation_label.setObjectName("rotation_label")
        self.rotation_slider = QtWidgets.QSlider(self.centralwidget)
        self.rotation_slider.setGeometry(QtCore.QRect(530, 120, 261, 16))
        self.rotation_slider.setMinimum(0)
        self.rotation_slider.setMaximum(100)
        self.rotation_slider.setSingleStep(10)
        self.rotation_slider.setProperty("value", 0)
        self.rotation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.rotation_slider.setInvertedAppearance(False)
        self.rotation_slider.setObjectName("rotation_slider")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "OpenGL PyQT Playground"))
        self.box_button.setText(_translate("main_window", "Box"))
        self.sphere_button.setText(_translate("main_window", "Sphere"))
        self.pyramid_button.setText(_translate("main_window", "Pyramid"))
        self.thor_button.setText(_translate("main_window", "Thor"))
        self.cylinder_button.setText(_translate("main_window", "Cylinder"))
        self.reset_button.setText(_translate("main_window", "Reset"))
        self.mous_wheel_check_box.setText(_translate("main_window", "Invert Mouse Wheel"))
        self.mouse_wheel_label.setText(_translate("main_window", "Mouse Wheel Sensitivity"))
        self.rotation_label.setText(_translate("main_window", "Rotation Sensitivity"))
