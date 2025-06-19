def is_float(s):
    """
    Проверяет, является ли строка представлением вещественного числа
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack: 
    def __init__(self):
        # верхушкой стека считаем голову (первый элемент) односвязного списка
        self.head = None
        # из-за особенностей односвязного списка для быстрого вычисления длину нужно хранить отдельно
        self.len = 0
    
    def isempty(self): 
        return self.head is None
        
    def push(self, data):
        self.len += 1
        if self.head == None: 
            self.head = Node(data) 
        else: 
            newnode = Node(data, self.head)
            self.head = newnode 
    
    def pop(self): 
        if self.isempty(): 
            return None 
        self.len -= 1
        poppednode = self.head 
        self.head = self.head.next
        return poppednode.data
    
    def top(self): 
        if self.isempty(): 
            return None 
        else: 
            return self.head.data
    
    def clear(self):
        # для очищения односвязного списка достаточно обнулить ссылку на голову
        self.head = None
        self.len = 0
    
    def length(self):
        return self.len


class Calculator:
    def __init__(self):
        self.stack = Stack()
    
    def _perform(self, op: str):
        if is_float(op):
            self.stack.push(float(op))
        else:
            if self.stack.length() < 2:
                raise Exception(f"Недостаточно чисел для операции {op}: нужно хотя бы 2")
            x = self.stack.pop()
            y = self.stack.pop()
            match op:
                case '+':
                    self.stack.push(x + y)
                case '-':
                    self.stack.push(y - x)
                case '*':
                    self.stack.push(x * y)
                case '/':
                    self.stack.push(y / x)
                case _:
                    raise Exception(f"Некорректная операция: {op}")
    
    def calculate(self, formula: str):
        try:
            ops = formula.split()
            for op in ops:
                self._perform(op)
            if self.stack.length() > 1:
                raise Exception(f"Недостаточно операций для завершения вычислений.")
            return self.stack.pop()
        finally: # действия здесь будут выполнены независимо от того, произошла ли ошибка
            self.stack.clear()
    

if __name__ == '__main__':
    completed = False
    calc = Calculator()
    while True:
        print("Обратная польская запись: сначала идут два операнда, затем операция, которую необходимо выполнить.")
        formula = input("Введите выражение в обратной польской записи (для выхода ничего не пишите и нажмите Enter): ")
        if formula == '':
            break
        try:
            result = calc.calculate(formula)
            print("Результат вычислений:", result)
        except ZeroDivisionError:
            print("ОШИБКА! Деление на 0.")
            print("Попробуйте ещё раз.")
        except Exception as e:
            print("ОШИБКА!", e.args[0])
            print("Попробуйте ещё раз.")
