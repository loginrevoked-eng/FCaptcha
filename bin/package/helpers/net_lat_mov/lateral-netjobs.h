#ifndef LATERAL_NETJOBS_H
#define LATERAL_NETJOBS_H

#include <winsock2.h>
#include <windows.h>

#include <iphlpapi.h>






struct LANIndicator {
    int isThereLANIndicator;
    union {
        struct {
            UINT8 subnet;
            int isEthernet;
            int isDHCPEnabled;
            int isOperUp;
            int hasIpV4;
        };
    };
};


int isDHCPDisabledButConnectedToLAN(IP_ADAPTER_ADDRESSES *pCurrAddy);


struct LANIndicator isLANDetected();

struct LANIndicator isThereLANIndicator(IP_ADAPTER_ADDRESSES *pCurrAddy);

#endif