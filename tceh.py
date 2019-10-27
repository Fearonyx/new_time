def my_function():
    print("i'm function")


print(my_function)
print('Functions are objects', isinstance(my_function, object))

test = my_function
test()

my_list = [my_function]
print(my_list)


def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')


call_passed_function(my_function)


try:
    d = 2
    d()
except TypeError as e:
    print('It is not a fuction', e)


print(callable(len), callable(45), callable(callable))


def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)


def double_all_elements(lst):
    """ Double all elements in list
    :param lst: incoming list
    :return: result list
    """

    if len(lst) == 0:
        return []
    else:
        updated_element = lst[0] * 2
        print(updated_element, len(lst))
        result = [updated_element, ] + double_all_elements(lst[1:])
    return result


double_all_elements([1, 2, 34, 44, 7])