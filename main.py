import asyncio
import faker
from PyQt5.QtGui import QIcon
from qasync import QEventLoop, asyncSlot
from pathlib import Path
from random import randint, choice
from queue import Queue

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

from generated_ui import Ui_MainWindow
from generated_3floor_lift import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self, loop, elevators, controller, elevator_views):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.label.adjustSize()
        self.setWindowTitle("Симулятор оператора лифта")
        # icon = QIcon(str(Path("src/plane.ico")))
        # self.setWindowIcon(icon)

        self.loop = loop

        self.elevators = elevators
        self.controller = controller
        self.elevator_views = elevator_views

        self.lift_window = None
        # self.ui.lift_1.clicked.connect(self.open_lift_window(1))
        for i in range(1, 65):
            lift_button = getattr(self.ui, f"lift_{i}")
            lift_button.clicked.connect(lambda _, id=i: self.open_lift_window(id))

    def closeEvent(self, event):
        self.loop.exec()  # по сути raise error xdd
        event.accept()  # Принимаем событие закрытия

    # @asyncSlot()
    def open_lift_window(self, id):
        self.elevator_views[id - 1].show()


class Elevator:
    def __init__(self, street_id, house_id, elevator_id, capacity):
        # Расположение
        self.street_id = street_id
        self.house_id = house_id
        self.elevator_id = elevator_id

        # Технические хар-ки
        self.capacity = capacity  # грузоподьёмность
        self.passengers = 0  # количество пассажиров внутри
        self.door_status = False  # двери открыты/закрыты
        self.lift_status = True  # состояние лифта вкл/выкл

        # Переменные логики
        self.current_floor = 1
        self.target_floor = None
        self.floors_queue = Queue()
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
    def __init__(self, controller, elevator):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.controller = controller
        self.elevator = elevator
        self.setWindowTitle(f"Elevator {elevator.elevator_id}")
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

    num_elevators = 4 * 4 * 4
    elevators = []
    for id in range(1, num_elevators + 1):
        elevators.append(Elevator(street_id=(id + 4 - 1) // 2 + 1, house_id=id % 4 + 1, elevator_id=id,
                                  capacity=randint(6, 14) * 50))
    controller = ElevatorController(elevators)
    elevator_views = [ElevatorView(controller, elevator) for elevator in elevators]

    # for view in elevator_views:
    #     view.show()

    # Отобразим главное окно после создания лифтов
    window = MainWindow(loop=loop, elevators=elevators, controller=controller, elevator_views=elevator_views)
    window.show()

    with loop:
        loop.run_forever()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
