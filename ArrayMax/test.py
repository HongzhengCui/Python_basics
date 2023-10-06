from array_max import array_max

def do_test(array):
    print("{}: {}".format(array,array_max(array)))

array1 = [ 77, 33, 19, 99, 42, 6, 27, 4 ]
array2 = [ -3, -42, -99, -1000, -999, -88, -77 ]
array3 = [ 425, 59, -3, 77, 0, 36]
array4 = ["string"]
array5 = [45.2, "string", 3, 0, "test"]

do_test(array1)
do_test(array2)
do_test(array3)
do_test("string passed")
do_test([])
do_test(array4)
do_test(array5)

