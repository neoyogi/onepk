# 2015.02.05 17:18:40 IST
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.util.Enum import *
from onep.LocationIDL.ttypes import CivicIDL, CustomIDL, GeoIDL, NetworkLocationIDL, LocationFilterIDL
from onep.thrift.Thrift import TException
from onep.SanetIDL.SanetIDL import Client
from onep.core.event.EventListener import EventListener
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from Shared.ttypes import ExceptionIDL
import logging
import uuid
AltType = enum(LOCATION_ALT_TYPE_METERS=1, LOCATION_ALT_TYPE_FLOORS=2, LOCATION_ALT_TYPE_FEET=15)
LocationSubtype = enum(LOCATION_TYPE_NONE=0, LOCATION_TYPE_GEO=1, LOCATION_TYPE_CIVIC=2, LOCATION_TYPE_ELIN=4, LOCATION_TYPE_CUSTOM=8)
CivicType = enum(LOCATION_CIVIC_COUNTY=1, LOCATION_CIVIC_CITY=2, LOCATION_CIVIC_CITY_DIVISION=3, LOCATION_CIVIC_NEIGHBORHOOD=4, LOCATION_CIVIC_STREET_GROUP=5, LOCATION_CIVIC_RES_7=6, LOCATION_CIVIC_RES_8=7, LOCATION_CIVIC_RES_9=8, LOCATION_CIVIC_RES_10=9, LOCATION_CIVIC_RES_11=10, LOCATION_CIVIC_RES_12=11, LOCATION_CIVIC_RES_13=12, LOCATION_CIVIC_RES_14=13, LOCATION_CIVIC_RES_15=14, LOCATION_CIVIC_LEADING_STREET_DIR=15, LOCATION_CIVIC_TRAILING_STREET_SUFFIX=16, LOCATION_CIVIC_STREET_SUFFIX=17, LOCATION_CIVIC_STREET_NUMBER=18, LOCATION_CIVIC_STREET_NUMBER_SUFFIX=19, LOCATION_CIVIC_LANDMARK=20, LOCATION_CIVIC_ADDITIONAL_LOC=21, LOCATION_CIVIC_NAME=22, LOCATION_CIVIC_POSTAL_CODE=23, LOCATION_CIVIC_BUILDING=24, LOCATION_CIVIC_UNIT=25, LOCATION_CIVIC_FLOOR=26, LOCATION_CIVIC_ROOM=27, LOCATION_CIVIC_TYPE_OF_PLACE=28, LOCATION_CIVIC_POSTAL_COMMUNITY_NAME=29, LOCATION_CIVIC_POST_OFFICE_BOX=30, LOCATION_CIVIC_ADDITIONAL_CODE=31, LOCATION_CIVIC_SEAT=32, LOCATION_CIVIC_PRIMARY_ROAD_NAME=33, LOCATION_CIVIC_ROAD_SECTION=34, LOCATION_CIVIC_BRANCH_ROAD_NAME=35, LOCATION_CIVIC_SUB_BRANCH_ROAD_NAME=36, LOCATION_CIVIC_STREET_NAME_PREMODIFIER=37, LOCATION_CIVIC_STREET_NAME_POSTMODIFIER=38)
LocationHandleType = enum(LocElementHandle=0, LocInterfaceHandle=1)

