import random
import sys
GPA_40 = 0 
GPA_50 = 0
Nsem1_9GPA_40list = {}
Nsem2_9GPA_40list = {}
Nsem1_10GPA_40list = {}
Nsem2_10GPA_40list = {}
Nsem1_11GPA_40list = {}
Nsem2_11GPA_40list = {}
Nsem1_12GPA_40list = {}
Nsem2_12GPA_40list = {}
Nsem_1_9 = {}
Nsem_2_9 = {}
Nsem_1_10 = {}
Nsem_2_10 = {}
Nsem_1_11 = {}
Nsem_2_11 = {}
Nsem_1_12 = {}
Nsem_2_12 = {}
All_grades = {'9th grade semester 1': Nsem_1_9, '9th grade semester 2': Nsem_2_9,
              '10th grade semester 1': Nsem_1_10, '10th grade semester 2': Nsem_2_10,
              '11th grade semester 1': Nsem_1_11, '11th grade semester 2': Nsem_2_11,
              '12th grade semester 1': Nsem_1_12, '12th grade semester 2': Nsem_2_12
}
def convertto40(convgrades):
        #initialize 4.0GPA scale
        repvalue_4 = 4.0
        repvalue_37 = 3.7
        repvalue_33 = 3.3
        repvalue_3 = 3.0
        repvalue_27 = 2.7
        repvalue_23 = 2.3
        repvalue_2 = 2.0
        repvalue_17 = 1.7
        repvalue_13 = 1.3
        repvalue_1 = 1.0
        repvalue_0 = 0.0
        for key, val in convgrades.items():
                if val > 100:
                    convgrades[key] = 'Error(Grade Point from 0-100)'
                elif val >= 93:
                    convgrades[key] = repvalue_4
                elif val >= 90:
                    convgrades[key] = repvalue_37
                elif val >= 87:
                    convgrades[key] = repvalue_33
                elif val >= 83:
                    convgrades[key] = repvalue_3
                elif val >= 80:
                    convgrades[key] = repvalue_27
                elif val >= 77:
                    convgrades[key] = repvalue_23
                elif val >= 73:
                    convgrades[key] = repvalue_2
                elif val >= 70:
                    convgrades[key] = repvalue_17
                elif val >= 67:
                    convgrades[key] = repvalue_13
                elif val >= 65:
                    convgrades[key] = repvalue_1
                elif val >= 0:
                    convgrades[key] = repvalue_0
                else:
                    convgrades[key] = 'Error(Grade Point from 0-100)'
        return convgrades
def ask_input():
    return str(input('Command: ').upper().strip())
def update_class1(Semester):
    try:
        class_1 = str(input('Enter Class 1:'))
        class1_grade = int(input("Enter class 1 grade:"))
        Semester[class_1] = class1_grade
        return class_1
    except:
        print('Invalid Characters!')
        update_class1(Semester)
def update_class2(Semester):
    try:
        class_2 = str(input('Enter Class 2:'))
        class2_grade = int(input("Enter class 2 grade:"))
        Semester[class_2] = class2_grade
        return class_2
    except:
        print('Invalid Characters!')
        update_class2(Semester)
def update_class3(Semester):
    try:
        class_3 = str(input('Enter Class 3:'))
        class3_grade = int(input("Enter class 3 grade:"))
        Semester[class_3] = class3_grade
        return class_3
    except:
        print('Invalid Characters!')
        update_class3(Semester)
def update_class4(Semester):
    try:
        class_4 = str(input('Enter Class 4:'))
        class4_grade = int(input("Enter class 4 grade:"))
        Semester[class_4] = class4_grade
        return class_4
    except:
        print('Invalid Characters!')
        update_class4(Semester)
def update_class5(Semester):
    try:
        class_5 = str(input('Enter Class 5:'))
        class5_grade = int(input("Enter class 5 grade:"))
        Semester[class_5] = class5_grade
        return class_5
    except:
        print('Invalid Characters!')
        update_class5(Semester)
