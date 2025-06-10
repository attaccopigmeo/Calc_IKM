def is_float(s):
    """
    Проверяет, является ли строка представлением вещественного числа
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


class Calculator:
    def __init__(self):
        self.stack = []
    
    def _perform(self, op: str):
        if is_float(op):
            self.stack.append(float(op))
        else:
            if len(self.stack) < 2:
                raise Exception(f"Недостаточно чисел для операции {op}: нужно хотя бы 2")
            x = self.stack.pop()
            y = self.stack.pop()
            match op:
                case '+':
                    self.stack.append(x + y)
                case '-':
                    self.stack.append(y - x)
                case '*':
                    self.stack.append(x * y)
                case '/':
                    self.stack.append(y / x)
                case _:
                    raise Exception(f"Некорректная операция: {op}")
    
    def calculate(self, formula: str):
        try:
            ops = formula.split()
            for op in ops:
                self._perform(op)
            if len(self.stack) > 1:
                raise Exception(f"Недостаточно операций для завершения вычислений.")
            return self.stack.pop()
        finally: # действия здесь будут выполнены независимо от того, произошла ли ошибка
            self.stack.clear()
    

if __name__ == '__main__':
    completed = False
    calc = Calculator()
    while True:
        print("Обратной польской записью выражения a b называется запись, в которой знак операции размещен за операндами a b. ")
        formula = input("Введите выражение в обратной польской записи (для выхода из программы ничего не вводя нажмите Enter): ")
        if formula == '':
            break
        try:
            result = calc.calculate(formula)
            print("Результат вычислений:", result)
        except Exception as e:
            print("ОШИБКА!", e.args[0])
            print("Попробуйте ещё раз.")