class CivicLocation(object):
    """
    LocationCivic consists of a standard CAType constant and
    the associated value. The CAType numbers are standardized in RFC 4776.
    For use of any arbitrary name and value, see the "Cisco Custom" location type.
    """


    def __init__(self, catype, value):
        """
        @param catype: CAtype number (RFC 4776).
        @param value: Value associated with catype.
        """
        self._catype = catype
        if not CivicType._is_valid(catype):
            raise OnepIllegalArgumentException('catype', 'invalid enum value')
        self._value = value



    def _get_catype(self):
        return self._catype


    catype = property(_get_catype)

    def _get_value(self):
        return self._value


    value = property(_get_value)

    def _toIDL(self):
        """
        Convert LocationCivic to CivicIDL.
        For internal use only
        """
        if self._catype == None:
            return 
        return CivicIDL(self._catype, self.value)



    @classmethod
    def _fromIDL(cls, idl):
        """
        Convert from CivicIDL to LocationCivic.
        For internal use only
        """
        if idl == None:
            return 
        if not isinstance(idl, CivicIDL):
            raise OnepIllegalArgumentException('idl', 'CivicIDL')
        else:
            return CivicLocation(idl.catype, idl.value)



    @classmethod
    def _toIDLList(cls, ci_list):
        """
        Conver from a list of LocationCivic to CivicIDL.
        For internal use only
        """
        if not ci_list:
            return []
        idl_list = []
        for ci in ci_list:
            if ci != None:
                idl_list.append(ci._toIDL())

        return idl_list



    @classmethod
    def _fromIDLList(cls, idl_list):
        """
        Conver a list of CivicIDL to LocationCivic.
        For internal use only
        """
        if not idl_list:
            return []
        obj_list = []
        for idl in idl_list:
            obj_list.append(CivicLocation._fromIDL(idl))

        return obj_list



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, CivicLocation):
            return False
        other = obj
        if not self.__str__() == other.__str__():
            return False
        return True



    def __str__(self):
        return CivicType.enumval(self._catype) + ': ' + self._value




class CustomLocation(object):
    """
    The Cisco Custom location type allows specification of multiple
    arbitrary name and value pairs, in order to describe a location.
    While the "Civic" type only allows specific, standardized, attributes such
    as "city", "road", etc., the Cisco Custom type allows any label and can be
    thus used to specify "Department", "Camera view direction", etc.
    """


    def __init__(self, name, value):
        """
        @param name: Name of the Custom location attribute.
        @param value: Value associated with Custom attribute name.
        """
        self._name = name
        self._value = value



    def _get_value(self):
        return self._value


    value = property(_get_value)

    def _toIDL(self):
        """
        Convert LocationCustom to CustomIDL.
        For internal use only
        @pad.exclude
        """
        return CustomIDL(self._name, self._value)



    @classmethod
    def _fromIDL(cls, idl):
        """
        Convert CustomIDL to LocationCustom.
        For internal use only
        @pad.exclude
        """
        if not idl:
            return None
        if not isinstance(idl, CustomIDL):
            raise OnepIllegalArgumentException('idl', 'CustomIDL')
        else:
            return CustomLocation(idl.name, idl.value)



    @classmethod
    def _toIDLList(cls, custom_list):
        """
        Conver from a list of LocationCustom to CustomIDL
        For internal use only
        @pad.exclude
        """
        if not custom_list:
            return []
        idl_list = []
        for cl in custom_list:
            if cl != None:
                idl_list.append(cl._toIDL())

        return idl_list



    @classmethod
    def _fromIDLList(cls, idlList):
        """
        Conver a list of CustomIDL to LocationCustom.
        For internal use only
        @pad.exclude
        """
        if not idlList:
            return []
        obj_list = []
        for idl in idlList:
            obj_list.append(CustomLocation._fromIDL(idl))

        return obj_list



    def __eq__(self, obj):
        if not obj:
            return False
        if not isinstance(obj, CustomLocation):
            return False
        other = obj
        if not self.__str__() == other.__str__():
            return False
        return True



    def __str__(self):
        return self._name + ': ' + self.value




