#
## BEGIN LICENSE BLOCK
#
# Copyright (c) <2012>, Raul Perez <repejota@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
## END LICENSE BLOCK
#

import sys
import os

from fhost import utils
from fhost.exceptions import InvalidHostnameException
from fhost.exceptions import InvalidIPException

class Hosts(object):
	"""A collection of Hosts

	This is a collection of Hosts implemented as a Python container.
	It is iterable and have CRUD methods helpers to maintain a 
	registry of available Hosts during **fhost** process execution.
	
	It also have hardcoded the common path where /etc/hosts file is 
	located.

	In the future discover code will be implemented, both to detect 
	the OS and its version and /etc/hosts location.
	"""

	# Default hosts file path ( hardcoded at this moment )
	hosts_file = "/etc/hosts"

	def __init__(self):
		"""Available hosts container constructor

		Initialized the collection and parses /etc/hosts file for the 
		first time.
		"""
		self.__hosts = []
		# parse hosts
		self.__parse(self.hosts_file)

	def __parse(self, path):
		"""Parse an hosts file

		Parses an /etc/hosts file and fills the container with all of
		its entries.

		Each host is composed by:

			* IP address
			* Main hostname
			* Alias to the main hostname

		:Results: None
		"""
		# Check if file exists
		if os.path.exists(path):
			# Open file read only
			f = open(path, "r")
			for line in f.readlines():
				# Clean line
				line = line.strip('\r').strip()
				# Do not want commented or blank lines
				if not line.startswith("#") and line!='':
					# Get parts
					line_parts = line.split()
					# Add item dict { ip_address, canonical_hostname, aliases }
					self.__hosts.append({"ip_address": line_parts[:1][0],
										 "canonical_hostname": line_parts[1:2][0],
										 "aliases": line_parts[2:]})
			# Close file
			f.close()

	def __save(self, path):
		"""Saves hosts file

		Saves this container ( one host per line ) to disk at specified path.

		Also checks if path is available and throws an excpetion if its not
		accedible.

		:Results: None
		"""
		# Open file to write
		f = open(path, "w")
		# Write each host
		for host in self.__hosts:
			f.write("%s\t%s\t%s\n" % (host['ip_address'], 
									  host['canonical_hostname'], 
									  " ".join(host['aliases'])))
		# Close file
		f.close()

	def __empty(self):
		"""Empty loaded hosts

		Erases all available hosts on this container and starts with
		an enmpty one.

		:Results: None
		"""
		self.__hosts = []	

	def __iter__(self):
		"""Hosts iterator

		Returns this container iterator.

		:Results: Iterator on hosts container.
		"""
		return iter(self.__hosts)

	def __len__(self):
		"""Returns number of hosts available

		Count how many hosts are in this container.

		:Results: int number of hosts
		"""
		return len(self.__hosts)

	def add(self, ip_address, canonical_hostname, *args):
		"""Add new hostname to the container.

		Each host is composed by:

			* IP address
			* Main hostname
			* Aliases to the main hostname

		At this moment multiple aliases are accepted and inserted but only one is 
		used and saved back.

		:Results: None
		"""
		if not utils.isValidIP(ip_address):
			raise InvalidIPException("%s is not a valid IP address" % ip_address)
			sys.exit(1)
		if not utils.isValidHostname(canonical_hostname):
			raise InvalidHostnameException("%s is not a valid hostname" % canonical_hostname)
			sys.exit(1)
		self.__hosts.append({"ip_address": ip_address, 
							 "canonical_hostname": canonical_hostname, 
							 "aliases": args})
		self.__save(self.hosts_file)

	def delete(self, canonical_hostname):
		"""Delete existing hostname.

		A valid hostname must be passed, no IP or alias are valid arguments.

		:Results: None
		"""
		if not utils.isValidHostname(canonical_hostname):
			raise InvalidHostnameException("%s is not a valid hostname" % canonical_hostname)
			sys.exit(1)
		self.__hosts = [{"ip_address": host["ip_address"], 
						 "canonical_hostname": host["canonical_hostname"], 
						 "aliases": host["aliases"]} 
						for host in self.__hosts 
						if host["canonical_hostname"]!=canonical_hostname]
		self.__save(self.hosts_file)