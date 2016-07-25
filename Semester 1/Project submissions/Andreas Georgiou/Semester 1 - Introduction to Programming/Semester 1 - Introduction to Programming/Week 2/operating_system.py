import os #imports the os library

print "Information about this computer"
print "-----------------------------"
print "List of Enviroment Variables.."
print "........................................................................"
print os.environ.keys()
print "........................................................................"
print "Computer name:     " + os.environ["COMPUTERNAME"]
print "Operating system:  " + os.environ["os"]
print "Processor type:    " + os.environ["PROCESSOR_ARCHITECTURE"]
print "Username:          " + os.environ["username"]

def env_key():
    environkey = raw_input("Enter the enviroment variable you wish to view: ").upper()
    if environkey == "TMP":
        print os.environ["tmp"]
        env_key()
    elif environkey == "COMPUTERNAME":
        print os.environ["COMPUTERNAME"]
        env_key()
    elif environkey == "USERDOMAIN":
        print os.environ["USERDOMAIN"]
        env_key()
    elif environkey == "DEFLOGDIR":
        print os.environ["DEFLOGDIR"]
        env_key()
    elif environkey == "VSEDEFLOGDIR":
        print os.environ["VSEDEFLOGDIR"]
        env_key()
    elif environkey == "PSMODULEPATH":
        print os.environ["PSMODULEPATH"]
        env_key()
    elif environkey == "COMMONPROGRAMFILES":
        print os.environ["COMMONPROGRAMFILES"]
        env_key()
    elif environkey == "HWTYPE":
        print os.environ["HWTYPE"]
        env_key()
    elif environkey == "PROCESSOR_IDENTIFIER(X86)":
        print os.environ["PROCESSOR_IDENTIFIER(X86)"]
        env_key()
    elif environkey == "PROCESSOR_IDENTIFIER":
        print os.environ["PROCESSOR_IDENTIFIER(X86)"]
        env_key()
    elif environkey == "WINDOWS_TRACING_FLAGS":
        print os.environ["WINDOWS_TRACING_FLAGS"]
        env_key()
    elif environkey == "TK_LIBRARY":
        print os.environ["TK_LIBRARY"]
        env_key()
    elif environkey == "TEMP":
        print os.environ["TEMP"]
        env_key()
    elif environkey == "HOME":
        print os.environ["HOME"]
        env_key()
    elif environkey == "PROGRAMFILES":
        print os.environ["PROGRAMFILES"]
        env_key()
    elif environkey == "PROCESSOR_REVISION":
        print os.environ["PROCESSOR_REVISION"]
        env_key()
    elif environkey == "SYSTEMROOT":
        print os.environ["SYSTEMROOT"]
        env_key()
    elif environkey == "COMMONPROGRAMFILES(X86)":
        print os.environ["COMMONPROGRAMFILES(X86)"]
        env_key()
    elif environkey == "COMMONPROGRAMFILES":
        print os.environ["COMMONPROGRAMFILES(X86)"]
        env_key()
    elif environkey == "PROCESSOR_ARCHITECTURE":
        print os.environ["PROCESSOR_ARCHITECTURE"]
        env_key()
    elif environkey == "TIX_LIBRARY":
        print os.environ["TIX_LIBRARY"]
        env_key()
    elif environkey == "ALLUSERSPROFILE":
        print os.environ["ALLUSERSPROFILE"]
        env_key()
    elif environkey == "LOCALAPPDATA":
        print os.environ["LOCALAPPDATA"]
        env_key()
    elif environkey == "HOMEPATH":
        print os.environ["HOMEPATH"]
        env_key()
    elif environkey == "PROGRAMW6432":
        print os.environ["PROGRAMW6432"]
        env_key()
    elif environkey == "USERNAME":
        print os.environ["USERNAME"]
        env_key()
    elif environkey == "LOGONSERVER":
        print os.environ["LOGONSERVER"]
        env_key()
    elif environkey == "SESSIONNAME":
        print os.environ["SESSIONNAME"]
        env_key()
    elif environkey == "PROGRAMDATA":
        print os.environ["PROGRAMDATA"]
        env_key()
    elif environkey == "TCL_LIBRARY":
        print os.environ["TCL_LIBRARY"]
        env_key()
    elif environkey == "PATH":
        print os.environ["PATH"]
        env_key()
    elif environkey == "USERDNSDOMAIN":
        print os.environ["USERDNSDOMAIN"]
        env_key()
    elif environkey == "PATHEXT":
        print os.environ["PATHEXT"]
        env_key()
    elif environkey == "PATHEXT":
        print os.environ["PATHEXT"]
        env_key()
    elif environkey == "FP_NO_HOST_CHECK":
        print os.environ["FP_NO_HOST_CHECK"]
        env_key()
    elif environkey == "WINDIR":
        print os.environ["WINDIR"]
        env_key()
    elif environkey == "WINDOWS_TRACING_LOGFILE":
        print os.environ["WINDOWS_TRACING_LOGFILE"]
        env_key()
    elif environkey == "HOMEDRIVE":
        print os.environ["HOMEDRIVE"]
        env_key()
    elif environkey == "HWMODEL":
        print os.environ["HWMODEL"]
        env_key()
    elif environkey == "SYSTEMDRIVE":
        print os.environ["SYSTEMDRIVE"]
        env_key()
    elif environkey == "COMSPEC":
        print os.environ["COMSPEC"]
        env_key()
    elif environkey == "NUMBER_OF_PROCESSORS":
        print os.environ["NUMBER_OF_PROCESSORS"]
        env_key()
    elif environkey == "APPDATA":
        print os.environ["APPDATA"]
        env_key()
    elif environkey == "PROCESSOR_LEVEL":
        print os.environ["PROCESSOR_LEVEL"]
        env_key()
    elif environkey == "COMMONPROGRAMW6432":
        print os.environ["COMMONPROGRAMW6432"]
        env_key()
    elif environkey == "OS":
        print os.environ["OS"]
        env_key()
    elif environkey == "PUBLIC":
        print os.environ["PUBLIC"]
        env_key()
    elif environkey == "USERPROFILE":
        print os.environ["USERPROFILE"]
        env_key()
    else:
        print "you must enter a valid Enviroment Variable from the list above."
        env_key()
