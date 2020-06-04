QT += testlib network xml
QT -= gui

CONFIG += c++11

include(../../../../qtxlsx/src/xlsx/qtxlsx.pri)

SOURCES += \
    testgateway.cpp \
    ../src/utils/gateway.cpp \
    ../src/utils/internalexception.cpp


HEADERS += \
    testgateway.h \
    ../src/utils/gateway.h \
    ../src/utils/internalexception.h

RESOURCES += \
    ../src/resources.qrc
