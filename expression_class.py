from gorynych_str_lib import *

class Expression_num:

    numbers = "1234567890"
    f_signs, s_signs, brackets= "/*", "+-", "()"
    signs = f_signs + s_signs + brackets

    def __init__(self, expr):
        self.expr = [expr]
        self.workable = False


    def print(self):
        print(arr2str(self.expr))


    def is_workable(self):
        return self.workable


    def make_workable(self):
        line = str2arr(arr2str(self.expr))

        line = delete_spaces(line)
        line = connect_numbers(line)

        self.expr = line
        self.workable = True


    def find_next_action(self):
        f = find_last_symbol(self.expr, "(")
        s = find_first_symbol(self.expr, ")", initial_pos=f)

        if f == -1:
            f = find_first_symbol(self.expr, "/*") - 2
            s = f + 4
            type = "mult"
        if f == -3:
            f = find_first_symbol(self.expr, "+-") - 2
            s = f + 4
            type = "add"
        if f == -3:
            type = "end"

        return (f, s, type)


    def get_next_action(self):
        f, s, type = self.find_next_action()
        if type == "end":
            return (False, [])

        action = self.expr[f+1:s]
        return (True, action)


    def do_action
