import asyncio
import faker
from PyQt5.QtGui import QIcon
from qasync import QEventLoop, asyncSlot
from pathlib import Path
from random import randint, choice

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

from generated_ui import Ui_MainWindow
from generated_3floor_lift import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self, loop=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.label.adjustSize()
        self.setWindowTitle("Симулятор оператора лифта")
        # icon = QIcon(str(Path("src/plane.ico")))
        # self.setWindowIcon(icon)

        self.loop = loop

        self.ui.st1_home1_lift1.clicked.connect(self.open_lift_window)

    def closeEvent(self, event):
        self.loop.exec()  # по сути raise error xdd
        event.accept()  # Принимаем событие закрытия

    def open_lift_window(self):
        self.lift_window = ElevatorView()
        self.lift_window.show()


class Elevator:
    def __init__(self, elevator_id):
        self.elevator_id = elevator_id
        self.current_floor = 1
        self.target_floor = None
        self.callbacks = []

    def move_to_floor(self, target_floor):
        self.target_floor = target_floor
        self.notify_observers()

    def register_observer(self, callback):
        self.callbacks.append(callback)

    def notify_observers(self):
        for callback in self.callbacks:
            callback(self.current_floor, self.target_floor)


class ElevatorController:
    def __init__(self, elevators):
        self.elevators = elevators

    def call_elevator(self, elevator_id, target_floor):
        self.elevators[elevator_id].move_to_floor(target_floor)


class ElevatorView(QWidget):
    def __init__(self, controller=1 , elevator=1):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.controller = controller
        self.elevator = elevator
        # self.setWindowTitle(f"Elevator {elevator.elevator_id}")
        # self.setGeometry(100, 100, 300, 200)

        # self.call_button = QPushButton("Call Elevator", self)
        # self.call_button.clicked.connect(self.call_elevator)
        #
        # self.elevator_label = QLabel("Elevator Status:", self)
        #
        # layout = QVBoxLayout()
        # layout.addWidget(self.call_button)
        # layout.addWidget(self.elevator_label)
        # self.setLayout(layout)
        #
        # self.elevator.register_observer(self.update_elevator_label)
    #
    # def call_elevator(self):
    #     target_floor = 5  # Replace with user input
    #     self.controller.call_elevator(self.elevator.elevator_id, target_floor)
    #
    # def update_elevator_label(self, current_floor, target_floor):
    #     status = f"Current Floor: {current_floor}, Target Floor: {target_floor}"
    #     self.elevator_label.setText(status)


def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    window = MainWindow(loop)
    window.show()

    # num_elevators = 3
    # elevators = [Elevator(elevator_id=i) for i in range(num_elevators)]
    # controller = ElevatorController(elevators)
    #
    # elevator_views = [ElevatorView(controller, elevator) for elevator in elevators]
    #
    # # for view in elevator_views:
    # #     view.show()
    #
    # with loop:
    #     loop.run_forever()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
