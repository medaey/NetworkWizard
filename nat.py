from utils import mode_configuration
from networks_info import get_wildcard_for_cidr

# Fonction pour configurer le nat statique
def nat_statique(interfacePublic, interfacePriver, ipPublic, ipPriver):
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
def nat_dynamique_overload(interfacePublic, interfacePriver, ipNetPriver, whiteCardCIDR):

	whiteCard = get_wildcard_for_cidr(whiteCardCIDR)

	mode_configuration()
	# Configuration des interfaces inside et outside
	print(f'interface {interfacePriver}')
	print(f'ip nat inside')
	print(f'exit')
	print(f'interface {interfacePublic}')
	print(f'ip nat outside')
	print(f'exit')
    # Configuration des adresses sources via ACL
	print(f'access-list 2 permit {ipNetPriver} {whiteCard}')
	print(f'ip nat inside source list 2 interface {interfacePublic} overload')
	print(f'end')