to_do_list = []

def show():
    print("-------------------TO DO LIST-------------------")
    print("OPTIONS:")
    print("1.View the list")
    print("2.Edit the list")
    print("3.Check completed")
    print("4.Exit")
    
while True:
    show()
    
    choose = int(input("Choose option : "))

    if choose == 1:
        if not to_do_list:
            print("\nYour list is empty")
        else:
            for index,task in enumerate(to_do_list,start=1):
                print(f"{index}.{task}")
            
    elif choose == 2:
        add = str(input("\nAdd the work : "))
        if add.strip():
            to_do_list.append(add)
            print(f"{add} is succesfully added")
        else:
            print("❌ Task cannot be empty!")
                    
    elif choose == 3:
        check = int(input("\nWrite completed one : "))
        actual = check-1
        try:
            if check > actual <len(to_do_list):
                if "===========Done" in to_do_list:
                    print("\nTASK IS ALREADY DONE")
                else:
                    p = to_do_list[actual] + "===========Done"
                    update = to_do_list.remove(add)
                    update1 = to_do_list.append(p)
                    print(p)
            else:
                print("INVALID")
        except ValueError:
            print("error")
            
    elif choose == 4:
        print("Goodbye! Have a productive day.")
        break
    
    else:
        print("❌ Invalid choice! Please select an option between 1 and 4.")