class GeoLocation(object):
    """
    GeoLocation contains geographic (GPS) location information
    for an object in agreement with RFC 3825.
    
    A geographic location is uniquely specified as:
    <ul>
     <li>Latitude plus resolution
     <li>Longitude plus resolution
     <li>Altitude plus resolution
    </ul> 
    """


    def __init__(self, latitude, longitude, altitude = 0, lat_resolution = 0, long_resolution = 0, alt_resolution = 0, alt_type = AltType.LOCATION_ALT_TYPE_METERS):
        """
        @param latitude: Latitude in degrees (North +, South -).
        @param longitude: Longitude in degrees (East +, West -).
        @param altitude: Altitude in meters or floors (Above sea level +, Below -).       
        @param lat_resolution: Latitude resolution in meters.
        @param long_resolution: Longitude resolution in meters.
        @param alt_resolution: Altitude resolution in meters or floors.
        @param alt_type: Units used in altitude - meters or floors.
        """
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._lat_resolution = lat_resolution
        self._long_resolution = long_resolution
        self._alt_resolution = alt_resolution
        self._alt_type = alt_type



    def _toIDL(self):
        """
        Convert GeoLocation to GeoIDL.
        For internal use only
        """
        return GeoIDL(str(self._latitude), str(self._lat_resolution), str(self._longitude), str(self._long_resolution), str(self._altitude), str(self._alt_resolution), AltType.LOCATION_ALT_TYPE_METERS if self._alt_type == None else int(self._alt_type))



    @classmethod
    def _fromIDL(cls, idl):
        """
        For internal use only
        """
        if not idl:
            return None
        if not isinstance(idl, GeoIDL):
            raise OnepIllegalArgumentException('idl', 'GeoIDL')
        else:
            if 0 == len(idl.latitude) or 0 == len(idl.longitude):
                return None
            else:
                lat = float(idl.latitude)
                longt = float(idl.longitude)
                latR = float(idl.lat_resolution) if idl.lat_resolution else 0
                longtR = float(idl.long_resolution) if idl.long_resolution else 0
                alt = float(idl.altitude) if idl.altitude else 0
                altR = float(idl.alt_resolution) if idl.alt_resolution else 0
                return GeoLocation(lat, longt, alt, latR, longtR, altR, AltType.LOCATION_ALT_TYPE_METERS if not idl.alt_type else idl.alt_type)



    def __eq__(self, obj):
        if obj == None:
            return False
        if isinstance(obj, GeoLocation):
            if self._latitude == obj._latitude and self._lat_resolution == obj._lat_resolution and self._longitude == obj._longitude and self._long_resolution == obj._long_resolution and self._altitude == obj._altitude and self._alt_resolution == obj._alt_resolution and self._alt_type == obj._alt_type:
                return True
        return False



    def __str__(self):
        return ' latitude: %s, \n            latResolution: %s,\n            longitude: %s,\n            longResolution: %s,\n            altitude: %s,\n            altResolution: %s,\n            altType: %s' % (self._latitude,
         self._lat_resolution,
         self._longitude,
         self._long_resolution,
         self._altitude,
         self._alt_resolution,
         self._alt_type)



LocationChangeEventChanger = enum(LOCATION_CHNG_NONE=0, LOCATION_CHNG_CLI=1, LOCATION_CHNG_NMSP=2, LOCATION_CHNG_SNMP=3, LOCATION_CHNG_CDP=4, LOCATION_CHNG_LLDP=5, LOCATION_CHNG_ONEP=6)

