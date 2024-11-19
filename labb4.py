from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
  def __init__(self) -> None:
    self.items: List[T] = []

  def push(self, item: T) -> None:
    self.items.append(item)
    return self.items
  
  def pop(self) -> T:
    if self.items:
      return self.items.pop()
    else:
      return "Empty List"
  
  def is_empty(self) -> bool:
    return len(self.items) == 0
  
  def size(self) -> int:
    return len(self.items)
  
intStack = Stack[int]()
intStack.push(1)
intStack.push(2)
print(intStack.pop())
print(intStack.is_empty())

strStack = Stack[str]()
strStack.push("Hello")
strStack.push("World")
print(strStack.pop())
print(strStack.is_empty())

# Extra
testStack = Stack[int]()
print(testStack.pop())
testStack.push(1)
print(testStack.size())