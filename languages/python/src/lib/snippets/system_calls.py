"""
System command calls and subprocess operations
"""
import os
import sys
import subprocess as sp
from subprocess import Popen, PIPE

def exec_cmd(cmd:str):
    """
    Execute command specified and 
    Return the return/exit code

    :: Params
    :: Positionals
    ::  - cmd : The command string to execute
    ::      Type: <string>
    """
    ret_Code:int = os.system(cmd)
    return ret_Code

def exec_return_using_communicate(cmd:str, verbose=False):
    """
    Execute command specified and 
    Return the stdout result using PIPE

    :: Params
    :: Positionals
    ::  - cmd : The command string to execute
    ::      Type: <string>
    ::
    ::  - verbose : If want to enable verbose output
    ::      Type: <boolean>
    ::      Valid Values: True|False
    """
    # Initialize Variables
    out:list = []

    # Process PIPE/subprocess system calls
    # proc = Popen(cmd)
    # proc.stdout;
    if(cmd != ""):
        # Prepare command list
        cmd_list = cmd.split(" ") # Split the command string into a space-delimited list
        cmd_exec = cmd_list[0] # First index is the executable
        cmd_args = cmd_list[1:] # Consecutive elements are the arguments
        cmd_run = [cmd_exec, *cmd_args] # Create a run list with [0] = Executable and all consecutive arguments are expanded into a list of all options/arguments

        # Begin
        with Popen(cmd_run, stdout=PIPE) as process:
            print("Input Command: {}".format(cmd_run))
            # Poll
            poll_value = process.poll() # Poll

            # Get standard output
            if(process.stdout != None):
                # Communicate and Decode stdout string
                stdout_val = process.communicate()[0].decode("utf-8").split("\n")[1:] # [0] = stdout, [1] = Error/exit status code

                # append into stdout list
                out = stdout_val

                # Close subprocess after use
                process.stdout.close()

    # Return output
    return out

def exec_return_real_time(cmd:str, real_time=False):
    """
    Execute command specified and 
    Return the stdout result using PIPE 
    in real time

    :: Params
    :: Positionals
    ::  - cmd : The command string to execute
    ::      Type: <string>
    ::
    ::  - real_time : If want to enable Real Time Output; 
    ::      - Notes
    ::          + Remove all display of output in the references if you enable this
    ::      Type: <boolean>
    ::      Valid Values: True|False
    """
    # Initialize Variables
    out:list = []
    nextline:str = ""

    # Process PIPE/subprocess system calls
    if(cmd != ""):
        # Prepare command list
        cmd_list = cmd.split(" ") # Split the command string into a space-delimited list
        cmd_exec = cmd_list[0] # First index is the executable
        cmd_args = cmd_list[1:] # Consecutive elements are the arguments
        cmd_run = [cmd_exec, *cmd_args] # Create a run list with [0] = Executable and all consecutive arguments are expanded into a list of all options/arguments

        # Begin
        with Popen(cmd_run, stdout=PIPE) as process:
            # Get next line in the list
            # nextline = process.stdout.readline().decode("utf-8").replace("\r\n", "\n")

            # poll to check if is still alive
            # poll = process.poll()

            # Do a loop to check if there are still lines from the process
            while True:
                # Get next line in the process stdout
                nextline = process.stdout.readline().decode("utf-8")

                # poll to check if is still alive
                poll = process.poll()

                """
                - Check if process has been terminated
                    process.poll() == None: The process has not yet been terminated
                    process.poll() != None: The process has been terminated
                """
                if nextline == "" and poll is not None:
                    # Process has terminated
                    # print("Process has been terminated.")
                    break
                elif nextline:
                    # There are still nextline

                    ## Format data
                    data = nextline.replace("\r\n", "\n").rstrip()

                    ## Manage data
                    out.append(data)

                    ## Check if realtime output is enabled
                    if(real_time):
                        print(data)

            ## Communicate and Decode stdout string
            # out = process.communicate()[0].decode("utf-8").split("\n")[1:] # [0] = stdout, [1] = Error/exit status code
            # exit_code = process.returncode

    # Return output
    return out

def main():
    """
    Debug tests
    """

if __name__ == "__main__":
    main()
