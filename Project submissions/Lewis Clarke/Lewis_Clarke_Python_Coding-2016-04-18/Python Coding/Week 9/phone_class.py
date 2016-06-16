
class Base(object):

    def __init__ (self, batery_life, signal_type, memory_size, screen_size, storage, card_slot):

        self.battery_life      = battery_life
        self.signal_type       = signal_type
        self.memory_size       = memory_size
        self.screen__size      = screen_size
        self.storage           = storage
        self.card_slot         = card_slot

    def turn_on(self):
        print 'initialising'

    def turn_off(self):
        print 'Phone is powering down'

    def low_battery(self):
        print 'Power at 20%'

    def flight_mode(self):
        print 'Flight mode activated'


class iphone6(Base):


    def __init__ (self):

        self.battery_life      = '14 hours standby'
        self.signal_type       = 'GSMA, 3G, LTE'
        self.memory_size       = '2GB Ram'
        self.screen__size      = '4.9 inches'
        self.storage           = '128GB'
        self.card_slot         = 'No'

class Samsung_s7_Edge(Base):


    def __init__ (self):

        self.battery_life      = '16 hours standby'
        self.signal_type       = 'GSMA, 3G, LTE'
        self.memory_size       = '3GB Ram'
        self.screen__size      = '5.5 inches'
        self.storage           = '32GB'
        self.card_slot         = 'yes up to 200GB'

    def edge_case(self):
        print 'Now Shippping with the new Edge case'

class htcm10(Base):

    def __init__(self):

        self.battery_life      = '16 hours standby'
        self.signal_type       = 'GSMA, 3G, LTE'
        self.memory_size       = '4GB Ram'
        self.screen__size      = '5.2 inches'
        self.storage           = '32GB/64BG'
        self.card_slot         = 'yes up to 200GB'


    def sd_card(self):
        print '200BG Kingston sd card included'
