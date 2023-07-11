"""
Python Practice Project
"""
# Built-in Libraries
import os
import sys
import datetime
import argparse # For CLI Argument Parsing
from pathlib import Path # For path handling
import subprocess as sp # For system command execution and subprocess Pipes

# External Libraries
import lib.snippets.system_calls as syscalls
import lib.snippets.files as file_snippets

def gen_cli_args():
    """
    Get and Process CLI arguments and options from the ArgumentParser and 
    return the parser and arguments
    """
    global parser, args

    if(parser == None):
        # Empty object
        # Create ArgumentParser class object
        parser = argparse.ArgumentParser()
    
    # Parse all arguments to an argument list
    args = parser.parse_args()

    # Return values
    return [parser, args]

def set_path_args():
    """
    Path-related arguments
    """
    global parser, args

    # Generate fresh argument parser
    parser, args = gen_cli_args()

    # Add CLI positional argument
    parser.add_argument("path")

    # Refresh parser and arguments
    parser, args = gen_cli_args()

def set_system_args():
    """
    System Calls related arguments
    """
    global parser, args

    # Refresh parser and arguments
    parser, args = gen_cli_args()

    """
    Add CLI optionals with argument values
    - Actions:
        - append : All consecutive usage of this option with a value will add the value to a list
    """
    parser.add_argument("-e", "--exec", action="append")

    """
    Add CLI optional flags (No values)
    - Actions:
    """
    parser.add_argument("-o", "--return-stdout", action="store_true")

    # Refresh parser and arguments
    parser, args = gen_cli_args()

def process_args():
    """
    Process CLI arguments and options
    """
    # Refresh parser and arguments
    parser, args = gen_cli_args()

    if args.exec:
        """
        Execute system command calls for each of the registered system commands
        """
        print("Commands to execute: {}".format(args.exec))
        print("")
        for arg in args.exec:
            # Execute current argument
            # Check if execute using system call, or pipe subprocesses
            if args.return_stdout:
                """
                Flag to enable: pipe subprocess to return stdout
                """
                # Initialize Variables
                out:list = []

                # Execute
                print("Executing [{}]...".format(arg))
                out = syscalls.exec_return(arg)

                # Completed
                ## Process Output
                print("")
                print("Standard Output:".format(arg))
                for curr_line in out:
                    print("{}".format(curr_line))
            else:
                # Return exit code
                ret_Code:int = syscalls.exec_cmd(arg)
                print("Return Code : {}".format(ret_Code))
                if(ret_Code == 0):
                    # 0 = Success
                    # 1 = Error
                    print("[+] Command [{}] executed successfully.".format(arg))

def init():
    """
    Initialization of defaults
    """
    global parser, args

    # Declare and Initialize
    parser = None
    args = None

def setup():
    """
    Basic Setup + preparing dependencies
    """
    init()
    # Get CLI Argument and options
    set_system_args()

def main():
    process_args()

if __name__ == "__main__":
    setup()
    main()

