import asyncio
import faker
from PyQt5.QtGui import QIcon
from faker import Faker
from qasync import QEventLoop, asyncSlot
from pathlib import Path
from random import randint, choice
from queue import Queue

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
import sys

from generated_ui import Ui_MainWindow
from generated_3floor_lift import Ui_Form as Ui_Form_3floors


class MainWindow(QMainWindow):
    def __init__(self, loop, elevators, controller, elevator_views, houses):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Симулятор оператора лифта")
        icon = QIcon(str(Path("src/lift.ico")))
        self.setWindowIcon(icon)

        self.loop = loop
        self.elevators = elevators
        self.controller = controller
        self.elevator_views = elevator_views
        self.houses = houses

        self.initiate_ui_values()

        self.lift_window = None

        # self.ui.label.adjustSize()

        # self.ui.lift_1.clicked.connect(self.open_lift_window(1))
        for i in range(1, 65):
            lift_button = getattr(self.ui, f"lift_{i}")
            lift_button.clicked.connect(lambda _, id=i: self.open_lift_window(id))

    @asyncSlot()
    async def elevators_simulation(self):
        pass

    def initiate_ui_values(self):
        fake = Faker('ru_RU')
        for i in range(1, 4 + 1):
            address = getattr(self.ui, f"address{i}")
            address.setText(f"Адрес - {fake.street_name()}")
        self.ui.floors1.setText(f"Этажей - {self.houses[0].floors_amount}")
        self.ui.live1.setText(f"Жильцов - {self.houses[0].live}")
        for i in range(2, 16 + 1):
            floor = getattr(self.ui, f"floors1_{i}")
            floor.setText(f"Этажей - {self.houses[i - 1].floors_amount}")
            live = getattr(self.ui, f"live1_{i}")
            live.setText(f"Жильцов - {self.houses[i - 1].live}")


    def closeEvent(self, event):
        self.loop.exec()  # по сути raise error xdd
        event.accept()  # Принимаем событие закрытия

    # @asyncSlot()
    def open_lift_window(self, id):
        self.elevator_views[id - 1].show()


class House:
    def __init__(self, street_id, house_id, floors_amount, live):
        # Расположение
        self.street_id = street_id
        self.house_id = house_id

        # Технические хар-ки
        self.live = live  # количество жителей

        # Переменные логики
        self.floors_amount = floors_amount
        self.left_calls = [False] * floors_amount
        self.right_calls = [False] * floors_amount



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
    def __init__(self, controller, elevator, floors):
        super().__init__()
        if floors == 3:
            self.ui = Ui_Form_3floors()
        # elif floors == 4:  # TODO
        #     self.ui = Ui_Form_4floors()
        # else:
        #     self.ui = Ui_Form_5floors()
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

    # Создадим классы лифтов, контроллеров и интерфейсов, а также самих домов
    num_elevators = 4 * 4 * 4
    elevators = []
    houses = []
    for id in range(1, num_elevators + 1):
        street_id = (id + 4 - 1) // 2 + 1
        house_id = id % 4 + 1
        floors_amount = 3  # TODO: random floors
        live = randint(100, 999)
        capacity = randint(6, 14) * 50

        elevators.append(Elevator(street_id, house_id, id, capacity))
        houses.append(House(street_id, house_id, floors_amount, live))
    controller = ElevatorController(elevators)
    elevator_views = [ElevatorView(controller, elevator, floors=3) for elevator in elevators]

    # Отобразим главное окно после создания лифтов
    window = MainWindow(loop, elevators, controller, elevator_views, houses)
    window.show()

    with loop:
        loop.run_forever()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
