import csv
import pandas
import numpy as np

"""
    This file contains basic data cube calculation.
    Data converted from csv to array using pandas.
    Specifically dimension drill up.
    
"""
def main():

    print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_2 Qestion_2")
    print("Name:       Yayi Ning\n\n")

    # data converted from csv to array using pandas
    df = pandas.read_csv('Q2data.csv', sep = ',', header = None)
    data_array = df.values

    print("Q2.a._____________________________________________________________________________")
    print("We have four dimensions (Location, Category, Rating, Price), where Location have 2 levels{State, City}.")
    print("Thus we have (2+1)*(1+1)*(1+1)*(1+1) = ", 3*2*2*2, " number of cuboids in this cube.")
    print("\n\n")

    print("Q2.b._____________________________________________________________________________")
    num_cells = data_array.shape[0]
    print("Number of cells in the cuboid = data_array.shape[0] = ", num_cells)
    print("\n\n")


    print("Q2.c._____________________________________________________________________________")
    print("Drill up by climbing up in the Location dimension, from City to State:")
    # data_drillup = data_array[:,[0,1,3,4,5]]
    data_drillup = []
    temp = data_array[:,[1,3,4,5]]
    compare_str = []

    for i in range(temp.shape[0]):
        temp[i, 3] = str(temp[i, 3])
        string_i = str(temp[i,0] + temp[i,1] + temp[i,2] + temp[i,3])
        if string_i not in compare_str:
            compare_str.append(string_i)
            data_drillup.append(data_array[i, [0, 1, 3, 4, 5]])

    data_drillup = np.array(data_drillup)
    print("Now the data data_drillup looks like:\n", data_drillup)
    print("Now data_drillup have shape: ", data_drillup.shape, ", it has ", data_drillup.shape[0]," cells left." )
    print("\n\n")


    print("Q2.d._____________________________________________________________________________")
    print("Further drill up (* , Category , Rating , Price):")
    # data_drillup2 = data_array[:,[0,3,4,5]]
    data_drillup2 = []
    temp = data_array[:, [3, 4, 5]]
    compare_str = []
    for i in range(temp.shape[0]):
        temp[i, 2] = str(temp[i, 2])
        string_i = str(temp[i, 0] + temp[i, 1] + temp[i, 2])
        if string_i not in compare_str:
            compare_str.append(string_i)
            data_drillup2.append(data_array[i,[0,3,4,5]])
    data_drillup2 = np.array(data_drillup2)
    print("Now the data data_drillup2 looks like:\n", data_drillup2)
    print("Now data_drillup2 have shape: ", data_drillup2.shape, ", it has ", data_drillup2.shape[0], " cells left.")
    print("\n\n")


    print("Q2.e._____________________________________________________________________________")
    count_Illinois_Moderate_3 = sum(data_array[i,4]=='moderate' and data_array[i,1]=='Illinois' and data_array[i,5]==3 for i in range(50))
    print("Count of (Location(state) = ’Illinois’ , * , rating = 3 , Price = ’Moderate’) = ", count_Illinois_Moderate_3)
    print("\n\n")


    print("Q2.f._____________________________________________________________________________")
    count_Chicago_food = sum(data_array[i,3]=='food' and data_array[i,2]=='Chicago' for i in range(50))
    print("Count of (Location(city) = ’Chicago’ , Category=’food’ , * , *) = ", count_Chicago_food)
    print("\n\n")


if __name__=="__main__":
    main()
