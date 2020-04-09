import sys
import numpy

# for copy and paste purpose
# [
#     Alabama,
#     Arizona,
#     Arkansas,
#     California,
#     Colorado,
#     Connecticut,
#     Delaware,
#     Florida,
#     Georgia,
#     Hawaii,
#     Idaho,
#     Illinois,
#     Indiana,
#     Iowa,
#     Kansas,
#     Kentucky,
#     Louisiana,
#     Maine,
#     Maryland,
#     Massachusetts,
#     Minnesota,
#     Mississippi,
#     Missouri,
#     Nebraska,
#     Nevada,
#     New_Hampshire,
#     New_Jersey,
#     New_Mexico,
#     New_York,
#     North_Carolina,
#     North_Dakota,
#     Ohio,
#     Oklahoma,
#     Oregon,
#     Pennsylvania,
#     Rhode_Island,
#     South_Carolina,
#     Tennessee,
#     Texas,
#     Utah,
#     Vermont,
#     Virginia,
#     Washington,
#     West_Virginia,
#     Wisconsin]

#again for copy and paste purpose
# [
#     convert_cases_to_ratio(Alabama[:9], ALABAMA_POPULATION),
#     convert_cases_to_ratio(Arizona[:9], ARIZONA_POPULATION),
#     convert_cases_to_ratio(Arkansas[:9], ARKANSAS_POPULATION),
#     convert_cases_to_ratio(California[:9], CALIFORNIA_POPULATION),
#     convert_cases_to_ratio(Colorado[:9], COLORADO_POPULATION),
#     convert_cases_to_ratio(Connecticut[:9], CONNECTICUT_POPULATION),
#     convert_cases_to_ratio(Delaware[:9], DELAWARE_POPULATION),
#     convert_cases_to_ratio(Florida[:9], FLORIDA_POPULATION),
#     convert_cases_to_ratio(Georgia[:9], GEORGIA_POPULATION),
#     convert_cases_to_ratio(Hawaii[:9], HAWAII_POPULATION),
#     convert_cases_to_ratio(Idaho[:9], IDAHO_POPULATION),
#     convert_cases_to_ratio(Illinois[:9], ILLINOIS_POPULATION),
#     convert_cases_to_ratio(Indiana[:9], INDIANA_POPULATION),
#     convert_cases_to_ratio(Iowa[:9], IOWA_POPULATION),
#     convert_cases_to_ratio(Kansas[:9], KANSAS_POPULATION),
#     convert_cases_to_ratio(Kentucky[:9], KENTUCKY_POPULATION),
#     convert_cases_to_ratio(Louisiana[:9], LOUISIANA_POPULATION),
#     convert_cases_to_ratio(Maine[:9], MAINE_POPULATION),
#     convert_cases_to_ratio(Maryland[:9], MARYLAND_POPULATION),
#     convert_cases_to_ratio(Massachusetts[:9], MASSACHUSETTS_POPULATION),
#     convert_cases_to_ratio(Minnesota[:9], MINNESOTA_POPULATION),
#     convert_cases_to_ratio(Mississippi[:9], MISSISSIPPI_POPULATION),
#     convert_cases_to_ratio(Missouri[:9], MISSOURI_POPULATION),
#     convert_cases_to_ratio(Nebraska[:9], NEBRASKA_POPULATION),
#     convert_cases_to_ratio(Nevada[:9], NEVADA_POPULATION),
#     convert_cases_to_ratio(New_Hampshire[:9], NEW_HAMPSHIRE_POPULATION),
#     convert_cases_to_ratio(New_Jersey[:9], NEW_JERSEY_POPULATION),
#     convert_cases_to_ratio(New_Mexico[:9], NEW_MEXICO_POPULATION),
#     convert_cases_to_ratio(New_York[:9], NEW_YORK_POPULATION),
#     convert_cases_to_ratio(North_Carolina[:9], NORTH_CAROLINA_POPULATION),
#     convert_cases_to_ratio(North_Dakota[:9], NORTH_DAKOTA_POPULATION),
#     convert_cases_to_ratio(Ohio[:9], OHIO_POPULATION),
#     convert_cases_to_ratio(Oklahoma[:9], OKLAHOMA_POPULATION),
#     convert_cases_to_ratio(Oregon[:9], OREGON_POPULATION),
#     convert_cases_to_ratio(Pennsylvania[:9], PENNSYLVANIA_POPULATION),
#     convert_cases_to_ratio(Rhode_Island[:9], RHODE_ISLAND_POPULATION),
#     convert_cases_to_ratio(South_Carolina[:9], SOUTH_CAROLINA_POPULATION),
#     convert_cases_to_ratio(Tennessee[:9], TENNESSEE_POPULATION),
#     convert_cases_to_ratio(Texas[:9], TEXAS_POPULATION),
#     convert_cases_to_ratio(Utah[:9], UTAH_POPULATION),
#     convert_cases_to_ratio(Vermont[:9], VERMONT_POPULATION),
#     convert_cases_to_ratio(Virginia[:9], VIRGINIA_POPULATION),
#     convert_cases_to_ratio(Washington[:9], WASHINGTON_POPULATION),
#     convert_cases_to_ratio(West_Virginia[:9], WEST_VIRGINIA_POPULATION),
#     convert_cases_to_ratio(Wisconsin[:9], WISCONSIN_POPULATION)]

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
Alaska = [102, 114, 119, 133, 143, 151, 157, 171, 185]
Arizona = [104, 152, 235, 326, 401, 508, 665, 773, 919, 1157, 1289, 1413, 1598, 1769, 2019, 2269, 2456]
Arkansas = [100, 118, 165, 201, 232, 308, 349, 386, 409, 449, 508, 564, 624, 683, 738, 743]
California = [114, 133, 157, 177, 198, 247, 335, 392, 472, 598, 675, 1006, 1224, 1468, 1733, 2102, 2535, 3006, 3801, 4643, 5763, 6932, 8155, 9191, 10701, 12026, 13438]
Colorado = [101, 131, 160, 183, 216, 277, 363, 475, 591, 720, 912, 1086, 1430, 1734, 2061, 2307, 2627, 2966, 3342, 3728, 4173, 4565, 4950]
Connecticut = [159, 194, 223, 327, 415, 618, 875, 1012, 1291, 1524, 1993, 2571, 3128, 3557, 3824, 4915, 5276, 5675]
Delaware = [119, 143, 165, 214, 232, 264, 319, 368, 393, 450, 593, 673]
Florida = [115, 149, 160, 216, 328, 432, 563, 763, 1007, 1227, 1467, 1977, 2484, 3198, 4038, 4950, 5704, 6741, 7773, 9008, 10268, 11545, 12350, 13324]
Georgia = [121, 146, 197, 287, 420, 555, 620, 800, 1097, 1387, 1643, 2198, 2446, 2683, 3032, 4117, 4748, 5444, 5967, 6383, 6742]
Hawaii = [106, 120, 151, 175, 204, 224, 258, 285, 319, 351, 371, 387, 410, 435]
Idaho = [123, 189, 230, 261, 310, 415, 525, 669, 891, 1013, 1077, 1101, 1170, 1210]
Illinois = [105, 160, 288, 422, 585, 753, 1049, 1285, 1535, 1865, 2538, 3026, 3491, 4596, 5057, 5994, 6980, 7695, 8904, 10357, 11256, 12262, 13549, 15078]
Indiana = [124, 199, 256, 361, 474, 636, 939, 1222, 1511, 1782, 2156, 2562, 3031, 3429, 3944, 4411, 4933, 5492, 5921, 6351]
Iowa = [105, 124, 145, 179, 235, 298, 336, 424, 497, 549, 614, 699, 786, 868, 946, 1048, 1145]
Kansas = [126, 171, 205, 264, 322, 371, 431, 485, 555, 623, 701, 750, 848, 903, 1011]
Kentucky = [124, 157, 198, 248, 302, 394, 439, 480, 594, 670, 770, 831, 917, 955, 1008, 1149, 1346]
Louisiana = [103, 136, 196, 280, 392, 537, 763, 837, 1172, 1388, 1795, 2305, 2746, 3315, 3540, 4025, 5237, 6424, 9150, 10297, 12496, 13010, 14867, 16284, 17030, 18283]
Maine = [107, 118, 142, 155, 168, 211, 253, 275, 303, 344, 376, 432, 456, 470, 499, 519, 537]
Maryland = [107, 150, 190, 244, 288, 349, 423, 580, 774, 992, 1239, 1413, 1660, 1985, 2331, 2758, 3125, 3609, 4045, 4371, 5529, 6185]
Massachusetts = [108, 123, 138, 164, 197, 218, 256, 328, 413, 525, 646, 777, 1159, 1838, 2417, 3240, 4257, 4955, 5752, 6620]
Michigan = [334, 549, 787, 1035, 1328, 1791, 2295, 2856, 3657, 4650, 5486, 6498, 7615, 9334, 10791, 12744, 14225, 15718, 17221, 18970, 20346]
Minnesota = [115, 137, 169, 235, 262, 287, 346, 398, 441, 503, 576, 629, 689, 742, 789, 865, 935, 986, 1069, 1154]
Mississippi = [140, 207, 249, 320, 377, 485, 579, 663, 758, 847, 937, 1073, 1177, 1358, 1455, 1638, 1738]
Missouri = [183, 255, 356, 502, 670, 838, 903, 1031, 1327, 1581, 1834, 2113, 2291, 2367]
Montana = [108, 147]
Nebraska = [113, 133, 149, 177, 215, 268, 292, 327, 370, 429]
Nevada = [101, 109, 124, 154, 190, 278, 321, 420, 535, 621, 738, 996, 1113, 1279, 1458, 1514, 1742, 1836, 1953]
New_Hampshire = [101, 108, 137, 158, 187, 214, 258, 314, 367, 415, 479, 540, 621, 669]
New_Jersey = [178, 267, 427, 742, 890, 1327, 1914, 2844, 3675, 4402, 6876, 8825, 11124, 13866, 16636, 18696, 22259, 25590, 29895, 34124, 37505]
New_Mexico = [100, 112, 136, 191, 208, 237, 281, 315, 363, 403, 495, 546, 627]
New_York = [105, 142, 173, 216, 325, 421, 613, 729, 950, 1374, 2382, 4152, 7102, 10356, 15168, 20875, 25665, 30811, 37258, 44635, 52318, 59513, 66497, 75795, 83712, 92381, 102863, 113704, 122031, 130689]
North_Carolina = [137, 184, 255, 297, 398, 504, 636, 763, 935, 1167, 1307, 1498, 1584, 1857, 2093, 2402]
North_Dakota = [109, 126, 147, 159, 173, 186, 207, 225, 237, 251]
Ohio = [119, 169, 247, 351, 442, 564, 704, 867, 1137, 1406, 1653, 1933, 2199, 2547, 2902, 3312, 3739, 4043, 4450]
Oklahoma = [106, 164, 248, 322, 377, 429, 481, 565, 719, 879, 988, 1159, 1252, 1327]
Oregon = [114, 137, 161, 191, 209, 266, 316, 414, 479, 548, 606, 690, 736, 826, 899, 999, 1068]
Pennsylvania = [133, 185, 268, 371, 479, 644, 851, 1127, 1687, 2218, 2751, 3394, 4087, 4843, 5805, 7016, 8420, 10017, 11510]
Rhode_Island = [106, 132, 165, 203, 239, 295, 408, 488, 566, 657, 711, 806, 902, 1082]
South_Carolina = [125, 173, 195, 298, 342, 424, 456, 539, 660, 774, 925, 1083, 1293, 1554, 1700, 1917, 2049]
South_Dakota = [108, 165, 212, 240, 288]
Tennessee = [154, 228, 371, 505, 615, 667, 784, 957, 1203, 1373, 1537, 1834, 2239, 2683, 2845, 3067, 3321, 3633]
Texas = [143, 194, 304, 334, 352, 715, 974, 1396, 1731, 2052, 2552, 2877, 3266, 3997, 4669, 5330, 6110, 6812]
Utah = [112, 136, 181, 257, 298, 346, 402, 480, 602, 719, 806, 886, 1012, 1074, 1246, 1428, 1605, 1675]
Vermont = [123, 158, 184, 221, 235, 256, 293, 321, 338, 389, 461, 512, 543]
Virginia = [114, 152, 220, 254, 290, 391, 460, 615, 739, 890, 1020, 1259, 1484, 1706, 2012, 2407, 2637, 2878]
Washington = [102, 136, 162, 267, 366, 457, 568, 642, 769, 904, 1012, 1187, 1376, 1524, 1793, 1996, 2221, 2469, 2580, 3207, 3723, 4310, 5062, 5515, 5984, 6585, 6966, 7591, 7984]
West_Virginia = [113, 124, 145, 162, 191, 217, 227, 282, 324, 345]
Wisconsin = [106, 155, 206, 281, 381, 416, 457, 585, 707, 842, 989, 1112, 1221, 1351, 1550, 1730, 1916, 2112, 2267]
Wyoming = [137, 153, 187]


