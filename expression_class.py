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
        line = go2nums(line)

        self.expr = line
        self.workable = True


    def find_next_action(self, pos=0):
        f = find_last_symbol(self.expr, "(", initial_pos=pos)
        s = find_first_symbol(self.expr, ")", initial_pos=f)
        type = "brackets"

        if f == -1:
            f = find_first_symbol(self.expr, "/*", initial_pos=pos) - 2
            s = f + 4
            type = "mult"
        if f == -3:
            f = find_first_symbol(self.expr, "+-", initial_pos=pos) - 2
            s = f + 4
            type = "add"
        if f == -3:
            type = "end"
        return (f, s, type)


    def find_real_next_action(self):
        f, s, type = self.find_next_action()
        _, action = self.get_next_action(f, s, type)


        while len(action) != 3:
            f, s, type = self.find_next_action(pos=f+1)
            is_action, action = self.get_next_action(f, s, type)

        return f, s, type, action


    def get_next_action(self, f, s, type):
        if type == "end":
            return (False, [])

        action = self.expr[f+1:s]
        return (True, action)


    def do_next_action(self, action):
        if action[1] == "/":
            return action[0]/action[2]
        elif action[1] == "*":
            return action[0]*action[2]
        elif action[1] == "+":
            return action[0]+action[2]
        elif action[1] == "-":
            return action[0]-action[2]


    def change_expression(self, value, f, s):
        for i in range(f, s):
            self.expr[i] = value

    def number_of_actions(self):
        signs = "/*-+"
        count = 0
        for i in self.expr:
            if str(i) in signs:
                count += 1
        return count


    def simplify(self):
        N = self.number_of_actions()
        for i in range(N):
            self.print()
            #f, s, type = self.find_next_action()
            #is_action, action = self.get_next_action(f, s, type)
            f, s, type, action = self.find_real_next_action()


            if True:
                value = self.do_next_action(action)
                if type == "brackets":
                    self.change_expression(" ", f, s)
                    self.change_expression(value, s, s+1)
                else:
                    self.change_expression(" ", f+1, s-1)
                    self.change_expression(value, s-1, s)
                self.expr = delete_spaces(self.expr)
