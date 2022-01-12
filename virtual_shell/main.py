# -----------------------------------------------------
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
# -----------------------------------------------------

import os

from rich.console import Console
from rich.theme import Theme


# FUNCTIONS
def clearTerminal():
    """Check user OS and clear chat"""

    if os.name == "nt":  # posx, java, nt
        os.system("cls")
    else:
        os.system("clear")


# commands
def whoami():
    """Retrun current user status information"""
    console.print(
        f"[info]Name[/] {USERNAME}[info], permisions[/] {PERMISION}"
        )


def mkdir(dirname):
    """make a directory"""
    path = os.path.join(CURRENT_PATH, dirname) 
    os.mkdir(path)

    try: 
        path = os.path.join(CURRENT_PATH, dirname)
        os.mkdir(path)
        os.makedirs(path, exist_ok = True)
    except OSError: 
        f = open(f"{CURRENT_PATH}logfile.txt", "a")
        f.write(f"\n {USERNAME} has created a directory {path}")
        f.close()


def commands():
    console.print("""
==================== COMMANDS ====================
whoami | return your status
mkdir dirname | make directory
    """)


# create a custum color theme
custom_theme = Theme(
    {
        "error": "bold red",
        "success": "bold green",
        "attention": "bold yellow",
        "warning": "bold magenta",
        "option": "#4169E1",
        "blocked": "#383B40",
        "info": "cyan",
        "green": "green",
        "blue": "blue",
    }
)


# Stylizing console!
console = Console(theme=custom_theme)

# tmp data TODO: take all data from data base
SHELLNAME = "kuramuShell"
USERNAME = "yukurasan"
HOSTNAME = "kuramuShell"
PERMISION = "dev"

# constants
CURRENT_PATH = "C:\\python3\\virtual_shell\\"
# START SCRIPT
clearTerminal()

console.print("""
-----------------------------------------------------
@Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
@github https://github.com/yuukuramu
@instagram https://www.instagram.com/raibisu.kuramu
@site https://yuukuramu.xyz
-----------------------------------------------------
""")

# main script functionality
if __name__ == "__main__":
    while True:
        try:
            command = [console.input(
                f"[green]{USERNAME}@{HOSTNAME}[/][blue]:~$[/] "
                ).lower().split()]

            for cmd in command:
                if cmd[0] == "whoami":
                    whoami()
                    break
                elif cmd[0] == "mkdir":
                    mkdir(cmd[1])
                    break
                else:
                    console.print("[warning][!][/] unknown command")

        except KeyboardInterrupt:
            console.print(f"\n[info]{SHELLNAME} has been closed[/]")
            exit()