class LocationChangeFilter(EventFilter):
    """
        The LocationChangeFilter is passed to Location.add_change_listener()
        when configuring for notification of location change events.
        Multiple filter attributes may be specified in a filter.
        Once the filter has been used to configure a listener, it is no longer
        needed and can be disposed. It can also be reused in order to setup 
        filtering for another listener.
        <p>
        Location change filter information:
        <ul>
        <li>What types of location data should be watched for changes
        </ul>
        (More filtering types may be added in the future.)
        <p><b>Example:</b></p>
            locA = ne.get_location()
            // Creating a filter for change events
            filter = LocationChangeFilter()
            filter.add_subtype(LocationSubtype.LOCATION_TYPE_GEO)
            // Add a listener for location change events
            listener = MyLocationChangeListener()        
            eh = locA.add_change_listener(listener, filter, null);
    
        <pre>
        
        """


    def __init__(self):
        """
                Constructs a LocationChangeFilter object.
        
                The LocationChangeFilter is used in order to filter what
                types of LocationChangeEvent should be sent.  Currently,
                the only type of filtering provided is via location subtype.
                If no filtering is specified, then changes to all types of
                location information contained in the Location will result
                in a notification.
                """
        super(LocationChangeFilter, self).__init__()
        self._subtype_list = []



    def add_subtype(self, subtype):
        """
        This method adds a subtype which the filter will allow.  
        Multiple subtypes may be added to the filter by calling this 
        method multiple times. If the input subtype is null or if the subtype
        is already added in the filter, no futher action will be take by 
        this method.
        
        @param subtype: The subtype to be added to the filter.
        """
        if not subtype:
            raise OnepIllegalArgumentException('subtype', 'None')
        if self._subtype_list == None:
            self._subtype_list = []
        self._subtype_list.append(subtype)



    def remove_subtype(self, subtype):
        """
                This method removes an allowed subtype from the filter.
                If the input subtype is null or if the sybtype
                is not found in the filter, no futher action will be 
                take by this method.
        
                @param subtype: The subtype to be removed from the filter.
                """
        try:
            self._subtype_list.remove(subtype)
        except ValueError:
            pass



    def has_subtype(self, subtype):
        """
        This function is used to query whether or not the filter is looking for
        a specific type of location data.
        
        @param subtype: Type of location information being requested
        @return: True if the subtype requested exists; False otherwise.
        """
        return subtype in self._subtype_list



    def _toIDL(self):
        """
        Convert LocationCivic to CivicIDL.
        For internal use only
        """
        if not self._subtype_list:
            return None
        return LocationFilterIDL(LocationChangeFilter._convertSubtypeListToBitmask(self._subtype_list))



    @classmethod
    def _fromIDL(cls, idl):
        """Convert from CivicIDL to LocationCivic"""
        if idl == None:
            return 
        else:
            return CivicLocation(idl.catype, idl.value)



    @classmethod
    def _convertSubtypeListToBitmask(cls, subtype_list):
        """Convert a list of subtype to its bitmask representation."""
        bitmask = 0
        for st in subtype_list:
            if st != None:
                bitmask |= st

        return bitmask



    def __len__(self):
        return len(self._subtype_list)




class LocationChangeListener(EventListener):
    """
    The listener interface for receiving location change events. 
    The class that is interested in processing a location change event 
    should implement this interface.
    """


    def handle_event(self, event, client_data):
        """
        Invoked when the a location change event is received from the network element.
        
        @param event: An event object which indicates that an VLAN Change event occurred in a network element. 
        @type event:   L{LocationChangeEvent<onep.location.location.LocationChangeEvent>}
        
        @param client_data: The client_data is an object that was passed in when
                   the application called an API to add/register the event listener. 
                   The application is responsible for casting the input client_data
                   to the appropriate class before using it.
        """
        pass




class LocationChangeEvent(EventObject):
    """
    The LocationChangeEvent is sent whenever a Location
    related event notification is needed.  The event is passed to
    the event listener if Location.add_change_listener() has been called for
    the affected Location.  The LocationChangeEvent 
    allows the receiving application to discover the type of event
    and information related to it.
    
    <p>
    Location change event information contains:
    <ul>
    <li>How the associated Location was changed
    <li>What information was changed
    <li>The associated Location object
    </ul>
    </p>
    """


    def __init__(self, element, eventHandle, location, sybtype_list, changer):
        super(LocationChangeEvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_LOCATION_CHANGE)
        self.log = logging.getLogger(__name__)
        self.location = location
        self._subtype_list = sybtype_list
        self.changer = changer



    def has_subtype(self, subtype):
        """
        This method is used to query whether or not a specific type of location
        information subtype exists.
        
        
        """
        return subtype in self._subtype_list



    def do_event(self, network_element):
        """
        Internal Use Only
        """
        msg = 'InterfaceVrfEvent.do_event: event_handle = ' + str(self.event_handle) + ' LocationChangeEvent.doEvent: eventHandle = ' + str(self.event_handle) + ' changer = ' + str(self.changer)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener:
            target_listener.handle_event(self, client_data)




