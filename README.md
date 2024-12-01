# E120 - A language by Typhoonz0 on GitHub

# READ BELOW TEXT FIRST
Read the WHOLE documentation and look at the example programs so you can make programs effeciently
Run a e120 file like this: `python3 e120.py <program_filepath>.e120`
Example: `python3 e120.py examples/colourtest.e120`

(If python3 doesn't work for you, update to python v3 or run every python3 command as just python)

e120 is a STACK based language - instead of using variables to store data it uses a giant list:
https://www.tutorialspoint.com/data_structures_algorithms/images/stack_representation.jpg

PROGRAMS WILL NOT RUN IF YOU DONT PLACE A START KEYWORD!

Install syntax highlighting and code completion in VSCODE:
Press `Ctrl + P` or `Cmd + P`
Type `>Install Extension From Location`
Press `ENTER` and choose the `/e120-vscode-syntax` folder
# READ ABOVE TEXT FIRST

It's best to view this in a markdown viewer - if you don't have one, thats fine, read on.
Credit to [bvdl.io](https://www.youtube.com/@bvdlio) on YouTube for the original interpreter.  
This file showcases the capabilities of E120. The commands included are:
- `start`
- `stop`
- `done`
- `push`
- `pop`
- `popquiet`
- `stack`
- `add`
- `sub`
- `mul`
- `div`
- `in`
- `out`
- `sl`
- `ifequ`
- `ifneq`
- `ifgtr`
- `iflsr`
- `ifequsp`
- `ifgtrsp`
- `ifneqsp`
- `program`
- `top`
- `goto`
- `shell`
- `external`
- `clear`
- `fullstack`
- `stacksize`
- `stacklen`
- `breakpoint`
- `@@@`
- `errorquiet`
- `errorloud`

## Command Descriptions
<> = required, [] = optional
### `start`
**Usage**: `start`  
This command marks the beginning of the program. Without this command, your program will not execute.

### `$`
**Usage**: `$ annotation`

Use `$` to write a comment.

### `in`
**Usage**: `in`  
Prompts the user for input and saves it onto the stack. 
Will print a new line after automatically.

### `out`
**Usage**: `out "<message>"`  
Prints the specified message to the console. 
Note: You must use `\n` to print a new line.

### `nfout`
**Usage**: `nfout "<message>"`  
Prints the specified message to the console with no escape encoding. 

### `goto`
**Usage**: `goto <function>`  
This will execute a function without using conditional statements.

### `program`
**Usage**: `program`  
Outputs the entire parsed program to the console, useful for debugging.

### `push`
**Usage**: `push <value>`  
Pushes a specified value onto the stack.

### `pop`
**Usage**: `pop`  
Prints the top value from the stack and moves the stack pointer by 1. 

### `popquiet`
**Usage**: `popquiet`  
Moves the stack pointer by 1 without printing its value.

### `stack`
**Usage**: `stack <index>`  
Prints the integer at the specified index on the stack.

### Math
- `add`: Adds the top two numbers on the stack. 
- `sub`: Subtracts the top two numbers on the stack. 
- `mul`: Multiplies the top two numbers on the stack. 
- `div`: Divides the top two numbers on the stack. 

### `top`
**Usage**: `top`  
Prints the 0th element on the stack (the top value).

### Conditional Statements
- **`ifequ <value> <function>`**: Executes `<function>` if the top of the stack is equal to `<value>`.
- **`ifneq <value> <function>`**: Executes `<function>` if the top of the stack is not equal to `<value>`.
- **`ifgtr <value> <function>`**: Executes `<function>` if the top of the stack is greater than `<value>`.
- **`iflsr <value> <function>`**: Executes `<function>` if the top of the stack is lesser than `<value>`.
- **`ifequsp <value> <function>`**: Executes `<function>` if `value` is equal to the stack pointer's position.
- **`ifneqsp <value> <function>`**: Executes `<function>` if `value` is not equal to the stack pointer's position.
- **`ifgtrsp <value> <function>`**: Executes `<function>` if `value` is greater than the stack pointer's position.
- **`iflsrsp <value> <function>`**: Executes `<function>` if `value` is lesser than the stack pointer's position.

### `clear`
**Usage**: `clear`  
Clears the stack completely.

### `fullstack`
**Usage**: `fullstack`  
Prints out the entire stack.

### `stacksize`
**Usage**: `stacksize <size>`  
Sets the stack size to the specified value.

### `breakpoint`
**Usage**: `breakpoint` or `@@@`  
Stops the program for debugging.

### `funcpos`
**Usage**: `funcpos`

Prints where all the functions are in a script.
After using funcpos, delete it before running your code otherwise your code won't work.

### `external`
**Usage**: `external "<filename> [line]"`  
Calls another `.e120` script.
Use the line argument to start at a specific line, great for using specific functions.
See funcpos above to find that line.
Runs the whole script if no line is specified.

### `shell`
**Usage**: `shell "<command>"`  
Uses your shell to execute commands. Make sure that these commands work on all shells or your program may work unexpectedly.
Examples:
`shell "echo Hello"`
`shell "python3 -c 'import os; print("You are on posix" if os.name == "posix" else "You are not on posix")'"`

### `errorquiet`/`errorloud`
**Usage**: `errorquiet` or `errorloud`

Sets the status for printing errors - some errors may still get printed.

### `done`
**Usage**: `done`  
Ends a function or statement to prevent unexpected code execution. Don't use stop unless you want the program to fully exit.

### `stop`
**Usage**: `stop`  
Fully stops the program. Use this when the program has finished executing.
