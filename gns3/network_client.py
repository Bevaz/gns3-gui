# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ipaddress


def getNetworkClientInstance(settings, network_manager):
    """
    Based on url return a network client instance
    """

    if settings.get("protocol", "http") == "ssh":
        from gns3.ssh_client import SSHClient
        return SSHClient(settings, network_manager)
    else:
        from gns3.http_client import HTTPClient
        return HTTPClient(settings, network_manager)


def getNetworkUrl(protocol, host, port, user=None, settings={}):
    """
    Return a network url from settings

    :param protocol: server protocol (http/ssh)
    :param host: host address
    :param port: port
    :param user: the username
    :param settings: Additional settings
    """

    if protocol == "ssh":
        return "{protocol}://{user}@{host}:{ssh_port}:{port}".format(protocol=protocol, user=user, host=host, port=port, ssh_port=settings["ssh_port"])
    elif user:

        try:
            ipaddress.IPv6Address(host.rsplit('%', 1)[0])  # remove any scope ID
            # this is an IPv6 address, we must surround it with brackets to be used in URLs (RFC2732)
            host = "[{}]".format(host)
        except ipaddress.AddressValueError:
            pass

        return "{protocol}://{user}@{host}:{port}".format(protocol=protocol, user=user, host=host, port=port)
    return "{protocol}://{host}:{port}".format(protocol=protocol, host=host, port=port)
