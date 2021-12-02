import os

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

# PyWebIO application
def main():
    put_text("Hello WOrld")


if __name__ == "__main__":
    start_server(main,debug="True", host="localhost", port=8080)
