import sys
import numpy

ALABAMA_POPULATION = 4858979
ALASKA_POPULATION = 738432
ARIZONA_POPULATION = 6828065
ARKANSAS_POPULATION = 2978204
CALIFORNIA_POPULATION = 39144818
COLORADO_POPULATION = 5456574
CONNECTICUT_POPULATION = 3590886
DELAWARE_POPULATION = 945934
FLORIDA_POPULATION = 20271272
GEORGIA_POPULATION = 10214860
HAWAII_POPULATION = 1431603
IDAHO_POPULATION = 1654930
ILLINOIS_POPULATION = 12859995
INDIANA_POPULATION = 6619680
IOWA_POPULATION = 3123899
KANSAS_POPULATION = 2911641
KENTUCKY_POPULATION = 4425092
LOUISIANA_POPULATION = 4670724
MAINE_POPULATION = 1329328
MARYLAND_POPULATION = 6006401
MASSACHUSETTS_POPULATION = 6794422
MICHIGAN_POPULATION = 9922576
MINNESOTA_POPULATION = 5489594
MISSISSIPPI_POPULATION = 2992333
MISSOURI_POPULATION = 6083672
MONTANA_POPULATION = 1032949
NEBRASKA_POPULATION = 1896190
NEVADA_POPULATION = 2890845
NEW_HAMPSHIRE_POPULATION = 1330608
NEW_JERSEY_POPULATION = 8958013
NEW_MEXICO_POPULATION = 2085109
NEW_YORK_POPULATION = 19795791
NORTH_CAROLINA_POPULATION = 10042802
NORTH_DAKOTA_POPULATION = 756927
OHIO_POPULATION = 11613423
OKLAHOMA_POPULATION = 3911338
OREGON_POPULATION = 4028977
PENNSYLVANIA_POPULATION = 12802503
RHODE_ISLAND_POPULATION = 1056298
SOUTH_CAROLINA_POPULATION = 4896146
SOUTH_DAKOTA_POPULATION = 858469
TENNESSEE_POPULATION = 6600299
TEXAS_POPULATION = 27469114
UTAH_POPULATION = 2995919
VERMONT_POPULATION = 626042
VIRGINIA_POPULATION = 8382993
WASHINGTON_POPULATION = 7170351
WEST_VIRGINIA_POPULATION = 1844128
WISCONSIN_POPULATION = 5771337
WYOMING_POPULATION = 586107

Alabama = [106, 131, 157, 196, 242, 386, 531, 639, 720, 827, 907, 979, 1084, 1251, 1454, 1569, 1739]
Alaska = [102,114,119,133,143,151,157,171,185]
Arizona = [104,152,235,326,401,508,665,773,919,1157,1289,1413,1598,1769,2019,2269,2456]
Arkansas = [100,118,165,201,232,308,349,386,409,449,508,564,624,683,738,743]


















def convert_cases_to_ratio(number_of_cases, population):
    for i in range(len(number_of_cases)):
        number_of_cases[i] = number_of_cases / population
    return number_of_cases


def get_prediction(A_matrix, b_vector, data_to_predict_with):

    # Ax = b
    # x = ((A^t)(A))^-1 * A^t * b

    AtA = ((A_matrix).transpose()).dot(A_matrix)
    AtA_inverse = numpy.linalg.inv(AtA)
    x_vector = (AtA_inverse.dot(A_matrix.transpose())).dot(b_vector)
    print("x_vector: ")
    print(x_vector)

    prediction = data_to_predict_with.dot(x_vector)
    print("prediction: ", prediction)

#first we do a prediction for michigan. we will grab 9 days worth of data and try to predict the number of cases on the
# 10th day using the data from all 45 states (all states excluding Michigan, Alaska, Montana, South Dakota and wyoming)

michigan_vector = numpy.array(convert_cases_to_ratio([], MICHIGAN_POPULATION))

A_matrix = []
b_vector = []

get_prediction(A_matrix, b_vector, michigan_vector)



#then we do predictions for states that have very little amount of data: Alaska, Montana, South Dakota and wyoming.

#Alaska:
alaskan_vector = numpy.array(convert_cases_to_ratio([], ALASKA_POPULATION))










