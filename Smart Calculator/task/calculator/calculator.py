data_set = {} # to hold the value gotten from input
final_list = [] # to get a list where signs are calculated and concatinated for calculation
new_list1 = [] # to get a list where signs are calculated
new_list2 = []
signs = ["-", "+", "*", "/", "^", "(", ")"]
updated_list = []

def get_input(val): #function to get the input data in dictionary

    try:
        latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        value_lists = val
        if value_lists.count("=") > 1:
            print("Invalid assignment")
        elif "=" in value_lists:
            value_lists = value_lists.split()
            if len(value_lists) == 1:
                list_calculation1(value_lists)
            elif len(value_lists) == 2:
                list_calculation2(value_lists)
            if len(value_lists[0]) == 1 and value_lists[0] not in latin:
                print("Invalid identifier")
            elif len(value_lists[0]) > 1:
                list_to_check = [x for x in value_lists[0]]
                count = 0
                for x in list_to_check:
                    if x in latin:
                        count = count + 1
                        if len(list_to_check) == count:
                            try:
                                value_lists[2] = int(value_lists[2])
                                data_set[value_lists[0]] = value_lists[2]
                            except ValueError:
                                try:
                                    value_lists[2] = data_set[value_lists[2]]
                                    data_set[value_lists[0]] = value_lists[2]
                                except KeyError:
                                    x = [x for x in value_lists[2]]
                                    count = 0
                                    for c in x:
                                        if c in latin:
                                            count = count + 1
                                            if len(x) == count:
                                                print("Unknown variable")
                                        else:
                                            print("Invalid assignment")
                                            break
                    else:
                        print("Invalid identifier")
                        break
            else:
                try:
                    value_lists[2] = int(value_lists[2])
                    data_set[value_lists[0]] = value_lists[2]
                except ValueError:
                    try:
                        value_lists[2] = data_set[value_lists[2]]
                        data_set[value_lists[0]] = value_lists[2]
                    except KeyError:
                        x = [x for x in value_lists[2]]
                        count = 0
                        for c in x:
                            if c in latin:
                                count = count + 1
                                if len(x) == count:
                                    print("Unknown variable")
                            else:
                                print("Invalid assignment")
                                break
        else:
            list_to_check = [x for x in value_lists]
            for x in list_to_check:
                if x in latin:
                    continue
                else:
                    return "Invalid identifier"
                    break
            return "Unknown Variable"
    except ValueError:
        print("Invalid assignment")


def stack_build(lists):
    stack_for_sign = []
    result = ""
    for x in lists:
        if x not in signs:
            result = result + " " + x
        elif len(stack_for_sign) == 0 or stack_for_sign[len(stack_for_sign) - 1] == "(":
            stack_for_sign.append(x)
        elif x == "*" or x == "/":
            if stack_for_sign[len(stack_for_sign) - 1] == "+" or stack_for_sign[len(stack_for_sign) - 1] == "-":
                stack_for_sign.append(x)
            elif x == "*" and (stack_for_sign[len(stack_for_sign) - 1] == "*" or stack_for_sign[len(stack_for_sign) - 1] == "/"):
                while stack_for_sign[len(stack_for_sign) - 1] in ["*", "/"]:
                    result = result + " " + stack_for_sign.pop()
                    if len(stack_for_sign) == 0:
                        break
                stack_for_sign.append(x)
            elif x == "/" and (stack_for_sign[len(stack_for_sign) - 1] == "/" or stack_for_sign[len(stack_for_sign) - 1] == "*"):
                while stack_for_sign[len(stack_for_sign) - 1] in ["*", "/"]:
                    result = result + " " + stack_for_sign.pop()
                    if len(stack_for_sign) == 0:
                        break
                stack_for_sign.append(x)
        elif x == "+" and (stack_for_sign[len(stack_for_sign) - 1] == "+" or stack_for_sign[len(stack_for_sign) - 1] == "-"):
            while stack_for_sign[len(stack_for_sign) - 1] in ["+", "-", "*", "/"]:
                result = result + " " + stack_for_sign.pop()
                if len(stack_for_sign) == 0:
                    break
            stack_for_sign.append(x)
        elif x == "-" and (stack_for_sign[len(stack_for_sign) - 1] == "-" or stack_for_sign[len(stack_for_sign) - 1] == "+"):
            while stack_for_sign[len(stack_for_sign) - 1] in ["+", "-", "*", "/"]:
                result = result + " " + stack_for_sign.pop()
                if len(stack_for_sign) == 0:
                    break
            stack_for_sign.append(x)
        elif x == "+" or x == "-":
            if stack_for_sign[len(stack_for_sign) - 1] == "*" or stack_for_sign[len(stack_for_sign) - 1] == "/":
                while stack_for_sign[len(stack_for_sign) - 1] in ["*", "/", "+", "-"]:
                    result = result + " " + stack_for_sign.pop()
                    if len(stack_for_sign) == 0:
                        break
                stack_for_sign.append(x)
            else:
                stack_for_sign.append(x)
        elif x == "(":
            stack_for_sign.append(x)
        elif x == ")":
            while stack_for_sign[len(stack_for_sign) - 1] != "(":
                result = result + " " + stack_for_sign.pop()
            stack_for_sign.pop()
    while len(stack_for_sign) != 0:
        result = result + " " + stack_for_sign.pop()
    return result.replace("  ", " ")


