from collections import Counter
from termcolor import colored
from pyfiglet import Figlet
import time
print("########################################################################")
f = Figlet(font='roman')
print(colored(f.renderText('StatPy'),'red'))
print("########################################################################")

ungrouped_data = []
x = 1

print (colored("WELCOME TO StatPy.", 'yellow'))
data_num = int(input("How many ungrouped elements?: "))
for x in range(data_num):
    entered_data = int(input("Enter ungrouped element: "))
    ungrouped_data.append(entered_data)

def main():
    print("\nSelect action below.")
    print("1.Find Mean")
    print("2.Find Median")
    print("3.Find Mode")
    print("4.Quit\n")

    choice = int(input("Action: "))

    def find_mean():
        y = 0
        for i in ungrouped_data:
            y += i
        result1 = y/data_num
        print ("The mean is: ",result1,'green')
        main()

    ungrouped_data.sort()
    def find_median():
        if data_num % 2 != 0:
            element_at_n = int((data_num + 1)/2)
            list_position = int(element_at_n - 1)
            print(ungrouped_data)
            print ("The median is: ",ungrouped_data[list_position],'green')
            main()
        else:
            val1 = int((data_num/2)-1)
            val2 = int(data_num/2)
            val3 = (ungrouped_data[val1] + ungrouped_data[val2])/2
            print("The median is: ",val3)
            main()

    def get_mode():
        num_repeat = Counter(ungrouped_data)
        result = num_repeat.most_common(1)[0][0]
        if num_repeat > 0:
            print("The mode is : ",result)
        else:
            print("No value is repeated")
        main()
        
    def close_program():
        print("Bye!")
        time.sleep(2)
        exit()

    if choice == 1:
        find_mean()
    if choice == 2:
        find_median()
    if choice == 3:
        get_mode()
    if choice == 4:
        close_program()

main()