def convert_cases_to_ratio(number_of_cases, population):
    if type(number_of_cases) == int:
        return number_of_cases / population

    for i in range(len(number_of_cases)):
        number_of_cases[i] = number_of_cases[i] / population
    return number_of_cases


def get_prediction(A_matrix, b_vector, data_to_predict_with, state_name, population, nth_day, actual_number):
    # Ax = b
    # x = ((A^t)(A))^-1 * A^t * b

    AtA = ((A_matrix).transpose()).dot(A_matrix)
    AtA_inverse = numpy.linalg.inv(AtA)
    x_vector = (AtA_inverse.dot(A_matrix.transpose())).dot(b_vector)
    print("x_vector: ")
    print(x_vector)

    prediction_ratio = data_to_predict_with.dot(x_vector)
    prediction_number = prediction_ratio * population

    if actual_number == -1:
        print("Prediction of number of Corona cases in " + state_name + " on " + str(nth_day) + "th day after exceeding 100:", prediction_number, "Actual number: ", actual_number)
    else:
        print("Prediction of number of Corona cases in " + state_name + " on " + str(nth_day) + "th day after exceeding 100:", prediction_number)

# first we do a prediction for michigan. we will grab 9 days worth of data and try to predict the number of cases on the
# 10th day using the data from all 44 states (all states excluding Michigan, Alaska, Montana, South Dakota and Wyoming)

