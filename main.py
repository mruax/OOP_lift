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

        self.loop = loop or asyncio.get_event_loop()
        self.elevators = elevators
        self.controller = controller
        self.elevator_views = elevator_views
        self.houses = houses

        self.initiate_ui_values()

        self.lift_window = None
        self.is_running = False

        # self.ui.label.adjustSize()

        self.ui.simultation_btn.clicked.connect(self.simulation_status)  # кнопка статуса симуляции
        for i in range(1, 65):  # кнопки вызова отдельного окна лифта
            lift_button = getattr(self.ui, f"lift_{i}")
            lift_button.clicked.connect(lambda _, id=i: self.open_lift_window(id))

    @asyncSlot()
    async def elevators_simulation(self):
        tasks = []
        for i in range(1, 64 + 1):
            # tasks.append(asyncio.create_task(self.controller))
            # tasks.append(asyncio.create_task(self.lift_simulation(...)))
            # обращаемся через контроллер
            tasks.append(asyncio.create_task(self.controller.elevators[i - 1].simulate_queue))

        self.is_running = True
        while self.is_running:
            a = randint(1, 100)
            await asyncio.sleep(1.0, self.loop)

        for task in tasks:
            task.cancel()

    @asyncSlot()
    async def lift_simulation(self, elevator_id):
        while True:
            elevator = self.controller.elevators[elevator_id - 1]
            house = self.houses[elevator_id - 1]
            a = randint(1, 100)
            if a <= 20:  # 7% на появление вызова
                floor = randint(1, house.floors_amount)
                # для простоты сделаем так, чтобы человек вызывал лифт на этаже только с одной стороны
                if not(house.left_calls[floor] and house.right_calls[floor]):
                    if a % 2 == 1:
                        house.left_calls[floor] = True
                    else:
                        house.right_calls[floor] = True
            await asyncio.sleep(1.0)

    def simulation_status(self):
        if self.is_running:
            self.ui.simultation_btn.setText("Начать симуляцию")
            self.is_running = False
        else:
            self.ui.simultation_btn.setText("Остановить симуляцию")
            self.is_running = True
            self.elevators_simulation()  # начинает симуляцию лифтов после нажатия кнопки

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
        self.is_running = False

    async def simulate_queue(self):
        while self.is_running:
            while not(self.floors_queue.empty()):
                # Сначала добираемся до этажа, а потом вниз спускаемся
                # Для простоты по пути не останавливаясь
                self.target_floor = self.floors_queue.get()
                for i in range(abs(self.target_floor - self.current_floor)):
                    await asyncio.sleep(5.0)
                    if self.target_floor > self.current_floor:
                        self.move_to_floor(self.current_floor + 1)  # вверх
                    else:
                        self.move_to_floor(self.current_floor - 1)  # вниз
                await asyncio.sleep(3.0)
                for i in range(abs(1 - self.current_floor)):
                    await asyncio.sleep(5.0)
                    self.move_to_floor(self.current_floor - 1)  # вниз
                await asyncio.sleep(3.0)
            self.target_floor = None
            await asyncio.sleep(1.0)

    def move_to_floor(self, target_floor):
        self.current_floor = target_floor

    def change_elevator_status(self):
        if self.lift_status:
            self.lift_status = False
        else:
            self.lift_status = True

    def change_door_status(self):
        if self.door_status:
            self.door_status = False
        else:
            self.door_status = True


class ElevatorController:
    def __init__(self, elevators):
        self.elevators = elevators

    def call_elevator(self, elevator_id, target_floor):
        self.elevators[elevator_id - 1].move_to_floor(target_floor)

    def change_elevator_status(self, elevator_id):
        self.elevators[elevator_id - 1].change_elevator_status()

    def change_door_status(self, elevator_id):
        self.elevators[elevator_id - 1].change_door_status()


