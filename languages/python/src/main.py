"""
Python Practice Project
"""
# Built-in Libraries
import os
import sys
import datetime
from pathlib import Path # For path handling
import subprocess as sp # For system command execution and subprocess Pipes

# External Libraries
import lib.snippets.system_calls as syscalls
import lib.snippets.files as file_snippets

def display_help():
    global argv, argc, exec

    help_msg:str = """Help:
    Synopsis/Syntax
        {} [options] <arguments>

    Parameters:
        - Options
            - With Arguments
                + {}
            - Flags
                + {}
                + {} 
                + {}
    """.format(
        exec,
        "begin : Start the system command call execution",
        "-e <command-string> | --execute <command-string> : Specify the command to execute; Repeat this to append to the command list",
        "-o | --redirect-stdout : Enable Redirect standard output",
        "-h | --help            : Display this help message",
        "-v | --version         : Display system version information"
    )
    print(help_msg)

def display_version():
    """
    Display system version
    """
    print("{}".format(PROG_NAME))
    print("System Version: {}".format(PROG_VERS))

def gen_cli_args():
    """
    Get and Process/sanitize CLI arguments and options and
    return the arguments
    """
    return [argc, argv]

def update_cli_args(index):
    """
    Update the CLI arguments list after
    removing the value and moving to the next options

    - Required if you are handling an option with arguments
    """
    global argv

    # Pop out the index
    argv.pop(index)

def execute():
    global flags

    # Get command list from flags
    cmd_list:list = flags["commands"]
    num_of_cmd = len(cmd_list)

    # Check if there are commands to execute
    if(num_of_cmd > 0):
        # Loop through all commands to execute
        for i in range(num_of_cmd):
            # Get current command
            cmd_str = cmd_list[i]

            """
            Execute current argument
            """
            # Check if execute using system call, or pipe subprocesses
            ## - Check for the 'redirect-stdout' flag
            if("redirect-stdout" in flags):
                # Keyword is in flag
                if (flags["redirect-stdout"] == True):
                    """
                    Flag to enable: pipe subprocess to return stdout
                    """
                    # Initialize Variables
                    out:list = []

                    # Execute
                    print("Executing [{}]...".format(cmd_str))
                    out = syscalls.exec_return_real_time(cmd_str, True)

                    # Completed
                    ## Process Output
                    # print("")
                    # print("Standard Output: {}".format(cmd_str))
                    # for curr_line in out:
                    #     print("{}".format(curr_line))
                else:
                    # Return exit code
                    ret_Code:int = syscalls.exec_cmd(cmd_str)
                    print("Return Code : {}".format(ret_Code))
                    if(ret_Code == 0):
                        # 0 = Success
                        # 1 = Error
                        print("[+] Command [{}] executed successfully.".format(cmd_str))
    else:
        print("No commands to execute")

def process_args():
    """
    Process CLI arguments and options
    """
    global argc, argv, flags

    # Declare variables
    # argc:int = 0
    # argv:list = []
    opt_value:str = ""

    # Obtain arguments
    # argc, argv = gen_cli_args()

    # Check if there are arguments provided
    if(argc > 0):
        # Arguments provided
        # Loop through all recorded arguments
        i:int = 0
        # While current index is not the last element
        while i < argc:
            # Get current argument
            arg:str = argv[i]

            # Check argument option
            ### Positionals
            if (arg == "begin"):
                ## Start command execution
                execute()
            ### Option with Arguments ###
            elif (arg == "-e") or (arg == "--execute"):
                """
                Execute system command calls for each of the registered system commands
                """
                # Check if there are arguments after this
                if (i != (argc - 1)):
                    # This is not the last element in the list

                    # Get the next index
                    i = i+1

                    ## Get command to execute 
                    cmd_str:str = argv[i]

                    ## Append command into command list
                    flags["commands"].append(cmd_str)

                    ## Pop out the option value
                    argv.pop(i)

                    ## Reduce the count
                    argc = argc-1

                    ## Reduce the current index by 1 to remove the value
                    i = i-1
            ### Flags ###
            elif (arg == "-o") or (arg == "--output"):
                # Enable Redirect standard output
                flags["redirect-stdout"] = True
            elif (arg == "-h") or (arg == "--help"):
                # Help Menu
                display_help()
            elif (arg == "-v") or (arg == "--version"):
                # Display system version
                display_version()
            else:
                # Default option
                print("Invalid option provided: [{}]".format(arg))

            ## Increase index
            i += 1
    else:
        # No arguments provided
        print("No arguments provided.")

def init():
    """
    Initialization of defaults
    """
    # Global Variables
    global exec, argc, argv, flags, PROG_NAME, PROG_VERS

    # Declare and Initialize
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)
    flags = {
        "redirect-stdout" : False,
        "commands" : []
    }
    PROG_NAME = "cli-arguments"
    PROG_VERS = "v0.1.0"

def setup():
    """
    Basic Setup + preparing dependencies
    """
    init()
    # Get CLI Argument and options
    gen_cli_args()

def main():
    process_args()

if __name__ == "__main__":
    setup()
    main()

