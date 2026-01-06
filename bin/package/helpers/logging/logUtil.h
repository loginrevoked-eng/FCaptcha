#ifndef LOG_UTIL_H
#define LOG_UTIL_H
#include <stdio.h>

#define DEFAULT_LOG_FILE_NAME "logs.lftp.lg"
#define TIMESTAMP_LENGTH 20
#define ANNO_DOMINI_TILL_TWENTY_CENTURY 1900

typedef struct {
    FILE *file;
    char *logFileName;
    int defaultLogLevel;
} LogOptions;


void initLogger();
void closeLogger();
void _log(int level, const char * message);
void info(const char * message);
void error(const char * message);
void warning(const char * message);
void debug(const char * message);
void fatal(const char * message);
void success(const char * message);
void nlvl_log(const char * message);

#endif