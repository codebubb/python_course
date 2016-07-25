class Phone(object):
    def __init__(self, battery_life, signal_strength, memory_size, screen_size):
        self.battery_life = battery_life
        self.signal_strength = signal_strength
        self.memory_size = memory_size
        self.screen_size = screen_size

    def switch_on(self):
        if self.battery_life > 0:
            print "Switching on phone..."

    def switch_off(self):
        print "Switching off phone..."

    def make_call(self):
        if self.signal_strength > 0:
            print "Dialing number..."
