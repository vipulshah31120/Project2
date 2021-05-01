#Deriving Error from Super Class Exception

class Error(Exception) :                # class Error is derived from super class Exception
                                        # Error is derived class for Exception, but
                                        # Base class for exceptions in this modulepass
    pass

class TransitionError(Error) :          # Raised when an operation attempts a state transition that's not allowed.
    def __init__(self, prev, nex, msg) :
        self.prev = prev
        self.nex = nex
        self.msg = msg                  # Error message thrown is saved in msg
try :
    raise(TransitionError(2, 3*2, 'Not Allowed'))

except TransitionError as Error :       # Value of Exception is stored in error
    print('Exception Occurred', Error.msg)
