import time

class TrafficLight:

    color1 = 'red'
    color2 = 'yellow'
    color3 = 'green'

    def __running(self):
        while True:
            self.color1
            time.sleep(2)
            print('now light red')
            self.color2
            time.sleep(7)
            print('now light yellow')
            self.color3
            time.sleep(4)
            print('now light green')

trl = TrafficLight()
trl._TrafficLight__running()
