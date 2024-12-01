

class Calc:

    __number_stack: list = []
    __action_stack: list = []
    __action: dict = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2,
        '^': 3
    }

    def __func(self, num1: float, num2: float, operation: chr) -> float:
        match operation:
            case '+': return num1 + num2
            case '-': return num1 - num2
            case '*': return num1 * num2
            case '/': return num1 / num2
            case '^': return num1 ** num2

    def __calc(self):
        num2 = self.__number_stack.pop()
        num1 = self.__number_stack.pop()
        result = self.__func(num1, num2, self.__action_stack.pop())
        self.__number_stack.append(result)

    def __is_action(self, action: str):
        if len(self.__action_stack) == 0:
            self.__action_stack.append(action)
        else:
            last_action = self.__action_stack[-1]
            if last_action == '(':
                self.__action_stack.append(action)
            else:
                if self.__action[last_action] < self.__action[action]:
                    self.__action_stack.append(action)
                else:
                    while self.__action[self.__action_stack[-1]] >= self.__action[action]:
                        self.__calc()
                        if len(self.__action_stack) < 1 or self.__action_stack[-1] == '(': break
                    self.__action_stack.append(action)

    def __temp_num_to_stack(self, temp_num: str) -> str:
        if len(temp_num) > 0:
            if len(self.__action_stack) == 1 and len(self.__number_stack) == 0:
                action = self.__action_stack.pop()
                if action == '-':
                    self.__number_stack.append(self.__func(0, float(temp_num), action))
                else:
                    raise TypeError
            else:
                self.__number_stack.append(float(temp_num))
        return ''

    def __run(self, primer: str) -> int or float:
        temp_num = ''
        for s in primer.replace(' ', ''):
            if s.isdigit() or s == '.' or s == ',':
                if s == ',':
                    temp_num += '.'
                else:
                    temp_num += s
            else:
                temp_num = self.__temp_num_to_stack(temp_num)
                if s in self.__action.keys():
                    self.__is_action(s)
                elif s == '(':
                    self.__action_stack.append(s)
                elif s == ')':
                    while self.__action_stack[-1] != '(':
                        self.__calc()
                    else: self.__action_stack.pop()
                else:
                    raise TypeError
        else:
            self.__temp_num_to_stack(temp_num)

        while len(self.__number_stack) > 1:
            self.__calc()

        result = self.__number_stack.pop()
        return int(result) if result % 1 == 0 else round(result, 2)

    def run(self, primer: str) -> int or float:
        return self.__run(primer)

    def get_result_digit(self, primer) -> int or None:
        if primer == "":
            return None
        try:
            result = self.__run(primer)
        except (ZeroDivisionError, TypeError, IndexError):
            return None
        return result

    def get_result_str(self, primer: str) -> list:
        self.__action_stack = []
        self.__number_stack = []
        if primer == "":
            return ["Строка пустая", 0]
        try:
            result = self.__run(primer)
        except ZeroDivisionError:
            return ["На ноль делить нельзя.", 0]
        except (TypeError, IndexError):
            return ["Проверьте корректность введенных данных", 0]
        return [f"Ответ: {result}", 1]
