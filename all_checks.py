#!/usr/bin/env python3

import os
import shutil
import sys
import socket
import psutil

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")


def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise."""    
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    if check_reboot():
        print("Pending Reboot.Step 3 new branch")
        sys.exit(1)
    print("Everything OK. update done on branch new feature")
    sys.exit(0)
main()
