# The contents of this file are subject to the Mozilla Public License
# Version 1.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS"
# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
# License for the specific language governing rights and limitations
# under the License.
#
# The Original Code is "Simplenlg".
#
# The Initial Developer of the Original Code is Ehud Reiter, Albert Gatt and Dave Westwater.
# Portions created by Ehud Reiter, Albert Gatt and Dave Westwater are
# Copyright (C) 2010-11 The University of Aberdeen. All Rights Reserved.
#
# Contributor(s): Ehud Reiter, Albert Gatt, Dave Wewstwater, Roman Kutlak, Margaret Mitchell.


# This class keeps track of the prefix for numbered lists.
class NumberedPrefix(object):
    def __init__(self):
        self.prefix = "0"

    def increment(self):
        dotPosition = self.prefix.rfind('.')
        if dotPosition < 0:
            counter = int(self.prefix)
            counter += 1
            self.prefix = str(counter)
        else:
            subCounterStr = self.prefix[dotPosition+1:]
            subCounter = int(subCounterStr)
            subCounter += 1
            self.prefix = self.prefix[:dotPosition] + "." + str(subCounter)

    # This method starts a new level to the prefix
    def upALevel(self):
        if self.prefix == "0":
            self.prefix = "1"
        else:
            self.prefix += ".1"

    # This method removes a level from the prefix .
    def downALevel(self):
        dotPosition = self.prefix.rfind('.')
        if dotPosition < 0:
            self.prefix = "0"
        else:
            self.prefix = self.prefix[:dotPosition]

    def getPrefix(self):
        return self.prefix

    def setPrefix(self, prefix):
        self.prefix = prefix