from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):
    """
    The base Employee class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Employee:
        return self._parent

    @parent.setter
    def parent(self, parent: Employee):
        """
        Optionally, the base Employee can declare an interface for setting and
        accessing a parent of the Employee in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Employee class. This way, you won't need to
    expose any concrete Employee classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level Employees.
    """

    def add(self, employee: Employee) -> None:
        pass

    def remove(self, employee: Employee) -> None:
        pass
    
    def getSalary(self, employee: Employee) -> None:
        pass
    
    def getName(self, employee: Employee) -> None:
        pass
    

    def is_manager(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        Employee can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Employee may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Developer(Employee):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-Employees.
    """

    def operation(self) -> str:
        return "80000"
    
class Maintance(Employee):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-Employees.
    """

    def operation(self) -> str:
        return "67000"
    
    
    
class BusinessAnalysis(Employee):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-Employees.
    """

    def operation(self) -> str:
        return "53000"

class Penetration(Employee):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-Employees.
    """

    def operation(self) -> str:
        return " 88000"



class Manager(Employee):
    """
    The Composite class represents the complex Employees that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self) -> None:
        self._children: List[Employee] = []

    """
    A Manager object can add or remove  and get salary other Employees (both simple or
    complex) to or from its child list.
    """

    def add(self, employee: Employee) -> None:
        self._children.append(employee)
        employee.parent = self

    def remove(self, employee: Employee) -> None:
        self._children.remove(employee)
        employee.parent = None
    
    def getName(self, employee: Employee) -> None:
        self._children.getName(employee)
        employee.parent = None
    

    def is_manager(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The manager executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the manager's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(employee: Employee) -> None:
    """
    The client code works with all of the Employees via the base interface.
    """

    print(f"RESULT: {employee.operation()}", end="")


def client_code2(employee1: Employee, employee2: Employee) -> None:
    """
    Thanks to the fact that the child-management operations are declared in the
    base Employee class, the client code can work with any Employee, simple or
    complex, without depending on their concrete classes.
    """

    if employee1.is_manager():
        employee1.add(employee2)

    print(f"RESULT: {employee1.operation()}", end="")
    


if __name__ == "__main__":
    # This way the client code can support the simple leaf Employees...
    simple = Developer()
    print("Client: Pay Scale to Developer:")
    client_code(simple)
    print("\n")
    
    simple1 = BusinessAnalysis()
    print("Client: Pay Scale to BusinessAnalysis:")
    client_code(simple1)
    print("\n")
    
    simple2 = Maintance()
    print("Client: Pay Scale to Maintance:")
    client_code(simple2)
    print("\n")

    # ...as well as the complex composites.
    
    tree = Manager()

    branch1 = Manager()
    branch1.add(Developer())
    branch1.add(Developer())

    branch2 = Manager()
    branch2.add(Developer())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Annual Pay Scales of all Employees:")
    client_code(tree)
    print("\n")

