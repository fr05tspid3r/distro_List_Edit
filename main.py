#i like this but it needs a way to verify things arent in the list already which would be hard, i also started a way to add new items and verify they arent there
# then add them with acording varients. but its an art project so maybe ill make something more proactive instead. 

# List (input)
distro_list = [
    "Kali", "AIX", "Alpine", "Anarchy", "Android", "Antergos", "antiX", "AOSC", "Apricity", "ArcoLinux", "ARCHlabs",
    "ArchStrike", "XFerience", "ArchMerge", "Arch", "Artix", "Arya", "Bedrock", "Bitrig", "BlackArch", "BLAG",
    "BlankOn", "BlueLight", "bonsai", "BSD", "BunsenLabs", "Calculate", "Carbs", "CentOS", "Chakra", "ChaletOS",
    "Chapeau", "Chrom*", "Cleanjaro", "ClearOS", "Clear_Linux", "Clover", "Condres", "Container_Linux", "CRUX",
    "Cucumber", "Debian", "Deepin", "DesaOS", "Devuan", "DracOS", "DragonFly", "Drauger", "Elementary", "EndeavourOS",
    "Endless", "EuroLinux", "Exherbo", "Fedora", "Feren", "FreeBSD", "FreeMiNT", "Frugalware", "Funtoo", "GalliumOS",
    "Gentoo", "Pentoo", "gNewSense", "GNU", "GoboLinux", "Grombyang", "Guix", "Haiku", "Huayra", "Hyperbola", "janus",
    "Kali", "KaOS", "KDE_neon", "Kibojoe", "Kogaion", "Korora", "KSLinux", "Kubuntu", "LEDE", "LFS", "Linux_Lite",
    "LMDE", "Lubuntu", "Lunar", "macos", "Mageia", "MagpieOS", "Mandriva", "Manjaro", "Maui", "Mer", "Minix",
    "LinuxMint", "MX_Linux", "Namib", "Neptune", "NetBSD", "Netrunner", "Nitrux", "NixOS, Nurunner", "NuTyX",
    "OBRevenge", "OpenBSD", "OpenIndiana", "OpenMandriva", "OpenWrt", "osmc", "Oracle", "PacBSD", "Parabola", "Pardus",
    "Parrot", "Parsix", "TrueOS", "PCLinuxOS", "Peppermint", "POP_OS", "OpenSUSE", "popos", "Porteus", "PostMarketOS",
    "Proxmox", "Puppy", "PureOS", "Qubes", "Radix, Raspbian", "Reborn_OS", "Redstar", "Redcore", "Refracted_Devuan",
    "Regata", "Rosa", "sabotage", "Sabayon", "Sailfish", "SalentOS", "Scientific", "Septor", "SharkLinux", "Siduction",
    "Slackware", "SliTaz", "SmartOS", "Solus", "Source_Mage", "Sparky", "Star", "SteamOS", "SunOS", "openSUSE_Leap",
    "openSUSE_Tumbleweed", "openSUSE", "SwagArch", "Tails", "Trisquel", "Ubuntu-Budgie", "Ubuntu-GNOME", "Ubuntu-MATE",
    "Ubuntu-Studio", "Ubuntu", "Void", "Obarun", "windows10", "Windows7", "Xubuntu", "Zorin", "IRIX", "Redhat",
    "Redhat_old", "Redhat_small", "Ubuntu"
]

# Make new list that includes these items
modified_distro_list = []

for item in distro_list:
    # Add the original item
    modified_distro_list.append(item)

    # Add the "_old" variant
    item_old = item + "_old"
    modified_distro_list.append(item_old)

    # Add the "_small" variant
    item_small = item + "_small"
    modified_distro_list.append(item_small)

# Add a new item to the list (toBeContinued)
# new_item = "NewDistro"
# modified_distro_list.append(new_item)



# Print the updated list
for item in modified_distro_list:
   print('"' + item + '"', end=' ')

