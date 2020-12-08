
"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "lechos22"
__authors__ = ["lechos22"]
__contact__ = "mail.lechos22@gmail.com"
__copyright__ = "Copyright 2020, lechos22"
__credits__ = ["lechos22"]
__date__ = "2020/12/08"
__deprecated__ = False
__email__ =  "mail.lechos22@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "lechos22"
__status__ = "Production"
__version__ = "0.0.1"

from kahoot import client
import random

bots=[]
print("How many bots? ")
botcount=int(input())
print("What PIN? ")
pin=int(input())
for i in range(botcount):
    bots+=[client()]
for i in bots:
    i.join(pin,str(random.choice(range(100000))))
