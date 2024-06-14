import subprocess

def run_command_in_path(command1, command2, path):
    try:
        # Run the first command in the specified path
        process1 = subprocess.Popen(command1, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Wait for the first command to finish
        process1.wait()
        
        # Print the standard output and standard error of the first command
        print("Command 1 - Standard Output:")
        print(process1.stdout.read())
        print("Command 1 - Standard Error:")
        print(process1.stderr.read())

        # Run the second command in the specified path
        process2 = subprocess.Popen(command2, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Wait for the second command to finish
        process2.wait()

        # Print the standard output and standard error of the second command
        print("Command 2 - Standard Output:")
        print(process2.stdout.read())
        print("Command 2 - Standard Error:")
        print(process2.stderr.read())

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Specify the commands to run
    command2 = r'C:\Users\useradmin\Desktop\CrimeAlert\Crime-Alert\CrimeTip\ipfs.exe init'
    command1 = r'C:\Users\useradmin\Desktop\CrimeAlert\Crime-Alert\CrimeTip\ipfs.exe daemon'
    
    # Specify the path where you want to run the commands
    path = r"C:\Users\useradmin\Desktop\CrimeAlert\Crime-Alert\CrimeTip"
    run_command_in_path(command1, command2, path)
