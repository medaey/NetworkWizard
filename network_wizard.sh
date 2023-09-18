#!/bin/bash
########################################################################
# Script d'aide a la configuration des équipements réseaux
#-----------------------------------------------------------------------
# Version : 202309180324
# Auteur : Medaey
########################################################################

# Variables du script
modelSwitch=$1
timestamp=$(date +'%Y%m%d%H%M')

switchHostname=SW-00
switchBannerText="/!\ ACCES RESERVE AU PERSONNEL AUTORISE UNIQUEMENT /!\ \n\nL'acces a ce dispositif est reserve uniquement au personnel autorise. Ce systeme est surveille et toute activite non autorisee entrainera des Poursuites conformement a la loi en vigueur. En vous connectant, vous Acceptez de respecter les reglementations et les politiques regissantes son utilisations.\n\nAVERTISSEMENT: L'acces ou l'utilisation non autorises de ce systeme peuvent entrainer de lourdes sanctions penales et/ou civiles. Toutes les activites effectuees sur ce dispositif sont enregistrees et surveillees.\n"
switchVlanManagementId=20

# Tableau associatif pour les VLAN
declare -A vlanList=(
  ["Management"]=$switchVlanManagementId
  ["Production"]=10
  ["VoIP"]=30
)

# Fonction pour générer le fichier de configuration
generateConfigFile() {
    local modelSwitch=$1
    cat > "./arubaConfigGenerator/$timestamp\_$modelSwitch.txt" << EOF
########################################################################
# FICHIER : ./arubaConfigGenerator/$timestamp\_$modelSwitch.txt
# MODEL : $modelSwitch
#-----------------------------------------------------------------------
# VERSION : $timestamp
########################################################################
# Avant de un coller les commandes, assurez-vous d'être connecté en mode enable sur le switch "HP-2530-24G#"

EOF
    globalSwitchConfig >> "./arubaConfigGenerator/$timestamp\_$modelSwitch.txt"
    vlanConfig >> "./arubaConfigGenerator/$timestamp\_$modelSwitch.txt"
}

# Configuration générale du switch
globalSwitchConfig() {
  cat << EOF
  configure terminal
  hostname "$switchHostname"
  spanning-tree
  banner motd * 
  $switchBannerText *
  idle-timeout 15
  no web-management
  no telnet-server
  time daylight-time-rule western-europe
  time timezone 2
EOF
}

# configuration des VLAN du switch
vlanConfig() {
  for vlanName in "${!vlanList[@]}"; do
    vlanId=${vlanList["$vlanName"]}
    cat << EOF
    vlan $vlanId
      name "$vlanName"
      no ip address
      exit
EOF
   done
   cat << EOF
   management-vlan $switchVlanManagementId
   write memory
EOF
}

main(){
  local modelSwitch=$1
  # Vérification des arguments
  if [ $# -ne 1 ]; then
      echo "Usage: $0 modelDuSwitch"
      exit 1
  fi
  # Création du répertoire de sortie
  mkdir -p arubaConfigGenerator || {
    echo "Erreur: Impossible de créer le répertoire de sortie."
    exit 1
  }
  # Appel de la fonction pour générer la configuration
  generateConfigFile "$modelSwitch"
}

main "$@"