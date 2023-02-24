# Création d'une liste de dictionnaires pour stocker les informations
networks = [
    {'slash': '/32', 'netmask': '255.255.255.255', 'wildcard': '0.0.0.0'},
    {'slash': '/31', 'netmask': '255.255.255.254', 'wildcard': '0.0.0.1'},
    {'slash': '/30', 'netmask': '255.255.255.252', 'wildcard': '0.0.0.3'},
    {'slash': '/29', 'netmask': '255.255.255.248', 'wildcard': '0.0.0.7'},
    {'slash': '/28', 'netmask': '255.255.255.240', 'wildcard': '0.0.0.15'},
    {'slash': '/27', 'netmask': '255.255.255.224', 'wildcard': '0.0.0.31'},
    {'slash': '/26', 'netmask': '255.255.255.192', 'wildcard': '0.0.0.63'},
    {'slash': '/25', 'netmask': '255.255.255.128', 'wildcard': '0.0.0.127'},
    {'slash': '/24', 'netmask': '255.255.255.0', 'wildcard': '0.0.0.255'},
    {'slash': '/23', 'netmask': '255.255.254.0', 'wildcard': '0.0.1.255'},
    {'slash': '/22', 'netmask': '255.255.252.0', 'wildcard': '0.0.3.255'},
    {'slash': '/21', 'netmask': '255.255.248.0', 'wildcard': '0.0.7.255'},
    {'slash': '/20', 'netmask': '255.255.240.0', 'wildcard': '0.0.15.255'},
    {'slash': '/19', 'netmask': '255.255.224.0', 'wildcard': '0.0.31.255'},
    {'slash': '/18', 'netmask': '255.255.192.0', 'wildcard': '0.0.63.255'},
    {'slash': '/17', 'netmask': '255.255.128.0', 'wildcard': '0.0.127.255'},
    {'slash': '/16', 'netmask': '255.255.0.0', 'wildcard': '0.0.255.255'},
    {'slash': '/15', 'netmask': '255.254.0.0', 'wildcard': '0.1.255.255'},
    {'slash': '/14', 'netmask': '255.252.0.0', 'wildcard': '0.3.255.255'},
    {'slash': '/13', 'netmask': '255.248.0.0', 'wildcard': '0.7.255.255'},
    {'slash': '/12', 'netmask': '255.240.0.0', 'wildcard': '0.15.255.255'},
    {'slash': '/11', 'netmask': '255.224.0.0', 'wildcard': '0.31.255.255'},
    {'slash': '/10', 'netmask': '255.192.0.0', 'wildcard': '0.63.255.255'},
    {'slash': '/9', 'netmask': '255.128.0.0', 'wildcard': '0.127.255.255'},
    {'slash': '/8', 'netmask': '255.0.0.0', 'wildcard': '0.255.255.255'},
    {'slash': '/7', 'netmask': '254.0.0.0', 'wildcard': '1.255.255.255'},
    {'slash': '/6', 'netmask': '252.0.0.0', 'wildcard': '3.255.255.255'},
    {'slash': '/5', 'netmask': '248.0.0.0', 'wildcard': '7.255.255.255'},
    {'slash': '/4', 'netmask': '240.0.0.0', 'wildcard': '15.255.255.255'},
    {'slash': '/3', 'netmask': '224.0.0.0', 'wildcard': '31.255.255.255'},
    {'slash': '/2', 'netmask': '192.0.0.0', 'wildcard': '63.255.255.255'},
    {'slash': '/1', 'netmask': '128.0.0.0', 'wildcard': '127.255.255.255'},
    {'slash': '/0', 'netmask': '0.0.0.0', 'wildcard': '255.255.255.255'}
]

# Retourne la white carte en fonction du cird
def get_wildcard_for_cidr(cidr):
    for network in networks:
        if network['slash'] == cidr:
            return network['wildcard']
        
# Retourne le masque réseau en fonction du cird
def get_netmask_for_cidr(cidr):
    for network in networks:
        if network['slash'] == cidr:
            return network['netmask']

# Appel la fonction get_netmask_for_cidr
#print(get_netmask_for_cidr("/24"))