# VLC ActiveX Control
# CVE-2007-4619, CVE-2007-6262

import logging
log = logging.getLogger("Thug")

def getVariable(self, arg):
    if len(arg) > 255:
        log.ThugLogging.log_exploit_event(self._window.url,
                                          "VLC ActiveX",
                                          "getVariable Overflow",
                                          cve = "CVE-2007-6262")

def setVariable(self, arg0, arg1):
    if len(arg0) > 255 or len(arg1) > 255:
        log.ThugLogging.log_exploit_event(self._window.url,
                                          "VLC ActiveX",
                                          "setVariable Overflow",
                                          cve = "CVE-2007-6262")

def addTarget(self, arg0, arg1, arg2, arg3):
    if len(arg0) > 255 or len(arg1) > 255 or len(arg2) > 255 or len(arg3) > 255:
        log.ThugLogging.log_exploit_event(self._window.url,
                                          "VLC ActiveX",
                                          "addTarget Overflow",
                                          cve = "CVE-2007-6262")