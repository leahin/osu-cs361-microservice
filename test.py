# A dummy client program to test Word List microservice.
# Enter either add(word), delete(word), get() to test microservice.
# Other keywords will do nothing or can crash the program.

if __name__ == '__main__':

    while True:
        action = input("Enter action: ")

        with open("temp.txt", "w") as temp:
            temp.truncate(0)
            temp.write(action)
