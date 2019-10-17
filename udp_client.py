import socket
UDP_IP_ADDRESS = "192.168.0.255"
UDP_PORT_NO = 6789
Message = "Hello, BAM"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

clientSock.sendto(Message.encode(),(UDP_IP_ADDRESS, UDP_PORT_NO))