class ElevatorView(QWidget):
    def __init__(self, houses, controller, elevator_id, floors):
        super().__init__()
        if floors == 3:
            self.ui = Ui_Form_3floors()
        # elif floors == 4:  # TODO
        #     self.ui = Ui_Form_4floors()
        # else:
        #     self.ui = Ui_Form_5floors()
        self.ui.setupUi(self)

        # TODO: init func -> checkbox T/F + ui on ending

        icon = QIcon(str(Path("src/lift.ico")))
        self.setWindowIcon(icon)
        self.setWindowTitle(f"Лифт №{elevator_id}")

        self.houses = houses
        self.controller = controller
        self.elevator_id = elevator_id

        self.initialize_ui()

        self.ui.change_lift_status_btn.clicked.connect(self.change_elevator_status)
        self.ui.change_door_status_btn.clicked.connect(self.change_door_status)

        # self.ui.left_floor_checkbox1.stateChanged.connect(self.elevator_call(floor=1))
        # self.ui.left_floor_checkbox2.stateChanged.connect(self.elevator_call(floor=2))
        # self.ui.left_floor_checkbox3.stateChanged.connect(self.elevator_call(floor=3))
        # self.ui.right_floor_checkbox1.stateChanged.connect(self.elevator_call(floor=1))
        # self.ui.right_floor_checkbox2.stateChanged.connect(self.elevator_call(floor=2))
        # self.ui.right_floor_checkbox3.stateChanged.connect(self.elevator_call(floor=3))
        # if floors == 4:
        #     self.ui.left_floor_checkbox4.stateChanged.connect(self.elevator_call(floor=4))
        #     self.ui.right_floor_checkbox4.stateChanged.connect(self.elevator_call(floor=4))
        # elif floors == 5:
        #     self.ui.left_floor_checkbox4.stateChanged.connect(self.elevator_call(floor=4))
        #     self.ui.right_floor_checkbox4.stateChanged.connect(self.elevator_call(floor=4))
        #     self.ui.left_floor_checkbox5.stateChanged.connect(self.elevator_call(floor=5))
        #     self.ui.right_floor_checkbox5.stateChanged.connect(self.elevator_call(floor=5))

    def initialize_ui(self):
        elevator = self.controller.elevators[self.elevator_id - 1]
        self.ui.label.setText(f"Грузоподъёмность {elevator.capacity}")
        if elevator.lift_status:
            self.ui.lift_status_label.setText(f"Лифт в рабочем состоянии")
        else:
            self.ui.lift_status_label.setText(f"Лифт остановлен")
        if elevator.door_status:
            self.ui.lift_door_status_label.setText(f"Двери открыты")
        else:
            self.ui.lift_door_status_label.setText(f"Двери закрыты")
        self.ui.lift_passengers_label.setText(f"Пассажиров внутри {elevator.passengers}")
        self.ui.lift_current_floor_label.setText(f"Текущий этаж {elevator.current_floor}")
        self.ui.lift_destination_label.setText(f"Направляется на этаж {elevator.target_floor}")
        b = elevator.floors_queue
        queue = []
        while not(b.empty()):
            queue.append(b.get())
        self.ui.lift_queue_label.setText(f"Очередь вызовов {str(queue)}")

        for floor, call in enumerate(self.houses[self.elevator_id - 1].left_calls):
            checkbox = getattr(self.ui, f"left_floor_checkbox{floor + 1}")
            checkbox.setChecked(call)
        for floor, call in enumerate(self.houses[self.elevator_id - 1].right_calls):
            checkbox = getattr(self.ui, f"right_floor_checkbox{floor + 1}")
            checkbox.setChecked(call)

    def change_elevator_status(self):
        self.controller.change_elevator_status(self.elevator_id)
        if self.controller.elevators[self.elevator_id - 1].lift_status:
            self.ui.lift_status_label.setText(f"Лифт в рабочем состоянии")
        else:
            self.ui.lift_status_label.setText(f"Лифт остановлен")

    def change_door_status(self):
        self.controller.change_door_status(self.elevator_id)
        if self.controller.elevators[self.elevator_id - 1].door_status:
            self.ui.lift_door_status_label.setText(f"Двери открыты")
        else:
            self.ui.lift_door_status_label.setText(f"Двери закрыты")

    def elevator_call(self, floor):
        pass
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
    elevator_views = [ElevatorView(houses, controller, elevator.elevator_id, floors=3) for elevator in elevators]

    # Отобразим главное окно после создания лифтов
    window = MainWindow(loop, elevators, controller, elevator_views, houses)
    window.show()

    with loop:
        loop.run_forever()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
