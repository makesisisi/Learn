class student:
    def __init__(self,a,b,c,d):
        self.name = a
        self.sex = b
        self.age = c
        self.size = d

    def listen(self):
        print('听课')

    def write(self):
        print('写作业')

stu1 = student('张三','男',15,165)
stu1.listen()