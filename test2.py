def passlen():
    password_length = input("Enter password length: ")
    return password_length

def upperMin():
    uppercase_minimum = input("Enter upppercase minimum: ")
    return uppercase_minimum

def lowerMin():
    lowercase_minimum = input("Enter lowercase minimum: ")
    return lowercase_minimum

def digitMin():
    digit_minimum = input("Enter digit minimum: ")
    return digit_minimum

def charcMin():
    special_minimumum = input("Enter special chacter minimum")
    return special_minimumum

def useALL():
    x = 15
    return x

def invalidFlag():
    raise Exception("Invalid flag")

def choose_flag(flag):
    options = {
        "-all" : useALL,
        "-u" : upperMin,
        "-l" : lowerMin,
        "-d" : digitMin,
        "-c" : charcMin
    }

    value_got = options.get(flag, invalidFlag)
    return value_got()

 
finish = choose_flag("-u")
print(finish)