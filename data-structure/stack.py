import gc

class Knot:
  def __init__(self, value, next) -> None:
    self.value = value
    self.next = next
  
  def free(self):
    del self

class Stack:
  def __init__(self) -> None:
    self.length = 0
    self.top = None
  
  def push(self, value):
    newKnot = Knot(value, self.top)    
    self.top = newKnot

    self.length++1

  def pop(self):
    # atribuindo o topo para a variavel a ser removida
    rm = self.top

    # Topo passa a ser o próximo nó
    self.top = self.top.next

    rm.free() # liberando a memória
    gc.collect() # chamando garbage collector

  def print(self):
    # Iniciando pelo topo da pilha
    knot = self.top

    while(knot is not None):
      print(knot.value)
      knot = knot.next
    

stack = Stack()

for i in range(1, 100):
  stack.push(i)

stack.pop()
stack.print()