class Person(object):
    
    @classmethod
    def first(cls):
        print('first')
    
    first = 'AAA'
        
    def __init__(self, name='anounymos'):
        self.name = name
    
    def name(self):
        print('name')
        
print(Person.first)

person = Person()
print(person.name)
