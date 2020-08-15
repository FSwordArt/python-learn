# -*- coding: utf-8 -*

menu = {'x':
            {'y':
                  {'i': 1}
              }
        }

def ThreeLM_1(menu):
    while True:
        for k in menu:
            print(k)

        key = input(">>>").strip()
        if key == 'b' or key == 'q':
            return key

        elif key in menu.keys() and menu[key]:
            ret = ThreeLM_1(menu[key])

            if ret == 'q':
                return 'q'




def ThreeLM_2(menu):
    while True:

        for k in menu:
            print(k)

        key = input(">>>").strip()
        if key == 'b' or key == 'q':
            return key

        elif key in menu.keys() and menu[key]:
            menu = menu[key]






print(ThreeLM_2(menu))