michigan_vector = numpy.array(convert_cases_to_ratio(Michigan[:9], MICHIGAN_POPULATION))

A_matrix = numpy.array([
    convert_cases_to_ratio(Alabama[:9], ALABAMA_POPULATION),
    convert_cases_to_ratio(Arizona[:9], ARIZONA_POPULATION),
    convert_cases_to_ratio(Arkansas[:9], ARKANSAS_POPULATION),
    convert_cases_to_ratio(California[:9], CALIFORNIA_POPULATION),
    convert_cases_to_ratio(Colorado[:9], COLORADO_POPULATION),
    convert_cases_to_ratio(Connecticut[:9], CONNECTICUT_POPULATION),
    convert_cases_to_ratio(Delaware[:9], DELAWARE_POPULATION),
    convert_cases_to_ratio(Florida[:9], FLORIDA_POPULATION),
    convert_cases_to_ratio(Georgia[:9], GEORGIA_POPULATION),
    convert_cases_to_ratio(Hawaii[:9], HAWAII_POPULATION),
    convert_cases_to_ratio(Idaho[:9], IDAHO_POPULATION),
    convert_cases_to_ratio(Illinois[:9], ILLINOIS_POPULATION),
    convert_cases_to_ratio(Indiana[:9], INDIANA_POPULATION),
    convert_cases_to_ratio(Iowa[:9], IOWA_POPULATION),
    convert_cases_to_ratio(Kansas[:9], KANSAS_POPULATION),
    convert_cases_to_ratio(Kentucky[:9], KENTUCKY_POPULATION),
    convert_cases_to_ratio(Louisiana[:9], LOUISIANA_POPULATION),
    convert_cases_to_ratio(Maine[:9], MAINE_POPULATION),
    convert_cases_to_ratio(Maryland[:9], MARYLAND_POPULATION),
    convert_cases_to_ratio(Massachusetts[:9], MASSACHUSETTS_POPULATION),
    convert_cases_to_ratio(Minnesota[:9], MINNESOTA_POPULATION),
    convert_cases_to_ratio(Mississippi[:9], MISSISSIPPI_POPULATION),
    convert_cases_to_ratio(Missouri[:9], MISSOURI_POPULATION),
    convert_cases_to_ratio(Nebraska[:9], NEBRASKA_POPULATION),
    convert_cases_to_ratio(Nevada[:9], NEVADA_POPULATION),
    convert_cases_to_ratio(New_Hampshire[:9], NEW_HAMPSHIRE_POPULATION),
    convert_cases_to_ratio(New_Jersey[:9], NEW_JERSEY_POPULATION),
    convert_cases_to_ratio(New_Mexico[:9], NEW_MEXICO_POPULATION),
    convert_cases_to_ratio(New_York[:9], NEW_YORK_POPULATION),
    convert_cases_to_ratio(North_Carolina[:9], NORTH_CAROLINA_POPULATION),
    convert_cases_to_ratio(North_Dakota[:9], NORTH_DAKOTA_POPULATION),
    convert_cases_to_ratio(Ohio[:9], OHIO_POPULATION),
    convert_cases_to_ratio(Oklahoma[:9], OKLAHOMA_POPULATION),
    convert_cases_to_ratio(Oregon[:9], OREGON_POPULATION),
    convert_cases_to_ratio(Pennsylvania[:9], PENNSYLVANIA_POPULATION),
    convert_cases_to_ratio(Rhode_Island[:9], RHODE_ISLAND_POPULATION),
    convert_cases_to_ratio(South_Carolina[:9], SOUTH_CAROLINA_POPULATION),
    convert_cases_to_ratio(Tennessee[:9], TENNESSEE_POPULATION),
    convert_cases_to_ratio(Texas[:9], TEXAS_POPULATION),
    convert_cases_to_ratio(Utah[:9], UTAH_POPULATION),
    convert_cases_to_ratio(Vermont[:9], VERMONT_POPULATION),
    convert_cases_to_ratio(Virginia[:9], VIRGINIA_POPULATION),
    convert_cases_to_ratio(Washington[:9], WASHINGTON_POPULATION),
    convert_cases_to_ratio(West_Virginia[:9], WEST_VIRGINIA_POPULATION),
    convert_cases_to_ratio(Wisconsin[:9], WISCONSIN_POPULATION)])

