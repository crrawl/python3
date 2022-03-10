
# class PythonSwitchStatement:
 
#     def switch(self, month):
#         default = "Incorrect month"
#         return getattr(self, 'case_' + str(month), lambda: default)()
 
#     def case_1(self):
#         return "January"
 
#     def case_2(self):
#         return "February"
 
#     def case_3(self):
#         return "March"
 
#     def case_4(self):
#         return "April"
 
#     def case_5(self):
#         return "May"
 
#     def case_6(self):
#         return "June"
 
# s = PythonSwitchStatement()
 
# print(s.switch(1))
# print(s.switch(3))
# print(s.switch(9))

class Switch():

    def switch(self, command):
        command[0].lower().strip()
        default = "[-] Unknown command"
        return getattr(self, f'cmd_{command[0]}', lambda: default)()

    def cmd_addrobot(self):
        return 'addrobot'

cmd_ = Switch()

while True:
    try:
        cmd = [agr for agr in input("command: ").split()]

    except KeyboardInterrupt:
        print('\n Programm closed')
        exit()

    print(cmd_.switch(cmd))
