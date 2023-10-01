'''
5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получения значений этого атрибута  нужно использовать методы get и set
5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий

'''
class Base:

    def __init__(self, last_name,first_name, dep):
        self.last_name = last_name
        self.first_name = first_name
        self.__dep = dep

    def get__dep(self):
        return self.__dep
    def hello(self):
        return f'Hello, my name is {self.last_name}  {self.first_name}!'


person_1 = Base('Smith','Alex','devops')

print(Base.__dict__)

print(person_1.hello())
print(person_1.get__dep())

print(person_1.__dict__)


person_2 = Base('Scoth','Nik','test')
print(person_2.hello())

class Tester(Base):
    def __init__(self,last_name, first_name, dep, lang):
        super().__init__(last_name, first_name, dep)
        self.lang = lang
    def name(self):
        return f'My name is {self.first_name} {self.last_name} and I love testing'

tester_1 = Tester('Max','Popov','it','java')
print(tester_1.name())

class ManualTester(Tester):

  def test(self):
      return 'I am tester'


manual_tester1 = ManualTester('Test', 'Alice', 'test', 'python')
print(manual_tester1.lang)
print(manual_tester1.first_name)
print(manual_tester1.test())
print(manual_tester1.hello())
print(manual_tester1.name())