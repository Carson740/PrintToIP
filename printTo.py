#printTo.py

import socket
import sys

# IP address and port of the printer
printer_ip = sys.argv[2]  # Get the printer IP address from the command line arguments
printer_type = sys.argv[1]
printer_port = 9100  # Default port used for printing
# Open the file to be printed
if printer_type == "print_pdf_b&w":
    with open('prints/B&WPrinterTest.pdf', 'rb') as f:
        # 'rb' mode is used to open the file in binary mode for reading

        # Create a socket connection to the printer
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Create a new socket object with the specified family (AF_INET for IPv4) and type (SOCK_STREAM for TCP)
        sock.connect((printer_ip, printer_port))
        # Connect to the printer using its IP address and the default port

        # Send the file contents to the printer
        while True:
            data = f.read(1024)
            # Read 1024 bytes of data from the file at a time
            if not data:
                # If there is no more data to read from the file, break out of the loop
                break
            sock.send(data)
            # Send the data to the printer over the socket connection

        # Close the socket connection
        sock.close()
elif printer_type == "print_pdf_color":
    with open('prints/ColorPrinterTest.pdf', 'rb') as f:
        # 'rb' mode is used to open the file in binary mode for reading

        # Create a socket connection to the printer
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Create a new socket object with the specified family (AF_INET for IPv4) and type (SOCK_STREAM for TCP)
        sock.connect((printer_ip, printer_port))
        # Connect to the printer using its IP address and the default port

        # Send the file contents to the printer
        while True:
            data = f.read(1024)
            # Read 1024 bytes of data from the file at a time
            if not data:
                # If there is no more data to read from the file, break out of the loop
                break
            sock.send(data)
            # Send the data to the printer over the socket connection

        # Close the socket connection
        sock.close()
elif printer_type == "print_label_4x6":
    print("printing")
    with open('prints/4x6 Test.prn', 'rb') as f:
        # 'rb' mode is used to open the file in binary mode for reading

        # Create a socket connection to the printer
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Create a new socket object with the specified family (AF_INET for IPv4) and type (SOCK_STREAM for TCP)
        sock.connect((printer_ip, printer_port))
        # Connect to the printer using its IP address and the default port

        # Send the file contents to the printer
        while True:
            data = f.read(1024)
            # Read 1024 bytes of data from the file at a time
            if not data:
                # If there is no more data to read from the file, break out of the loop
                break
            sock.send(data)
            # Send the data to the printer over the socket connection

        # Close the socket connection
        sock.close()
