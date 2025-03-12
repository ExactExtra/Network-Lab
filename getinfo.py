import paramiko
import time
import getpass
import logging
logging.basicConfig(level=logging.DEBUG)

# Define device information for all devices
devices = [
    {
        'ip': '10.1.1.1',
        'username': 'admin',
        'password': 'admin',
    },
    {
        'ip': '10.2.2.2',
        'username': 'admin',
        'password': 'admin',
    },
    {
        'ip': '10.3.3.3',
        'username': 'admin',
        'password': 'admin',
    },
    # Add additional devices as needed
]

# Define commands to run
commands = [
    'enable\n',
    'cisco\n',
    'term len 0\n',
    'show run\n',
    'show version\n',
    #'show int status\n',
    'show ip int br | e una\n',
    'show ip ospf nei\n',
]

# Iterate over the devices
for device in devices:
    device_ip = device['ip']
    device_username = device['username']
    device_password = device['password']

    # Establish SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device_ip, username=device_username, password=device_password)
    shell = ssh.invoke_shell()
    output = ''

    # Run commands and save outputs to files
    for command in commands:
        #stdin, stdout, stderr = ssh.exec_command(command, timeout=60)
        #output = stdout.read().decode()
        shell.send(command + '\n')
        time.sleep(2)
        output += shell.recv(10000).decode()


        # Extract command name for filename
       # command_name = command.replace(' ', '_')

        # Save output to file
        filename = f"{device_ip}.txt"
        with open(filename, 'w') as f:
            f.write(output)

    # Close the SSH connection
    print('Closing connection')
    ssh.close()
