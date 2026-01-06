#ifndef HOSTS_H
#define HOSTS_H

#define MAX_LOG 300


int get_arpCache(void (*info)(const char *message), void (*error)(const char *message), void(*nlvl_log)(const char *message),const char *nextfunc);
#endif