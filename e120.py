"""
[Source code for the E120 programming language.]
[Read /README.md to use E120 properly]

(:

@@@@@@@@  @@@  @@@@@@   @@@@@@ 
@@!      @@@@ @@   @@@ @@!  @@@
@!!!:!    !@!   .!!@!  @!@  !@!
!!:       !!!  !!:     !!:  !!!
: :: ::   ::  :.:: :::  : : :: 

"""

import sys
from sys import exit
import os

program_filepath = sys.argv[1]
start_line = int(sys.argv[2]) if len(sys.argv) > 2 else None 
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
start_found = False

for line in program_lines:
    if not start_found:
        if line.strip().startswith("start"):
            start_found = True
        continue 
    parts  = line.split(" ")
    code = parts[0]

    if code == "":
        continue
    
    if code.startswith("$"):
        continue

    if code.endswith(":"):
        label_tracker[code[:-1]] = token_counter
        continue

    program.append(code)
    token_counter += 1

    if code in {"push", "stack", "stacksize"}:
        if code == "push":
            try:
                number = int(parts[1])
                program.append(number)
                token_counter += 1
            except ValueError:
                try:
                    number = float(parts[1])
                    program.append(number)
                    token_counter += 1
                except ValueError: # very cursed lmao
                    raise ValueError

        else:
            number = int(parts[1])
            program.append(number)
            token_counter += 1

    elif code in {"out", "nfout", "shell", "external"}:
        fs = ' '.join(parts[1:])
        string_literal = fs.split('$')[0]
        string_literal = string_literal.strip().strip('"')
        program.append(string_literal)
        token_counter += 1

    elif code in {"goto"}:
        label = parts[1]
        program.append(label)
        token_counter += 1

# to do - add for loops

    elif code in {"ifequ","ifneq","ifgtr","iflsr","ifequsp","ifgtrsp","iflsrsp","ifneqsp", "for"}:
        v = parts[1]
        program.append(v)
        token_counter += 1
        label = parts[2]
        program.append(label)
        token_counter += 1

class Stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp    = -1
        self.size = size 

    def push(self, number):
        if self.sp >= self.size - 1:
            if printerror:
                print(f"\033[48;5;{1}m\033[1;39m → [e120 - Stack Overflow] ← \033[0m")
            exit(1)
        else:
            self.sp += 1
            self.buf[self.sp] = number

    def pop(self): # pop with no output
        if self.sp < 0:
            if printerror:
                print(f"\033[48;5;{1}m\033[1;39m → [e120 - Stack underflow] ← \033[0m")
            exit(1)  
        number = self.buf[self.sp]
        self.sp -= 1
        return number

    def outpop(self): # pop with output
        if self.sp < 0:
            print(f"\033[48;5;{1}m\033[1;39m → [e120 - Stack underflow] ← \033[0m")
            exit(1) 
        number = self.buf[self.sp]
        self.sp -= 1
        print(number ,end="")
    
    def top(self):
        return self.buf[self.sp]
    def reverse(self):
        stack.buf = stack.buf.reverse()

pc = 0
stack = Stack(1024)
printerror = True

if start_line is not None:
    pc = min(max(0, start_line - 1), len(program) - 1)  

while program[pc] != "done":
    code = program[pc]
    pc += 1

    if code in {"push", "stack", "stacksize", "stacklen"}:
        number = program[pc]
        pc += 1

        if code == "push":
            stack.push(number)

        elif code == "stack":
            print(stack.buf[number], end="")

        elif code == "stacksize":  
            stack.buf = [0 for _ in range(number)]

        elif code == "stacklen":
            print(len(stack.buf) ,end="")

    elif code == "errorquiet":
        printerror = False

    elif code == "errorloud":
        printerror = True
        
    elif code == "pop":
            stack.outpop()
        
    elif code == "popquiet":
            stack.pop()
        
    elif code == "funcpos":
        print(label_tracker,end="")

    elif code == "external": # call external script - use funcpos to figure out where to start - VERY USEFUL if wanting to start at a function
        string_literal = program[pc]
        pc += 1
        try:
            os.system(f"python3 e120.py {string_literal}")
        except:
            os.system(f"python e120.py {string_literal}")

    elif code in {"out", "outsl", "shell", "external", "nfout"}:
        string_literal = program[pc]
        cle = len(string_literal)
        pc += 1

        if code == "out":
            string_literal = string_literal.encode('utf-8').decode('unicode_escape')
            print(string_literal, end="")
        if code == "nfout":
            print(string_literal, end="")
        elif code == "shell":
            os.system(string_literal)

    elif code in {"goto"}:
        if code == "goto":
            label = program[pc]
            pc += 1 
            if label in label_tracker:
                pc = label_tracker[label]

    elif code.startswith("if"):
        n1, label = int(program[pc]), program[pc + 1]
        pc += 2
        condition_met = False
        if code == "ifequ" and stack.top() == n1:
            condition_met = True
        elif code == "ifneq" and stack.top() != n1:
            condition_met = True
        elif code == "ifgtr" and stack.top() < n1:
            condition_met = True
        elif code == "iflsr" and stack.top() > n1:
            condition_met = True
        elif code == "ifequsp" and stack.sp == n1:
            condition_met = True
        elif code == "ifneqsp" and stack.sp != n1:
            condition_met = True
        elif code == "ifgtrsp" and stack.sp < n1:
            condition_met = True
        elif code == "iflsrsp" and stack.sp > n1:
            condition_met = True
        if condition_met:
            pc = label_tracker.get(label, pc)

    elif code in {"add", "sub", "mul", "div"}:
        a = stack.pop()
        b = stack.pop()
        if code == "add": 
            stack.push(a+b)
        elif code == "sub":
            stack.push(b-a)
        elif code == "mul":
            stack.push(b*a)
        elif code == "div":
            try:
                stack.push(b/a)
            except ZeroDivisionError:
                if printerror:
                    print(f"\033[48;5;{1}m\033[1;39m → [e120 - Cannot divide by 0] ← \033[0m")

    elif code in {"program", "fullstack", "clear", "top", "funcpos"}:
        if code == "program": 
            print(program)

        elif code == "fullstack": 
            print(stack.buf)

        elif code == "clear":
            stack.sp = -1
            for x in range(len(stack.buf)):
                stack.push(0) 
            stack.sp = -1

        elif code == "top": 
            print(stack.buf[stack.sp] ,end="")

        elif code.startswith(c):
                continue
    elif code == "breakpoint" or code == "@@@":
        if printerror:
            print(f"\033[48;5;{1}m\033[1;39m → [e120 - Breakpoint reached] ← \033[0m")
        exit(0)

    elif code == "stop":
        exit(0)

    elif code == "in":
        number = input(prompt)
        try:
            number = int(number)
        except ValueError:
            try:
                number = float(number)
            except ValueError:
                if printerror:
                    print(f"\033[48;5;{1}m\033[1;39m → [e120 - {number} is not a float or an int] ← \033[0m")
                    exit(1)
        stack.push(number)

    else:
        if printerror:
            print(f"\033[48;5;{1}m\033[1;39m → [e120 - Unexpected code received {program[pc-1]}] ← \033[0m")
            exit(1)

# credit to bvdl.io for the starting commands: halt (stop), push, pop, add, sub, print (out), read (in), jump eq 0 L1 (ifequ x l1), jump gt 0 (ifgtr x l1)
