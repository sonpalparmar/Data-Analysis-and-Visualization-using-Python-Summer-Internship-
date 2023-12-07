# 1. check wrong password attempt . give 3 attempts only, after 3 attempts wrong password then session expired

def p(d):
    s = input(("Enter password : "))
    if (s == d):
        return True
    else:
        return False


def enter():
    u = input(("Set username : "))
    s = input(("Set password : "))
    info = {}
    info["name"] = u
    info["password"] = s
    print("Again enter password to login")
    for i in range(0, 4):
        if i == 3:
            print("Account blocked ans session expired")
            break
        ans = p(info.get("password", None))
        if ans:
            print("You have entered the right password")
            break
        elif not ans and i < 3:
            print("Wrong password try again !!")
        

enter()