b_vector = numpy.array([
    convert_cases_to_ratio(Alabama[9], ALABAMA_POPULATION),
    convert_cases_to_ratio(Arizona[9], ARIZONA_POPULATION),
    convert_cases_to_ratio(Arkansas[9], ARKANSAS_POPULATION),
    convert_cases_to_ratio(California[9], CALIFORNIA_POPULATION),
    convert_cases_to_ratio(Colorado[9], COLORADO_POPULATION),
    convert_cases_to_ratio(Connecticut[9], CONNECTICUT_POPULATION),
    convert_cases_to_ratio(Delaware[9], DELAWARE_POPULATION),
    convert_cases_to_ratio(Florida[9], FLORIDA_POPULATION),
    convert_cases_to_ratio(Georgia[9], GEORGIA_POPULATION),
    convert_cases_to_ratio(Hawaii[9], HAWAII_POPULATION),
    convert_cases_to_ratio(Idaho[9], IDAHO_POPULATION),
    convert_cases_to_ratio(Illinois[9], ILLINOIS_POPULATION),
    convert_cases_to_ratio(Indiana[9], INDIANA_POPULATION),
    convert_cases_to_ratio(Iowa[9], IOWA_POPULATION),
    convert_cases_to_ratio(Kansas[9], KANSAS_POPULATION),
    convert_cases_to_ratio(Kentucky[9], KENTUCKY_POPULATION),
    convert_cases_to_ratio(Louisiana[9], LOUISIANA_POPULATION),
    convert_cases_to_ratio(Maine[9], MAINE_POPULATION),
    convert_cases_to_ratio(Maryland[9], MARYLAND_POPULATION),
    convert_cases_to_ratio(Massachusetts[9], MASSACHUSETTS_POPULATION),
    convert_cases_to_ratio(Minnesota[9], MINNESOTA_POPULATION),
    convert_cases_to_ratio(Mississippi[9], MISSISSIPPI_POPULATION),
    convert_cases_to_ratio(Missouri[9], MISSOURI_POPULATION),
    convert_cases_to_ratio(Nebraska[9], NEBRASKA_POPULATION),
    convert_cases_to_ratio(Nevada[9], NEVADA_POPULATION),
    convert_cases_to_ratio(New_Hampshire[9], NEW_HAMPSHIRE_POPULATION),
    convert_cases_to_ratio(New_Jersey[9], NEW_JERSEY_POPULATION),
    convert_cases_to_ratio(New_Mexico[9], NEW_MEXICO_POPULATION),
    convert_cases_to_ratio(New_York[9], NEW_YORK_POPULATION),
    convert_cases_to_ratio(North_Carolina[9], NORTH_CAROLINA_POPULATION),
    convert_cases_to_ratio(North_Dakota[9], NORTH_DAKOTA_POPULATION),
    convert_cases_to_ratio(Ohio[9], OHIO_POPULATION),
    convert_cases_to_ratio(Oklahoma[9], OKLAHOMA_POPULATION),
    convert_cases_to_ratio(Oregon[9], OREGON_POPULATION),
    convert_cases_to_ratio(Pennsylvania[9], PENNSYLVANIA_POPULATION),
    convert_cases_to_ratio(Rhode_Island[9], RHODE_ISLAND_POPULATION),
    convert_cases_to_ratio(South_Carolina[9], SOUTH_CAROLINA_POPULATION),
    convert_cases_to_ratio(Tennessee[9], TENNESSEE_POPULATION),
    convert_cases_to_ratio(Texas[9], TEXAS_POPULATION),
    convert_cases_to_ratio(Utah[9], UTAH_POPULATION),
    convert_cases_to_ratio(Vermont[9], VERMONT_POPULATION),
    convert_cases_to_ratio(Virginia[9], VIRGINIA_POPULATION),
    convert_cases_to_ratio(Washington[9], WASHINGTON_POPULATION),
    convert_cases_to_ratio(West_Virginia[9], WEST_VIRGINIA_POPULATION),
    convert_cases_to_ratio(Wisconsin[9], WISCONSIN_POPULATION)])

get_prediction(A_matrix, b_vector, michigan_vector, "Michigan", MICHIGAN_POPULATION, 10, Michigan[9])

# then we do predictions for states that have very little amount of data: Alaska, Montana, South Dakota and wyoming.

# Alaska: get prediction for 10th day
Alaskan_vector = numpy.array(convert_cases_to_ratio(Alaska[:9], MICHIGAN_POPULATION))
