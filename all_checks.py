#!/usr/bin/env python3

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.Step 3 new branch")
        sys.exit(1)
    print("Everything OK. update done on branch new feature")
    sys.exit(0)
main()
