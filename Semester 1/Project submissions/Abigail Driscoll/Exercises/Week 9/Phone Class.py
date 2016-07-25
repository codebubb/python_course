class base():
    def __init__(self, battery_life, memory_size, camera_quality, screen_size, resolution)
        self.battery_life = battery_life
        self.memory_size = memory_size
        self.camera_quality = camera_quality
        self.screen_size = screen_size
        self.resolution = resolution
    def switch_on(self):
        print("Hello, phone is turning on")

    def switch_off(self):
        print("Goodbye, phone is shutting down")

    def make_call(self):
        print("Now calling")

    def low_battery(self):
        print("Low battery, please charge)"

class iphone_5c(base):
            def __init__(self):
                self.battery_life = "28 Hours"
                self.memory_size = "8 GB"
                self.camera_quality = "8 megapixels"
                self.resolution = "640 x 1136"


class Sony_Experia(base):
