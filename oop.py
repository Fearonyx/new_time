class Bag(object):
    def __init__(self, ):
        self.capacity = 100
        self.storage = []

    def is_fit(self, thing):
        if self.capacity >= thing.volume:
            self.capacity -= thing.volume
            self.storage.append(thing.name)

        else:
            print(f'Not enough space for {thing.name}.')

        return self.storage, self.capacity


class Packet(Bag):
    def __init__(self):
        super().__init__()
        self.capacity = 35


class Object(object):
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


objects = {'bottle': 15, 'apple': 7, 'notebook': 32, 'car': 200}
bag = Bag()
packet = Packet()
for key, value in objects.items():
    thing = Object(key, value)
    bag.is_fit(thing)
    packet.is_fit(thing)
egg = Object('egg', 1)
bag.is_fit(egg)
s = ' '.join(item for item in bag.storage)
print(f'{s} is in bag. Free space is {bag.capacity}')

s = ' '.join(item for item in packet.storage)
print(f'{s} is in bag. Free space is {packet.capacity}')


