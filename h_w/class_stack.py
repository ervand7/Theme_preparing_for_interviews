class Stack:
    def __init__(self, opening_symbols='([{', closing_symbols=')]}', status=True):
        self.stack_list = []
        self.opening_symbols = opening_symbols
        self.closing_symbols = closing_symbols
        self.status = status

    def is_empty(self):
        if not self.stack_list:  # if self.stack_list is empty - True, there is nothing in self.stack_list
            return print(True)
        else:
            return print(False)  # if self.stack_list is full at least 1 bracket - False, there is nothing

    # _ _ _ _ _ _
    # Two functions, demanded by the task
    def push_(self, some_brackets=''):
        for i in some_brackets:
            if i in self.opening_symbols:
                self.stack_list.append(i)

    def peek(self):
        return self.stack_list[-1]
    # _ _ _ _ _ _

    def pop_(self):
        return self.stack_list.pop()

    def size(self):
        return len(self.stack_list)

    def push_and_calculate(self, input_brackets: str):
        self.status = True
        for i in input_brackets:
            if i in self.opening_symbols:
                self.stack_list.append(i)
            elif i in self.closing_symbols:
                if not self.stack_list:
                    self.status = False
                    break

                deleted_open_bracket = self.pop_()
                if deleted_open_bracket == '(' and i == ')':
                    continue
                if deleted_open_bracket == '[' and i == ']':
                    continue
                if deleted_open_bracket == '{' and i == '}':
                    continue
                self.status = False
                break

        if self.status and self.size() == 0:
            return print('Balanced')
        else:
            return print('Not balanced')


if __name__ == '__main__':
    experimental = Stack()
    experimental.push_and_calculate('()')
    experimental.push_and_calculate('}{}')
    experimental.push_and_calculate('[([])((([[[]]])))]{()}')
    experimental.push_and_calculate('(((([{}]))))')
    experimental.push_and_calculate('{{[()]}}')
    experimental.push_and_calculate('}{}')
    experimental.push_and_calculate('{{[(])]}}')
    experimental.push_and_calculate('[[{())}]')
# __________________________________________________________________


# __________________________________________________________________
# ||||||||||||| a variant in global scope for debugging |||||||||||||
# s = '{[]}()'
# stack = []
# status = True  # Изначально скажем, что все наши скобочные последовательности правильные
# for i in s:
#     if i in '([{':
#         stack.append(i)
#     elif i in ')]}':
#         # чтобы сразу избежать ошибки pop from empty list, которая у нас возникнет, к примеру, если закрывающихся
#         # скобок будет больше, чем открывающихся, мы ставим условие прерывания цикла:
#         if not stack:  # Если stack пустой
#             status = False
#             break
#
#         open_bracket = stack.pop()  # тут при каждой итерации будет удаляться каждый элемент, который попал в stack
#         # print(open_bracket)
#         if open_bracket == '(' and i == ')':  # если только что удаленный элемент равен '(' и i == ')', то
#             # возвращаемся в начало цикла и повторяем до тех пор пока у нач не исчезнут все подобные элементы
#             continue
#         if open_bracket == '[' and i == ']':
#             continue
#         if open_bracket == '{' and i == '}':
#             continue
#         # если мы не попадаем в одно из этих трех условий, то:
#         status = False
#         break
#
# if status and len(stack) == 0:
#     print('Balanced')
# else:
#     print('Not balanced')
