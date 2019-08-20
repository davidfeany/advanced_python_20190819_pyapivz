#! /usr/bin/python

def main():
    while True:
        try:
            print("Enter the name of a file: ")
            name = input()
            with open(name, 'w') as myfile:
                myfile.write("This worked")
        except Exception as err:
            print("Error writing to your file... trying again...", err)
        else:
            break
    print("Thanks for making that simple file")

main()
