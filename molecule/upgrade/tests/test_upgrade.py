# ansible-role-fixbuf
# Copyright 2020 Carnegie Mellon University.
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING
# INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON
# UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
# AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR
# PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE
# MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND
# WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
# Released under a MIT (SEI)-style license, please see license.txt or contact
# permission@sei.cmu.edu for full terms.
# [DISTRIBUTION STATEMENT A] This material has been approved for public
# release and unlimited distribution.  Please see Copyright notice for
# non-US Government use and distribution.
# CERT is registered in the U.S. Patent and Trademark Office by Carnegie
# Mellon University.
# This Software includes and/or makes use of the following Third-Party Software
# subject to its own license:
# 1. ansible (https://github.com/ansible/ansible/tree/devel/licenses)
# Copyright 2019 Red Hat, Inc.
# 2. molecule
# (https://github.com/ansible-community/molecule/blob/master/LICENSE)
# Copyright 2018 Red Hat, Inc.
# 3. testinfra (https://github.com/philpep/testinfra/blob/master/LICENSE)
# Copyright 2020 Philippe Pepiot.
# DM20-0460
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fixbuf_version(host):
    version = "2.4.2"
    command = """PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig \
                 pkg-config --modversion libfixbuf"""

    cmd = host.run(command)

    assert version in cmd.stdout
