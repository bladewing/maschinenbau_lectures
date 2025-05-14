import time


class Countdown:
    def __init__(self, name, val):
        self.remaining = val
        self.name = name
        self.state = "stopped"

    def start(self):
        self.state = "running"

    def stop(self):
        self.state = "stopped"

    def over(self):
        if self.remaining > 0:
            return False
        else:
            return True

    def tick(self):
        if self.state == "running":
            self.remaining = self.remaining - 1

    def restart(self, val):
        self.remaining = val
        self.state = "running"


countdown = Countdown("Sprengung", 15)

countdown.start()

while not countdown.over():
    print(countdown.name, " verbleibend:", countdown.remaining)
    time.sleep(1)
    countdown.tick()
print("bang")
