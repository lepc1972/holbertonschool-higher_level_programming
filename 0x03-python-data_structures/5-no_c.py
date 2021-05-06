def no_c(my_string):
    noc_string = ""
    for i in my_string:
        if (i != "c" and i != "C"):
            noc_string =noc_string + i
    return noc_string
