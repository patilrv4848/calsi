from calcu import do_addition,do_substraction,do_divsion
from mulc import do_multi
from arear import calarea
def main():
    print("welcome to the calculator app")
    print("\n select the function") 
    print("1. Add") 
    print("2. substract")
    print("3. multiplication")
    print("4. division")
    print("5.area calulation")
    user_input =input("select the fuction: ")

    a=int(input ("value of A : "))
    b=int(input("value of B: "))

    if user_input == "1":
        result =do_addition(a,b)
    elif user_input == "2":
        result =do_substraction(a,b)
    elif user_input == "3":
        result =do_multi(a,b)
    elif user_input == "4":
        result =do_divsion(a,b)
    elif user_input == "5":
        result =calarea(a,b)

    print('Result:',result)
if __name__ == '__main__':
    main()