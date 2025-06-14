class animal:
    def __init__(self, habitat):
        self.habitat = habitat
    def print_habitat(self):
        print(self.habitat)
    def sound(se,how):
        se.how = how
        print(se.how)
class dog(animal):
    def __init__(slf):
        super().__init__("they always eats")
    def soun(sel):
        print("haaa")
x = dog()
x.print_habitat()
x.sound("emo")
        
