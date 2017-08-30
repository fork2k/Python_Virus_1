# This is an educational virus made by Jason Gahr 2017
# This is not meant to cause harm
import os
import sys
import socket
import virus_defines



def main(args):
    users_operating_system = os.uname() 
    print users_operating_system[0]
    if users_operating_system[0] == "windows" or "Windows":
        print "Windows!"
    else:
        print "[!] OS is not reconized! Exiting now"
        sys.exit()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

