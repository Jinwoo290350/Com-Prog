class Radio:
    def __init__(self):
        self.__mode = "FM"
        self.__frequency = 87.5
    def get_mode(self) -> str:
        return self.__mode

    def get_frequency(self) -> float:
        return self.__frequency

    def set_mode(self, mode: str) -> None:
        if mode == "FM":
            self.__mode = "FM"
            self.__frequency = 87.5
        elif mode == "AM":
            self.__mode = "AM"
            self.__frequency = 150.0

    def set_frequency(self, frequency: float) -> None:
        if self.__mode == "FM" and 87.5 <= frequency <= 108.0:
            self.__frequency = frequency
        elif self.__mode == "AM" and 150.0 <= frequency <= 280.0:
            self.__frequency = frequency

    def adjust_frequency(self, frequency: float) -> bool:
        new_freq = self.__frequency + frequency
        if self.__mode == "FM" and 87.5 <= new_freq <= 108.0:
            self.__frequency = new_freq
            return True
        elif self.__mode == "AM" and 150.0 <= new_freq <= 280.0:
            self.__frequency = new_freq
            return True
        return False

    def __str__(self) -> str:
        if self.__mode == "AM":
            return f"{self.__mode} Radio: {self.__frequency:.1f} kHz"
        else:
            return f"{self.__mode} Radio: {self.__frequency:.1f} MHz"