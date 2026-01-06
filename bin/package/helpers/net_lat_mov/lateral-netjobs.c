#include <winsock2.h>
#include <windows.h>
#include <iphlpapi.h>
#include <stdio.h>
#include "lateral-netjobs.h"



#pragma comment(lib, "iphlpapi.lib")
#pragma comment(lib, "ws2_32.lib")


int isDHCPDisabledButConnectedToLAN(IP_ADAPTER_ADDRESSES *pCurrAddy) {
    return 1;
}

struct LANIndicator getEmptyIndicator() {
    struct LANIndicator indicator = { 0, 0, 0, 0, 0, 0 };
    return indicator;
}
struct LANIndicator isThereLANIndicator(IP_ADAPTER_ADDRESSES *pCurrAddy) {
    if (pCurrAddy == NULL) return getEmptyIndicator();
    int InterfaceIsUp = (pCurrAddy->OperStatus == IfOperStatusUp);
    int hasIpAdress =  (pCurrAddy->FirstUnicastAddress != NULL);
    int isEthernet = (pCurrAddy->IfType == IF_TYPE_ETHERNET_CSMACD);
    int hasIpV4 = 0;
    int DHCPEnabled = pCurrAddy->Dhcpv4Enabled;

    UINT8 bitsForNetwork = 0;
    if (InterfaceIsUp && hasIpAdress && isEthernet) {
        PIP_ADAPTER_UNICAST_ADDRESS pUnicast = pCurrAddy->FirstUnicastAddress;
        while (pUnicast) {
            if (pUnicast->Address.lpSockaddr->sa_family == AF_INET) {
                hasIpV4 = 1;
                bitsForNetwork = pUnicast->OnLinkPrefixLength;
                break;
            }
            pUnicast = pUnicast->Next;
        }
        struct LANIndicator indicator = {
            .isThereLANIndicator = (hasIpV4 && (DHCPEnabled || isDHCPDisabledButConnectedToLAN(pCurrAddy))),
            .subnet = bitsForNetwork, 
            .isEthernet = isEthernet, 
            .isDHCPEnabled = DHCPEnabled, 
            .isOperUp = InterfaceIsUp,
            .hasIpV4 = hasIpV4
        };
        return indicator;
    }
    return getEmptyIndicator();
}


struct LANIndicator isLANDetected() {
    DWORD dwSize = 0;
    if (GetAdaptersAddresses(AF_UNSPEC, GAA_FLAG_INCLUDE_PREFIX, NULL, NULL, &dwSize) != ERROR_BUFFER_OVERFLOW)
        return getEmptyIndicator();

    PIP_ADAPTER_ADDRESSES pAddresses = (IP_ADAPTER_ADDRESSES*)malloc(dwSize);
    if (!pAddresses) return getEmptyIndicator();

    if (GetAdaptersAddresses(AF_UNSPEC, GAA_FLAG_INCLUDE_PREFIX, NULL, pAddresses, &dwSize) != NO_ERROR) {
        free(pAddresses);
        return getEmptyIndicator();
    }

    PIP_ADAPTER_ADDRESSES pCurr = pAddresses;
    struct LANIndicator lanindicator = getEmptyIndicator();
    while (pCurr) {
        lanindicator = isThereLANIndicator(pCurr);
        if (lanindicator.isThereLANIndicator){
            break;
        }
        pCurr = pCurr->Next;
    }

    free(pAddresses);
    return lanindicator;
}