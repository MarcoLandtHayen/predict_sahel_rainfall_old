# predict_sahel_rainfall
Predict rainfall in the African Sahel region with various machine learning and deep learning methods.
Results are shown separately for each ESM (CESM and FOCI) and lead time (0 / 1 / 3 / 6 months), ordered by mean squared error of predicted vs. true target.

## CESM

### lead 0

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs except PREC_SAHEL, normalized | 0.854   | 0.475   |

### lead 1

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| CNN/fc   | Marco  | all inputs | 0.995   | 0.317   |
| lin. reg.   | Marco  | all inputs, normalized | 1.003   | 0.304   |
| CNN/fc   | Marco  | univariate | 1.064   | 0.192   |

### lead 3

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs, normalized | 1.061   | 0.2   |

### lead 6

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs, normalized | 1.064   | 0.19   |


## FOCI

### lead 0

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs except PREC_SAHEL, normalized | 0.7   | 0.384   |

### lead 1

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs, normalized | 0.776   | 0.234   |

### lead 3

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs, normalized | 0.802   | 0.144   |

### lead 6

| Model       | Author | Description | mse (test)   | correl (test) |
| :---        | :---:  |    :---    |    :---:      |    :---:      |
| lin. reg.   | Marco  | all inputs, normalized | 0.817   | 0.071   |
