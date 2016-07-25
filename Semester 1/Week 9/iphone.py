from phone import Phone

class iPhone(Phone):
  def __init__(self, battery_life, signal_strength, memory_size):
    super(iPhone, self).__init__(battery_life, signal_strength, memory_size, 5)

  def updateiTunes(self):
    if self.signal_strength > 0:
      print "Updating iTunes..."