env_key()


#Enviroment variables listed below:
#['TMP', 'COMPUTERNAME', 'USERDOMAIN', 'DEFLOGDIR',
#'VSEDEFLOGDIR', 'PSMODULEPATH', 'COMMONPROGRAMFILES',
#'HWTYPE', 'PROCESSOR_IDENTIFIER', 'PROGRAMFILES', 'PROCESSOR_REVISION',
#'SYSTEMROOT', 'HOME', 'PROGRAMFILES(X86)', 'WINDOWS_TRACING_FLAGS',
#'TK_LIBRARY', 'TEMP', 'COMMONPROGRAMFILES(X86)', 'PROCESSOR_ARCHITECTURE',
#'TIX_LIBRARY', 'ALLUSERSPROFILE', 'LOCALAPPDATA', 'HOMEPATH',
#'PROGRAMW6432', 'USERNAME', 'LOGONSERVER', 'SESSIONNAME', 'PROGRAMDATA',
#'TCL_LIBRARY', 'PATH', 'USERDNSDOMAIN', 'PATHEXT', 'FP_NO_HOST_CHECK',
#'WINDIR', 'WINDOWS_TRACING_LOGFILE', 'HOMEDRIVE', 'HWMODEL', 'SYSTEMDRIVE',
#'COMSPEC', 'NUMBER_OF_PROCESSORS', 'APPDATA', 'PROCESSOR_LEVEL',
#'COMMONPROGRAMW6432', 'OS', 'PUBLIC', 'USERPROFILE']
