def approach1():
    while True:
        user_input = input("what do you wanna do: ").strip().lower()
        call = sorted("call next")
        add = sorted("add")
        exit = sorted("exit")
        user_input = sorted(user_input)

        if user_input == call:
            print("call next") 
        elif user_input == add:
            print("add") 
        elif user_input == exit:
            print("exit")
        else:
            print("else")
        break


def approach2():
    while True:
        user_input = input("what do you wanna do: ").strip().lower()
        call = sorted("call next")
        add = sorted("add")
        exit = sorted("exit")
        user_input = sorted(user_input)

        a = 0
        b = 0
        c = 0

        for i in user_input:
            if i in call:
                a += 1
            if i in add:
                b += 1
            if i in exit:
                c += 1
        
        if len(user_input) > 5 and len(user_input) < 12:
            a += 1
        elif len(user_input) < 5 and len(user_input) < 3:
            b += 1
        elif len(user_input) <= 3 and len(user_input) >= 2:
            c += 1
        else:
            pass
        
        if a > b and a > c:
            print("call next")
        elif b > a and b > c:
            print("add")
        elif c > a and c > b:
            print("exit")
        else:
            print("invalid input")

approach1()
approach2()
