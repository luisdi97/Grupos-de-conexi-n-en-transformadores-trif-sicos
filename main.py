from PyQt5 import QtCore, QtGui, QtWidgets
import math
import cmath

resize_1 = False
resize_2 = False

def mag_ang(mag, ang_deg):
    ang_rad = ang_deg*math.pi/180
    out = mag*(math.cos(ang_rad) + 1j*math.sin(ang_rad))
    return out

def rango_360_ang(ang):
    while(ang<0 or ang>=360):
        if(ang<0):
            ang += 360
        elif(ang>=360):
            ang -= 360
    return ang

class MyMainWindow(QtWidgets.QMainWindow):
    def resizeEvent(self, event):
        if(resize_1):
            ui.graphicsView.fitInView(ui.scene_1.sceneRect().adjusted(0,0,10,20),QtCore.Qt.KeepAspectRatio)
        if(resize_2):
            ui.graphicsView_2.fitInView(ui.scene_2.sceneRect().adjusted(0,0,10,20),QtCore.Qt.KeepAspectRatio)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout.addWidget(self.comboBox_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(
            lambda: self.button_click(MainWindow)
            )
        
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        
        self.scene_1 = QtWidgets.QGraphicsScene()        
        
        '''
        1 Primario
        '''
        
        self.scene_1.clear()
        
        font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
        
        item_1 = self.scene_1.addText("L1", font=font_used)
        pos = QtCore.QPointF(71,20)
        item_1.setPos(pos-item_1.boundingRect().center())
        
        item_2 = self.scene_1.addText("L2", font=font_used)
        pos = QtCore.QPointF(71,40)
        item_2.setPos(pos-item_2.boundingRect().center())
        
        item_3 = self.scene_1.addText("L3", font=font_used)
        pos = QtCore.QPointF(71,60)
        item_3.setPos(pos-item_3.boundingRect().center())
        
        pen_used = QtGui.QPen()
        
        pen_used.setWidth(3)
        
        self.scene_1.addLine (87, 20, 363, 20, pen=pen_used)
        self.scene_1.addLine (87, 40, 363, 40, pen=pen_used)
        self.scene_1.addLine (87, 60, 363, 60, pen=pen_used)
        
        self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        
        self.scene_1.addLine (132, 20, 132, 268, pen=pen_used)
        self.scene_1.addLine (225, 40, 225, 268, pen=pen_used)
        self.scene_1.addLine (318, 60, 318, 268, pen=pen_used)
        
        self.scene_1.addLine (132, 268, 318, 268, pen=pen_used)
        
        self.scene_1.addEllipse(106-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_1.addEllipse(200-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_1.addEllipse(292-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        
        item_4 = self.scene_1.addText("A", font=font_used)
        pos = QtCore.QPointF(104,176)
        item_4.setPos(pos-item_4.boundingRect().center())
        
        item_5 = self.scene_1.addText("B", font=font_used)
        pos = QtCore.QPointF(200,176)
        item_5.setPos(pos-item_5.boundingRect().center())
        
        item_6 = self.scene_1.addText("C", font=font_used)
        pos = QtCore.QPointF(292,176)
        item_6.setPos(pos-item_6.boundingRect().center())
        
        self.scene_1.addRect(115, 116, 33, 120,
                              pen=QtGui.QPen(QtGui.QColor("red")),
                              brush=QtGui.QBrush(QtGui.QColor("red"))
                              )
        
        self.scene_1.addRect(208, 116, 33, 120,
                              pen=QtGui.QPen(QtGui.QColor("green")),
                              brush=QtGui.QBrush(QtGui.QColor("green"))
                              )
        
        self.scene_1.addRect(302, 116, 33, 120,
                              pen=QtGui.QPen(QtGui.QColor("blue")),
                              brush=QtGui.QBrush(QtGui.QColor("blue"))
                              )
        
        self.graphicsView.setScene(self.scene_1)
        global resize_1
        resize_1 = True
        
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        
        self.scene_2 = QtWidgets.QGraphicsScene()        
        
        '''
        1 Secundario
        '''
        
        self.scene_2.clear()
        
        pen_used = QtGui.QPen()
        
        pen_used.setWidth(3)
        
        self.scene_2.addLine (132, 17, 318, 17, pen=pen_used)
        
        self.scene_2.addLine (132, 17, 132, 224, pen=pen_used)
        self.scene_2.addLine (225, 17, 225, 244, pen=pen_used)
        self.scene_2.addLine (318, 17, 318, 264, pen=pen_used)        
        
        font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
        
        item_4 = self.scene_2.addText("a", font=font_used)
        pos = QtCore.QPointF(104,109)
        item_4.setPos(pos-item_4.boundingRect().center())
        
        item_5 = self.scene_2.addText("b", font=font_used)
        pos = QtCore.QPointF(198,109)
        item_5.setPos(pos-item_5.boundingRect().center())
        
        item_6 = self.scene_2.addText("c", font=font_used)
        pos = QtCore.QPointF(292,109)
        item_6.setPos(pos-item_6.boundingRect().center())
        
        self.scene_2.addEllipse(106-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_2.addEllipse(200-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_2.addEllipse(292-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        
        self.scene_2.addRect(115, 50, 33, 120,
                              pen=QtGui.QPen(QtGui.QColor("red")),
                              brush=QtGui.QBrush(QtGui.QColor("red"))
                              )
        
        self.scene_2.addRect(208, 50, 33, 120,
                              pen=QtGui.QPen(QtGui.QColor("green")),
                              brush=QtGui.QBrush(QtGui.QColor("green"))
                              )
        
        self.scene_2.addRect(302, 50, 33, 120,
                              pen=QtGui.QPen(QtGui.QColor("blue")),
                              brush=QtGui.QBrush(QtGui.QColor("blue"))
                              )
        
        item_1 = self.scene_2.addText("l1", font=font_used)
        pos = QtCore.QPointF(72,225)
        item_1.setPos(pos-item_1.boundingRect().center())
        
        item_2 = self.scene_2.addText("l2", font=font_used)
        pos = QtCore.QPointF(72,245)
        item_2.setPos(pos-item_2.boundingRect().center())
        
        item_3 = self.scene_2.addText("l3", font=font_used)
        pos = QtCore.QPointF(72,265)
        item_3.setPos(pos-item_3.boundingRect().center())
        
        self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
        self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
        self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
        
        self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
        
        self.graphicsView_2.setScene(self.scene_2)
        global resize_2
        resize_2 = True
        
        self.verticalLayout_3.addWidget(self.graphicsView_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMaximumSize(QtCore.QSize(250, 250))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("Horas/0.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMaximumSize(QtCore.QSize(300, 300))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Estrella-Estrella_Delta-Delta.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        MainWindow.setWindowTitle("Grupos de conexión en transformadores trifásicos")
        self.label.setText("Grupos de conexión en transformadores trifásicos")
        self.label_7.setText("Secuencia")
        self.comboBox_5.setItemText(0, "Positiva")
        self.comboBox_5.setItemText(1, "Negativa")
        self.label_11.setText("Alimentación")
        self.comboBox.setItemText(0, "1 2 3")
        self.comboBox.setItemText(1, "1 3 2")
        self.comboBox.setItemText(2, "2 1 3")
        self.comboBox.setItemText(3, "2 3 1")
        self.comboBox.setItemText(4, "3 2 1")
        self.comboBox.setItemText(5, "3 1 2")
        self.label_8.setText( "Conexión primario")
        self.comboBox_2.setItemText(0, "Estrella 1")
        self.comboBox_2.setItemText(1, "Estrella 2")
        self.comboBox_2.setItemText(2, "Delta 1")
        self.comboBox_2.setItemText(3, "Delta 2")
        self.label_9.setText("Conexión secundario")
        self.comboBox_3.setItemText(0, "Estrella 1")
        self.comboBox_3.setItemText(1, "Estrella 2")
        self.comboBox_3.setItemText(2, "Delta 1")
        self.comboBox_3.setItemText(3, "Delta 2")
        self.comboBox_3.setItemText(4, "Zig-Zag 1")
        self.comboBox_3.setItemText(5, "Zig-Zag 2")
        self.comboBox_3.setItemText(6, "Zig-Zag 3")
        self.comboBox_3.setItemText(7, "Zig-Zag 4")
        self.label_10.setText("Salida")
        self.comboBox_6.setItemText(0, "1 2 3")
        self.comboBox_6.setItemText(1, "1 3 2")
        self.comboBox_6.setItemText(2, "2 1 3")
        self.comboBox_6.setItemText(3, "2 3 1")
        self.comboBox_6.setItemText(4, "3 2 1")
        self.comboBox_6.setItemText(5, "3 1 2")
        self.pushButton.setText("Ejecutar")
        self.label_2.setText("Primario")
        self.label_3.setText("Secundario")
        self.label_4.setText("Grupo de conexión")
        self.label_5.setText("Yy0")
        self.label_6.setText("Relación de tensiones línea-línea")

    def button_click(self, MainWindow):
        self.comboBox_3.currentText()        
        
        '''
        Secuencia
        '''
        
        if self.comboBox_5.currentText() == "Positiva":
            secuencia = 1
        elif self.comboBox_5.currentText() == "Negativa":
            secuencia = 2
        
        '''
        Alimentación
        '''
        
        if self.comboBox.currentText() == "1 2 3":
            alimentacion = 1
        elif self.comboBox.currentText() == "1 3 2":
            alimentacion = 2
        elif self.comboBox.currentText() == "2 1 3":
            alimentacion = 3
        elif self.comboBox.currentText() == "2 3 1":
            alimentacion = 4
        elif self.comboBox.currentText() == "3 2 1":
            alimentacion = 5
        elif self.comboBox.currentText() == "3 1 2":
            alimentacion = 6
            
        '''
        Conexión primario
        '''
        
        if self.comboBox_2.currentText() == "Estrella 1":
            primario = 1
        elif self.comboBox_2.currentText() == "Estrella 2":
            primario = 2
        elif self.comboBox_2.currentText() == "Delta 1":
            primario = 3
        elif self.comboBox_2.currentText() == "Delta 2":
            primario = 4
        
        '''
        Conexión secundario
        '''
        
        if self.comboBox_3.currentText() == "Estrella 1":
            secundario = 1
        elif self.comboBox_3.currentText() == "Estrella 2":
            secundario = 2
        elif self.comboBox_3.currentText() == "Delta 1":
            secundario = 3
        elif self.comboBox_3.currentText() == "Delta 2":
            secundario = 4
        elif self.comboBox_3.currentText() == "Zig-Zag 1":
            secundario = 5
        elif self.comboBox_3.currentText() == "Zig-Zag 2":
            secundario = 6
        elif self.comboBox_3.currentText() == "Zig-Zag 3":
            secundario = 7
        elif self.comboBox_3.currentText() == "Zig-Zag 4":
            secundario = 8
        
        '''
        Salida
        '''
        
        if self.comboBox_6.currentText() == "1 2 3":
            salida = 1
        elif self.comboBox_6.currentText() == "1 3 2":
            salida = 2
        elif self.comboBox_6.currentText() == "2 1 3":
            salida = 3
        elif self.comboBox_6.currentText() == "2 3 1":
            salida = 4
        elif self.comboBox_6.currentText() == "3 2 1":
            salida = 5
        elif self.comboBox_6.currentText() == "3 1 2":
            salida = 6
        
        '''
        Inicio del cálculo del grupo de conexión
        '''

        if secuencia == 1:
            V1 = mag_ang(1,0)
            V2 = mag_ang(1,-120)
            V3 = mag_ang(1,120)
            
        elif secuencia == 2:
            V1 = mag_ang(1,0)
            V2 = mag_ang(1,120)
            V3 = mag_ang(1,-120)



        if alimentacion == 1:
            VA = V1
            VB = V2
            VC = V3
            
        elif alimentacion == 2:
            VA = V1
            VB = V3
            VC = V2

        elif alimentacion == 3:
            VA = V2
            VB = V1
            VC = V3
            
        elif alimentacion == 4:
            VA = V2
            VB = V3
            VC = V1
            
        elif alimentacion == 5:
            VA = V3
            VB = V2
            VC = V1
            
        elif alimentacion == 6:
            VA = V3
            VB = V1
            VC = V2



        if primario == 1:
            VAAp = VA
            VBBp = VB
            VCCp = VC

            VApA = -VAAp
            VBpB = -VBBp
            VCpC = -VCCp

        elif primario == 2:
            VApA = VA
            VBpB = VB
            VCpC = VC

            VAAp = -VApA
            VBBp = -VBpB
            VCCp = -VCpC
            
        elif primario == 3:
            VAAp = VA - VC
            VBBp = VB - VA
            VCCp = VC - VB

            VApA = -VAAp
            VBpB = -VBBp
            VCpC = -VCCp
            
        elif primario == 4:
            VAAp = VA - VB
            VBBp = VB - VC
            VCCp = VC - VA

            VApA = -VAAp
            VBpB = -VBBp
            VCpC = -VCCp



        if secundario == 1:
            Vll = VAAp - VBBp

        elif secundario == 2:
            Vll = VApA - VBpB
            
        elif secundario == 3:
            Vll = VBpB
            
        elif secundario == 4:
            Vll = VAAp
            
        elif secundario == 5:
            Vll = (VBpB + VAAp) - (VCpC + VBBp)

        elif secundario == 6:
            Vll = (VCpC + VAAp) - (VApA + VBBp)
            
        elif secundario == 7:
            Vll = (VBBp + VApA) - (VCCp + VBpB)

        elif secundario == 8:
            Vll = (VCCp + VApA) - (VAAp + VBpB)



        if salida == 1:
            VLL = V1 - V2
            
        elif salida == 2:
            VLL = V1 - V3

        elif salida == 3:
            VLL = V2 - V1
            
        elif salida == 4:
            VLL = V2 - V3
            
        elif salida == 5:
            VLL = V3 - V2
            
        elif salida == 6:
            VLL = V3 - V1



        '''
        Índice Horario
        '''
        Theta_LL = cmath.phase(VLL)*180/math.pi
        Theta_ll = cmath.phase(Vll)*180/math.pi
        desfase = rango_360_ang(Theta_ll - Theta_LL)
        indice = int(round(desfase/30,1))
        
        # string = [secuencia, alimentacion, primario, secundario, salida]
        
        # for n in range(len(string)):
        #     print(string[n]) 

        # print("Índice horario es:"+str(indice))
        
        
        
        
        '''
        Dibujar primario
        '''
        
        if primario == 1:          
            self.scene_1.clear()
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_1 = self.scene_1.addText("L1", font=font_used)
            pos = QtCore.QPointF(71,20)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_1.addText("L2", font=font_used)
            pos = QtCore.QPointF(71,40)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_1.addText("L3", font=font_used)
            pos = QtCore.QPointF(71,60)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_1.addLine (87, 20, 363, 20, pen=pen_used)
            self.scene_1.addLine (87, 40, 363, 40, pen=pen_used)
            self.scene_1.addLine (87, 60, 363, 60, pen=pen_used)
            
            if alimentacion == 1:              
                self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 20, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 40, 225, 268, pen=pen_used)
                self.scene_1.addLine (318, 60, 318, 268, pen=pen_used)
            
            elif alimentacion == 2:
                self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 20, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 60, 225, 268, pen=pen_used)
                self.scene_1.addLine (318, 40, 318, 268, pen=pen_used)
            
            elif alimentacion == 3:
                self.scene_1.addEllipse(132-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 40, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 20, 225, 268, pen=pen_used)
                self.scene_1.addLine (318, 60, 318, 268, pen=pen_used)
            
            elif alimentacion == 4:
                self.scene_1.addEllipse(132-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 40, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 60, 225, 268, pen=pen_used)
                self.scene_1.addLine (318, 20, 318, 268, pen=pen_used)
            
            elif alimentacion == 5:                
                self.scene_1.addEllipse(132-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 60, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 40, 225, 268, pen=pen_used)
                self.scene_1.addLine (318, 20, 318, 268, pen=pen_used)
            
            elif alimentacion == 6:                
                self.scene_1.addEllipse(132-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 60, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 20, 225, 268, pen=pen_used)
                self.scene_1.addLine (318, 40, 318, 268, pen=pen_used)
            
            self.scene_1.addLine (132, 268, 318, 268, pen=pen_used)
            
            self.scene_1.addEllipse(106-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(200-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(292-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            item_4 = self.scene_1.addText("A", font=font_used)
            pos = QtCore.QPointF(104,176)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_1.addText("B", font=font_used)
            pos = QtCore.QPointF(200,176)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_1.addText("C", font=font_used)
            pos = QtCore.QPointF(292,176)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_1.addRect(115, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_1.addRect(208, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_1.addRect(302, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.graphicsView.setScene(self.scene_1)
            
        elif primario == 2:
            self.scene_1.clear()
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_1 = self.scene_1.addText("L1", font=font_used)
            pos = QtCore.QPointF(71,20)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_1.addText("L2", font=font_used)
            pos = QtCore.QPointF(71,40)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_1.addText("L3", font=font_used)
            pos = QtCore.QPointF(71,60)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_1.addLine (87, 20, 363, 20, pen=pen_used)
            self.scene_1.addLine (87, 40, 363, 40, pen=pen_used)
            self.scene_1.addLine (87, 60, 363, 60, pen=pen_used)
            
            if alimentacion == 1:              
                self.scene_1.addEllipse(112-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(205-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(298-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (112, 20, 112, 268, pen=pen_used)
                self.scene_1.addLine (205, 40, 205, 268, pen=pen_used)
                self.scene_1.addLine (298, 60, 298, 268, pen=pen_used)
            
            elif alimentacion == 2:
                self.scene_1.addEllipse(112-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(205-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(298-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (112, 20, 112, 268, pen=pen_used)
                self.scene_1.addLine (205, 60, 205, 268, pen=pen_used)
                self.scene_1.addLine (298, 40, 298, 268, pen=pen_used)
            
            elif alimentacion == 3:
                self.scene_1.addEllipse(112-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(205-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(298-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (112, 40, 112, 268, pen=pen_used)
                self.scene_1.addLine (205, 20, 205, 268, pen=pen_used)
                self.scene_1.addLine (298, 60, 298, 268, pen=pen_used)
            
            elif alimentacion == 4:
                self.scene_1.addEllipse(112-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(205-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(298-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (112, 40, 112, 268, pen=pen_used)
                self.scene_1.addLine (205, 60, 205, 268, pen=pen_used)
                self.scene_1.addLine (298, 20, 298, 268, pen=pen_used)
            
            elif alimentacion == 5:                
                self.scene_1.addEllipse(112-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(205-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(298-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (112, 60, 112, 268, pen=pen_used)
                self.scene_1.addLine (205, 40, 205, 268, pen=pen_used)
                self.scene_1.addLine (298, 20, 298, 268, pen=pen_used)
            
            elif alimentacion == 6:                
                self.scene_1.addEllipse(112-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(205-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(298-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (112, 60, 112, 268, pen=pen_used)
                self.scene_1.addLine (205, 20, 205, 268, pen=pen_used)
                self.scene_1.addLine (298, 40, 298, 268, pen=pen_used)
            
            self.scene_1.addLine (162, 83, 348, 83, pen=pen_used)
            
            self.scene_1.addLine (162, 83, 162, 268, pen=pen_used)
            self.scene_1.addLine (255, 83, 255, 268, pen=pen_used)
            self.scene_1.addLine (348, 83, 348, 268, pen=pen_used)
            
            self.scene_1.addLine (112, 268, 162, 268, pen=pen_used)
            self.scene_1.addLine (205, 268, 255, 268, pen=pen_used)
            self.scene_1.addLine (298, 268, 348, 268, pen=pen_used)
            
            self.scene_1.addEllipse(136-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(229-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(322-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            item_4 = self.scene_1.addText("A", font=font_used)
            pos = QtCore.QPointF(134,176)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_1.addText("B", font=font_used)
            pos = QtCore.QPointF(228,176)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_1.addText("C", font=font_used)
            pos = QtCore.QPointF(322,176)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_1.addRect(145, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_1.addRect(238, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_1.addRect(331, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.graphicsView.setScene(self.scene_1)
            
        elif primario == 3:            
            self.scene_1.clear()
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_1 = self.scene_1.addText("L1", font=font_used)
            pos = QtCore.QPointF(71,20)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_1.addText("L2", font=font_used)
            pos = QtCore.QPointF(71,40)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_1.addText("L3", font=font_used)
            pos = QtCore.QPointF(71,60)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_1.addLine (87, 20, 363, 20, pen=pen_used)
            self.scene_1.addLine (87, 40, 363, 40, pen=pen_used)
            self.scene_1.addLine (87, 60, 363, 60, pen=pen_used)
            
            if alimentacion == 1:              
                self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 20, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 40, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 60, 318, 251, pen=pen_used)
            
            elif alimentacion == 2:
                self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 20, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 60, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 40, 318, 251, pen=pen_used)
            
            elif alimentacion == 3:
                self.scene_1.addEllipse(132-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 40, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 20, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 60, 318, 251, pen=pen_used)
            
            elif alimentacion == 4:
                self.scene_1.addEllipse(132-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 40, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 60, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 20, 318, 251, pen=pen_used)
            
            elif alimentacion == 5:                
                self.scene_1.addEllipse(132-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 60, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 40, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 20, 318, 251, pen=pen_used)
            
            elif alimentacion == 6:                
                self.scene_1.addEllipse(132-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 60, 132, 268, pen=pen_used)
                self.scene_1.addLine (225, 20, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 40, 318, 251, pen=pen_used)
            
            self.scene_1.addLine (132, 100, 168, 100, pen=pen_used)
            self.scene_1.addLine (225, 100, 261, 100, pen=pen_used)
            self.scene_1.addLine (318, 100, 354, 100, pen=pen_used)
            
            self.scene_1.addLine (168, 100, 168, 251, pen=pen_used)
            self.scene_1.addLine (261, 100, 261, 251, pen=pen_used)
            self.scene_1.addLine (354, 100, 354, 268, pen=pen_used)
            
            self.scene_1.addLine (168, 251, 225, 251, pen=pen_used)
            self.scene_1.addLine (261, 251, 318, 251, pen=pen_used)        
            
            self.scene_1.addLine (132, 268, 354, 268, pen=pen_used)
            
            self.scene_1.addEllipse(106-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(200-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(292-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            item_4 = self.scene_1.addText("A", font=font_used)
            pos = QtCore.QPointF(104,176)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_1.addText("B", font=font_used)
            pos = QtCore.QPointF(200,176)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_1.addText("C", font=font_used)
            pos = QtCore.QPointF(292,176)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_1.addRect(115, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_1.addRect(208, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_1.addRect(302, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.graphicsView.setScene(self.scene_1)
            
        elif primario == 4:
            self.scene_1.clear()
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_1 = self.scene_1.addText("L1", font=font_used)
            pos = QtCore.QPointF(71,20)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_1.addText("L2", font=font_used)
            pos = QtCore.QPointF(71,40)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_1.addText("L3", font=font_used)
            pos = QtCore.QPointF(71,60)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_1.addLine (87, 20, 363, 20, pen=pen_used)
            self.scene_1.addLine (87, 40, 363, 40, pen=pen_used)
            self.scene_1.addLine (87, 60, 363, 60, pen=pen_used)
            
            if alimentacion == 1:              
                self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 20, 132, 251, pen=pen_used)
                self.scene_1.addLine (225, 40, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 60, 318, 268, pen=pen_used)
            
            elif alimentacion == 2:
                self.scene_1.addEllipse(132-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 20, 132, 251, pen=pen_used)
                self.scene_1.addLine (225, 60, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 40, 318, 268, pen=pen_used)
            
            elif alimentacion == 3:
                self.scene_1.addEllipse(132-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 40, 132, 251, pen=pen_used)
                self.scene_1.addLine (225, 20, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 60, 318, 268, pen=pen_used)
            
            elif alimentacion == 4:
                self.scene_1.addEllipse(132-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 40, 132, 251, pen=pen_used)
                self.scene_1.addLine (225, 60, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 20, 318, 268, pen=pen_used)
            
            elif alimentacion == 5:                
                self.scene_1.addEllipse(132-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 60, 132, 251, pen=pen_used)
                self.scene_1.addLine (225, 40, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 20, 318, 268, pen=pen_used)
            
            elif alimentacion == 6:                
                self.scene_1.addEllipse(132-5.5, 60-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(225-5.5, 20-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_1.addEllipse(318-5.5, 40-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_1.addLine (132, 60, 132, 251, pen=pen_used)
                self.scene_1.addLine (225, 20, 225, 251, pen=pen_used)
                self.scene_1.addLine (318, 40, 318, 268, pen=pen_used)
            
            self.scene_1.addLine (75, 100, 132, 100, pen=pen_used)
            self.scene_1.addLine (168, 100, 225, 100, pen=pen_used)
            self.scene_1.addLine (261, 100, 318, 100, pen=pen_used)
            
            self.scene_1.addLine (75, 100, 75, 268, pen=pen_used)
            self.scene_1.addLine (168, 100, 168, 251, pen=pen_used)
            self.scene_1.addLine (261, 100, 261, 251, pen=pen_used)
            
            self.scene_1.addLine (132, 251, 168, 251, pen=pen_used)
            self.scene_1.addLine (225, 251, 261, 251, pen=pen_used)        
            
            self.scene_1.addLine (75, 268, 318, 268, pen=pen_used)
            
            self.scene_1.addEllipse(106-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(200-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_1.addEllipse(292-5.5, 127-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            item_4 = self.scene_1.addText("A", font=font_used)
            pos = QtCore.QPointF(104,176)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_1.addText("B", font=font_used)
            pos = QtCore.QPointF(200,176)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_1.addText("C", font=font_used)
            pos = QtCore.QPointF(292,176)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_1.addRect(115, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_1.addRect(208, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_1.addRect(302, 116, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.graphicsView.setScene(self.scene_1)
            
            
        
        '''
        Dibujar secundario
        '''
        
        if secundario == 1:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (132, 17, 318, 17, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 17, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 17, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 17, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 17, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 17, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 17, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 244, pen=pen_used) 
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a", font=font_used)
            pos = QtCore.QPointF(104,109)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b", font=font_used)
            pos = QtCore.QPointF(198,109)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c", font=font_used)
            pos = QtCore.QPointF(292,109)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
        
        elif secundario == 2:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (112, 17, 162, 17, pen=pen_used)
            self.scene_2.addLine (205, 17, 255, 17, pen=pen_used)
            self.scene_2.addLine (298, 17, 348, 17, pen=pen_used)
            
            if salida == 1:              
                self.scene_2.addEllipse(112-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(205-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(298-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (112, 17, 112, 224, pen=pen_used)
                self.scene_2.addLine (205, 17, 205, 244, pen=pen_used)
                self.scene_2.addLine (298, 17, 298, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(112-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(205-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(298-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (112, 17, 112, 224, pen=pen_used)
                self.scene_2.addLine (205, 17, 205, 264, pen=pen_used)
                self.scene_2.addLine (298, 17, 298, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(112-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(205-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(298-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (112, 17, 112, 244, pen=pen_used)
                self.scene_2.addLine (205, 17, 205, 224, pen=pen_used)
                self.scene_2.addLine (298, 17, 298, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(112-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(205-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(298-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (112, 17, 112, 244, pen=pen_used)
                self.scene_2.addLine (205, 17, 205, 264, pen=pen_used)
                self.scene_2.addLine (298, 17, 298, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(112-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(205-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(298-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (112, 17, 112, 264, pen=pen_used)
                self.scene_2.addLine (205, 17, 205, 244, pen=pen_used)
                self.scene_2.addLine (298, 17, 298, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(112-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(205-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(298-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (112, 17, 112, 264, pen=pen_used)
                self.scene_2.addLine (205, 17, 205, 224, pen=pen_used)
                self.scene_2.addLine (298, 17, 298, 244, pen=pen_used) 
            
            self.scene_2.addLine (162, 17, 162, 202, pen=pen_used)
            self.scene_2.addLine (255, 17, 255, 202, pen=pen_used)
            self.scene_2.addLine (348, 17, 348, 202, pen=pen_used)        
            
            self.scene_2.addLine (162, 202, 348, 202, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a", font=font_used)
            pos = QtCore.QPointF(134,109)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b", font=font_used)
            pos = QtCore.QPointF(228,109)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c", font=font_used)
            pos = QtCore.QPointF(322,109)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(136-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(229-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(322-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(145, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(238, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(331, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
            
        elif secundario == 3:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (132, 17, 354, 17, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 34, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 34, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 34, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 34, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 34, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 17, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 34, 318, 244, pen=pen_used) 
            
            self.scene_2.addLine (168, 34, 225, 34, pen=pen_used)
            self.scene_2.addLine (261, 34, 318, 34, pen=pen_used)
            
            self.scene_2.addLine (168, 34, 168, 185, pen=pen_used)
            self.scene_2.addLine (261, 34, 261, 185, pen=pen_used)
            self.scene_2.addLine (354, 17, 354, 185, pen=pen_used)
            
            self.scene_2.addLine (132, 185, 168, 185, pen=pen_used)
            self.scene_2.addLine (225, 185, 261, 185, pen=pen_used)
            self.scene_2.addLine (318, 185, 354, 185, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a", font=font_used)
            pos = QtCore.QPointF(104,109)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b", font=font_used)
            pos = QtCore.QPointF(198,109)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c", font=font_used)
            pos = QtCore.QPointF(292,109)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
        
        elif secundario == 4:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (75, 17, 318, 17, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 34, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 34, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 34, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 34, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 34, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 34, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 34, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 17, 318, 244, pen=pen_used)
            
            self.scene_2.addLine (132, 34, 168, 34, pen=pen_used)
            self.scene_2.addLine (225, 34, 261, 34, pen=pen_used)
            
            self.scene_2.addLine (75, 17, 75, 185, pen=pen_used)
            self.scene_2.addLine (168, 34, 168, 185, pen=pen_used)
            self.scene_2.addLine (261, 34, 261, 185, pen=pen_used)
            
            self.scene_2.addLine (75, 185, 132, 185, pen=pen_used)
            self.scene_2.addLine (168, 185, 225, 185, pen=pen_used)
            self.scene_2.addLine (261, 185, 318, 185, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a", font=font_used)
            pos = QtCore.QPointF(104,109)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b", font=font_used)
            pos = QtCore.QPointF(198,109)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c", font=font_used)
            pos = QtCore.QPointF(292,109)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 158-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 120,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
            
        elif secundario == 5:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (132, 17, 354, 17, pen=pen_used)
            
            self.scene_2.addLine (132, 17, 132, 101, pen=pen_used)
            self.scene_2.addLine (225, 33, 225, 101, pen=pen_used)
            self.scene_2.addLine (318, 33, 318, 101, pen=pen_used)
            
            self.scene_2.addLine (197, 33, 225, 33, pen=pen_used)
            self.scene_2.addLine (290, 33, 318, 33, pen=pen_used)
            
            self.scene_2.addLine (354, 17, 354, 118, pen=pen_used)
            
            self.scene_2.addLine (132, 101, 318, 101, pen=pen_used)
            
            self.scene_2.addLine (197, 33, 161, 118, pen=pen_used)
            self.scene_2.addLine (290, 33, 254, 118, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a2", font=font_used)
            pos = QtCore.QPointF(104,64)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b2", font=font_used)
            pos = QtCore.QPointF(198,64)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c2", font=font_used)
            pos = QtCore.QPointF(292,64)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.scene_2.addLine (132, 118, 161, 118, pen=pen_used)
            self.scene_2.addLine (225, 118, 254, 118, pen=pen_used)
            self.scene_2.addLine (318, 118, 354, 118, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 244, pen=pen_used)
            
            item_7 = self.scene_2.addText("a1", font=font_used)
            pos = QtCore.QPointF(104,145)
            item_7.setPos(pos-item_7.boundingRect().center())
            
            item_8 = self.scene_2.addText("b1", font=font_used)
            pos = QtCore.QPointF(198,145)
            item_8.setPos(pos-item_8.boundingRect().center())
            
            item_9 = self.scene_2.addText("c1", font=font_used)
            pos = QtCore.QPointF(292,145)
            item_9.setPos(pos-item_9.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
            
        elif secundario == 6:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (87, 17, 318, 17, pen=pen_used)
            
            self.scene_2.addLine (132, 33, 132, 101, pen=pen_used)
            self.scene_2.addLine (225, 33, 225, 101, pen=pen_used)
            self.scene_2.addLine (318, 17, 318, 101, pen=pen_used)
            
            self.scene_2.addLine (132, 33, 161, 33, pen=pen_used)
            self.scene_2.addLine (225, 33, 254, 33, pen=pen_used)
            
            self.scene_2.addLine (87, 17, 87, 118, pen=pen_used)
            
            self.scene_2.addLine (132, 101, 318, 101, pen=pen_used)
            
            self.scene_2.addLine (161, 33, 197, 118, pen=pen_used)
            self.scene_2.addLine (254, 33, 290, 118, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a2", font=font_used)
            pos = QtCore.QPointF(104,64)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b2", font=font_used)
            pos = QtCore.QPointF(198,64)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c2", font=font_used)
            pos = QtCore.QPointF(292,64)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.scene_2.addLine (87, 118, 132, 118, pen=pen_used)
            self.scene_2.addLine (197, 118, 225, 118, pen=pen_used)
            self.scene_2.addLine (290, 118, 318, 118, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 118, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 118, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 118, 318, 244, pen=pen_used)            
            
            item_7 = self.scene_2.addText("a1", font=font_used)
            pos = QtCore.QPointF(104,145)
            item_7.setPos(pos-item_7.boundingRect().center())
            
            item_8 = self.scene_2.addText("b1", font=font_used)
            pos = QtCore.QPointF(198,145)
            item_8.setPos(pos-item_8.boundingRect().center())
            
            item_9 = self.scene_2.addText("c1", font=font_used)
            pos = QtCore.QPointF(292,145)
            item_9.setPos(pos-item_9.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
            
        elif secundario == 7:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (87, 17, 354, 17, pen=pen_used)
            
            self.scene_2.addLine (132, 33, 318, 33, pen=pen_used)
            
            self.scene_2.addLine (132, 33, 132, 101, pen=pen_used)
            self.scene_2.addLine (225, 33, 225, 101, pen=pen_used)
            self.scene_2.addLine (318, 33, 318, 101, pen=pen_used)        
            
            self.scene_2.addLine (87, 17, 87, 101, pen=pen_used)
            
            self.scene_2.addLine (87, 101, 132, 101, pen=pen_used)
            self.scene_2.addLine (182, 101, 225, 101, pen=pen_used)
            self.scene_2.addLine (275, 101, 318, 101, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a2", font=font_used)
            pos = QtCore.QPointF(104,64)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b2", font=font_used)
            pos = QtCore.QPointF(198,64)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c2", font=font_used)
            pos = QtCore.QPointF(292,64)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.scene_2.addLine (87, 118, 132, 118, pen=pen_used)
            self.scene_2.addLine (183, 118, 225, 118, pen=pen_used)
            self.scene_2.addLine (276, 118, 318, 118, pen=pen_used)
            
            self.scene_2.addLine (132, 118, 132, 187, pen=pen_used)
            self.scene_2.addLine (225, 118, 225, 187, pen=pen_used)
            self.scene_2.addLine (318, 118, 318, 187, pen=pen_used)
            
            self.scene_2.addLine (182, 101, 146, 187, pen=pen_used)
            self.scene_2.addLine (275, 101, 239, 187, pen=pen_used)
            
            self.scene_2.addLine (132, 187, 146, 187, pen=pen_used)
            self.scene_2.addLine (225, 187, 239, 187, pen=pen_used)
            self.scene_2.addLine (318, 187, 354, 187, pen=pen_used)
            
            self.scene_2.addLine (87, 118, 87, 204, pen=pen_used)
            self.scene_2.addLine (183, 118, 183, 204, pen=pen_used)
            self.scene_2.addLine (276, 118, 276, 204, pen=pen_used)
            
            self.scene_2.addLine (354, 17, 354, 187, pen=pen_used)
            
            self.scene_2.addLine (87, 204, 132, 204, pen=pen_used)
            self.scene_2.addLine (183, 204, 225, 204, pen=pen_used)
            self.scene_2.addLine (276, 204, 318, 204, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 244, pen=pen_used)
            
            item_7 = self.scene_2.addText("a1", font=font_used)
            pos = QtCore.QPointF(104,145)
            item_7.setPos(pos-item_7.boundingRect().center())
            
            item_8 = self.scene_2.addText("b1", font=font_used)
            pos = QtCore.QPointF(198,145)
            item_8.setPos(pos-item_8.boundingRect().center())
            
            item_9 = self.scene_2.addText("c1", font=font_used)
            pos = QtCore.QPointF(292,145)
            item_9.setPos(pos-item_9.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
            
        elif secundario == 8:
            self.scene_2.clear()
            
            pen_used = QtGui.QPen()
            
            pen_used.setWidth(3)
            
            self.scene_2.addLine (87, 17, 354, 17, pen=pen_used)
            
            self.scene_2.addLine (132, 33, 318, 33, pen=pen_used)
            
            self.scene_2.addLine (132, 33, 132, 101, pen=pen_used)
            self.scene_2.addLine (225, 33, 225, 101, pen=pen_used)
            self.scene_2.addLine (318, 33, 318, 101, pen=pen_used)        
            
            self.scene_2.addLine (87, 17, 87, 187, pen=pen_used)
            
            self.scene_2.addLine (354, 17, 354, 101, pen=pen_used)
            
            self.scene_2.addLine (132, 101, 161, 101, pen=pen_used)
            self.scene_2.addLine (225, 101, 254, 101, pen=pen_used)
            self.scene_2.addLine (318, 101, 354, 101, pen=pen_used)
            
            font_used = QtGui.QFont("Times", 11, QtGui.QFont.Bold)
            
            item_4 = self.scene_2.addText("a2", font=font_used)
            pos = QtCore.QPointF(104,64)
            item_4.setPos(pos-item_4.boundingRect().center())
            
            item_5 = self.scene_2.addText("b2", font=font_used)
            pos = QtCore.QPointF(198,64)
            item_5.setPos(pos-item_5.boundingRect().center())
            
            item_6 = self.scene_2.addText("c2", font=font_used)
            pos = QtCore.QPointF(292,64)
            item_6.setPos(pos-item_6.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 83-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 50, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            self.scene_2.addLine (132, 118, 156, 118, pen=pen_used)
            self.scene_2.addLine (225, 118, 249, 118, pen=pen_used)
            self.scene_2.addLine (318, 118, 354, 118, pen=pen_used)
            
            self.scene_2.addLine (132, 118, 132, 187, pen=pen_used)
            self.scene_2.addLine (225, 118, 225, 187, pen=pen_used)
            self.scene_2.addLine (318, 118, 318, 187, pen=pen_used)
            
            self.scene_2.addLine (161, 101, 197, 187, pen=pen_used)
            self.scene_2.addLine (254, 101, 290, 187, pen=pen_used)
            
            self.scene_2.addLine (87, 187, 132, 187, pen=pen_used)
            self.scene_2.addLine (197, 187, 225, 187, pen=pen_used)
            self.scene_2.addLine (290, 187, 318, 187, pen=pen_used)
            
            self.scene_2.addLine (156, 118, 156, 204, pen=pen_used)
            self.scene_2.addLine (249, 118, 249, 204, pen=pen_used)
            self.scene_2.addLine (354, 118, 354, 204, pen=pen_used)
            
            self.scene_2.addLine (132, 204, 156, 204, pen=pen_used)
            self.scene_2.addLine (225, 204, 249, 204, pen=pen_used)
            self.scene_2.addLine (318, 204, 354, 204, pen=pen_used)
            
            if salida == 1:                
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 264, pen=pen_used) 
                
            elif salida == 2:
                self.scene_2.addEllipse(132-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 224, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 244, pen=pen_used) 
            
            elif salida == 3:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 264, pen=pen_used) 
            
            elif salida == 4:
                self.scene_2.addEllipse(132-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 244, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 264, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 224, pen=pen_used) 
            
            elif salida == 5:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 244, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 224, pen=pen_used) 
            
            elif salida == 6:
                self.scene_2.addEllipse(132-5.5, 264-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(225-5.5, 224-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                self.scene_2.addEllipse(318-5.5, 244-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
                
                self.scene_2.addLine (132, 204, 132, 264, pen=pen_used)
                self.scene_2.addLine (225, 204, 225, 224, pen=pen_used)
                self.scene_2.addLine (318, 204, 318, 244, pen=pen_used)
            
            item_7 = self.scene_2.addText("a1", font=font_used)
            pos = QtCore.QPointF(104,145)
            item_7.setPos(pos-item_7.boundingRect().center())
            
            item_8 = self.scene_2.addText("b1", font=font_used)
            pos = QtCore.QPointF(198,145)
            item_8.setPos(pos-item_8.boundingRect().center())
            
            item_9 = self.scene_2.addText("c1", font=font_used)
            pos = QtCore.QPointF(292,145)
            item_9.setPos(pos-item_9.boundingRect().center())
            
            self.scene_2.addEllipse(106-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(200-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            self.scene_2.addEllipse(292-5.5, 164-5.5, 11, 11, pen=QtGui.QPen(QtGui.QColor("black")), brush=QtGui.QBrush(QtGui.QColor("black")))
            
            self.scene_2.addRect(115, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("red")),
                                  brush=QtGui.QBrush(QtGui.QColor("red"))
                                  )
            
            self.scene_2.addRect(208, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("green")),
                                  brush=QtGui.QBrush(QtGui.QColor("green"))
                                  )
            
            self.scene_2.addRect(302, 130, 33, 39,
                                  pen=QtGui.QPen(QtGui.QColor("blue")),
                                  brush=QtGui.QBrush(QtGui.QColor("blue"))
                                  )
            
            item_1 = self.scene_2.addText("l1", font=font_used)
            pos = QtCore.QPointF(72,225)
            item_1.setPos(pos-item_1.boundingRect().center())
            
            item_2 = self.scene_2.addText("l2", font=font_used)
            pos = QtCore.QPointF(72,245)
            item_2.setPos(pos-item_2.boundingRect().center())
            
            item_3 = self.scene_2.addText("l3", font=font_used)
            pos = QtCore.QPointF(72,265)
            item_3.setPos(pos-item_3.boundingRect().center())
            
            self.scene_2.addLine (87, 224, 363, 224, pen=pen_used)
            self.scene_2.addLine (87, 244, 363, 244, pen=pen_used)
            self.scene_2.addLine (87, 264, 363, 264, pen=pen_used)
            
            self.graphicsView_2.setScene(self.scene_2)
            
            
            
        '''
        Escribir grupo de conexión
        '''
        
        if primario == 1 or primario == 2:
            Letra_primario = "Y"
        elif primario == 3 or primario == 4:
            Letra_primario = "D"
        
        if secundario == 1 or secundario == 2:
            Letra_secundario = "y"
        elif secundario == 3 or secundario == 4:
            Letra_secundario = "d"
        elif secundario == 5 or secundario == 6 or secundario == 7 or secundario == 8:
            Letra_secundario = "z"
        
        grupo = Letra_primario+Letra_secundario+str(indice)
        
        # print(grupo)
        
        self.label_5.setText(grupo)
        
        
        
        '''
        Elegir imagen reloj
        '''
        
        if indice == 0:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/0.png"))
        
        elif indice == 1:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/1.png"))
            
        elif indice == 2:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/2.png"))
            
        elif indice == 3:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/3.png"))
            
        elif indice == 4:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/4.png"))
            
        elif indice == 5:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/5.png"))
            
        elif indice == 6:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/6.png"))
            
        elif indice == 7:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/7.png"))
            
        elif indice == 8:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/8.png"))
            
        elif indice == 9:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/9.png"))
            
        elif indice == 10:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/10.png"))
            
        elif indice == 11:
            self.label_12.setPixmap(QtGui.QPixmap("Horas/11.png"))
        
        
        
        '''
        Elegir imagen relación VLL/vll
        '''
        
        if primario == 1 or primario == 2:
            if secundario == 1 or secundario == 2:
                self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Estrella-Estrella_Delta-Delta.png"))
            
            elif secundario == 3 or secundario == 4:
                self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Estrella-Delta.png"))
            
            elif secundario == 5 or secundario == 6 or secundario == 7 or secundario == 8:
                self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Estrella-Zig-Zag.png"))
        
        elif primario == 3 or primario == 4:
            if secundario == 1 or secundario == 2:
                self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Delta-Estrella.png"))
            
            elif secundario == 3 or secundario == 4:
                self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Estrella-Estrella_Delta-Delta.png"))
            
            elif secundario == 5 or secundario == 6 or secundario == 7 or secundario == 8:
                self.label_13.setPixmap(QtGui.QPixmap("Relaciones/Delta-Zig-Zag.png"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