stackfor_calculation = []
def stack_calculation(postflix):
    for x in postflix.split(" "):
        if x.isnumeric():
            stackfor_calculation.append(x)
        elif x.isnumeric() == False and x not in signs:
            try:
                stackfor_calculation.append(str(data_set[x]))
            except KeyError:
                pass
        elif x in signs:
            a = stackfor_calculation.pop()
            b = stackfor_calculation.pop()
            stackfor_calculation.append(str(int(eval(b + x + a))))
    return int(stackfor_calculation[len(stackfor_calculation) - 1])


def list_calculation1(lists): #if no spce between the input eg m=4
    a = str()
    b = str()
    for x in lists[0]:
        if x != "=" and "=" in lists:
            b = b + x
            continue
        if x != "=":
            a = a + x
            continue
        elif x == "=":
            lists.clear()
            lists.append(a)
            lists.append(x)
            continue
    lists.append(b)


def list_calculation2(lists): # if 1 space between input eg m =4
    l =[]
    a = str()
    b = str()
    for x in lists:
        for y in x:
            if y != "=" and "=" in l:
                b = b + y
            if y != "=":
                a = a + y
            elif y == "=":
                l.append(a)
                l.append(y)
        l.append(b)
    l.remove("")
    lists.clear()
    return lists.extend(l)

def sign_identification(lists):
    for key in lists.split(" "):
        if "-" in key and key.count("-") >= 2:
            if key.count("-") % 2 == 1:
                new_list1.append("-")
            elif key.count("-") % 2 == 0:
                new_list1.append("+")
        elif "+" in key and key.count("+") > 1:
            new_list1.append("+")
        elif "*" in key and key.count("*") > 1:
            new_list1.clear()
            break
        elif "/" in key and key.count("/") > 1:
            new_list1.clear()
            break
        else:
            new_list1.append(key)
    if new_list1:
        return " ".join(new_list1)
    else:
        return "Invalid Expression"

def evaluation(data):
    a = ""
    updated_list = []
    count = 0
    for x in data:
        count = count + 1
        if x not in signs:
            a = a + x
        elif x in signs:
            updated_list.append(a)
            a = ""
            updated_list.append(x)
        if x == data[len(data) - 1] and count == len(data):
            updated_list.append(a)
    updated_list = [x for x in updated_list if x != '' and x != ' ']
    return updated_list




while True:
    new_list1.clear()
    stackfor_calculation.clear()
    try:
        operation = input()
        if not operation:
            pass
        elif "=" in operation:
            get_input(operation)
        elif operation.startswith("/") :
            if operation == "/help":
                print("The program calculates the sum and subtraction of numbers")
            elif operation == "/exit":
                print("Bye!")
                break
            else:
                print("Unknown command")
        elif "+" in operation or "-" in operation or "*" in operation or "/" in operation:
            if operation.count("(") != operation.count(")"):
                print("Invalid Expression")
                continue
            else:
                try:
            #print(stack_build(evaluation(sign_identification(operation))))
                    print(stack_calculation(stack_build(evaluation(sign_identification(operation)))))
                except IndexError:
                    print("Invalid Expression")

        elif get_input(operation) == "Invalid identifier":
            print("Unknown Variable")
        else:
            print(data_set[operation])
    except KeyError:
        print("Unknown variable")


