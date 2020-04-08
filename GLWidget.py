from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint, Qt, pyqtSignal

import math

class GLWidget(QtWidgets.QOpenGLWidget):
    xRotationChanged = pyqtSignal(int)
    yRotationChanged = pyqtSignal(int)
    zRotationChanged = pyqtSignal(int)
    orthoChanged = pyqtSignal(float)

    def __init__(self, parent):
        # super(GLWidget, self).__init__(parent)
        self.objects = {
            'box': self.makeBox,
            'sphere': self.makeSphere,
            'pyramid': self.makePyramid,
            'thor': self.makeThor,
            'cylinder': self.makeCylinder
        }
        QtWidgets.QOpenGLWidget.__init__(self, parent)
        # Positioning
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.orthoSize = 1

        self.invertedWheel = False
        self.mouseWheelSensitivity = 5
        self.rotationSensitivity = 5

        self.GLlighting = False

        self.lastPos = QPoint()

        self.object = None

    def setGLlighting(self, value: bool) -> None:
        self.GLlighting = value
        self.update()

    def setMouseWheelInvertion(self, value: bool) -> None:
        self.invertedWheel = value

    def setMouseWheelSensitivity(self, value: int) -> None:
        self.mouseWheelSensitivity = value

    def setRotationSensitivity(self, value: int) -> None:
        self.rotationSensitivity = value

    def getObjectsNames(self):
        return self.objects.keys()

    def setObject(self, objectName, **kwargs):
        if objectName == 'sphere':
            r = kwargs['r']
            step = kwargs['step']
            self.object = self.objects[objectName](r, step)
        elif objectName == 'thor':
            ir = kwargs['ir']
            step = kwargs['step']
            self.object = self.objects[objectName](ir, step)
        elif objectName == 'cylinder':
            r = kwargs['r']
            h = kwargs['h']
            step = kwargs['step']
            self.object = self.objects[objectName](r, h, step)
        else:
            self.object = self.objects[objectName]()
        self.update()

    def makeBox(self):
        drawBoxList = glGenLists(1)
        glNewList(drawBoxList, GL_COMPILE)
        # Front
        glBegin(GL_POLYGON)
        glNormal(0, 0, -1)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, -0.5, -0.5)
        glEnd()

        # Back
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glNormal(0, 0, 1)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glEnd()
        #
        # Right
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 1.0)
        glNormal(1, 0, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glEnd()
        #
        # Left
        glBegin(GL_POLYGON)
        glColor3f(0.0, 1.0, 0.0)
        glNormal(-1, 0, 0)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()
        #
        # Top
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 1.0)
        glNormal(0, 1, 0)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, -0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glEnd()
        #
        # Bottom
        glBegin(GL_POLYGON)
        glNormal(0, -1, 0)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glEnd()
        glEndList()

        return drawBoxList

    def makeSphere(self, r, step):
        drawSphereList = glGenLists(1)
        glNewList(drawSphereList, GL_COMPILE)
        for i in range(step + 1):
            lat0 = math.pi * (-0.5 + i - 1 / step)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)

            lat1 = math.pi * (-0.5 + i / step)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)
            glBegin(GL_QUAD_STRIP)
            for j in range(step + 1):
                lng = 2 * math.pi * (j - 1) / step
                x = math.cos(lng)
                y = math.sin(lng)
                glNormal3f(x * zr0, y * zr0, z0)
                glColor3f(i % 2, 1, 0)
                glVertex3f(r * x * zr0, r * y * zr0, r * z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glColor3f(1, j % 2, 0)
                glVertex3f(r * x * zr1, r * y * zr1, r * z1)
            glEnd()
        glEndList()
        return drawSphereList

    def makeThor(self, internal_radius, step):
        drawThorList = glGenLists(1)
        glNewList(drawThorList, GL_COMPILE)
        for i in range(step + 1):
            glBegin(GL_QUAD_STRIP)
            for j in range(step + 1):
                k = 1
                while k >= 0:
                    s = (i + k) % step + 0.5
                    t = j % step
                    radius = 1 - internal_radius
                    x = (1 + radius * math.cos(s * 2 * math.pi / step)) * math.sin(t * 2 * math.pi / step)
                    y = (1 + radius * math.cos(s * 2 * math.pi / step)) * math.cos(t * 2 * math.pi / step)
                    z = radius * math.sin(s * 2 * math.pi / step)
                    glNormal(x, y, z)
                    glVertex3f(x, y, z)
                    k -= 1
            glEnd()
        glEndList()
        return drawThorList

    def makePyramid(self):
        drawPyramidList = glGenLists(1)
        glNewList(drawPyramidList, GL_COMPILE)
        # Face 1
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 1.0)
        glNormal(0, 0.5, 0.5)
        glVertex3f(0.5, 0.5, 0)
        glVertex3f(-0.5, 0.5, 0)
        glVertex3f(0, 0, 0.5)
        glEnd()
        #
        # Face 2
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glNormal(-0.5, 0, 0.5)
        glVertex3f(-0.5, 0.5, 0)
        glVertex3f(-0.5, -0.5, 0)
        glVertex3f(0, 0, 0.5)
        glEnd()
        #
        # Face 3
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 1.0)
        glNormal(0, -0.5, 0.5)
        glVertex3f(-0.5, -0.5, 0)
        glVertex3f(0.5, -0.5, 0)
        glVertex3f(0, 0, 0.5)
        glEnd()
        #
        # Face 4
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.5, 1.0)
        glNormal(0.5, 0, 0.5)
        glVertex3f(0.5, -0.5, 0)
        glVertex3f(0.5, 0.5, 0)
        glVertex3f(0, 0, 0.5)
        glEnd()
        #
        # Bottom
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glNormal(0, 0, -1)
        glVertex3f(-0.5, -0.5, 0.0)
        glVertex3f(0.5, -0.5, 0.0)
        glVertex3f(0.5, 0.5, 0.0)
        glVertex3f(-0.5, 0.5, 0.0)
        glEnd()
        glEndList()
        return drawPyramidList

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self.GLlighting:
            glEnable(GL_LIGHTING)
            glEnable(GL_LIGHT0)
            glEnable(GL_COLOR_MATERIAL)

            glShadeModel(GL_SMOOTH)
            #TODO ShadeModel checkbox

            glMaterialfv(GL_FRONT, GL_SPECULAR, 1, 1, 1, 1)
            glMaterialfv(GL_FRONT, GL_SHININESS, 50)
            glLightfv(GL_LIGHT0, GL_POSITION, 0.5, -1, -0.2, 0)

            # glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
            # glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
            # glLightfv(GL_LIGHT0, GL_DIFFUSE, 0.7, 0.7, 0.7)
            # glLightfv(GL_LIGHT0, GL_AMBIENT, 0.1, 0.1, 0.1)
            # # glLightfv(GL_LIGHT0, GL_SPECULAR, 0.1, 0.1, 0.1)
            # # glLightfv(GL_LIGHT0, GL_POSITION, 0, 1.5, 1, 0)
            # # glLightf(GL_LIGHT0, GL_AMBIENT, 0, 0, 0, 1)
            # # glLightf(GL_LIGHT0, GL_DIFFUSE, 1, 1, 1, 1)
            # # glLightf(GL_LIGHT0, GL_SPECULAR, 1, 1, 1, 1)
            # # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, 0.2, 0.2, 0.2, 1)
            # # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, 1, 1, 1, 1)
            # # glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, 0, 0, 0, 1)
        else:
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            glDisable(GL_COLOR_MATERIAL)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.orthoSize, +self.orthoSize, +self.orthoSize, -self.orthoSize, 2.0, 15.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # glOrtho(-self.orthoSize, +self.orthoSize, +self.orthoSize, -self.orthoSize, 2.0, 15.0)
        # glTranslatef(-2.5, 0.5, -6.0)
        glTranslated(0.0, 0.0, -10.0)
        glColor3f(1.0, 1.5, 0.0)

        glRotated(self.xRot / self.rotationSensitivity, 1.0, 0.0, 0.0)
        glRotated(self.yRot / self.rotationSensitivity, 0.0, 1.0, 0.0)
        glRotated(self.zRot / self.rotationSensitivity, 0.0, 0.0, 1.0)

        glCallList(self.object)

        # glFlush()

    def makeCylinder(self, radius: float, height: float, step: int):
        step = 1 / step
        drawCylinderList = glGenLists(1)
        glNewList(drawCylinderList, GL_COMPILE)
        # Draw the tube
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUAD_STRIP)
        angle = 0
        while angle < 2 * math.pi:
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glNormal3f(x, y, height // 2)
            glVertex3f(x, y, height // 2)
            glNormal3f(x, y, -height // 2)
            glVertex3f(x, y, -height // 2)
            angle += step
        glVertex3f(radius, 0, height // 2)
        glVertex3f(radius, 0, -height // 2)
        glEnd()
        # Draw the circles
        glColor3f(1, 0.5, 0.5)
        glBegin(GL_POLYGON)
        angle = 0
        while angle < 2 * math.pi:
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glNormal3f(x, y, height // 2)
            glVertex3f(x, y, height // 2)
            angle += step
        glVertex3f(radius, 0, height // 2)
        glEnd()
        glBegin(GL_POLYGON)
        angle = 0
        while angle < 2 * math.pi:
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glNormal3f(x, y, -height // 2)
            glVertex3f(x, y, -height // 2)
            angle += step
        glVertex3f(radius, 0, -height // 2)
        glEnd()
        glEndList()

        return drawCylinderList

    def resetPosition(self) -> None:
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.orthoSize = 1
        self.update()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.orthoSize, +self.orthoSize, +self.orthoSize, -self.orthoSize, 2.0, 15.0)
        glMatrixMode(GL_MODELVIEW)

    def initializeGL(self):
        self.setObject('cylinder', r=0.5, h=1, step=100)
        # self.object = self.objects['box']()
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.width(), self.height())
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, self.width() / self.height(), 0.1, 100.0)

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & Qt.LeftButton:
            self.setXRotation(self.xRot + dy)
            self.setYRotation(self.yRot + dx)
        elif event.buttons() & Qt.RightButton:
            self.setXRotation(self.xRot + dy)
            self.setZRotation(self.zRot + dx)

    def mousePressEvent(self, event):
        self.lastPos = event.pos()

    def wheelEvent(self, event):
        delta = event.angleDelta().y() / (120 * self.mouseWheelSensitivity)
        delta = -delta if self.invertedWheel else delta
        print(f'Wheel: {delta}')
        self.setOrtho(self.orthoSize + delta)

    def setOrtho(self, value):
        value = self.normalizeOrtho(value)
        if value != self.orthoSize:
            self.orthoSize = value
            # self.orthoChanged.emit(value)
            self.update()
            print(value)

    def normalizeOrtho(self, value):
        if value < 0.05:
            return 0.05
        if value > 2:
            return 2
        return value

    def print_angles(self):
        print(f'X: {self.xRot}\t'
              f'Y: {self.yRot}\t'
              f'Z: {self.zRot}\t')

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.update()
        self.print_angles()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.update()
        self.print_angles()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.update()
        self.print_angles()

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle