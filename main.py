from nat import nat_statique, nat_dynamique_overload
from tunnel import tunnel_gre
from route import route_static
from networks_info import get_network_info_for_cidr

# Fonction principale
def main ():
	
	# Affiche le masque et la whitecard d'un réseau par raport a la notation CIDR
	#get_network_info_for_cidr(cidr="/10")
	
	# Genere un script de config cisco pour du nat dynamique
	nat_dynamique_overload (interfacePublic="Serial0/0/0", interfacePriver="GigabitEthernet0/0", ipNetPriver="172.16.0.0", whiteCard="0.252.255.255")
	
	# Genere un script de config cisco cisco pour un tunnel gre
	#tunnel_gre (interfacePublic="Serial0/0/0", ipInterfaceTunnel="192.168.0.1", maskInterfaceTunnel="255.255.255.252",  ipPublicDestination="64.100.13.2", interfaceName="Tunnel0")
	
	# Genere un script de config cisco de config cisco pour une route statique
	#route_static (reseauDest = "172.16.4.0", reseauDestMask = "255.255.252.0", ipNextRouter = "192.168.0.1")
main()
print (f'')