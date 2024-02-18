🌴 Description:

This script allows you to scan ports on a target host to check which ports are open and which are closed.

🌴 How to Use:

Clone the Repository:

Clone the repository to your local machine using the following command:

        bash

    git clone <repository_url>

Navigate to the Directory:

    Move into the directory of the cloned repository:

    bash

    cd basic-port-scanner

Run the Script:

    Execute the Python script by running the following command:

        python main.py

    Enter the Target Host:
        You will be prompted to enter the target host. Provide the IP address or domain name of the host you want to scan.

    Specify Port Scanning Method:
        You will be asked if you want to scan specific ports. Type "y" for yes or "n" for no.

    Enter Port Range (If Applicable):
        If you choose to scan specific ports, enter the port numbers separated by commas when prompted.
        If you choose not to scan specific ports, the script will scan ports from 1 to 1024 by default.

    View Scan Results:
        The script will start scanning the specified ports on the target host.
        It will display whether each port is open or closed.
        After the scan completes, it will list the open ports on the target host.

That's it! You've successfully used the basic port scanner to check for open ports on a target host.
