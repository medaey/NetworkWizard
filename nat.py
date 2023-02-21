from utils import mode_configuration

# Fonction pour configurer le nat statique
def nat_statique(interfacePublic:int = "serial 0/0/0", interfacePriver:int = "fe 0/1", ipPublic:int = "192.168.1.100", ipPriver:int = "201.49.10.30"):
	mode_configuration()
	# Configuration des interfaces inside et outside
	print(f'interface {interfacePriver}')
	print(f'ip nat inside')
	print(f'exit')
	print(f'interface {interfacePublic}')
	print(f'ip nat outside')
	print(f'exit')
    # Configuration des ip inside et outside
	print(f'ip nat inside source static {ipPriver} {ipPublic}')
	print(f'end')

# Fonction pour configurer le nat dynamique avec surcharge
def nat_dynamique_overload(interfacePublic:int = "serial 0/0/0", interfacePriver:int = "fe 0/1", ipNetPriver:int = "192.168.1.0", maskInverse:int = "0.0.0.255"):
	mode_configuration()
	# Configuration des interfaces inside et outside
	print(f'interface {interfacePriver}')
	print(f'ip nat inside')
	print(f'exit')
	print(f'interface {interfacePublic}')
	print(f'ip nat outside')
	print(f'exit')
    # Configuration des adresses sources via ACL
	print(f'access-list 2 permit {ipNetPriver} {maskInverse}')
	print(f'ip nat inside source list 2 interface {interfacePublic} overload')
	print(f'end')