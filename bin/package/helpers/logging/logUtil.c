#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include "logUtil.h"



static LogOptions *options = NULL;

void getTime(char *timeBuffer){
    time_t t = time(NULL);
    struct tm timeStruct;
    int error = localtime_s(&timeStruct, &t);
    if (error==0){
        snprintf(timeBuffer, TIMESTAMP_LENGTH, "%04d-%02d-%02d %02d:%02d:%02d",
                timeStruct.tm_year + ANNO_DOMINI_TILL_TWENTY_CENTURY,
                timeStruct.tm_mon + 1,
                timeStruct.tm_mday,
                timeStruct.tm_hour,
                timeStruct.tm_min,
                timeStruct.tm_sec);
    }else{
        snprintf(timeBuffer, TIMESTAMP_LENGTH, "localtime_s() returned %d", error);
    }
}


void initLogger(){
    static LogOptions logObj = {
        .file = NULL,
        .logFileName = DEFAULT_LOG_FILE_NAME,
        .defaultLogLevel = 0
    };
    if (logObj.file == NULL){
        logObj.file = fopen(logObj.logFileName, "a");
        if (!logObj.file) {
            perror("fopen failed");
        } 
    }
    options = &logObj;

}


void _log(int level,const char *message) {
    if (level == 0) level = options->defaultLogLevel;
    if(level==100){
        fprintf(options->file,message);
        fflush(options->file);
        return;
    }
    char *level_str = "INFO";
    switch(level) {
        case 1:  level_str = "WARNING-DEBUG"; break;
        case 2:  level_str = "ERROR";         break;
        case 3:  level_str = "FATAL";         break;
        case 5:  level_str = "SUCCESS";       break;
        default: level_str = "INFO";          break;
    }
    char timeBuffer[TIMESTAMP_LENGTH];
    getTime(timeBuffer);
    fprintf(options->file, "[ %s ] [ %s ] %s\n", timeBuffer, level_str, message);
    fflush(options->file);
}

void closeLogger(){
    if (options->file) fclose(options->file);
}
void info(const char *message){
    _log(0, message);
}
void success(const char *message){
    _log(5, message);
}
void error(const char *message){
    _log(2, message);
}
void fatal(const char *message){
    _log(3, message);
}
void warning(const char *message){
    _log(1, message);
}
void debug(const char *message){
    _log(1, message);
}
void nlvl_log(const char *message){
    _log(100, message);
}