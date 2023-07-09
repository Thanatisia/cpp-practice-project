# C++ practice project

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
This is a practice ground for implementing various C++ concepts 

[Currently implemented]
- CLI Argument parsing, 
- system command calling and 
- working on pipes.

Generally, the aim is to create a write-up/documentation repository to reference whenever I want to implement the above in C++

- Documentations as to how things works will be added in due time
```

## Setup
+ Please refer to [BUILD.md](BUILD.md) for instructions to setup the application

## Documentation
### Synopsis/Syntax
```console
cpp-practice-project {options} <arguments>
```

### Parameters
- Positionals
- Optionals
    - With Arguments
        + `-e "<command to execute>"` | `--exec "<command to execute>"` : Specify command to execute; Reusable, repeat usage to append more commands to execute
    - Flags

### Usage
- Executing commands
    ```console
    cpp-practice-project -e "cmd-1 opts"
    ```

- Executing multiple commands
    ```console
    cpp-practice-project -e "cmd-1 opts" -e "cmd-2 opts" ...
    ```

## Wiki

### Snippets and Examples

## Resources

## References
+ [raymii - Execute a command and get both output and exit code](https://raymii.org/s/articles/Execute_a_command_and_get_both_output_and_exit_code.html)

## Remarks
