def func1(arg1, arg2):
    """This function takes two arguments, sets the first argument to the second, and returns. Pointless...
    
    :param arg1: Some value
    :type arg1: [type]
    :param arg2: Another value
    :type arg2: [type]
    :return: Argument 1
    :rtype: [type]
    """
    arg1 = arg2
    return arg1


def func2():
    """Function with no return type
    
    :return: [description]
    :rtype: [type]
    """
    return None


def func3(arg1):
    """[summary]
    
    :param arg1: [description]
    :type arg1: [type]
    :return: [description]
    :rtype: [type]
    """
    try:
        x = 10 / arg1
    except ZeroDivisionError:
        raise("Division by zero")
    return x