class Location(object):
    """
    Location class stores all information related to physical location
    in the real world. It is used by multiple Service Sets, including
    Element (NetworkElement & NetworkInterface) and Identity.
    
    Location provides location information in various forms:
    ELIN ("Equipment Line Item Number" or
              "Emergency Location Identification Number")
    Civic address (CAtype attributes as defined in RFC 4776)
    Cisco Custom address "Name" and "Value" pairs
    Geographic address information
    
    Any entity which has location data may have any one or more of these defined
    simultaneously.  Each type of location data is defined independently of the
    others.
    
    Location usage includes the following cases:
     * <ul>
     * <li>Network Element
     * <li>Network Interface
     * <li>Identify
     * </ul>
    In the case of NetworkElement, Location specifies the physical location
    of the device itself. This may be used in order to locate a device 
    in a building or machine room, find devices which will be affected by 
    maintenance,etc.
    
    In the case of NetworkInterface, Location specifies the physical location
    of the end point of the cable attached on the port.  This information may be
    used in order to track down the location of devices attached to this port.
    Any sessions which are started from devices attached to the port will inherit
    their location data from that port.
    
    When used in the Identity Service Set, Location specifies the
    physical location associated with the end point(s) of the session and/or the
    location of the end-user associated with the session.  
    
    @undocumented: toIDL
    """

    _location_handle_dict = {}

    def civic_location(self, catype):
        if catype:
            if self._civic_list:
                for lct in self._civic_list:
                    if lct and lct._catype:
                        return lct.value




    def __init__(self, elin = None, civic_list = None, custom_list = None, geo = None):
        """
              @param elin: The ELIN phone number string containing ELIN information. 
                  It can be None if the information is not specified. This is not supported on asr1k
              @param civic_list: A list of LocationCivic containing civic location information.
                  It can be None if the information is not specified. 
              @param custom_list: A list of LocationCustom containing custom location information.
                  It can be None if the information is not specified. 
              @param geo: The GeoLocation object containing Geo location information.
                  It can be None if the information is not specified. 
              
        
              """
        self.log = logging.getLogger(__name__)
        if elin:
            self.log.error('elin is not supported')
            from onep.core.exception.OnepException import OnepNotSupportedException
            raise OnepNotSupportedException('elin is not supported')
        self._elin = ''
        self._civic_list = civic_list
        self._custom_list = custom_list
        self._geo = geo
        self._loc_handle_type = None
        self._element = None
        self._network_intf = None
        self._event_manager = None
        self._location_handle = int(uuid.uuid1()) & 4294967295L
        self._location_handle_dict[self._location_handle] = self



    def _get_elin(self):
        from onep.core.exception import OnepNotSupportedException
        raise OnepNotSupportedException('elin is not supported')
        return self._elin


    elin = property(_get_elin)

    def _set_civic_list(self, civic_list):
        self._civic_list = civic_list



    def _get_civic_list(self):
        return self._civic_list


    _doc_civic_list = '\n    The list containing civic location information\n    '
    civic_list = property(_get_civic_list, _set_civic_list, None, _doc_civic_list)

    def _set_custom_list(self, custom_list):
        self._custom_list = custom_list



    def _get_custom_list(self):
        return self._custom_list


    _doc_custom_list = '\n    The list containing custom location information\n    '
    custom_list = property(_get_custom_list, _set_custom_list, None, _doc_custom_list)

    def _set_geo(self, geo):
        if geo == None:
            raise OnepIllegalArgumentException('geo', 'None')
        elif not isinstance(geo, GeoLocation):
            raise OnepIllegalArgumentException('geo', 'GeoLocation')
        self._geo = geo



    def _get_geo(self):
        return self._geo


    _doc_geo = '\n    The GeoLocation object containing Geo location information.\n    '
    geo = property(_get_geo, _set_geo, None, _doc_geo)

    def __eq__(self, obj):
        if obj == None:
            return False
        if self._elin == obj._elin and self._geo == obj._geo:
            return True
        return False



    def __str__(self):
        return ' elin: %s, \n            civic_list: %s,\n            custom_list: %s,\n            geo: %s,\n            location_handle: %s\n        ' % (self._elin,
         str(self._civic_list),
         self._custom_list,
         str(self._geo),
         self._location_handle)



    def _has_subtype(self, subtype):
        """
                This method is used to query whether or not a specific type of location
                information subtype exists.
                
                @param subtype:
                    Type of location information being requested
                @return true if the subtype requested exists; false otherwise.
        
                """
        subtype_dict = {LocationSubtype.enumval(LocationSubtype.LOCATION_TYPE_ELIN): self._elin,
         LocationSubtype.enumval(LocationSubtype.LOCATION_TYPE_CIVIC): self._civic_list,
         LocationSubtype.enumval(LocationSubtype.LOCATION_TYPE_CUSTOM): self._custom_list,
         LocationSubtype.enumval(LocationSubtype.LOCATION_TYPE_GEO): self._geo}
        try:
            has_subtype = subtype_dict[subtype]
        except KeyError:
            return False
        if has_subtype:
            if isinstance(has_subtype, list):
                if len(has_subtype) > 0:
                    return True
            else:
                return True
        return False



    def add_civic_location(self, catype, value):
        """
        This method adds one standardized Civic Address information element
        associated with the Location, indexed by catype and specifying the value
        for the new element.
        
        @param catype RFC4776 standard CAtype for the new civic location element.
        @param value A string representing the civic location info. A None for the
            value is considered a parameter error.
        @throws OnepIllegalArgumentException
            The exception is thrown when input catype parameter is invalid, or
            if the input catype already exist in this Location instance.
            If the "catype" is already present, it cannot be added again, but
            must be removed first.   
        """
        if catype == None:
            raise OnepIllegalArgumentException('catype', 'None')
        if value == None or len(value) == 0:
            raise OnepIllegalArgumentException('value', 'None')
        if not self._civic_list:
            self._civic_list = []
        else:
            for lct in self._civic_list:
                if lct and lct._catype == catype:
                    raise OnepIllegalArgumentException('catype aleady exist')

        self._civic_list.append(CivicLocation(catype, value))



    def remove_civic_location(self, catype):
        """
                This method removes one standardized Civic Address information element
                associated with the Location, indexed by catype. 
                
                If no match is found, this method will not take action.
                
                @param catype RFC4776 standard CAtype for the new civic location element.
                @throws OnepIllegalArgumentException
                    The exception is thrown when input parameter is invalid.
        
                """
        if catype == None:
            raise OnepIllegalArgumentException('catype', 'None')
        if not self.civic_list:
            return 
        target = None
        for lct in self._civic_list:
            if lct and lct._catype == catype:
                target = lct
                break

        if target:
            self._civic_list.remove(target)



    def remove_civic_location_list(self):
        """
           This method removes all Civic Address information
           associated with the Location.
        
           """
        self.civic_list = None



    def get_custom_location(self, name):
        """
        This method gets one standardized Custom Address information element
        associated with the Location, indexed by name.
        
        @param name Name of the custom location element to retrieve.
        @return A string representing the Custom location info; null if no 
            Custom location information is not defined for this 
            Location instance or no value has been assigned for 
            the custom name passed.
        
        """
        if name == None:
            return 
        if self.custom_list == None:
            return 
        for lc in self.custom_list:
            if lc and lc._name and lc._name == name:
                return lc.value




    def add_custom_location(self, name, value):
        """
                This method adds one Cisco Custom Address information tuple
                associated with the Location, specifying the name and value
                for the new element.
        
                Each element of the Custom Address information is represented as a
                (name,value) tuple, where both are strings.
                
                @param name Name of the custom location element, which is 
                    case-sensitive.
                @param value A string representing the Custom location info.
                @throws OnepIllegalArgumentException
                    The exception is thrown when input parameter is invalid,
                    or if the input name already exist in this Location instance.
                    If the name is already present, it cannot be added again, but
                    must be removed first.
                """
        if not name:
            raise OnepIllegalArgumentException('name', 'None')
        if not value:
            raise OnepIllegalArgumentException('value', 'None')
        if not self._custom_list:
            self._custom_list = []
        else:
            for lc in self._custom_list:
                if lc and lc._name and lc._name == name:
                    raise OnepIllegalArgumentException('name aleady exist')

        self._custom_list.append(CustomLocation(name, value))



    def remove_custom_location(self, name):
        """
        This method removes one Cisco Custom Address information element
        associated with the Location, indexed by name.
        
        If no match is found, this method will not take action.
        
        Each element of the Custom Address information is represented as a
        (name,value) tuple, where both are strings.
        
        @param name Name of the custom location element.
            @throws OnepIllegalArgumentException
            The exception is thrown when input parameter is invalid.
        """
        if name == None or len(name) == 0:
            raise OnepIllegalArgumentException('name', 'None')
        target = None
        for lc in self._custom_list:
            if lc and lc._name and lc._name == name:
                target = lc
                break

        if target:
            self.custom_list.remove(target)



    def remove_custom_location_list(self):
        """
        This method removes all Custom Address information
        associated with the Location.
        
        Each element of the Custom Address information is represented as a
        (name,value) tuple, where both are strings.
        """
        self.custom_list = None



    def remove_geo_location(self):
        """
        This method removes the Geolocation (GPS) Address information
        associated with the Location.
        
        """
        self._geo = None



    def _convert_subtype_list_to_bitmask(self):
        """
        Convert a list of subtype to its bitmask representation. For internal use
        only.
        @undocumented: _convert_subtype_list_to_bitmask
        """
        bitmask = 0
        for st in LocationSubtype.keys():
            if self._has_subtype(st):
                bitmask |= LocationSubtype.toInteger(st)

        return bitmask



    @classmethod
    def _convert_subtype_bitmast_to_list(self, type_mask):
        """
        Convert bitmask of subtype to a list of subtype. 
        For internal use only.
        @undocumented: _convert_subtype_bitmast_to_list
        """
        st_list = []
        for st in LocationSubtype.keys():
            if LocationSubtype.toInteger(st) & type_mask > 0:
                st_list.append(LocationSubtype.toInteger(st))

        return st_list



    @classmethod
    def _get_location_by_id(self, location_id):
        """
        Get Location object by ID.
        """
        return self._location_handle_dict[location_id]



    def toIDL(self):
        """
        Convert Location instance to NetworkLocationIDL.
        For internal use only
        """
        if self._geo == None:
            geo_idl = GeoLocation(0, 0)._toIDL()
        else:
            geo_idl = self._geo._toIDL()
        return NetworkLocationIDL(self._convert_subtype_list_to_bitmask(), self._elin, CivicLocation._toIDLList(self._civic_list), CustomLocation._toIDLList(self._custom_list), geo_idl)



    def _set_element_attachment(self, ne):
        """
        Set the network element this instance is attached to.
        For internal use only
        @undocumented: _set_element_attachment
        """
        self._element = ne
        self._loc_handle_type = LocationHandleType.LocElementHandle



    def _set_element_interface_attachment(self, interface):
        """
        Set the network interface this instance is attached to.
        @undocumented: _set_element_interface_attachment
        """
        self._network_intf = interface
        self._element = interface.network_element
        self._loc_handle_type = LocationHandleType.LocElementHandle



    def add_change_listener(self, listener, loc_filter, client_data):
        """
                Add a location change listener to the Location object. 
                Multiple listeners can be associate with an instance of Location.
                
                @param listener
                    The LocationChangeListener object that handles the events.
                @type listener: L{LocationChangeListener<onep.location.location.LocationChangeListener>}
                
                @param loc_filter
                    The LocationChangeFilter to specify criteria of interested location
                    change events.
                @type loc_filter: L{LocationChangeFilter<onep.location.location.LocationChangeFilter>}
                
                @param clientData
                    The client data associated with the listener. This client data 
                    will be part of input parameters when the handleEvent method 
                    in the listener is invoked.
                @type clientData: L{object}
                
                @return EventHandle, a numeric ID associated with this event
                    registration. The eventHandle is used to unregister the listener
                    using the removeLocationChangeListener method. If registration fails, -1
                    is returned.
                @throws OnepConnectionException
                    The exception is thrown when connection to a network element
                    has failed.
                @throws OnepRemoteProcedureException
                    The exception is thrown when error has occurred in the remote
                    procedure call made to a network element
                @throws OnepException
                    The exception is thrown when an internal error occurs
        
                """
        if not listener:
            raise OnepIllegalArgumentException('listener', 'None')
        if not loc_filter:
            raise OnepIllegalArgumentException('filter', 'None or empty')
        if self._loc_handle_type == None:
            raise OnepException('Location instance is not attached to' + 'NetworkElement or NetworkInterface')
        if self._loc_handle_type == LocationHandleType.LocElementHandle:
            if not self._element:
                raise OnepException('Location instance is not attached to' + 'NetworkElement')
            loc_client = self._element.location_client
            session = self._element.session_handle
            attachement_handle = 0
            self._event_manager = self._element.event_manager
        elif self._loc_handle_type == LocationHandleType.LocInterfaceHandle:
            if not self._network_intf:
                raise OnepException('Location instance is not attached to' + 'NetworkElement')
            loc_client = self._network_intf._network_element.location_client
            session = self._network_intf._network_element.session_handle
            attachement_handle = self._network_intf._xos_handle
            self._event_manager = self._network_intf._network_element.event_manager
        if not (loc_client and session and self._event_manager):
            raise OnepConnectionException()
        try:
            event_prop = loc_client.LocationChangeEvent_registerIDL(session.id, self._loc_handle_type, attachement_handle, self._location_handle, loc_filter._toIDL())
            if event_prop:
                self._event_manager.add_listener(event_prop.eventHandle, listener, client_data)
            self.log.info('Registered Location Listener with event handle')
            return event_prop.eventHandle
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_change_listener(self, event_handle):
        """
                Remove location change event listener. This method will remove the listener
                associated with the given event_handle and the corresponding registered
                event on the Location will be removed as well
                
                @param event_handle
                    Registered event identifier.
        
                @throws OnepIllegalArgumentException
                    This exception is thrown when eventHandle is not valid or is
                    unregistered already.
                <p><b>Example:</b></p>
                <pre>
                    location = ne.get_location();
                    eh = locA.add_change_listener(listener, filter, null);
                    location.remove_changeListener(eh);
                </pre>
                """
        if not event_handle:
            raise OnepIllegalArgumentException('event_handle', 'None')
        if not isinstance(event_handle, int):
            raise OnepIllegalArgumentException('event_handle', 'int')
        if event_handle:
            self._event_manager.remove_listener(event_handle)




def fromIDL(idl):
    """
    Convert from NetworkLocationIDL to Location. For internal use only
    """
    if idl == None:
        raise OnepIllegalArgumentException('idl', 'None')
    if not isinstance(idl, NetworkLocationIDL):
        raise OnepIllegalArgumentException('idl', 'NetworkLocationIDL')
    else:
        cv_list = CivicLocation._fromIDLList(idl.civic)
        cu_list = CustomLocation._fromIDLList(idl.custom)
        geo = GeoLocation._fromIDL(idl.geo)
        return Location(elin=idl.elin, civic_list=cv_list, custom_list=cu_list, geo=geo)



# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:40 IST
