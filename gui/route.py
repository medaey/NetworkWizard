from utils import mode_configuration
from networks_info import get_netmask_for_cidr

def route_static(reseauDest, reseauDestCIDR, ipNextRouter):

    reseauDestMask = get_netmask_for_cidr(reseauDestCIDR)
    mode_configuration()
    print (f'ip route {reseauDest} {reseauDestMask} {ipNextRouter}')
    print (f'end')