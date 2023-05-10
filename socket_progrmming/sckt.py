import socket as sk
# Importing socket package

# Creating a socket
mySock = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
# AF_INET refers to the address-family ipv4. 
# The SOCK_STREAM means connection-oriented TCP protocol.

#Example of Retreiving ip of a site
ip =  sk.gethostbyname("www.google.com")
print(ip)

