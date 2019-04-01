
# 3rd party modules
from slot import SLOT

def slot():
    return [SLOT[key] for key in sorted(SLOT.keys())]
