class Men():
    def do_their_work(self):
        print('Вы занимаетесь своим делом')
    def eat(self):
        print('"звуки поглащения пищи"')
    
Adam = Men()
Adam.do_their_work()

class Student(Men):
    def study(self):
        print('Вы учитесь')
Max = Student()
Max.study()
Max.eat()
