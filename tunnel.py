from utils import mode_configuration

def tunnel_gre (interfaceName:int = "Tunnel0", ipInterfaceTunnel:int = "192.168.0.1", maskInterfaceTunnel:int = "255.255.255.0", interfacePublic:int = "serial 0/0/0", ipPublicDestination:int = "80.2.0.2"):
    mode_configuration()
    print (f'interface {interfaceName}')
    print (f'ip address {ipInterfaceTunnel} {maskInterfaceTunnel}')
    print (f'tunnel source {interfacePublic}')
    print (f'tunnel destination {ipPublicDestination}')
    print (f'tunnel mode gre ip')
    print(f'end')