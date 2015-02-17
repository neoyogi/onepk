__author__ = 'yogesh'
from base import onepbase
from onep.interfaces import InterfaceStatus
from onep.interfaces import NetworkInterface
import onep.interfaces.InterfaceFilter
import socket

class DeviceInterfaces(onepbase):
    def __init__(self):
        super(DeviceInterfaces,self).__init__()


    def getInterfacesOfType(self,interface_Type,has_address_assigned=False):
        if interface_Type == "loopback":
            interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_LOOPBACK
        elif interface_Type == "ethernet":
            interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ETHERNET
        elif interface_Type == "gigabitethernet":
            interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_GIGABIT_ETHERNET
        elif interface_Type == "serial":
            interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_SERIAL
        elif interface_Type == "any":
            interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        interface_address_list = list()
        interfaceList = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
        elemAddress = socket.gethostbyname(self.network_element.host_address)
        for networkInterface in interfaceList:
            if networkInterface.interface_type == interfaceType:
                address = networkInterface.get_address_list()
                if address and elemAddress not in address:
                    interface_address_list.append((networkInterface.name, address))
        return interface_address_list

    def get_all_interfaces(self):
        interfaceList = dict()
        interfaces = None
        interfaceAddress = None
        interfaceName = None
        try:
            interfaces = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
        except Exception, e:
            self.logger.error(e)
        for eachinterface in interfaces:
            interfaceName = eachinterface.name
            interfaceAddress = eachinterface.get_address_list()
            interfaceList[interfaceName] = (eachinterface,interfaceAddress)
        return interfaceList

    def get_address_for_interface(self, network_interface):
        return network_interface.get_address_list()

    def get_up_interfaces(self):
        interfaceList = None
        networkInterface = None
        try:
            interfaceList = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
            for networkInterface in interfaceList:
                if networkInterface.get_status().link == InterfaceStatus.InterfaceState.ONEP_IF_STATE_OPER_UP:
                    return networkInterface
        except Exception, e:
            self.logger.error(e)
        return None

    def get_interface_prefix(self,networkInterface):
        prefixes = list()
        for prefix in networkInterface.get_prefix_list():
            prefixes.append(prefix.prefix_length)
        return prefixes

    def setInterfaceIPAddress(self,networkInterface,address,prefix=24):
        if networkInterface == None:
            self.logger.error("No interfaces are available!")
            return None


if __name__ == "__main__":
    interface = DeviceInterfaces()
    print(interface.getInterfacesOfType("any"))
    print(interface.get_interface_prefix(interface.get_up_interfaces()))
    print(interface.get_all_interfaces())
    interface.disconnect()
