"""
A script which is used to input the NV items for required NR and LTE bands in MTPs
"""


choice = int(input("Please provide the choice . 1 for LTE . 2 for NR  :"))
band_inputs = [int(y) for y in input("Enter the bands to be enabled seperated by comma :").split(',')]
less_than_64 = []
more_than_64 = []
for value in band_inputs:
    if value <=64:
        less_than_64.append(value)
    else:
        more_than_64.append(value)

def band_value_0_64():
    val1 = int(128)
    list1_new = []
    for i in range(0, val1):
        list1_new.append(str(0))
    for j in less_than_64:
        list1_new[-j] = str(1)

    new = "".join(list1_new)
    nv_ls64 = int(new, 2)
    return nv_ls64

def band_value_65_124():
    val2 = int(128)
    list2_new = []
    for i in range(0,val2):
        list2_new.append(str(0))
    for j in more_than_64:
        val3 = j-64
        list2_new[-val3] = str(1)

    new2 = "".join(list2_new)
    nv_gt64 = int(new2, 2)
    return nv_gt64

if choice == 1:
    print(f"Please input the value for NV 65633 as {band_value_0_64()}")
    print(f"Please input the value for NV 73680 as {band_value_65_124()}")
elif choice == 2:
    print(f"Please input bits_1_64 in NV 74213 as {band_value_0_64()}")
    print(f"Pkease input bits_65_128 in NV 74213 as {band_value_65_124()}")
else:
    print("invalid option chosen. Bye")