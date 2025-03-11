# SPDX-FileCopyrightText: © 2025 Spencer Rak
# SPDX-License-Identifier: MIT

import asyncio
import logging
import os
import socket


from socketchat.config import logconfig

class Server:
    def __init__(self, ipv4addr, port, name=None, motd=None):
        try:
            self.ipv4addr = IPv4Address(ipv4addr)
        except ipaddress.AddressValueError as e:
            logger.fatal(f"{ipv4addr} is not a valid ipv4address")
            exit()
        self.port = port
        self.name = name
        self.motd = motd
        self.ssock = socket.socket((self.ipv4addr, self.port))

    def setup(self):
        try:
            self.ssock.bind()

        pass

    def accept_client(self):
        pass

    def send_msg(self):
        pass

    def recv_msg(self):
        pass

    def remove_client(self):
        pass
