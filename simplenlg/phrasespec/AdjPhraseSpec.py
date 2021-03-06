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

from ..framework.NLGElement     import *
from ..framework.PhraseCategory import *
from ..framework.PhraseElement  import *


# This class defines a adjective phrase.  
class AdjPhraseSpec(PhraseElement):
    def __init__(self, phraseFactory):
        super().__init__(PhraseCategory.ADJECTIVE_PHRASE)
        self.setFactory(phraseFactory)

    # sets the adjective (head) of the phrase
    def setAdjective(self, adjective):
        if isinstance(adjective, NLGElement):
            self.setHead(adjective)
        else:
            adjectiveElement = self.getFactory().createWord(adjective, LexicalCategory.ADJECTIVE)
            self.setHead(adjectiveElement)

    # @return adjective (head) of  phrase
    def getAdjective(self):
        return self.getHead()
