def pass_check(get_pass):
    check_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    check_spec_char = ["!", "@", "#", "$", "%", "&", "*"]
    # letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]  W RAZIE POTRZEBY! / IF IS NEEDED TO USE!

    err_check = len(get_pass)

    nums = 0
    nums = int(nums)
    char = 0
    char = int(char)

    for i in get_pass:
        if i in check_nums:
            nums += 1
        elif i in check_spec_char:
            char += 1

    summar = nums + char
    
    if nums >= 2 and char >= 2:
        if summar == err_check:
            result = False
        else:
            result = True
    elif nums == err_check or char == err_check:
        result = False
    else:
        result = False

    return result

get_pass = input("Witaj, podaj swoje hasło, a ja sprawdzę, czy jest ono bezpieczne: ")

x = len(get_pass)

checking = pass_check(get_pass)

if x >= 7:
    if checking == True:
        print("Twoje hasło jest wystarczająco silne. Brawo! :P")
    else: 
        print("Musisz ulepszyć swoje zabezpieczenia! :C")
else:
    print("Twoje hasło ma zbyt mało znaków!")
