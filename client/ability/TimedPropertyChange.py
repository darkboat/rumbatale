from client.globals import globals

class TimedPropertyChange:
    def __init__(self, object, property, newValue, time):
        self.object = object
        self.property = property
        self.defaultValue = getattr(getattr(self.object, property[0]), property[1])
        self.newValue = newValue
        self.time = time

        setattr(getattr(self.object, property[0]), property[1], newValue)

        globals.timedChanges.append(self)

    def revertPropertyChange(self):
        setattr(getattr(self.object, self.property[0]), self.property[1], self.defaultValue)