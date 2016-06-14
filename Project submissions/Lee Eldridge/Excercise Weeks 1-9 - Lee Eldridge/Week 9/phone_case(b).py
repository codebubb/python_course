class op_system():

    def __init__(self, battery_life, signal_strength, memory_size, screen_size):
        self.battery_life = battery_life
        self.signal_strength = signal_strength
        self.memory_size = memory_size
        self.screen_size = screen_size
    
    def switch_on(self):
        print "Phone is switching on..."

    def switch_off(self):
        print "Phone is switching off..."

    def make_call(self):
        number = raw_input("Please enter the number you would like to dial: ")
        print "Calling", number+"."

class iPhone_6s(op_system):
    
    def __init__(self, battery_life, signal_strength, memory_size, screen_size):
        self.battery_life = "12 hours"
        self.signal_strength = "100%"
        self.memory_size = "100 gb"
        self.screen_size = "7.4 inches"
    def i_on(self):
        self.switch_on()
        print "Siri says hello."
    def i_off(self):
        self.switch_off()
        print "Siri says goodbye."

class Windows_phone(op_system):
    
    def __init__(self, battery_life, signal_strength, memory_size, screen_size):
        self.battery_life = "17 hours"
        self.signal_strength = "100%"
        self.memory_size = "200 gb"
        self.screen_size = "7.4 inches"
    def i_on(self):
        self.switch_on()
        print "Cortana says hello."
    def i_off(self):
        self.switch_off()
        print "Cortana says goodbye."

iPhone_6s(12, 4, 5, 6).i_on()
#iPhone_6s(12, 4, 5, 6).i_off()

Windows_phone(12, 4, 5, 6).i_on()
