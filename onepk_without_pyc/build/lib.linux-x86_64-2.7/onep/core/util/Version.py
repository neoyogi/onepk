# 2015.02.05 17:18:08 IST
from onep.thrift.Thrift import TException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.util.Enum import enum
from onep.discovery.ServiceSetDescription import ServiceSetDescription
from onep.Constants.constants import ONEP_VERSION_MAJOR, ONEP_VERSION_MINOR, ONEP_VERSION_MAINTENANCE
from Shared.ttypes import ExceptionIDL

class Version(object):
    """
        Version class represents the version of a onePK component. 
        The component could be the client-side package version or the 
        server-side version. 
        For onePK applications to work, the server-side and the client-side
        versioning have to be compatible.
    
        onePK has foundation package and optional packages (e.g. LISP, VTY etc)
        Each of these packages have a server side which resides
        on the Network Element and a client side which resides in the
        application in any of the hosting models. The client side
        corresponds to the SDK package used by application.
    
        The onePK server side as well as client-side versions are identified 
        with a version number in the form of:  "<b><i>major.minor.maintenance</i></b>"
        Any "major" release upgrade is not backward compatible, whereas any "minor"
        or "maintenance" release upgrade is backward compatible. 
    
        - Major version number reflects the main version of the package
        and changes only when API signatures changes in non-compatible way. 
        - Minor version numbers changes when new functionalities are added, such
        as addition of new API, or addition of a new parameter to an API in
        backward-compatible way.
        - Maintenance version numbers changes with bug fixes, document changes or
        support library changes.
        
        The usage of versioning by applications is described below.
        Consider the case where the application client side is running a higher 
        minor version than the server side.
    
        Case 1:
    
        Application does no version checking. 
        In this case calling a method not supported on the connected Network Element will result in 
        application runtime fault (application will receive exception 
        specifying the method is not supported, causing it to abort).
    
        Case 2:
    
        Application checks versions and exits gracefully. 
        In this case there is no runtime fault and application can exit gracefully.
    
        Case 3:
    
        Application checks versions, and continues. 
        When Application knows that it only uses Network Element-supported methods 
        there is no problem. 
        When Application uses methods not supported on the connected Network Element, it would need to 
        set a condition that causes the application to synthesize the missing 
        functionality using only the Network Element supported methods instead.
        """


    def __init__(self, major, minor, maintenance):
        """
        Constructor for internal use only.
        """
        self.major = major
        self.minor = minor
        self.maintenance = maintenance


    VersionCompare = enum('ONEP_VERSION_NCP', 'ONEP_VERSION_MATCH', 'ONEP_VERSION_GT', 'ONEP_VERSION_LT')

    @classmethod
    def get_package_version(cls, ssName):
        """
        This method gets the package (Service Set) version which this client program 
        is currently using.
        
        
        @param ssName: Specifies the Service Set whose version is requested.
        @return:  Version object for the Service Set. If the input service set name is null
                or unsupported, null will be returned.
        """
        if ssName == ServiceSetDescription.ServiceSetName.ONEP_BASE_SERVICE_SET:
            return Version(ONEP_VERSION_MAJOR, ONEP_VERSION_MINOR, ONEP_VERSION_MAINTENANCE)
        else:
            if ssName == ServiceSetDescription.ServiceSetName.ONEP_LISP_SERVICE_SET:
                return Version(ONEP_VERSION_LISP_MAJOR, ONEP_VERSION_LISP_MINOR, ONEP_VERSION_LISP_MAINTENANCE)
            return None



    @classmethod
    def get_element_version(cls, element, ssName):
        """
        This method gets the Service Set version of the given Network Element.
        
        @param element: The Network Element to get the version from.
        @param ssName: Specifies the Service Set whose version is requested.
        @return:  Version object for the Service Set. If any of the input parameters  
                is null or unsupported, null will be returned.
        @raise OnepConnectionException:
                    The exception is thrown when the Network Element
                    is not connected.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the remote
                    procedure call made to the Network Element.
        """
        if element == None or ssName == None:
            return 
        if not element.is_connected():
            raise OnepConnectionException('network element is not connected')
        try:
            ver_idl = element.api_client.NetworkElement_getVersionIDL(element.session_handle._id, ssName)
            if ver_idl != None:
                return Version(ver_idl.major, ver_idl.minor, ver_idl.maint)
            raise OnepRemoteProcedureException()
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    @classmethod
    def version_check(cls, element, ssName):
        """
        This method checks version compatibility between the a given Network Element and
        this client program. The result of the compatibility check
        is provided in the form of VersionCompare enum values.
        The specified Network Element should be in the connected state for the API to validate the
        compatibility check.
        
        The results of the comparison should be interpreted as follows:
            - ONEP_VERSION_NCP:   The client side and Network Element versions are not compatible for the given package
            - ONEP_VERSION_GT:    The client side version is greater than NE version for the given package
            - ONEP_VERSION_LT:    The client side version is less than Network Element version for the given package
            - ONEP_VERSION_MATCH: The client side and Network Element versions are exact match
        
        @param element: The Network Element with which the applications
                        version compatibility check needs to be done for the
                        specified package.
        @param ssName: Specifies the Service Set to be checked.
        @return: The result of version check is returned as value of VersionCompare enum.
                If any of the input parameters is null or unsupported, 
                null will be returned.
        @raise OnepConnectionException:
                    The exception is thrown when the Network Element
                    is not connected.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the remote
                    procedure call made to the Network Element.
        """
        if element == None or ssName == None:
            return 
        client_version = cls.get_package_version(ssName)
        if client_version == None:
            return 
        ne_version = cls.get_element_version(element, ssName)
        if ne_version == None:
            return 
        if client_version.major != ne_version.major:
            return Version.VersionCompare.ONEP_VERSION_NCP
        if client_version.minor > ne_version.minor:
            return Version.VersionCompare.ONEP_VERSION_GT
        if client_version.minor < ne_version.minor:
            return Version.VersionCompare.ONEP_VERSION_LT
        if client_version.maintenance > ne_version.maintenance:
            return Version.VersionCompare.ONEP_VERSION_GT
        if client_version.maintenance < ne_version.maintenance:
            return Version.VersionCompare.ONEP_VERSION_LT
        return Version.VersionCompare.ONEP_VERSION_MATCH



    def check_major(self, major):
        """
        This method checks if the Version instance matches a given
        specific major number.
        
        @param major: Integer representing the major number.
        @return: True if the major version have exact match;
                false otherwise.
        """
        return self.major == major



    def check_minor(self, minor):
        """
        This method checks if the Version instance matches a given
        specific minor number.
        
        @param minor: Integer representing the major number.
        @return: True if the minor version have exact match;
                false otherwise.
        """
        return self.minor == minor



    def check_maintenance(self, maintenance):
        """
        This method checks if the Version instance matches a given
        specific maintenance number.
        
        @param maintenance: Integer representing the maintenance number.
        @return: True if the maintenance versions have exact match;
                false otherwise.
        """
        return self.maintenance == maintenance



    def check_exact(self, major, minor, maintenance):
        """
        This method checks if this Version instance matches a given
        specific major, minor and maintenance number. 
        
        
        @param major: Integer representing the major number.
        @param minor: Integer representing the minor number.
        @param maintenance: Integer representing the maintenance number.
        
        @return: True if the major, minor and maintenance version have exact match;
                false otherwise.
        """
        return self.major == major and self.minor == minor and self.maintenance == maintenance



    def __str__(self):
        return str(self.major) + '.' + str(self.minor) + '.' + str(self.maintenance)



Version.VersionCompare = enum('ONEP_VERSION_NCP', 'ONEP_VERSION_MATCH', 'ONEP_VERSION_GT', 'ONEP_VERSION_LT')

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:08 IST
