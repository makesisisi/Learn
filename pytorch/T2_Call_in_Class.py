class person:
    def __init__(self):
        print("init completed")
    
    def __call__(self, name):
        print("__call__" + "hello " + name)
        
    def hello(self, name):
        print("hello " + name)
        