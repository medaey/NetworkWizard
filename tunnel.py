import networks_info
from utils import mode_configuration

def tunnel_gre (interfaceName, ipInterfaceTunnel, interfacePublic, ipPublicDestination, ipInterfaceTunnelCIDR):

    ipInterfaceTunnelMask = networks_info.get_netmask_for_cidr(ipInterfaceTunnelCIDR)

    mode_configuration()
    print (f'interface {interfaceName}')
    print (f'ip address {ipInterfaceTunnel} {ipInterfaceTunnelMask}')
    print (f'tunnel source {interfacePublic}')
    print (f'tunnel destination {ipPublicDestination}')
    print (f'tunnel mode gre ip')
    print(f'end')