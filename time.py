class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.set_time(hour, minute, second)

    def set_time(self, hour, minute, second):
        if 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60:
            self.hour = hour
            self.minute = minute
            self.second = second
        else:
            raise ValueError("Не верный формат")

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_second(self):
        return self.second

    def print_time(self):
        print(f"{self.hour} часов {self.minute} минут {self.second} секунд")

    def print_time_ampm(self):
        if self.hour >= 12:
            ampm = "p.m."
            hour = self.hour - 12 if self.hour > 12 else self.hour
        else:
            ampm = "a.m."
            hour = self.hour if self.hour > 0 else 12
        print(f"{hour} {ampm} {self.minute} минут {self.second} секунд")

    def increment_second(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.increment_minute()

    def increment_minute(self):
        self.minute += 1
        if self.minute >= 60:
            self.minute = 0
            self.increment_hour()

    def increment_hour(self):
        self.hour += 1
        if self.hour >= 24:
            self.hour = 0


# Пример использования класса
time = Time(16, 18, 3)
time.print_time()  # Выводит: 16 часов 18 минут 3 секунды
time.print_time_ampm()  # Выводит: 4 p.m. 18 минут 3 секунды
time.increment_second()
time.print_time()  # Выводит: 16 часов 18 минут 4 секунды