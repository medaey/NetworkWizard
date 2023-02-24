from cisco import networks_info, nat, tunnel, route

# Fonction principale
def main ():
	
	# Affiche le masque et la whitecard d'un réseau par raport a la notation CIDR
	#print(networks_info.get_netmask_for_cidr("/10"))
	
	# Genere un script de config cisco pour du nat dynamique
	# nat.nat_dynamique_overload (
	# 	interfacePublic="Serial0/0/0",
	# 	interfacePriver="GigabitEthernet0/0",
	# 	ipNetPriver="172.16.0.0",
	# 	ipNetPriverCIDR="/24"
	# )
	
	# Genere un script de config cisco cisco pour un tunnel gre
	# tunnel.tunnel_gre (
	#  	interfacePublic="Serial0/0/0",
	#  	ipInterfaceTunnel="192.168.0.1",
	#  	ipInterfaceTunnelCIDR="/30",
	#  	ipPublicDestination="64.100.13.2",
	#  	interfaceName="Tunnel0"
	# )
	
	# Genere un script de config cisco de config cisco pour une route statique

	# route.route_static (
	# 	reseauDest = "172.16.4.0",
	#  	reseauDestCIDR = "/22",
	# 	ipNextRouter = "192.168.0.1"
	# )

main()
print (f'')

nat_statique