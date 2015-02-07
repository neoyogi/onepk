__author__ = 'yogesh'
from base import onepbase
from onep.interfaces import InterfaceStatus
from onep.interfaces import NetworkInterface
import onep.interfaces.InterfaceFilter
import socket

class DeviceInterfaces(onepbase):
    def __init__(self):
        super(DeviceInterfaces,self).__init__()


    def getInterfaceOfType(self,interface_Type,has_address_assigned=False):
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
                    interface_address_list.append((networkInterface, address))
        return interface_address_list

    def get_all_interfaces(self):
        interfaceList = None
        try:
            interfaceList = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
        except Exception, e:
            self.logger.error(e)
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

    


if __name__ == "__main__":
    interface = DeviceInterfaces()
    print(interface.getInterfaceOfType("gigabitethernet"))
    print(interface.get_up_interfaces())
    interface.disconnect()
