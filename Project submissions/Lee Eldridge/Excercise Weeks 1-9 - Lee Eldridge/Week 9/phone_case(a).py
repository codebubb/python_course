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


new_phone = op_system("12 hours", "100%", "100 gb", "7 inches")
new_phone.make_call()
