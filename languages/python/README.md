# Python practice project

## Table of Contents
+ [Information](#information)
+ [Setup](BUILD.md)
+ [Documentation](#documentation)
+ [Resources](#resources)
+ [References](#references)
+ [Remarks](#remarks)

## Information
### Description
```
This is a practice ground for implementing various Python concepts 

[Currently implemented]
- CLI Argument parsing, 
- system command calling and 
- working on pipes.

Generally, similar to the C++ practice project, the aim is to create a write-up/documentation repository to reference whenever I want to implement the above in Python

- Documentations as to how things works will be added in due time
```

## Setup
+ Please refer to [BUILD.md](BUILD.md) for instructions to setup the application

## Documentation
### Synopsis/Syntax
```console
python src/main.py {options} <arguments>
```

### Parameters
- Positionals
- Optionals
    - With Arguments
        + `-e "<command to execute>"` | `--exec "<command to execute>"` : Specify command to execute; Reusable, repeat usage to append more commands to execute
    - Flags
        + -o | --return-stdout : Enables return standard output; Runs command using subprocess PIPE instead of system execute; Default: Disabled

### Usage
- Executing commands
    ```console
    python src/main.py -e "cmd-1 opts"
    ```

- Executing multiple commands
    ```console
    python src/main.py -e "cmd-1 opts" -e "cmd-2 opts" ...
    ```

- Executing using system call and return exit/return code
    ```console
    python src/main.py -e "cmd-1 opts" ...
    ```

- Executing using subprocess PIPING to return standard output
    ```console
    python src/main.py -e "cmd-1 opts" ... -o
    ```

## Wiki

### Snippets and Examples

## Resources

## References
+ [RealPython - Python Command Line Interfaces with Argparse](https://realpython.com/command-line-interfaces-python-argparse/)

## Remarks
