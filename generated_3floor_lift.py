# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3floor_lift_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(609, 705)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 591, 541))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_part_4 = QtWidgets.QVBoxLayout()
        self.left_part_4.setObjectName("left_part_4")
        self.left_floor_layout_10 = QtWidgets.QHBoxLayout()
        self.left_floor_layout_10.setObjectName("left_floor_layout_10")
        self.left_floor_lbl_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.left_floor_lbl_3.setObjectName("left_floor_lbl_3")
        self.left_floor_layout_10.addWidget(self.left_floor_lbl_3)
        self.left_floor_checkbox3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.left_floor_checkbox3.setCheckable(True)
        self.left_floor_checkbox3.setObjectName("left_floor_checkbox3")
        self.left_floor_layout_10.addWidget(self.left_floor_checkbox3)
        self.left_part_4.addLayout(self.left_floor_layout_10)
        self.line_11 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.left_part_4.addWidget(self.line_11)
        self.left_floor_layout_11 = QtWidgets.QHBoxLayout()
        self.left_floor_layout_11.setObjectName("left_floor_layout_11")
        self.left_floor_lbl_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.left_floor_lbl_2.setObjectName("left_floor_lbl_2")
        self.left_floor_layout_11.addWidget(self.left_floor_lbl_2)
        self.left_floor_checkbox2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.left_floor_checkbox2.setCheckable(True)
        self.left_floor_checkbox2.setObjectName("left_floor_checkbox2")
        self.left_floor_layout_11.addWidget(self.left_floor_checkbox2)
        self.left_part_4.addLayout(self.left_floor_layout_11)
        self.line_12 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.left_part_4.addWidget(self.line_12)
        self.left_floor_layout_12 = QtWidgets.QHBoxLayout()
        self.left_floor_layout_12.setObjectName("left_floor_layout_12")
        self.left_floor_lbl_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.left_floor_lbl_1.setObjectName("left_floor_lbl_1")
        self.left_floor_layout_12.addWidget(self.left_floor_lbl_1)
        self.left_floor_checkbox1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.left_floor_checkbox1.setCheckable(True)
        self.left_floor_checkbox1.setObjectName("left_floor_checkbox1")
        self.left_floor_layout_12.addWidget(self.left_floor_checkbox1)
        self.left_part_4.addLayout(self.left_floor_layout_12)
        self.horizontalLayout_2.addLayout(self.left_part_4)
        self.line_13 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_2.addWidget(self.line_13)
        self.lift_floor_slider_2 = QtWidgets.QSlider(self.horizontalLayoutWidget_6)
        self.lift_floor_slider_2.setOrientation(QtCore.Qt.Vertical)
        self.lift_floor_slider_2.setObjectName("lift_floor_slider_2")
        self.horizontalLayout_2.addWidget(self.lift_floor_slider_2)
        self.line_14 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.horizontalLayout_2.addWidget(self.line_14)
        self.right_part_2 = QtWidgets.QVBoxLayout()
        self.right_part_2.setObjectName("right_part_2")
        self.right_floor_layout_14 = QtWidgets.QHBoxLayout()
        self.right_floor_layout_14.setObjectName("right_floor_layout_14")
        self.right_floor_lbl_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.right_floor_lbl_3.setObjectName("right_floor_lbl_3")
        self.right_floor_layout_14.addWidget(self.right_floor_lbl_3)
        self.right_floor_checkbox3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.right_floor_checkbox3.setCheckable(True)
        self.right_floor_checkbox3.setObjectName("right_floor_checkbox3")
        self.right_floor_layout_14.addWidget(self.right_floor_checkbox3)
        self.right_part_2.addLayout(self.right_floor_layout_14)
        self.line_15 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.right_part_2.addWidget(self.line_15)
        self.right_floor_layout_15 = QtWidgets.QHBoxLayout()
        self.right_floor_layout_15.setObjectName("right_floor_layout_15")
        self.right_floor_lbl_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.right_floor_lbl_2.setObjectName("right_floor_lbl_2")
        self.right_floor_layout_15.addWidget(self.right_floor_lbl_2)
        self.right_floor_checkbox2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.right_floor_checkbox2.setCheckable(True)
        self.right_floor_checkbox2.setObjectName("right_floor_checkbox2")
        self.right_floor_layout_15.addWidget(self.right_floor_checkbox2)
        self.right_part_2.addLayout(self.right_floor_layout_15)
        self.line_16 = QtWidgets.QFrame(self.horizontalLayoutWidget_6)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.right_part_2.addWidget(self.line_16)
        self.right_floor_layout_16 = QtWidgets.QHBoxLayout()
        self.right_floor_layout_16.setObjectName("right_floor_layout_16")
        self.right_floor_lbl_1 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.right_floor_lbl_1.setObjectName("right_floor_lbl_1")
        self.right_floor_layout_16.addWidget(self.right_floor_lbl_1)
        self.right_floor_checkbox1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_6)
        self.right_floor_checkbox1.setCheckable(True)
        self.right_floor_checkbox1.setObjectName("right_floor_checkbox1")
        self.right_floor_layout_16.addWidget(self.right_floor_checkbox1)
        self.right_part_2.addLayout(self.right_floor_layout_16)
        self.horizontalLayout_2.addLayout(self.right_part_2)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 560, 591, 131))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.operator_functions = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.operator_functions.setContentsMargins(0, 0, 0, 0)
        self.operator_functions.setObjectName("operator_functions")
        self.lift_info = QtWidgets.QVBoxLayout()
        self.lift_info.setObjectName("lift_info")
        self.lift_status_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lift_status_label.setObjectName("lift_status_label")
        self.lift_info.addWidget(self.lift_status_label)
        self.lift_door_status_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lift_door_status_label.setObjectName("lift_door_status_label")
        self.lift_info.addWidget(self.lift_door_status_label)
        self.lift_passengers_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lift_passengers_label.setObjectName("lift_passengers_label")
        self.lift_info.addWidget(self.lift_passengers_label)
        self.lift_current_floor_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lift_current_floor_label.setObjectName("lift_current_floor_label")
        self.lift_info.addWidget(self.lift_current_floor_label)
        self.lift_destination_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lift_destination_label.setObjectName("lift_destination_label")
        self.lift_info.addWidget(self.lift_destination_label)
        self.lift_queue_label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.lift_queue_label.setObjectName("lift_queue_label")
        self.lift_info.addWidget(self.lift_queue_label)
        self.operator_functions.addLayout(self.lift_info)
        self.lift_functions = QtWidgets.QVBoxLayout()
        self.lift_functions.setObjectName("lift_functions")
        self.change_lift_status_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.change_lift_status_btn.setObjectName("change_lift_status_btn")
        self.lift_functions.addWidget(self.change_lift_status_btn)
        self.change_door_status_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.change_door_status_btn.setObjectName("change_door_status_btn")
        self.lift_functions.addWidget(self.change_door_status_btn)
        self.send_to_floor_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.send_to_floor_btn.setObjectName("send_to_floor_btn")
        self.lift_functions.addWidget(self.send_to_floor_btn)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label.setObjectName("label")
        self.lift_functions.addWidget(self.label)
        self.operator_functions.addLayout(self.lift_functions)
        self.operator_functions.setStretch(0, 7)
        self.operator_functions.setStretch(1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.left_floor_lbl_3.setText(_translate("Form", "Этаж 3"))
        self.left_floor_checkbox3.setText(_translate("Form", "Вызов"))
        self.left_floor_lbl_2.setText(_translate("Form", "Этаж 2"))
        self.left_floor_checkbox2.setText(_translate("Form", "Вызов"))
        self.left_floor_lbl_1.setText(_translate("Form", "Этаж 1"))
        self.left_floor_checkbox1.setText(_translate("Form", "Вызов"))
        self.right_floor_lbl_3.setText(_translate("Form", "Этаж 3"))
        self.right_floor_checkbox3.setText(_translate("Form", "Вызов"))
        self.right_floor_lbl_2.setText(_translate("Form", "Этаж 2"))
        self.right_floor_checkbox2.setText(_translate("Form", "Вызов"))
        self.right_floor_lbl_1.setText(_translate("Form", "Этаж 1"))
        self.right_floor_checkbox1.setText(_translate("Form", "Вызов"))
        self.lift_status_label.setText(_translate("Form", "Лифт в рабочем состоянии"))
        self.lift_door_status_label.setText(_translate("Form", "Двери закрыты"))
        self.lift_passengers_label.setText(_translate("Form", "Пассажиров внутри 0"))
        self.lift_current_floor_label.setText(_translate("Form", "Текущий этаж 1"))
        self.lift_destination_label.setText(_translate("Form", "Направляется на этаж None"))
        self.lift_queue_label.setText(_translate("Form", "Очередь вызовов []"))
        self.change_lift_status_btn.setText(_translate("Form", "Остановить/Запустить"))
        self.change_door_status_btn.setText(_translate("Form", "Открыть/Закрыть двери"))
        self.send_to_floor_btn.setText(_translate("Form", "Отправить на этаж n"))
        self.label.setText(_translate("Form", "Грузоподъёмность 100"))
