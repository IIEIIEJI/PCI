__author__ = 'tburnashevr'
class Subject():
    def __init__(self):
        self.observers = set()

    def register(self, observer):
        self.observers.add(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(self, msg)


class Observer():
    def __init__(self, name):
        self.name = name

    def update(self, subject, msg):
        print '[Observer {0}]: <{1}>'.format(self.name, msg)


tony = Observer('Tony')
angela = Observer('Angela')

subject = Subject()
subject.register(tony)
subject.register(angela)

subject.notify('Hello world!')
# [Observer Tony]: `Hello world!`
# [Observer Angela]: `Hello world!