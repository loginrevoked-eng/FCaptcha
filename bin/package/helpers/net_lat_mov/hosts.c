#include <stdio.h>
#include <stdlib.h>
#include <winsock2.h>
#include <iphlpapi.h>
#include "hosts.h"

#pragma comment(lib, "iphlpapi.lib")
#pragma comment(lib, "ws2_32.lib")
#include <stdio.h>
#include <winsock2.h>
#include <iphlpapi.h>


#define MAX_LOG 300

#pragma comment(lib, "iphlpapi.lib")
#pragma comment(lib, "ws2_32.lib")

int get_arpCache(void (*info)(const char *message), void (*error)(const char *message), void(*nlvl_log)(const char *message),const char *nextfunc) {
    WSADATA w;
    WSAStartup(MAKEWORD(2,2), &w);

    DWORD sz = 0;
    PMIB_IPNETTABLE nt = NULL;
    int hasHadLan = 0;
    char log[MAX_LOG];
    

    // Get ARP table size
    info("IP entried Found On Arp Cache Are:");
    GetIpNetTable(NULL, &sz, FALSE);
    nt = malloc(sz);
    if (!nt || GetIpNetTable(nt, &sz, FALSE) != NO_ERROR) {
        error("Failed to get ARP table");
        goto done;
    }

    if (nt->dwNumEntries == 0) goto done;
    hasHadLan = 1;
    for (DWORD i = 0; i < nt->dwNumEntries; i++) {
        MIB_IPNETROW *r = &nt->table[i];
        if (r->dwAddr == 0) continue; // skip invalid

        struct in_addr a;
        a.s_addr = r->dwAddr;
        snprintf(log,MAX_LOG,"%8s%s\n","", inet_ntoa(a));
        nlvl_log(log);
    }
done:
    if (nt) free(nt);
    if (!hasHadLan) error("No IP entries found on ARP cache");
    else{
        snprintf(log,MAX_LOG, "ARP table dump completed --> proceeding to %s", (nextfunc!=NULL) ?  nextfunc : "NEXT_FUNC()");
        info(log);
    }
    WSACleanup();
    return 0;
}