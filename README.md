Fixbuf
=========

A role for installing the netsa tools fixbuf library. libfixbuf provides an implementation of the [IPFIX](http://www.ietf.org/html.charters/ipfix-charter.html) Protocol as a C library, for building IPFIX Collecting and Exporting Processes. See the API [documentation](https://tools.netsa.cert.org/fixbuf/libfixbuf/index.html) for details, including build instructions and known issues. 

Role Variables
--------------

Available variables are listed below, along with default values (see [defaults/main.yml](defaults/main.yml)):

	fixbuf_version

The version of fixbuf to install.  The master branch will always point to the latest available version.

	fixbuf_name: "libfixbuf-{{fixbuf_version}}"
	fixbuf_tgz: "{{fixbuf_name}}.tar.gz"
	fixbuf_url: "http://tools.netsa.cert.org/releases/{{fixbuf_tgz}}"
	fixbuf_timeout: 10
	fixbuf_checksums:
  		'2.4.0': sha256:bf20f9f7986a525ea6cc648d32f4ba30bfeb2a83f8c830bc39c48dfa7a415175
  		'2.3.0': sha256:ed63314f21a7a6bbf0d08da416403237a867c3f3496d061f10e148e6d8ecea63
	fixbuf_checksum: '{{fixbuf_checksums[fixbuf_version]}}'

Helper variables used to download the fixbuf release from the [netsa tools site](https://tools/netsa.cert.org).

	silk_ldconfig_template: "silkconf.j2"
	silk_ldconfig_file_path: /etc/ld.so.conf.d/silk.conf

Used to configure the dynamic loader to search for silk libraries.

The variable files in [vars/](vars/) contain the necessary packages to install for this and other netsa tools roles that might depend on this role.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: fixbuf
           tags: [ 'fixbuf' ]

License
-------

Copyright 2020 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Released under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
CERT® is registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.
This Software includes and/or makes use of the following Third-Party Software subject to its own license:
1. ansible (https://github.com/ansible/ansible/tree/devel/licenses) Copyright 2019 Red Hat, Inc.
2. molecule (https://github.com/ansible-community/molecule/blob/master/LICENSE) Copyright 2018 Red Hat, Inc.
3. testinfra (https://github.com/philpep/testinfra/blob/master/LICENSE) Copyright 2020 Philippe Pepiot.
DM20-0460

Author Information
------------------

This role was created in 2019 by [Matt Heckathorn](https://resources.sei.cmu.edu/library/author.cfm?authorID=2403).
