# 8.	Exception Hierarchy: Design a hierarchy of custom exceptions with different levels of specificity.
class zero_se_nhi_hoga_yrrr(Exception):
    
    pass

class MyAppException(Exception):
    pass

class InputValidationException(MyAppException):
    pass

class DatabaseConnectionException(MyAppException):
    pass

class DatabaseQueryException(DatabaseConnectionException):
    pass

class AuthenticationException(MyAppException):
    pass

class PermissionDeniedException(AuthenticationException):
    pass

class UserNotFoundException(AuthenticationException):
    pass
