# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_updated.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 671, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.streetLayout1 = QtWidgets.QVBoxLayout()
        self.streetLayout1.setObjectName("streetLayout1")
        self.st1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.st1_lbl.setObjectName("st1_lbl")
        self.streetLayout1.addWidget(self.st1_lbl, 0, QtCore.Qt.AlignTop)
        self.address1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.address1.setObjectName("address1")
        self.streetLayout1.addWidget(self.address1)
        self.homesLayout1 = QtWidgets.QHBoxLayout()
        self.homesLayout1.setObjectName("homesLayout1")
        self.st1_home1Layout = QtWidgets.QVBoxLayout()
        self.st1_home1Layout.setObjectName("st1_home1Layout")
        self.house1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1.setObjectName("house1")
        self.st1_home1Layout.addWidget(self.house1)
        self.floors1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1.setObjectName("floors1")
        self.st1_home1Layout.addWidget(self.floors1)
        self.live1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1.setObjectName("live1")
        self.st1_home1Layout.addWidget(self.live1)
        self.lift_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_1.setObjectName("lift_1")
        self.st1_home1Layout.addWidget(self.lift_1)
        self.lift_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_2.setObjectName("lift_2")
        self.st1_home1Layout.addWidget(self.lift_2)
        self.lift_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_3.setObjectName("lift_3")
        self.st1_home1Layout.addWidget(self.lift_3)
        self.lift_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_4.setObjectName("lift_4")
        self.st1_home1Layout.addWidget(self.lift_4)
        self.homesLayout1.addLayout(self.st1_home1Layout)
        self.st1_home2Layout = QtWidgets.QVBoxLayout()
        self.st1_home2Layout.setObjectName("st1_home2Layout")
        self.house1_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_2.setObjectName("house1_2")
        self.st1_home2Layout.addWidget(self.house1_2)
        self.floors1_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_2.setObjectName("floors1_2")
        self.st1_home2Layout.addWidget(self.floors1_2)
        self.live1_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_2.setObjectName("live1_2")
        self.st1_home2Layout.addWidget(self.live1_2)
        self.lift_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_5.setObjectName("lift_5")
        self.st1_home2Layout.addWidget(self.lift_5)
        self.lift_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_6.setObjectName("lift_6")
        self.st1_home2Layout.addWidget(self.lift_6)
        self.lift_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_7.setObjectName("lift_7")
        self.st1_home2Layout.addWidget(self.lift_7)
        self.lift_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_8.setObjectName("lift_8")
        self.st1_home2Layout.addWidget(self.lift_8)
        self.homesLayout1.addLayout(self.st1_home2Layout)
        self.st1_home3Layout = QtWidgets.QVBoxLayout()
        self.st1_home3Layout.setObjectName("st1_home3Layout")
        self.house1_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_3.setObjectName("house1_3")
        self.st1_home3Layout.addWidget(self.house1_3)
        self.floors1_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_3.setObjectName("floors1_3")
        self.st1_home3Layout.addWidget(self.floors1_3)
        self.live1_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_3.setObjectName("live1_3")
        self.st1_home3Layout.addWidget(self.live1_3)
        self.lift_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_9.setObjectName("lift_9")
        self.st1_home3Layout.addWidget(self.lift_9)
        self.lift_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_10.setObjectName("lift_10")
        self.st1_home3Layout.addWidget(self.lift_10)
        self.lift_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_11.setObjectName("lift_11")
        self.st1_home3Layout.addWidget(self.lift_11)
        self.lift_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_12.setObjectName("lift_12")
        self.st1_home3Layout.addWidget(self.lift_12)
        self.homesLayout1.addLayout(self.st1_home3Layout)
        self.st1_home4Layout = QtWidgets.QVBoxLayout()
        self.st1_home4Layout.setObjectName("st1_home4Layout")
        self.house1_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_4.setObjectName("house1_4")
        self.st1_home4Layout.addWidget(self.house1_4)
        self.floors1_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_4.setObjectName("floors1_4")
        self.st1_home4Layout.addWidget(self.floors1_4)
        self.live1_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_4.setObjectName("live1_4")
        self.st1_home4Layout.addWidget(self.live1_4)
        self.lift_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_13.setObjectName("lift_13")
        self.st1_home4Layout.addWidget(self.lift_13)
        self.lift_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_14.setObjectName("lift_14")
        self.st1_home4Layout.addWidget(self.lift_14)
        self.lift_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_15.setObjectName("lift_15")
        self.st1_home4Layout.addWidget(self.lift_15)
        self.lift_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_16.setObjectName("lift_16")
        self.st1_home4Layout.addWidget(self.lift_16)
        self.homesLayout1.addLayout(self.st1_home4Layout)
        self.homesLayout1.setStretch(0, 1)
        self.homesLayout1.setStretch(1, 1)
        self.homesLayout1.setStretch(2, 1)
        self.homesLayout1.setStretch(3, 1)
        self.streetLayout1.addLayout(self.homesLayout1)
        self.streetLayout1.setStretch(0, 1)
        self.streetLayout1.setStretch(2, 10)
        self.gridLayout.addLayout(self.streetLayout1, 0, 0, 1, 1)
        self.streetLayout1_6 = QtWidgets.QVBoxLayout()
        self.streetLayout1_6.setObjectName("streetLayout1_6")
        self.st1_lbl_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.st1_lbl_4.setObjectName("st1_lbl_4")
        self.streetLayout1_6.addWidget(self.st1_lbl_4, 0, QtCore.Qt.AlignTop)
        self.address2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.address2.setObjectName("address2")
        self.streetLayout1_6.addWidget(self.address2)
        self.homesLayout1_6 = QtWidgets.QHBoxLayout()
        self.homesLayout1_6.setObjectName("homesLayout1_6")
        self.st1_home1Layout_6 = QtWidgets.QVBoxLayout()
        self.st1_home1Layout_6.setObjectName("st1_home1Layout_6")
        self.house1_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_5.setObjectName("house1_5")
        self.st1_home1Layout_6.addWidget(self.house1_5)
        self.floors1_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_5.setObjectName("floors1_5")
        self.st1_home1Layout_6.addWidget(self.floors1_5)
        self.live1_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_5.setObjectName("live1_5")
        self.st1_home1Layout_6.addWidget(self.live1_5)
        self.lift_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_17.setObjectName("lift_17")
        self.st1_home1Layout_6.addWidget(self.lift_17)
        self.lift_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_18.setObjectName("lift_18")
        self.st1_home1Layout_6.addWidget(self.lift_18)
        self.lift_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_19.setObjectName("lift_19")
        self.st1_home1Layout_6.addWidget(self.lift_19)
        self.lift_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_20.setObjectName("lift_20")
        self.st1_home1Layout_6.addWidget(self.lift_20)
        self.homesLayout1_6.addLayout(self.st1_home1Layout_6)
        self.st1_home2Layout_6 = QtWidgets.QVBoxLayout()
        self.st1_home2Layout_6.setObjectName("st1_home2Layout_6")
        self.house1_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_6.setObjectName("house1_6")
        self.st1_home2Layout_6.addWidget(self.house1_6)
        self.floors1_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_6.setObjectName("floors1_6")
        self.st1_home2Layout_6.addWidget(self.floors1_6)
        self.live1_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_6.setObjectName("live1_6")
        self.st1_home2Layout_6.addWidget(self.live1_6)
        self.lift_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_21.setObjectName("lift_21")
        self.st1_home2Layout_6.addWidget(self.lift_21)
        self.lift_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_22.setObjectName("lift_22")
        self.st1_home2Layout_6.addWidget(self.lift_22)
        self.lift_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_23.setObjectName("lift_23")
        self.st1_home2Layout_6.addWidget(self.lift_23)
        self.lift_24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_24.setObjectName("lift_24")
        self.st1_home2Layout_6.addWidget(self.lift_24)
        self.homesLayout1_6.addLayout(self.st1_home2Layout_6)
        self.st1_home3Layout_6 = QtWidgets.QVBoxLayout()
        self.st1_home3Layout_6.setObjectName("st1_home3Layout_6")
        self.house1_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_7.setObjectName("house1_7")
        self.st1_home3Layout_6.addWidget(self.house1_7)
        self.floors1_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_7.setObjectName("floors1_7")
        self.st1_home3Layout_6.addWidget(self.floors1_7)
        self.live1_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_7.setObjectName("live1_7")
        self.st1_home3Layout_6.addWidget(self.live1_7)
        self.lift_25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_25.setObjectName("lift_25")
        self.st1_home3Layout_6.addWidget(self.lift_25)
        self.lift_26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_26.setObjectName("lift_26")
        self.st1_home3Layout_6.addWidget(self.lift_26)
        self.lift_27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_27.setObjectName("lift_27")
        self.st1_home3Layout_6.addWidget(self.lift_27)
        self.lift_28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_28.setObjectName("lift_28")
        self.st1_home3Layout_6.addWidget(self.lift_28)
        self.homesLayout1_6.addLayout(self.st1_home3Layout_6)
        self.st1_home4Layout_6 = QtWidgets.QVBoxLayout()
        self.st1_home4Layout_6.setObjectName("st1_home4Layout_6")
        self.house1_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_8.setObjectName("house1_8")
        self.st1_home4Layout_6.addWidget(self.house1_8)
        self.floors1_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_8.setObjectName("floors1_8")
        self.st1_home4Layout_6.addWidget(self.floors1_8)
        self.live1_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_8.setObjectName("live1_8")
        self.st1_home4Layout_6.addWidget(self.live1_8)
        self.lift_29 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_29.setObjectName("lift_29")
        self.st1_home4Layout_6.addWidget(self.lift_29)
        self.lift_30 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_30.setObjectName("lift_30")
        self.st1_home4Layout_6.addWidget(self.lift_30)
        self.lift_31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_31.setObjectName("lift_31")
        self.st1_home4Layout_6.addWidget(self.lift_31)
        self.lift_32 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_32.setObjectName("lift_32")
        self.st1_home4Layout_6.addWidget(self.lift_32)
        self.homesLayout1_6.addLayout(self.st1_home4Layout_6)
        self.homesLayout1_6.setStretch(0, 1)
        self.homesLayout1_6.setStretch(1, 1)
        self.homesLayout1_6.setStretch(2, 1)
        self.homesLayout1_6.setStretch(3, 1)
        self.streetLayout1_6.addLayout(self.homesLayout1_6)
        self.streetLayout1_6.setStretch(0, 1)
        self.streetLayout1_6.setStretch(2, 10)
        self.gridLayout.addLayout(self.streetLayout1_6, 0, 1, 1, 1)
        self.streetLayout1_7 = QtWidgets.QVBoxLayout()
        self.streetLayout1_7.setObjectName("streetLayout1_7")
        self.st1_lbl_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.st1_lbl_5.setObjectName("st1_lbl_5")
        self.streetLayout1_7.addWidget(self.st1_lbl_5, 0, QtCore.Qt.AlignTop)
        self.address3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.address3.setObjectName("address3")
        self.streetLayout1_7.addWidget(self.address3)
        self.homesLayout1_7 = QtWidgets.QHBoxLayout()
        self.homesLayout1_7.setObjectName("homesLayout1_7")
        self.st1_home1Layout_7 = QtWidgets.QVBoxLayout()
        self.st1_home1Layout_7.setObjectName("st1_home1Layout_7")
        self.house1_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_9.setObjectName("house1_9")
        self.st1_home1Layout_7.addWidget(self.house1_9)
        self.floors1_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_9.setObjectName("floors1_9")
        self.st1_home1Layout_7.addWidget(self.floors1_9)
        self.live1_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_9.setObjectName("live1_9")
        self.st1_home1Layout_7.addWidget(self.live1_9)
        self.lift_33 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_33.setObjectName("lift_33")
        self.st1_home1Layout_7.addWidget(self.lift_33)
        self.lift_34 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_34.setObjectName("lift_34")
        self.st1_home1Layout_7.addWidget(self.lift_34)
        self.lift_35 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_35.setObjectName("lift_35")
        self.st1_home1Layout_7.addWidget(self.lift_35)
        self.lift_36 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_36.setObjectName("lift_36")
        self.st1_home1Layout_7.addWidget(self.lift_36)
        self.homesLayout1_7.addLayout(self.st1_home1Layout_7)
        self.st1_home2Layout_7 = QtWidgets.QVBoxLayout()
        self.st1_home2Layout_7.setObjectName("st1_home2Layout_7")
        self.house1_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_10.setObjectName("house1_10")
        self.st1_home2Layout_7.addWidget(self.house1_10)
        self.floors1_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_10.setObjectName("floors1_10")
        self.st1_home2Layout_7.addWidget(self.floors1_10)
        self.live1_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_10.setObjectName("live1_10")
        self.st1_home2Layout_7.addWidget(self.live1_10)
        self.lift_37 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_37.setObjectName("lift_37")
        self.st1_home2Layout_7.addWidget(self.lift_37)
        self.lift_38 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_38.setObjectName("lift_38")
        self.st1_home2Layout_7.addWidget(self.lift_38)
        self.lift_39 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_39.setObjectName("lift_39")
        self.st1_home2Layout_7.addWidget(self.lift_39)
        self.lift_40 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_40.setObjectName("lift_40")
        self.st1_home2Layout_7.addWidget(self.lift_40)
        self.homesLayout1_7.addLayout(self.st1_home2Layout_7)
        self.st1_home3Layout_7 = QtWidgets.QVBoxLayout()
        self.st1_home3Layout_7.setObjectName("st1_home3Layout_7")
        self.house1_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_11.setObjectName("house1_11")
        self.st1_home3Layout_7.addWidget(self.house1_11)
        self.floors1_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_11.setObjectName("floors1_11")
        self.st1_home3Layout_7.addWidget(self.floors1_11)
        self.live1_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_11.setObjectName("live1_11")
        self.st1_home3Layout_7.addWidget(self.live1_11)
        self.lift_41 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_41.setObjectName("lift_41")
        self.st1_home3Layout_7.addWidget(self.lift_41)
        self.lift_42 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_42.setObjectName("lift_42")
        self.st1_home3Layout_7.addWidget(self.lift_42)
        self.lift_43 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_43.setObjectName("lift_43")
        self.st1_home3Layout_7.addWidget(self.lift_43)
        self.lift_44 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_44.setObjectName("lift_44")
        self.st1_home3Layout_7.addWidget(self.lift_44)
        self.homesLayout1_7.addLayout(self.st1_home3Layout_7)
        self.st1_home4Layout_7 = QtWidgets.QVBoxLayout()
        self.st1_home4Layout_7.setObjectName("st1_home4Layout_7")
        self.house1_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_12.setObjectName("house1_12")
        self.st1_home4Layout_7.addWidget(self.house1_12)
        self.floors1_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_12.setObjectName("floors1_12")
        self.st1_home4Layout_7.addWidget(self.floors1_12)
        self.live1_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_12.setObjectName("live1_12")
        self.st1_home4Layout_7.addWidget(self.live1_12)
        self.lift_45 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_45.setObjectName("lift_45")
        self.st1_home4Layout_7.addWidget(self.lift_45)
        self.lift_46 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_46.setObjectName("lift_46")
        self.st1_home4Layout_7.addWidget(self.lift_46)
        self.lift_47 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_47.setObjectName("lift_47")
        self.st1_home4Layout_7.addWidget(self.lift_47)
        self.lift_48 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_48.setObjectName("lift_48")
        self.st1_home4Layout_7.addWidget(self.lift_48)
        self.homesLayout1_7.addLayout(self.st1_home4Layout_7)
        self.homesLayout1_7.setStretch(0, 1)
        self.homesLayout1_7.setStretch(1, 1)
        self.homesLayout1_7.setStretch(2, 1)
        self.homesLayout1_7.setStretch(3, 1)
        self.streetLayout1_7.addLayout(self.homesLayout1_7)
        self.streetLayout1_7.setStretch(0, 1)
        self.streetLayout1_7.setStretch(2, 10)
        self.gridLayout.addLayout(self.streetLayout1_7, 1, 0, 1, 1)
        self.streetLayout1_8 = QtWidgets.QVBoxLayout()
        self.streetLayout1_8.setObjectName("streetLayout1_8")
        self.st1_lbl_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.st1_lbl_6.setObjectName("st1_lbl_6")
        self.streetLayout1_8.addWidget(self.st1_lbl_6, 0, QtCore.Qt.AlignTop)
        self.address4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.address4.setObjectName("address4")
        self.streetLayout1_8.addWidget(self.address4)
        self.homesLayout1_8 = QtWidgets.QHBoxLayout()
        self.homesLayout1_8.setObjectName("homesLayout1_8")
        self.st1_home1Layout_8 = QtWidgets.QVBoxLayout()
        self.st1_home1Layout_8.setObjectName("st1_home1Layout_8")
        self.house1_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_13.setObjectName("house1_13")
        self.st1_home1Layout_8.addWidget(self.house1_13)
        self.floors1_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_13.setObjectName("floors1_13")
        self.st1_home1Layout_8.addWidget(self.floors1_13)
        self.live1_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_13.setObjectName("live1_13")
        self.st1_home1Layout_8.addWidget(self.live1_13)
        self.lift_49 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_49.setObjectName("lift_49")
        self.st1_home1Layout_8.addWidget(self.lift_49)
        self.lift_50 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_50.setObjectName("lift_50")
        self.st1_home1Layout_8.addWidget(self.lift_50)
        self.lift_51 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_51.setObjectName("lift_51")
        self.st1_home1Layout_8.addWidget(self.lift_51)
        self.lift_52 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_52.setObjectName("lift_52")
        self.st1_home1Layout_8.addWidget(self.lift_52)
        self.homesLayout1_8.addLayout(self.st1_home1Layout_8)
        self.st1_home2Layout_8 = QtWidgets.QVBoxLayout()
        self.st1_home2Layout_8.setObjectName("st1_home2Layout_8")
        self.house1_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_14.setObjectName("house1_14")
        self.st1_home2Layout_8.addWidget(self.house1_14)
        self.floors1_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_14.setObjectName("floors1_14")
        self.st1_home2Layout_8.addWidget(self.floors1_14)
        self.live1_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_14.setObjectName("live1_14")
        self.st1_home2Layout_8.addWidget(self.live1_14)
        self.lift_53 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_53.setObjectName("lift_53")
        self.st1_home2Layout_8.addWidget(self.lift_53)
        self.lift_54 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_54.setObjectName("lift_54")
        self.st1_home2Layout_8.addWidget(self.lift_54)
        self.lift_55 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_55.setObjectName("lift_55")
        self.st1_home2Layout_8.addWidget(self.lift_55)
        self.lift_56 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_56.setObjectName("lift_56")
        self.st1_home2Layout_8.addWidget(self.lift_56)
        self.homesLayout1_8.addLayout(self.st1_home2Layout_8)
        self.st1_home3Layout_8 = QtWidgets.QVBoxLayout()
        self.st1_home3Layout_8.setObjectName("st1_home3Layout_8")
        self.house1_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_15.setObjectName("house1_15")
        self.st1_home3Layout_8.addWidget(self.house1_15)
        self.floors1_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_15.setObjectName("floors1_15")
        self.st1_home3Layout_8.addWidget(self.floors1_15)
        self.live1_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_15.setObjectName("live1_15")
        self.st1_home3Layout_8.addWidget(self.live1_15)
        self.lift_57 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_57.setObjectName("lift_57")
        self.st1_home3Layout_8.addWidget(self.lift_57)
        self.lift_58 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_58.setObjectName("lift_58")
        self.st1_home3Layout_8.addWidget(self.lift_58)
        self.lift_59 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_59.setObjectName("lift_59")
        self.st1_home3Layout_8.addWidget(self.lift_59)
        self.lift_60 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_60.setObjectName("lift_60")
        self.st1_home3Layout_8.addWidget(self.lift_60)
        self.homesLayout1_8.addLayout(self.st1_home3Layout_8)
        self.st1_home4Layout_8 = QtWidgets.QVBoxLayout()
        self.st1_home4Layout_8.setObjectName("st1_home4Layout_8")
        self.house1_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.house1_16.setObjectName("house1_16")
        self.st1_home4Layout_8.addWidget(self.house1_16)
        self.floors1_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.floors1_16.setObjectName("floors1_16")
        self.st1_home4Layout_8.addWidget(self.floors1_16)
        self.live1_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.live1_16.setObjectName("live1_16")
        self.st1_home4Layout_8.addWidget(self.live1_16)
        self.lift_61 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_61.setObjectName("lift_61")
        self.st1_home4Layout_8.addWidget(self.lift_61)
        self.lift_62 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_62.setObjectName("lift_62")
        self.st1_home4Layout_8.addWidget(self.lift_62)
        self.lift_63 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_63.setObjectName("lift_63")
        self.st1_home4Layout_8.addWidget(self.lift_63)
        self.lift_64 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.lift_64.setObjectName("lift_64")
        self.st1_home4Layout_8.addWidget(self.lift_64)
        self.homesLayout1_8.addLayout(self.st1_home4Layout_8)
        self.homesLayout1_8.setStretch(0, 1)
        self.homesLayout1_8.setStretch(1, 1)
        self.homesLayout1_8.setStretch(2, 1)
        self.homesLayout1_8.setStretch(3, 1)
        self.streetLayout1_8.addLayout(self.homesLayout1_8)
        self.streetLayout1_8.setStretch(0, 1)
        self.streetLayout1_8.setStretch(2, 10)
        self.gridLayout.addLayout(self.streetLayout1_8, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 560, 671, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.simultation_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.simultation_btn.setObjectName("simultation_btn")
        self.horizontalLayout.addWidget(self.simultation_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.st1_lbl.setText(_translate("MainWindow", "Улица 1"))
        self.address1.setText(_translate("MainWindow", "Адрес"))
        self.house1.setText(_translate("MainWindow", "Дом 1"))
        self.floors1.setText(_translate("MainWindow", "Этажей"))
        self.live1.setText(_translate("MainWindow", "Жильцов"))
        self.lift_1.setText(_translate("MainWindow", "Лифт 1"))
        self.lift_2.setText(_translate("MainWindow", "Лифт 2"))
        self.lift_3.setText(_translate("MainWindow", "Лифт 3"))
        self.lift_4.setText(_translate("MainWindow", "Лифт 4"))
        self.house1_2.setText(_translate("MainWindow", "Дом 2"))
        self.floors1_2.setText(_translate("MainWindow", "Этажей"))
        self.live1_2.setText(_translate("MainWindow", "Жильцов"))
        self.lift_5.setText(_translate("MainWindow", "Лифт 5"))
        self.lift_6.setText(_translate("MainWindow", "Лифт 6"))
        self.lift_7.setText(_translate("MainWindow", "Лифт 7"))
        self.lift_8.setText(_translate("MainWindow", "Лифт 8"))
        self.house1_3.setText(_translate("MainWindow", "Дом 3"))
        self.floors1_3.setText(_translate("MainWindow", "Этажей"))
        self.live1_3.setText(_translate("MainWindow", "Жильцов"))
        self.lift_9.setText(_translate("MainWindow", "Лифт 9"))
        self.lift_10.setText(_translate("MainWindow", "Лифт 10"))
        self.lift_11.setText(_translate("MainWindow", "Лифт 11"))
        self.lift_12.setText(_translate("MainWindow", "Лифт 12"))
        self.house1_4.setText(_translate("MainWindow", "Дом 4"))
        self.floors1_4.setText(_translate("MainWindow", "Этажей"))
        self.live1_4.setText(_translate("MainWindow", "Жильцов"))
        self.lift_13.setText(_translate("MainWindow", "Лифт 13"))
        self.lift_14.setText(_translate("MainWindow", "Лифт 14"))
        self.lift_15.setText(_translate("MainWindow", "Лифт 15"))
        self.lift_16.setText(_translate("MainWindow", "Лифт 16"))
        self.st1_lbl_4.setText(_translate("MainWindow", "Улица 2"))
        self.address2.setText(_translate("MainWindow", "Адрес"))
        self.house1_5.setText(_translate("MainWindow", "Дом 1"))
        self.floors1_5.setText(_translate("MainWindow", "Этажей"))
        self.live1_5.setText(_translate("MainWindow", "Жильцов"))
        self.lift_17.setText(_translate("MainWindow", "Лифт 17"))
        self.lift_18.setText(_translate("MainWindow", "Лифт 18"))
        self.lift_19.setText(_translate("MainWindow", "Лифт 19"))
        self.lift_20.setText(_translate("MainWindow", "Лифт 20"))
        self.house1_6.setText(_translate("MainWindow", "Дом 2"))
        self.floors1_6.setText(_translate("MainWindow", "Этажей"))
        self.live1_6.setText(_translate("MainWindow", "Жильцов"))
        self.lift_21.setText(_translate("MainWindow", "Лифт 21"))
        self.lift_22.setText(_translate("MainWindow", "Лифт 22"))
        self.lift_23.setText(_translate("MainWindow", "Лифт 23"))
        self.lift_24.setText(_translate("MainWindow", "Лифт 24"))
        self.house1_7.setText(_translate("MainWindow", "Дом 3"))
        self.floors1_7.setText(_translate("MainWindow", "Этажей"))
        self.live1_7.setText(_translate("MainWindow", "Жильцов"))
        self.lift_25.setText(_translate("MainWindow", "Лифт 25"))
        self.lift_26.setText(_translate("MainWindow", "Лифт 26"))
        self.lift_27.setText(_translate("MainWindow", "Лифт 27"))
        self.lift_28.setText(_translate("MainWindow", "Лифт 28"))
        self.house1_8.setText(_translate("MainWindow", "Дом 4"))
        self.floors1_8.setText(_translate("MainWindow", "Этажей"))
        self.live1_8.setText(_translate("MainWindow", "Жильцов"))
        self.lift_29.setText(_translate("MainWindow", "Лифт 29"))
        self.lift_30.setText(_translate("MainWindow", "Лифт 30"))
        self.lift_31.setText(_translate("MainWindow", "Лифт 31"))
        self.lift_32.setText(_translate("MainWindow", "Лифт 32"))
        self.st1_lbl_5.setText(_translate("MainWindow", "Улица 3"))
        self.address3.setText(_translate("MainWindow", "Адрес"))
        self.house1_9.setText(_translate("MainWindow", "Дом 1"))
        self.floors1_9.setText(_translate("MainWindow", "Этажей"))
        self.live1_9.setText(_translate("MainWindow", "Жильцов"))
        self.lift_33.setText(_translate("MainWindow", "Лифт 33"))
        self.lift_34.setText(_translate("MainWindow", "Лифт 34"))
        self.lift_35.setText(_translate("MainWindow", "Лифт 35"))
        self.lift_36.setText(_translate("MainWindow", "Лифт 36"))
        self.house1_10.setText(_translate("MainWindow", "Дом 2"))
        self.floors1_10.setText(_translate("MainWindow", "Этажей"))
        self.live1_10.setText(_translate("MainWindow", "Жильцов"))
        self.lift_37.setText(_translate("MainWindow", "Лифт 37"))
        self.lift_38.setText(_translate("MainWindow", "Лифт 38"))
        self.lift_39.setText(_translate("MainWindow", "Лифт 39"))
        self.lift_40.setText(_translate("MainWindow", "Лифт 40"))
        self.house1_11.setText(_translate("MainWindow", "Дом 3"))
        self.floors1_11.setText(_translate("MainWindow", "Этажей"))
        self.live1_11.setText(_translate("MainWindow", "Жильцов"))
        self.lift_41.setText(_translate("MainWindow", "Лифт 41"))
        self.lift_42.setText(_translate("MainWindow", "Лифт 42"))
        self.lift_43.setText(_translate("MainWindow", "Лифт 43"))
        self.lift_44.setText(_translate("MainWindow", "Лифт 44"))
        self.house1_12.setText(_translate("MainWindow", "Дом 4"))
        self.floors1_12.setText(_translate("MainWindow", "Этажей"))
        self.live1_12.setText(_translate("MainWindow", "Жильцов"))
        self.lift_45.setText(_translate("MainWindow", "Лифт 45"))
        self.lift_46.setText(_translate("MainWindow", "Лифт 46"))
        self.lift_47.setText(_translate("MainWindow", "Лифт 47"))
        self.lift_48.setText(_translate("MainWindow", "Лифт 48"))
        self.st1_lbl_6.setText(_translate("MainWindow", "Улица 4"))
        self.address4.setText(_translate("MainWindow", "Адрес"))
        self.house1_13.setText(_translate("MainWindow", "Дом 1"))
        self.floors1_13.setText(_translate("MainWindow", "Этажей"))
        self.live1_13.setText(_translate("MainWindow", "Жильцов"))
        self.lift_49.setText(_translate("MainWindow", "Лифт 49"))
        self.lift_50.setText(_translate("MainWindow", "Лифт 50"))
        self.lift_51.setText(_translate("MainWindow", "Лифт 51"))
        self.lift_52.setText(_translate("MainWindow", "Лифт 52"))
        self.house1_14.setText(_translate("MainWindow", "Дом 2"))
        self.floors1_14.setText(_translate("MainWindow", "Этажей"))
        self.live1_14.setText(_translate("MainWindow", "Жильцов"))
        self.lift_53.setText(_translate("MainWindow", "Лифт 53"))
        self.lift_54.setText(_translate("MainWindow", "Лифт 54"))
        self.lift_55.setText(_translate("MainWindow", "Лифт 55"))
        self.lift_56.setText(_translate("MainWindow", "Лифт 56"))
        self.house1_15.setText(_translate("MainWindow", "Дом 3"))
        self.floors1_15.setText(_translate("MainWindow", "Этажей"))
        self.live1_15.setText(_translate("MainWindow", "Жильцов"))
        self.lift_57.setText(_translate("MainWindow", "Лифт 57"))
        self.lift_58.setText(_translate("MainWindow", "Лифт 58"))
        self.lift_59.setText(_translate("MainWindow", "Лифт 59"))
        self.lift_60.setText(_translate("MainWindow", "Лифт 60"))
        self.house1_16.setText(_translate("MainWindow", "Дом 4"))
        self.floors1_16.setText(_translate("MainWindow", "Этажей"))
        self.live1_16.setText(_translate("MainWindow", "Жильцов"))
        self.lift_61.setText(_translate("MainWindow", "Лифт 61"))
        self.lift_62.setText(_translate("MainWindow", "Лифт 62"))
        self.lift_63.setText(_translate("MainWindow", "Лифт 63"))
        self.lift_64.setText(_translate("MainWindow", "Лифт 64"))
        self.simultation_btn.setText(_translate("MainWindow", "Начать симуляцию"))
        self.menuhelp.setTitle(_translate("MainWindow", "Help"))
