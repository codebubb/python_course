class base():
    def __init__(self, battery_life, signal_strength, cpu, gpu, memory_size, ram, camera_quality, screen_size, resolution, card_slot):
        self.battery_life    = battery_life
        self.signal_strength = signal_strength
        self.cpu             = cpu
        self.gpu             = gpu
        self.memory_size     = memory_size
        self.ram             = ram
        self.camera_quality  = camera_quality
        self.screen_size     = screen_size
        self.resolution      = resolution
        self.card_slot       = card_slot
        
    def switch_on(self):
        print "Starting up phone"

    def switch_off(self):
        print "Shutting down phone"

    def make_call(self):
        print "Calling"

    def low_bat(self):
        print "Battery low, charge"


class iphone_6s(base):
    def __init__(self):
        self.battery_life    = "240 hours"
        self.signal_strength = "GSM / CDMA / HSPA / EVDO / LTE"
        self.cpu             = "Dual-core 1.84 GHz Twister"
        self.gpu             = "PowerVR GT7600 (six-core graphics)"
        self.memory_size     = "16/64/128 GB"
        self.ram             = "2 GB RAM"
        self.camera_quality  = "12 MP, f/2.2, 29mm, phase detection autofocus, dual-LED (dual tone) flash"
        self.screen_size     = "4.7 inches"
        self.resolution      = "750 x 1334 pixels (~326 ppi pixel density)"
        self.card_slot       = "No memory card slot"

    def fake_accessory(self):
        print "This cable or accessory is not certified and may not work reliably with this iPhone."


class samsung_s7(base):
    def __init__(self):
        self.battery_life    = "480 hours"
        self.signal_strength = "GSM / HSPA / LTE"
        self.cpu             = "Dual-core 2.15 GHz Kryo & dual-core 1.6 GHz Kryo, Quad-core 2.3 GHz Mongoose + quad-core 1.6 GHz Cortex-A53"
        self.gpu             = "Adreno 530, Mali-T880 MP12"
        self.memory_size     = "32/64 GB"
        self.ram             = "4 GB RAM"
        self.camera_quality  = "12 MP, f/1.7, 26mm, phase detection autofocus, OIS, LED flash"
        self.screen_size     = "5.1 inches"
        self.resolution      = "1440 x 2560 pixels (~577 ppi pixel density)"
        self.card_slot       = "microSD, up to 200 GB"

    def app_protector(self):
        print "SMART APP PROTECTOR. Smart app protector is running."


class xperia_z5(base):
    def __init__(self):
        self.battery_life    = "520 hours"
        self.signal_strength = "GSM / HSPA / LTE"
        self.cpu             = "Quad-core 1.5 GHz Cortex-A53 & Quad-core 2.0 GHz Cortex-A57"
        self.gpu             = "Adreno 430"
        self.memory_size     = "32 GB"
        self.ram             = "3 GB RAM"
        self.camera_quality  = "23 MP, f/2.0, 24mm, phase detection autofocus, LED flash"
        self.screen_size     = "5.2 inches"
        self.resolution      = "1080 x 1920 pixels (~428 ppi pixel density)"
        self.card_slot       = "microSD, up to 200 GB"

    def unlock(self):
        print "Swipe up or down to unlock"


specs = iphone_6s()
specs.fake_accessory() # Testing to see if iphone_6s fake_accessory method runs.
print specs.cpu # Testing to see if iphone_6s self.cpu member prints.

