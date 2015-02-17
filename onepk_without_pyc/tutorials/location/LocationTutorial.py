#!/usr/bin/env python

# Copyright (c) 2010-2014 by Cisco Systems, Inc.
# 
# THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
# BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
# CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
# APPLICATION.
# 
# Redistribution and use of the sample code, with or without
# modification, are permitted provided that the following conditions
# are met:
# Redistributions of source code must retain the above disclaimer.
# 
# package: tutorials.location

import sys
import logging
from time import sleep
from BaseTutorial import BaseTutorial
from onep.location import Location,CivicLocation, CustomLocation, GeoLocation 
from onep.location import LocationChangeFilter, LocationChangeListener
from onep.location import CivicType, AltType, LocationSubtype

logger = logging.getLogger('onep:LocationTutorial')
logger.setLevel(logging.INFO)

class LocationTutorial(BaseTutorial):
    """ create a civic location object """
    #  START SNIPPET: create_civic_location
    civic_location = CivicLocation(CivicType.LOCATION_CIVIC_POSTAL_CODE, '95035')
    #  END SNIPPET: create_civic_location
    """ create a custom location object """
    #  START SNIPPET: create_custom_location
    custom_location = CustomLocation('campus', 'sjc')
    #  END SNIPPET: create_custom_location
    
#START SNIPPET: example_listener
class ExampleLocationChangeListener(LocationChangeListener):
    def handle_event(self, event, client_data):
        if event.has_subtype(LocationSubtype.LOCATION_TYPE_GEO):
            logger.info('Geo location information changed.')
        if event.has_subtype(LocationSubtype.LOCATION_TYPE_CUSTOM):
            logger.info('Custom location information changed.')
        if event.has_subtype(LocationSubtype.LOCATION_TYPE_CIVIC):
            logger.info('Civic location information changed.')
        logger.info('The location is changed to: \n' +str(event.location))
#END SNIPPET: example_listener
    
if __name__ == "__main__":
    tutorial = LocationTutorial(sys.argv)
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    
    civic_location_list = []
    civic_location_list.append(LocationTutorial.civic_location)
    
    custom_location_list = []
    custom_location_list.append(LocationTutorial.custom_location)
    custom_location_list.append(CustomLocation('building', '23'))
    
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("IdentityTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        logger.info('Setting the location of the network element')
        
        """ create a geo location object """
        #  START SNIPPET: create_geo_location
        geo_location = GeoLocation(37.41, -121.91, 
                                   altitude = 26,
                                   alt_type = AltType.LOCATION_ALT_TYPE_METERS)
        #  END SNIPPET: create_geo_location
        """ create a location object """
        #  START SNIPPET: create_location
        location = Location(civic_list=civic_location_list, custom_list=custom_location_list, geo=geo_location)
        #  END SNIPPET: create_location
        """ add a civic location to the location object """
        #  START SNIPPET: add_civic_location
        location.add_civic_location(CivicType.LOCATION_CIVIC_TYPE_OF_PLACE, 'office')
        #  END SNIPPET: add_civic_location
        
        #  START SNIPPET: set_location
        tutorial.network_element.set_location(location)
        #  END SNIPPET: set_location
        
        logger.info("The network element's location is set to " + str(location))
        logger.info("Verify the location on the network element using CLI 'sh location host'")
        raw_input('Hit Enter to continue.')
        
        intf_location = location
        """ add a custom location to the location object """
        #  START SNIPPET: add_custom_location
        intf_location.add_custom_location('rack', '367')
        #  END SNIPPET: add_custom_location
        intf = tutorial.get_an_interface()
        if intf is None:
            raise Exception('No interface available for use.')

        logger.info('Setting the location of interface ' + intf.name)
        #  START SNIPPET: set_interface_location
        intf.set_location(intf_location)
        #  END SNIPPET: set_interface_location
        
        logger.info('The interface location is set to ' + str(intf.get_location()))
        logger.info("Verify the location on the Network Element using following CLI commands:")
        logger.info("sh location geo-location interface " + intf.name)
        logger.info("sh location civic-location interface " + intf.name)
        logger.info("sh location custom-location interface " + intf.name)
        raw_input('Hit Enter to continue.')
        
        """ create a location change event filter and add location subtypes to the filter """
        #  START SNIPPET: create_filter
        loc_filter = LocationChangeFilter()
        loc_filter.add_subtype(LocationSubtype.LOCATION_TYPE_GEO)
        loc_filter.add_subtype(LocationSubtype.LOCATION_TYPE_CUSTOM)
        loc_filter.add_subtype(LocationSubtype.LOCATION_TYPE_CIVIC)
        #  END SNIPPET: create_filter
        
        loc_listener = ExampleLocationChangeListener()
        
        """ get the network element location """
        #START SNIPPET: get_location
        location = tutorial.network_element.get_location()
        #END SNIPPET: get_location
        
        logger.info('Adding the location change listener.')
        #START SNIPPET: add_listener
        event_handle = location.add_change_listener(loc_listener, loc_filter, 'client_data')
        #END SNIPPET: add_listener
        
        """ remove geo location from location object """
        #START SNIPPET: remove_geo
        location.remove_geo_location()
        #END SNIPPET: remove_geo
        """ remove custom location list from the object """
        #START SNIPPET: remove_custom_list
        location.remove_custom_location_list()
        #END SNIPPET: remove_custom_list
        """ remove geo location from location object """
        #START SNIPPET: remove_civic
        location.remove_civic_location(CivicType.LOCATION_CIVIC_TYPE_OF_PLACE)
        #END SNIPPET: remove_civic
        logger.info('Updating the network element location.')
        tutorial.network_element.set_location(location)
        
        sleep(10)
        logger.info('Removing the location change listener.')
        #START SNIPPET: remove_listener
        location.remove_change_listener(event_handle)
        #END SNIPPET: remove_listener
    except Exception as e:
        logger.error(str(e))
    finally:
        logger.info('disconnecting from the network element.')
        tutorial.disconnect()
        sys.exit(0)
