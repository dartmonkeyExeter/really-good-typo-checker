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
                b += 1.5
            if i in exit:
                c += 1.25
        
        if len(user_input) > 5 and len(user_input) < 12:
            a += 0.5
        elif len(user_input) < 5 and len(user_input) > 3:
            b += 0.5
        elif len(user_input) <= 3 and len(user_input) >= 2:
            c += 0.75
        else:
            pass
        print(f'{a} {b} {c}')
        if a > b and a > c:
            spell_check = "call next"
        elif b > a and b > c:
            spell_check = "add"
        elif c > a and c > b:
            spell_check = "exit"
        elif c < 1 and b < 1 and a < 1:
            spell_check = "i'm not sure what you mean... :("
        
        if spell_check == "i'm not sure what you mean... :(":
            print(spell_check)
        else:
            while True:
                yes_no = input(f"did you mean {spell_check}? (Y/N)").upper().strip()
                if yes_no[0] == "Y":
                    print(f"gotcha, running {spell_check}")
                elif yes_no[0] == "N":
                    print("i'll do better next time!")
                else:
                    print("invalid input!!!")


approach2()
