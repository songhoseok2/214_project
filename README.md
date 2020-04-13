# 214_project

This is the python script for the prediction of the number of COVID-19 cases in Alaska, Montana, South Dakota and Wyoming after n day has passed since exceeding 100 in number.

## Process

We first make an array of the ratio of the patients to the state's population.
```python
onvert_cases_to_ratio(Alabama[:n], ALABAMA_POPULATION),
        convert_cases_to_ratio(Arizona[:n], ARIZONA_POPULATION),
        .
        .
        .
        convert_cases_to_ratio(West_Virginia[:n], WEST_VIRGINIA_POPULATION),
        convert_cases_to_ratio(Wisconsin[:n], WISCONSIN_POPULATION)]
```

Then we use these data to make a prediction of the number of cases in Michigan on the 10th day after exceeding 100, to test for the accuracy of this script.
```
michigan_vector = numpy.array(convert_cases_to_ratio(Michigan[:9], MICHIGAN_POPULATION))
A_matrix = numpy.array(get_nth_day_worth_of_data(9))
b_vector = numpy.array(get_nth_days_data(10))
get_prediction(A_matrix, b_vector, michigan_vector, "Michigan", MICHIGAN_POPULATION, 10, Michigan[9])
```


## get_prediction

get_prediction is the function that calculates the least square solution (x*) according to the Theorem 5.4.6 in the textbook.
![image failed to load](https://github.com/songhoseok2/214_project/blob/master/Annotation%202020-04-13%20151014.png)

the function calculates the predicted ratio of the COVID-19 pateients to the total population of the state, and computes the raw number of the patients by multiplying the ratio to the provided population.

```
AtA = ((A_matrix).transpose()).dot(A_matrix)
    AtA_inverse = numpy.linalg.inv(AtA)
    x_vector = (AtA_inverse.dot(A_matrix.transpose())).dot(b_vector)
    print("x_vector: ")
    print(x_vector)

    prediction_ratio = data_to_predict_with.dot(x_vector)
    prediction_number = prediction_ratio * population
```

after the test for the accuracy, we proceed to the calculation of the predicted number of COVID-19 cases on the 10th, 3rd, 6th and 4th day after the number exceeds 100 for Alaska, Montana, South Dakota and Wyoming repectively by feeding in the appropriate A matrices, b vectors and state populations into the get_prediction functions. The production of the A matrix and the b vector is shown in the codes of the script.



