# AssemblerSimulator (ReTI-Interpreter), 2019 by Leon Steinbach

## Usage

```python interpreter.py <file.txt>```

## Info

* The program has 32 bits of memory.
* Commands are separated by linebreaks.
* Parameters of commands are separated by one space.
* Comments can be written in a separat line with a # at the beginning.

## Commands

```LOAD <M>       # Loads the value of the adress M to the accumulator.
STORE <M>      # Stores the accumulator value in the adress M.
SETACC <d>     # Sets the accumulator value to a digit d.
MOVE <M1> <M2> # Copies the value in adress M1 to adress M2.
ADD <M1> <M2>  # Adds the value of the adress M2 to the value of the adress M1.
SUB <M1> <M2>  # Subtracts the value of the adress M2 from the value of the adress M1.
JUMP <o> <d>   # Compares the accumulator value with the operand o. If true, the programm jumps d lines.
JUMP <d>       # The programm jumps d lines.
PRINT          # Prints the accumulator value.
```
