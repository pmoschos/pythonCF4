class AbstractStudentDAO:
    """Defines the Student DAO API"""

    def insert(self):
        raise NotImplementedError()
    
    def update(self):
        raise NotImplementedError()
    
    def delete(self):
        raise NotImplementedError()
    
    def getOne(self):
        raise NotImplementedError()

class StudentImpl(AbstractStudentDAO):
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def getOne(self):
        pass

from abc import ABC, abstractmethod

class ABCInventory(ABC):

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        pass

class Inventory(ABCInventory):
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.add_item(item)
    
    