import os
from pywebio.input import input
from pywebio.output import put_text as printt

name = input("username: ")
age  = input("age: ")

printt(f"Your name is {name} \nAnd your age is {age} ")