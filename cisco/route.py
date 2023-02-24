from cisco.utils import mode_configuration
import cisco.networks_info as networks_info

def route_static(reseauDest, reseauDestCIDR, ipNextRouter):

    reseauDestMask = networks_info.get_netmask_for_cidr(reseauDestCIDR)
    mode_configuration()
    print (f'ip route {reseauDest} {reseauDestMask} {ipNextRouter}')
    print (f'end')