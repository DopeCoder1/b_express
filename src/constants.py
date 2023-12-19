from enum import Enum

class Environment(str,Enum):
    LOCAL = "LOCAL"
    STAGGING = "STAGGING"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.LOCAL, self.STAGGING, self.TESTING)
    
    @property
    def is_testing(self):
        return self == self.TESTING
    
    @property
    def is_deployed(self):
        return self == self.PRODUCTION
    