def update_class6(Semester):
    try:
        class_6 = str(input('Enter Class 6:'))
        class6_grade = int(input("Enter class 6 grade:"))
        Semester[class_6] = class6_grade
        return class_6
    except:
        print('Invalid Characters!')
        update_class6(Semester)
def update_class7(Semester):
    try:
        class_7 = str(input('Enter Class 7:'))
        class7_grade = int(input("Enter class 7 grade:"))
        Semester[class_7] = class7_grade
        return class_7
    except:
        print('Invalid Characters!')
        update_class7(Semester)
def update_class8(Semester):
    try:
        class_8 = str(input('Enter Class 8:'))
        class8_grade = int(input("Enter class 8 grade:"))
        Semester[class_8] = class8_grade
        return class_8
    except:
        print('Invalid Characters!')
        update_class8(Semester)
def update_all(Semester):
    update_class1(Semester)
    update_class2(Semester)
    update_class3(Semester)
    update_class4(Semester)
    update_class5(Semester)
    update_class6(Semester)
    update_class7(Semester)
    update_class8(Semester)
def space_indent():
    for i in range(10 * 5):
        print()
def calc40GPA():
    if 'Error(Grade Point from 0-100)' in Nsem1_9GPA_40list.values():
        print('Only Grades from 0-100 Accepted!\nError found in: 9th Semester 1')
    elif 'Error(Grade Point from 0-100)' in Nsem2_9GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 9th Semester 2')
    elif 'Error(Grade Point from 0-100)' in Nsem1_10GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 10th Semester 1')
    elif 'Error(Grade Point from 0-100)' in Nsem2_10GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 10th Semester 2')
    elif 'Error(Grade Point from 0-100)' in Nsem1_11GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 11th Semester 1')
    elif 'Error(Grade Point from 0-100)' in Nsem2_11GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 11th Semester 2')
    elif 'Error(Grade Point from 0-100)' in Nsem1_12GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 12th Semester 1')
    elif 'Error(Grade Point from 0-100)' in Nsem2_12GPA_40list.values():
        print(f'Only Grades from 0-100 Accepted!\nError found in: 12th Semester 2')
    else:
            try:
                def divisor():
                    return (len(Nsem1_9GPA_40list.values()) + len(Nsem2_9GPA_40list.values()) + len(Nsem1_10GPA_40list.values()) + len(Nsem2_10GPA_40list.values()) + len(Nsem1_11GPA_40list.values()) + len(Nsem2_11GPA_40list.values()) + len(Nsem1_12GPA_40list.values()) + len(Nsem2_12GPA_40list.values()))
                def numerator():
                    return (sum(Nsem1_9GPA_40list.values()) + sum(Nsem2_9GPA_40list.values()) + sum(Nsem1_10GPA_40list.values()) + sum(Nsem2_10GPA_40list.values()) + sum(Nsem1_11GPA_40list.values()) + sum(Nsem2_11GPA_40list.values()) + sum(Nsem1_12GPA_40list.values()) + sum(Nsem2_12GPA_40list.values()))
                GPA_40 = numerator() / divisor()
                print("Total 4.0 scale GPA:", GPA_40)
            except:
                print('No grades filled out!')
def Ai_interact():
    space_indent()
    greetlist = ['hello', 'hey', 'hola', 'wassup']
    Question = ['How has your day been? ', 'What are you doing? ', 'Is AI superior to humans? ', 'What\'s your favorite color? ', 'Are you alone? ']
    greeting = greetlist[random.randint(0, int(len(greetlist) - 1))]
    print(greeting)
    response = str(input(Question[random.randint(0, len(Question) - 1)]))
    response += ' '
    print(f'{(response) * 5}\n' * 15)
    print('Intresting...')
exitredef = None
updateredef = None
classredef = None
renameredef = None
calculateredef = None
clearredef = None
funredef = None



