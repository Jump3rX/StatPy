from collections import Counter
from termcolor import *
import colorama
from pyfiglet import Figlet
import time
colorama.init()
f = Figlet(font='roman')
print(colored(f.renderText('StatPy'),'green'))

ungrouped_data = []
x = 1

cprint("\tWELCOME TO StatPy.", 'yellow')
data_num = int(input("\tHow many ungrouped elements?: "))
for x in range(data_num):
    entered_data = int(input("\tEnter ungrouped element: "))
    ungrouped_data.append(entered_data)

def main():
    cprint("\n\tSelect action below.",'green')
    cprint("\t1.Find Mean",'green')
    cprint("\t2.Find Median",'green')
    cprint("\t3.Find Mode",'green')
    cprint("\t4.Quit\n",'green')
    choice = int(input("\tAction: "))

    def find_mean():
        y = 0
        for i in ungrouped_data:
            y += i
        result1 = y/data_num
        print("\tThe mean is: ",result1)
        main()

    ungrouped_data.sort()
    def find_median():
        if data_num % 2 != 0:
            element_at_n = int((data_num + 1)/2)
            list_position = int(element_at_n - 1)
            print("\t",ungrouped_data)
            print ("\tThe median is: ",ungrouped_data[list_position])
            main()
        else:
            val1 = int((data_num/2)-1)
            val2 = int(data_num/2)
            val3 = (ungrouped_data[val1] + ungrouped_data[val2])/2
            print("\tThe median is: ",val3)
            main()

    def get_mode():
        num_repeat = Counter(ungrouped_data)
        result = num_repeat.most_common(1)[0][0]
        print("\tThe mode is : ",result)
        main()
        
    def close_program():
        print("\tBye!")
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
    if choice > 4:
        print("\tAction incorrect, please select again.")
        main()

main()
