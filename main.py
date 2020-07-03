#!/usr/bin/env python3

from expression_class import Expression_num

a = Expression_num("")
#a = Expression_num("1 + 23 * (2 + 3*6)")

#a = Expression_num("1 + 23 * 2 + 32+4")

a.make_workable()
#a.find_real_next_action()
a.simplify()

a.print()
