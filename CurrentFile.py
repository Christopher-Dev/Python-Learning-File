#classes and objects

class Robot:
    def _init_(self, n, c, w):
        self.name = name
        self.color = c
        self.weight = w
        
    def introduce_self(self):
        print('My name is ' + self.name)

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)

class Person:
    def _init_(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i
        
    def sit_down(self):
        self.is_sitting = True
        
    def stand_up(self):
        self.is_sitting = False
        
    