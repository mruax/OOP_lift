import asyncio
import faker
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
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

    @asyncSlot()  # это все 64 таски, цикл с loop
    async def elevators_simulation(self):
        tasks = []
        for id in range(1, 64 + 1):
            # tasks.append(asyncio.create_task(self.controller))
            tasks.append(asyncio.create_task(self.lift_simulation(elevator_id=id)))
            # обращаемся через контроллер
            tasks.append(asyncio.create_task(self.controller.elevators[id - 1].simulate_queue()))

        self.is_running = True
        while self.is_running:
            a = randint(1, 100)
            print(a)
            await asyncio.sleep(1.0, self.loop)

        for task in tasks:
            task.cancel()

    # @asyncSlot() - это отдельная таска, свой цикл без общего loop
    async def lift_simulation(self, elevator_id):
        elevator = self.controller.elevators[elevator_id - 1]
        house = self.houses[elevator_id - 1]
        while True:
            a = randint(1, 100)
            if a <= 20:  # 13% на появление вызова
                floor = randint(1, house.floors_amount) - 1
                # для простоты сделаем так, чтобы человек вызывал лифт на этаже только с одной стороны
                if not(house.left_calls[floor] or house.right_calls[floor]):
                    if a % 2 == 1:
                        house.left_calls[floor] = True
                    else:
                        house.right_calls[floor] = True
                    self.elevator_views[elevator_id - 1].update_checkboxes()

                    elevator.floors_queue.put(floor + 1)

            # self.elevator_views[elevator_id - 1].ui.label.setText(str(a))  # ===============================
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
    def __init__(self, street_id, house_id, elevator_id, capacity, floors_amount):
        # Расположение
        self.street_id = street_id
        self.house_id = house_id
        self.elevator_id = elevator_id

        # Количество этажей в доме с этим лифтом
        self.floors_amount = floors_amount

        # Технические хар-ки
        self.capacity = capacity  # грузоподьёмность
        self.passengers = 0  # количество пассажиров внутри
        self.door_status = False  # двери открыты/закрыты
        self.lift_status = True  # состояние лифта вкл/выкл

        # Переменные логики
        self.current_floor = 1
        self.target_floor = None
        self.floors_queue = Queue()

        # self.callbacks = []  # это важная часть, для общения между моделью и контроллером
        self.scroll_callback = None
        self.checkers_callback = None
        self.door_status_callback = None
        self.passengers_status_callback = None
        self.current_floor_status_callback = None
        self.target_floor_status_callback = None
        self.queue_status_callback = None

        self.is_running = True

    async def simulate_queue(self):
        step = 100 // (self.floors_amount - 1)
        while self.is_running:
            while not(self.floors_queue.empty()):
                # Сначала добираемся до этажа, а потом вниз спускаемся
                # Для простоты по пути не останавливаясь
                # self.notify_observer_ql(self.elevator_id)
                self.target_floor = self.floors_queue.get()
                status = 1
                passengers = 0
                if not(self.target_floor == self.current_floor):
                    self.notify_observer_ck(self.current_floor)
                    # self.notify_observer_cf(self.current_floor)
                    # self.notify_observer_tf(self.target_floor)
                    for i in range(abs(self.target_floor - self.current_floor)):
                        # self.notify_observer_cf(self.current_floor)
                        if self.target_floor > self.current_floor:
                            for j in range(10):
                                status += step / 10
                                self.notify_observer_sc(status)
                                await asyncio.sleep(6.0 / 10)
                            self.move_to_floor(self.current_floor + 1)  # вверх
                        else:
                            for j in range(10):
                                status -= step / 10
                                self.notify_observer_sc(status)
                                await asyncio.sleep(6.0 / 10)
                            self.move_to_floor(self.current_floor - 1)  # вниз
                    self.notify_observer_ds(True)
                    await asyncio.sleep(3.0)
                    passengers += randint(1, 4)
                    # self.notify_observer_pa(passengers)
                    self.notify_observer_ds(False)
                    self.notify_observer_sc(status)
                    self.notify_observer_ck(self.current_floor)

                    # random_floor = randint(1, self.floors_amount)
                    # self.target_floor = random_floor
                    # self.notify_observer_tf(self.target_floor)
                    for i in range(abs(1 - self.current_floor)):
                        # self.notify_observer_cf(self.current_floor)
                        for j in range(10):
                            status -= step / 10
                            self.notify_observer_sc(status)
                            await asyncio.sleep(6.0 / 10)
                        self.move_to_floor(self.current_floor - 1)  # вниз
                    passengers = 0
                    # self.notify_observer_pa(passengers)
                else:
                    self.notify_observer_ck(self.current_floor)
                    # self.notify_observer_tf(self.target_floor)
                    # self.notify_observer_cf(self.current_floor)
                    # self.notify_observer_pa(passengers)

                self.notify_observer_ds(True)
                await asyncio.sleep(3.0)
                # self.notify_observer_pa(passengers)
                # self.notify_observer_tf(self.target_floor)
                # self.notify_observer_cf(self.current_floor)
                self.notify_observer_ds(False)
                self.notify_observer_sc(status)
                self.notify_observer_ck(self.current_floor)
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

    def register_sc_observer(self, callback):
        self.scroll_callback = callback

    def register_ck_observer(self, callback):
        self.checkers_callback = callback

    def register_ds_observer(self, callback):
        self.door_status_callback = callback

    # def register_pa_observer(self, callback):
    #     self.passengers_status_callback = callback
    #
    # def register_cf_observer(self, callback):
    #     self.current_floor_status_callback = callback
    #
    # def register_tf_observer(self, callback):
    #     self.target_floor_status_callback = callback

    # def register_ql_observer(self, callback):
    #     self.queue_status_callback = callback

    def notify_observer_sc(self, status):
        self.scroll_callback(status)

    def notify_observer_ck(self, floor):
        self.checkers_callback(floor)

    def notify_observer_ds(self, status):
        self.door_status_callback(status)

    # def notify_observer_pa(self, passengers):
    #     self.passengers_status_callback(passengers)
    #
    # def notify_observer_cf(self, current_floor):
    #     self.current_floor_status_callback(current_floor)
    #
    # def notify_observer_tf(self, target_floor):
    #     self.target_floor_status_callback(target_floor)

    # def notify_observer_ql(self, elevator_id):
    #     self.queue_status_callback(elevator_id)


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

        icon = QIcon(str(Path("src/lift.ico")))
        self.setWindowIcon(icon)
        self.setWindowTitle(f"Лифт №{elevator_id}")

        self.houses = houses
        self.controller = controller
        self.elevator_id = elevator_id

        self.initialize_ui()

        self.ui.lift_floor_slider_2.setStyleSheet("QSlider::handle:vertical { background-image: url('src/lift_v2.png'); }")
        # self.ui.lift_floor_slider_2.setStyleSheet(
        #     """
        #     QSlider::handle:vertical {
        #         background-image: url('src/lift_v2.png');
        #         height: 15px;
        #         width: 15px;
        #     }
        #     """
        # )


        self.ui.change_lift_status_btn.clicked.connect(self.change_elevator_status)
        self.ui.change_door_status_btn.clicked.connect(self.change_door_status)

        self.controller.elevators[self.elevator_id - 1].register_sc_observer(self.update_elevator_scrollbar)
        self.controller.elevators[self.elevator_id - 1].register_ck_observer(self.update_elevator_status)
        self.controller.elevators[self.elevator_id - 1].register_ds_observer(self.update_door_status)
        # self.controller.elevators[self.elevator_id - 1].register_pa_observer(self.update_passangers_status)
        # self.controller.elevators[self.elevator_id - 1].register_cf_observer(self.update_current_floor_status)
        # self.controller.elevators[self.elevator_id - 1].register_tf_observer(self.update_target_floor_status)
        # self.controller.elevators[self.elevator_id - 1].register_ql_observer(self.update_queue_status)

        # self.ui.left_floor_checkbox1.stateChanged.connect(self.elevator_call)
        # self.ui.left_floor_checkbox2.stateChanged.connect(self.elevator_call)
        # self.ui.left_floor_checkbox3.stateChanged.connect(self.elevator_call)
        # self.ui.right_floor_checkbox1.stateChanged.connect(self.elevator_call)
        # self.ui.right_floor_checkbox2.stateChanged.connect(self.elevator_call)
        # self.ui.right_floor_checkbox3.stateChanged.connect(self.elevator_call)
        # if floors == 4:
        #     self.ui.left_floor_checkbox4.stateChanged.connect(self.elevator_call)
        #     self.ui.right_floor_checkbox4.stateChanged.connect(self.elevator_call)
        # elif floors == 5:
        #     self.ui.left_floor_checkbox4.stateChanged.connect(self.elevator_call)
        #     self.ui.right_floor_checkbox4.stateChanged.connect(self.elevator_call)
        #     self.ui.left_floor_checkbox5.stateChanged.connect(self.elevator_call)
        #     self.ui.right_floor_checkbox5.stateChanged.connect(self.elevator_call)

    def initialize_ui(self, status=None):
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
        self.update_checkboxes()

    def update_checkboxes(self):
        for floor, call in enumerate(self.houses[self.elevator_id - 1].left_calls):
            checkbox = getattr(self.ui, f"left_floor_checkbox{floor + 1}")
            checkbox.setChecked(call)
        for floor, call in enumerate(self.houses[self.elevator_id - 1].right_calls):
            checkbox = getattr(self.ui, f"right_floor_checkbox{floor + 1}")
            checkbox.setChecked(call)

    def change_elevator_status(self):
        self.controller.change_elevator_status(self.elevator_id)
        if self.controller.elevators[self.elevator_id - 1].lift_status:
            self.ui.lift_status_label.setText("Лифт в рабочем состоянии")
        else:
            self.ui.lift_status_label.setText("Лифт остановлен")

    def change_door_status(self):
        self.controller.change_door_status(self.elevator_id)
        if self.controller.elevators[self.elevator_id - 1].door_status:
            self.ui.lift_door_status_label.setText("Двери открыты")
        else:
            self.ui.lift_door_status_label.setText("Двери закрыты")

    def update_elevator_scrollbar(self, status):
        self.ui.lift_floor_slider_2.setValue(int(status))

    def update_elevator_status(self, floor):
        self.houses[self.elevator_id - 1].left_calls[floor - 1] = False
        self.houses[self.elevator_id - 1].right_calls[floor - 1] = False

    def update_door_status(self, status):
        if status:
            self.ui.lift_door_status_label.setText("Двери открыты")
        else:
            self.ui.lift_door_status_label.setText("Двери закрыты")

    # def update_passangers_status(self, passengers):
    #     self.ui.lift_passengers_label.setText(f"Пассажиров внутри {passengers}")
    #
    # def update_current_floor_status(self, current_floor):
    #     self.ui.lift_current_floor_label.setText(f"Текущий этаж {current_floor}")
    #
    # def update_target_floor_status(self, target_floor):
    #     self.ui.lift_destination_label.setText(f"Направляется на этаж {target_floor}")

    # def update_queue_status(self, elevator_id):
    #     b = self.controller.elevators[elevator_id - 1].floors_queue copy.deepcopy <-
    #     queue = []
    #     while not (b.empty()):
    #         queue.append(b.get())
    #     self.ui.lift_queue_label.setText(f"Очередь вызовов {str(queue)}")

    # def elevator_call(self):
    #     pass  # не изменяем флаг


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

        elevators.append(Elevator(street_id, house_id, id, capacity, floors_amount))
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
