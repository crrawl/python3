# -----------------------------------------------------
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
# -----------------------------------------------------

# veriables

CURRENT_USER = "admin:777" # Later connect this from DB FORM = user:permisions
# funcitons
def whoami():
    print(CURRENT_USER)

def help():
    print(f"=== Allowed commands for {CURRENT_USER}! ===")
    name, perm = CURRENT_USER.split(":")
    if perm == 777:
        print(f"""
/help
/whoami
        """)
def errorNotFound():
    print("Command not found") 

if __name__ == "__main__":

    while True:
        try:
            cmd = input("insert a command > ").split()
        except ValueError:
            cmd, agr = input("insert a command > ").split()
        except ValueError:
            cmd, agr, agr1 = input("insert a command > ").split()
        
        if cmd == list("/whoami"):
            print(cmd)
            whoami()
            break
        elif cmd == "/help".lower():
            help()
        else:
            errorNotFound()
