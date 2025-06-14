class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "hi"
p1 = person("madhu",16)
print(p1)
