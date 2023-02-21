from nat import nat_statique, nat_dynamique_overload
from tunnel import tunnel_gre

# Fonction principale
def main ():
	#nat_statique (interfacePublic="serial 0/0/0", ipPublic="201.49.10.30", interfacePriver="fe 0/1", ipPriver="192.168.1.100")
	#nat_dynamique_overload (interfacePublic="Serial0/0/0", interfacePriver="GigabitEthernet0/0", ipNetPriver="172.16.4.0", maskInverse="0.252.255.255")
	tunnel_gre (interfacePublic="Serial0/0/0", ipInterfaceTunnel="192.168.0.1", maskInterfaceTunnel="255.255.255.252",  ipPublicDestination="64.100.13.2", interfaceName="Tunnel0")
main()
print (f'')