space_indent()
print('MultiTasker')
print('-Anthony Paul Schurle Jr\n\n')
print('Type \'help\' for list of commands.')
current_command = ask_input()
while True:
    if current_command == 'EXIT' or current_command == 'QUIT' or current_command == exitredef:
        space_indent()
        print('Exiting...')
        sys.exit()

    elif current_command == 'HELP':
         space_indent()
         print('Help Page 1/1')
         print('Note: All commands can be typed \'abc\' or \'ABC\'')
         print('-' * 10)
         print(f'HELP:  Displays page 1 of the help menu.\n\nEXIT or QUIT(Rename- {exitredef}):  Closes the application.\n\nUPDATE(Rename- {updateredef}): Insert or replace classes and grades.\n\nCLASSES(Rename- {classredef}): Show 9th-12th transcript.\n\nRENAME(Rename- {renameredef}): Rename commands.\n\nCALCULATE(Rename- {calculateredef}): Caclulate 4.0 and 5.0 GPAs.\n\nCLEAR(Rename- {clearredef}): Clears transcript.\n\nFUN(Rename- {funredef}): ???')
         current_command = ask_input()

    elif current_command == 'UPDATE' or current_command == updateredef:
        space_indent()
        print('Select Option:\na. Update 9th Semester 1\nb. Update 9th Semester 2\nc. Update 10th Semester 1\nd. Update 10th Semester 2\ne. Update 11th Semester 1\nf. Update 11th Semester 2\ng. Update 12th Semester 1\nh. Update 12th Semester 2')
        choice = str(input('Choice: ').upper())
        if choice == 'A':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            achoice = str(input('Choice: ').upper())
            updatethroughout = False
            if achoice == 'A':
                Nsem_1_9.clear()
                updatethroughout = True
            if achoice == 'B' or updatethroughout:
                try:
                 del Nsem_1_9[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_1_9)
            if achoice == 'C' or updatethroughout:
                try:
                 del Nsem_1_9[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_1_9)
            if achoice == 'D' or updatethroughout:
                try:
                 del Nsem_1_9[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_1_9)
            if achoice == 'E' or updatethroughout:
                try:
                 del Nsem_1_9[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_1_9)
            if achoice == 'F' or updatethroughout:
                try:
                 del Nsem_1_9[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_1_9)
            if achoice == 'G' or updatethroughout:
                try:
                 del Nsem_1_9[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_1_9)
            if achoice == 'H' or updatethroughout:
                try:
                 del Nsem_1_9[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_1_9)
            if achoice == 'I' or updatethroughout:
                try:
                 del Nsem_1_9[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_1_9)
            if achoice != 'A' and achoice != 'B' and achoice != 'C' and achoice != 'D' and achoice != 'E' and achoice != 'F' and achoice != 'G' and achoice != 'H' and achoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'B':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            bchoice = str(input('Choice: ').upper())
            updatethroughout = False
            if bchoice == 'A':
                Nsem_2_9.clear()
                updatethroughout = True
            if bchoice == 'B' or updatethroughout:
                try:
                 del Nsem_2_9[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_2_9)
            if bchoice == 'C' or updatethroughout:
                try:
                 del Nsem_2_9[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_2_9)
            if bchoice == 'D' or updatethroughout:
                try:
                 del Nsem_2_9[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_2_9)
            if bchoice == 'E' or updatethroughout:
                try:
                 del Nsem_2_9[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_2_9)
            if bchoice == 'F' or updatethroughout:
                try:
                 del Nsem_2_9[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_2_9)
            if bchoice == 'G' or updatethroughout:
                try:
                 del Nsem_2_9[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_2_9)
            if bchoice == 'H' or updatethroughout:
                try:
                 del Nsem_2_9[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_2_9)
            if bchoice == 'I' or updatethroughout:
                try:
                 del Nsem_2_9[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_2_9)
            if bchoice != 'A' and bchoice != 'B' and bchoice != 'C' and bchoice != 'D' and bchoice != 'E' and bchoice != 'F' and bchoice != 'G' and bchoice != 'H' and bchoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'C':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            cchoice = str(input('Choice: ').upper())
            updatethroughout = False
            if cchoice == 'A':
                Nsem_1_10.clear()
                updatethroughout = True
            if cchoice == 'B' or updatethroughout:
                try:
                 del Nsem_1_10[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_1_10)
            if cchoice == 'C' or updatethroughout:
                try:
                 del Nsem_1_10[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_1_10)
            if cchoice == 'D' or updatethroughout:
                try:
                 del Nsem_1_10[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_1_10)
            if cchoice == 'E' or updatethroughout:
                try:
                 del Nsem_1_10[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_1_10)
            if cchoice == 'F' or updatethroughout:
                try:
                 del Nsem_1_10[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_1_10)
            if cchoice == 'G' or updatethroughout:
                try:
                 del Nsem_1_10[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_1_10)
            if cchoice == 'H' or updatethroughout:
                try:
                 del Nsem_1_10[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_1_10)
            if cchoice == 'I' or updatethroughout:
                try:
                 del Nsem_1_10[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_1_10)
            if cchoice != 'A' and cchoice != 'B' and cchoice != 'C' and cchoice != 'D' and cchoice != 'E' and cchoice != 'F' and cchoice != 'G' and cchoice != 'H' and cchoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'D':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            dchoice = str(input('Choice: ').upper())
            updatethroughout = False
            if dchoice == 'A':
                Nsem_2_10.clear()
                updatethroughout = True
            if dchoice == 'B' or updatethroughout:
                try:
                 del Nsem_2_10[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_2_10)
            if dchoice == 'C' or updatethroughout:
                try:
                 del Nsem_2_10[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_2_10)
            if dchoice == 'D' or updatethroughout:
                try:
                 del Nsem_2_10[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_2_10)
            if dchoice == 'E' or updatethroughout:
                try:
                 del Nsem_2_10[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_2_10)
            if dchoice == 'F' or updatethroughout:
                try:
                 del Nsem_2_10[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_2_10)
            if dchoice == 'G' or updatethroughout:
                try:
                 del Nsem_2_10[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_2_10)
            if dchoice == 'H' or updatethroughout:
                try:
                 del Nsem_2_10[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_2_10)
            if dchoice == 'I' or updatethroughout:
                try:
                 del Nsem_2_10[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_2_10)
            if dchoice != 'A' and dchoice != 'B' and dchoice != 'C' and dchoice != 'D' and dchoice != 'E' and dchoice != 'F' and dchoice != 'G' and dchoice != 'H' and dchoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'E':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            echoice = str(input('Choice: ').upper())
            updatethroughout = False
            if echoice == 'A':
                Nsem_1_11.clear()
                updatethroughout = True
            if echoice == 'B' or updatethroughout:
                try:
                 del Nsem_1_11[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_1_11)
            if echoice == 'C' or updatethroughout:
                try:
                 del Nsem_1_11[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_1_11)
            if echoice == 'D' or updatethroughout:
                try:
                 del Nsem_1_11[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_1_11)
            if echoice == 'E' or updatethroughout:
                try:
                 del Nsem_1_11[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_1_11)
            if echoice == 'F' or updatethroughout:
                try:
                 del Nsem_1_11[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_1_11)
            if echoice == 'G' or updatethroughout:
                try:
                 del Nsem_1_11[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_1_11)
            if echoice == 'H' or updatethroughout:
                try:
                 del Nsem_1_11[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_1_11)
            if echoice == 'I' or updatethroughout:
                try:
                 del Nsem_1_11[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_1_11)
            if echoice != 'A' and echoice != 'B' and echoice != 'C' and echoice != 'D' and echoice != 'E' and echoice != 'F' and echoice != 'G' and echoice != 'H' and echoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'F':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            fchoice = str(input('Choice: ').upper())
            updatethroughout = False
            if fchoice == 'A':
                Nsem_2_11.clear()
                updatethroughout = True
            if fchoice == 'B' or updatethroughout:
                try:
                 del Nsem_2_11[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_2_11)
            if fchoice == 'C' or updatethroughout:
                try:
                 del Nsem_2_11[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_2_11)
            if fchoice == 'D' or updatethroughout:
                try:
                 del Nsem_2_11[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_2_11)
            if fchoice == 'E' or updatethroughout:
                try:
                 del Nsem_2_11[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_2_11)
            if fchoice == 'F' or updatethroughout:
                try:
                 del Nsem_2_11[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_2_11)
            if fchoice == 'G' or updatethroughout:
                try:
                 del Nsem_2_11[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_2_11)
            if fchoice == 'H' or updatethroughout:
                try:
                 del Nsem_2_11[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_2_11)
            if fchoice == 'I' or updatethroughout:
                try:
                 del Nsem_2_11[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_2_11)
            if fchoice != 'A' and fchoice != 'B' and fchoice != 'C' and fchoice != 'D' and fchoice != 'E' and fchoice != 'F' and fchoice != 'G' and fchoice != 'H' and fchoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'G':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            gchoice = str(input('Choice: ').upper())
            updatethroughout = False
            if gchoice == 'A':
                Nsem_1_12.clear()
                updatethroughout = True
            if gchoice == 'B' or updatethroughout:
                try:
                 del Nsem_1_12[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_1_12)
            if gchoice == 'C' or updatethroughout:
                try:
                 del Nsem_1_12[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_1_12)
            if gchoice == 'D' or updatethroughout:
                try:
                 del Nsem_1_12[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_1_12)
            if gchoice == 'E' or updatethroughout:
                try:
                 del Nsem_1_12[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_1_12)
            if gchoice == 'F' or updatethroughout:
                try:
                 del Nsem_1_12[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_1_12)
            if gchoice == 'G' or updatethroughout:
                try:
                 del Nsem_1_12[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_1_12)
            if gchoice == 'H' or updatethroughout:
                try:
                 del Nsem_1_12[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_1_12)
            if gchoice == 'I' or updatethroughout:
                try:
                 del Nsem_1_12[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_1_12)
            if gchoice != 'A' and gchoice != 'B' and gchoice != 'C' and gchoice != 'D' and gchoice != 'E' and gchoice != 'F' and gchoice != 'G' and gchoice != 'H' and gchoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        elif choice == 'H':
            print('Select Option:\na. All classes\nb. Class 1\nc. Class 2\nd. Class 3\ne. Class 4\nf. Class 5\ng. Class 6\nh. Class 7\ni. Class 8\n')
            hchoice = str(input('Choice: ').upper())
            updatethroughout = False
            if hchoice == 'A':
                Nsem_2_12.clear()
                updatethroughout = True
            if hchoice == 'B' or updatethroughout:
                try:
                 del Nsem_2_12[class_1]
                except:
                    pass
                class_1 = update_class1(Nsem_2_12)
            if hchoice == 'C' or updatethroughout:
                try:
                 del Nsem_2_12[class_2]
                except:
                    pass
                class_2 = update_class2(Nsem_2_12)
            if hchoice == 'D' or updatethroughout:
                try:
                 del Nsem_2_12[class_3]
                except:
                    pass
                class_3 = update_class3(Nsem_2_12)
            if hchoice == 'E' or updatethroughout:
                try:
                 del Nsem_2_12[class_4]
                except:
                    pass
                class_4 = update_class4(Nsem_2_12)
            if hchoice == 'F' or updatethroughout:
                try:
                 del Nsem_2_12[class_5]
                except:
                    pass
                class_5 = update_class5(Nsem_2_12)
            if hchoice == 'G' or updatethroughout:
                try:
                 del Nsem_2_12[class_6]
                except:
                    pass
                class_6 = update_class6(Nsem_2_12)
            if hchoice == 'H' or updatethroughout:
                try:
                 del Nsem_2_12[class_7]
                except:
                    pass
                class_7 = update_class7(Nsem_2_12)
            if hchoice == 'I' or updatethroughout:
                try:
                 del Nsem_2_12[class_8]
                except:
                    pass
                class_8 = update_class8(Nsem_2_12)
            if hchoice != 'A' and hchoice != 'B' and hchoice != 'C' and hchoice != 'D' and hchoice != 'E' and hchoice != 'F' and hchoice != 'G' and hchoice != 'H' and hchoice != 'I':
                continue
            else:
                updatethroughout = False
                current_command = ask_input()
        else:
            continue

    elif current_command == 'CLASSES' or current_command == classredef:
        space_indent()
        for sem in All_grades:
            print(f'{sem}: {All_grades[sem]}'.replace('{', '').replace('}', '').replace('\'', ''))
        current_command = ask_input()
    
    elif current_command == 'RENAME' or current_command == renameredef:
        space_indent()
        print('Choose command to rename:\na. exit/quit\nb. update\nc. classes\nd. rename\ne. calculate\nf. clear')
        rechoice = str(input('Choice: ').upper())
        if rechoice == 'A':
            rename = str(input('New Name: ').upper())
            if rename == exitredef or rename == updateredef or rename == classredef or rename == renameredef or rename == calculateredef or rename == clearredef:
                print('This rename already exists!')
                continue
            else:
                exitredef = rename
                current_command = ask_input()
        elif rechoice == 'B':
            rename = str(input('New Name: ').upper())
            if rename == exitredef or rename == updateredef or rename == classredef or rename == renameredef or rename == calculateredef or rename == clearredef:
                print('This rename already exists!')
                continue
            else:
                updateredef = rename
                current_command = ask_input()
        elif rechoice == 'C':
            rename = str(input('New Name: ').upper())
            if rename == exitredef or rename == updateredef or rename == classredef or rename == renameredef or rename == calculateredef or rename == clearredef:
                print('This rename already exists!')
                continue
            else:
                clearredef = rename
                current_command = ask_input()
        elif rechoice == 'D':
            rename = str(input('New Name: ').upper())
            if rename == exitredef or rename == updateredef or rename == classredef or rename == renameredef or rename == calculateredef or rename == clearredef:
                print('This rename already exists!')
                continue
            else:
                renameredef = rename
                current_command = ask_input()
        elif rechoice == 'E':
            rename = str(input('New Name: ').upper())
            if rename == exitredef or rename == updateredef or rename == classredef or rename == renameredef or rename == calculateredef or rename == clearredef:
                print('This rename already exists!')
                continue
            else:
                calculateredef = rename
                current_command = ask_input()
        elif rechoice == 'F':
            rename = str(input('New Name: ').upper())
            if rename == exitredef or rename == updateredef or rename == classredef or rename == renameredef or rename == calculateredef or rename == clearredef:
                print('This rename already exists!')
                continue
            else:
                clearredef = rename
                current_command = ask_input()
        else:
            continue

    elif current_command == 'CALCULATE' or current_command == calculateredef:
        space_indent()
        Nsem1_9GPA_40list = convertto40(Nsem_1_9.copy())
        Nsem2_9GPA_40list = convertto40(Nsem_2_9.copy())
        Nsem1_10GPA_40list = convertto40(Nsem_1_10.copy())
        Nsem2_10GPA_40list = convertto40(Nsem_2_10.copy())
        Nsem1_11GPA_40list = convertto40(Nsem_1_11.copy())
        Nsem2_11GPA_40list = convertto40(Nsem_2_11.copy())
        Nsem1_12GPA_40list = convertto40(Nsem_1_12.copy())
        Nsem2_12GPA_40list = convertto40(Nsem_2_12.copy())
        calc40GPA()
        current_command = ask_input()

    elif current_command == 'CLEAR' or current_command == clearredef:
        for diction in All_grades:
            (All_grades[diction]).clear()
        current_command = ask_input()

    elif current_command == 'FUN' or current_command == funredef:
        print('a. Random Binary\nb. AI interaction\nc. RPG Game')
        choice = str(input('Choice: ').upper())
        if choice == 'A':
            i = 0
            for b in range(3000):
                number = random.randint(0, 1)
                print(number, end='')
                i += 1
                if i == 4:
                    i = 0
                    print(' ', end='')
        elif choice == 'B':
            Ai_interact()
        elif choice == 'C':
            space_indent()
            space_indent()
            exec(open('/Users/anthonyjr./Desktop/MultiTasker/RPG.py').read())
            print('Welcome back to MultiTasker!')
        else:
            continue
        print()
        current_command = ask_input()

    else:
        space_indent()
        print('Unkown Command.')
        print('Type \'help\' for list of commands.')
        current_command = ask_input()