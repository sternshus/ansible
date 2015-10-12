# (c) 2014, Brian Coca, Josh Drake, et al
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.




class BaseCacheModule(object):

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError

    def keys(self):
        raise NotImplementedError

    def contains(self, key):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def flush(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError
