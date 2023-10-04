#!/bin/bash
########################################################################
# Script d'aide à la configuration des équipements réseaux
#-----------------------------------------------------------------------
# Version : 202310050105
# Auteur : Medaey
########################################################################

# Variables par défaut
defaultModelSwitch="HP-2530"
defaultSwitchHostname="SW-0001"
defaultVlans="Prod:10,Admin:20,VoIP:30"
defaultSwitchVlanManagementId=20
defaultSwitchBanner="/!\ ACCES RESERVE AU PERSONNEL AUTORISE UNIQUEMENT /!\ \n\nL'acces a ce dispositif est reserve uniquement au personnel autorise. Ce systeme est surveille et toute activite non autorisee entrainera des Poursuites conformement a la loi en vigueur. En vous connectant, vous Acceptez de respecter les reglementations et les politiques regissantes son utilisations.\n\nAVERTISSEMENT: L'acces ou l'utilisation non autorises de ce systeme peuvent entrainer de lourdes sanctions penales et/ou civiles. Toutes les activites effectuees sur ce dispositif sont enregistrees et surveillees.\n"

# Configurations
switchModel=${defaultModelSwitch}
switchVlans=${defaultVlans}
switchManagementId=${defaultSwitchVlanManagementId}
switchBannerText=${defaultSwitchBanner}
switchHostname=${defaultSwitchHostname}

# Fonction pour afficher l'aide
display_help() {
  echo "Usage: $0 [-m <modelSwitch>] [-n <switchHostname>] [-v \"vlan1:id1,vlan2:id2,vlan3:id3,...\"] [-g <defaultSwitchVlanManagementId>] [-b \"banner text\"] [--help]"
  echo "Options:"
  echo "  -m, --model             Modèle du switch (par défaut: ${defaultModelSwitch})"
  echo "  -n, --hostname          Nom d'hôte du switch (par défaut: ${defaultSwitchHostname})"
  echo "  -v, --vlans             VLANs à configurer (par défaut: ${defaultVlans})"
  echo "  -g, --management-vlan   ID du VLAN de gestion (par défaut: ${defaultSwitchVlanManagementId})"
  echo "  -b, --banner            Texte de la bannière (par défaut: ${defaultSwitchBanner:0:50}...)"
  echo "  -h, --help              Afficher ce message d'aide"
  echo
  echo "Exemple:"
  echo "  $0 -m HP-2530 -n ${defaultSwitchHostname} -v \"${defaultVlans}\" -g ${defaultSwitchVlanManagementId}"
}


# Fonction pour générer le fichier de configuration
generateConfigFile() {
  local timestamp=$(date +'%Y%m%d%H%M')
  cat > "${timestamp}_${switchModel}.txt" << EOF
########################################################################
# FICHIER : ${timestamp}_${switchModel}.txt
# MODEL : ${switchModel}
# Gestion VLAN : ${switchManagementId}
#-----------------------------------------------------------------------
# VERSION : ${timestamp}
########################################################################
# Avant de un coller les commandes, assurez-vous d'être connecté en mode enable sur le switch "${switchModel}#"

EOF
  globalSwitchConfig >> "${timestamp}_${switchModel}.txt"
  vlanConfig >> "${timestamp}_${switchModel}.txt"
}

# Configuration générale du switch
globalSwitchConfig() {
  cat << EOF
  configure terminal
  hostname ${switchHostname}
  spanning-tree
  banner motd * 
  ${switchBannerText} *
  idle-timeout 15
  no web-management
  no telnet-server
  time daylight-time-rule western-europe
  time timezone 2
EOF
}

# Configuration des VLAN du switch
vlanConfig() {
  IFS=',' read -ra vlanArr <<< "$switchVlans"

  for vlanInfo in "${vlanArr[@]}"; do
    IFS=':' read -ra vlan <<< "$vlanInfo"
    vlanId=${vlan[1]}
    cat << EOF
    vlan ${vlanId}
      name "${vlan[0]}"
      no ip address
      exit
EOF
  done

  echo "management-vlan ${switchManagementId}"
  cat << EOF
   write memory
EOF
}

main() {
  # Parsing des options et des arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    -m|--model)
      switchModel="$2"
      shift 2
      ;;
    -n|--hostname)
      switchHostname="$2"
      shift 2
      ;;
    -v|--vlans)
      switchVlans="$2"
      shift 2
      ;;
    -g|--management-vlan)
      switchManagementId="$2"
      shift 2
      ;;
    -b|--banner)
      switchBannerText="$2"
      shift 2
      ;;
    -h|--help)
      display_help
      exit 0
      ;;
    *)
      echo "Option invalide: $1"
      display_help
      exit 1
      ;;
  esac
done

  # Appel de la fonction pour générer la configuration
  generateConfigFile
}

main "$@"