import json

# a Python object (dict):
dict = {
    "N": '''Ko izvadīs kods zemāk ?
#include<stdio.h>
int main(){printf ("Hi World\n");return 0;}

[option](a)[/] Izvadīsies Hi World
[option](b)[/] Izvadīsies - Incorrect module: name does imported
[option](c)[/] Izvadīsies - SyntaxError: invalid syntax
'''
}

# convert into JSON:
y = json.dumps(dict)

# the result is a JSON string:
print(y)