def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    positional arguments: pos_arg1, pos_arg2
    option arguments: opt_arg1, opt_arg2
    additional positional arguments (*args)\
    additional keyword argumentts (**kwargs)
    """
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)
    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)

    # Print addiotional posiotional arguments
    if args:
        print("Addiotinal positional arguments:")
        for arg in args:
            print(arg)
    
    # print additional keyword arguments
    if kwargs:
        print("Additional Keyword Arguments")
        for key, value in kwargs.items():
            print(f"{key} : {value}")

test_args_func("Hello", "CF", opt_arg1=10, opt_arg2=100)
print("-----------")
test_args_func("Hello", "CF", opt_arg1=10, keyw_arg1 = "Python", keyw_arg2 = "Android")