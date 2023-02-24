from utils import mode_configuration

def route_static(reseauDest:int = "172.16.4.0", reseauDestMask:int = "255.255.252.0", ipNextRouter:int = "192.168.0.1"):
    mode_configuration()
    print (f'ip route {reseauDest} {reseauDestMask} {ipNextRouter}')
    print (f'end')