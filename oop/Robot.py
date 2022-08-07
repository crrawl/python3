class Robot():
    
    population = 0

    def __init__(self, name):
        self.name = name

        print(f'[!] Initializing {self.name} ...')
        Robot.population += 1
        print(f'[+] Initialized {self.name}')
    
    def __del__(self):
        
        print(f'[!] Destroing {self.name} ...')
        
        Robot.population -= 1
        print(f'[+] {self.name} Destroyed')
        
        if Robot.population == 0:
            print(f'[!] {self.name} is lastest') 
        else:
            print(f'[!] Bare {Robot.population} robots online')

    def sayHi(self):
        print(f'[SERVER] My master call me {self.name}')
    
    @staticmethod
    def count():
        print(f'[SERVER] We have {Robot.population} robots')

android = Robot('mark-1')
android.sayHi()
Robot.count()

android1 = Robot('mark-2')
android1.sayHi()
Robot.count()