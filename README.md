# DataCost
Calculate cost-based metrics about binary classification data.

These cost metrics are used at the core of the classification algorithms CSTree, CSForest, BCSForest,
and BCF.

Full documentation available [here]
(http://htmlpreview.github.io/?https://github.com/mikesiers/DataCost/blob/master/docs/datacost.html).

## Quick Guide ##

### Step 1: Installing the Library ###

The library can be downloaded and installed using pip. Enter this at the terminal (Mac/Linux/Unix) or
command prompt (Windows):

```shell
pip install datacost
```

### Step 2: Importing the Library ###

At a Python command line or in a Python script, write this to load the library:

```python
import datacost
```

### Step 3: Defining a Cost-Matrix ###

Cost-matrices in datacost are in the format shown in the code block below. They're a dictionary with the
keys 'TP', 'TN', 'FP', and 'FN'.

```python
cost_matrix = {'TP':1, 'TN':0, 'FP':1, 'FN':5}
```

### Step 4: Calculating a Metric ###

A list of available metrics is available further down in this ReadMe. The following example code
calculates the expected cost for a dataset with 4 positive records, 10 negative records. It uses
the cost_matrix defined in Step 3. It should output approximately 16.47. Try it out!

```python
datacost.expected_cost(4, 10, cost_matrix)
```

## Basic Notation Used in this Readme ##

- *N*<sub>*TN*</sub>: Number of *true negative* predictions.
- *N*<sub>*TP*</sub>: Number of *true positive* predictions.
- *N*<sub>*FN*</sub>: Number of *false negative* predictions.
- *N*<sub>*FP*</sub>: Number of *false positive* predictions.
- *C*<sub>*TN*</sub>: Cost incurred by *true negative* predictions.
- *C*<sub>*TP*</sub>: Cost incurred by *true positive* predictions.
- *C*<sub>*FN*</sub>: Cost incurred by *false negative* predictions.
- *C*<sub>*FP*</sub>: Cost incurred by *false positive* predictions.

## What Can Be Calculated Using datacost:

### Cost of Labelling a Set of Data Points as Either Negative or Positive
The cost incurred by labelling as negative is calculated as:

*C*<sub>*N*</sub> = *N*<sub>*TN*</sub> X *C*<sub>*TN*</sub> +
*N*<sub>*FN*</sub> X *C*<sub>*FN*</sub>

The cost incurred by labelling as positive is calculated as:

*C*<sub>*P*</sub> = *N*<sub>*TP*</sub> X *C*<sub>*TP*</sub> +
*N*<sub>*FP*</sub> X *C*<sub>*FP*</sub>

### Expected Cost
The expected cost is typically a representation of how much a set of data
points can be expected to cost a business. It is represented by the symbol *E*.
The equation for *E* is as follows:

![Expected Cost](https://raw.githubusercontent.com/mikesiers/DataCost/master/readmeImg/ExpectedCost.gif)

### Expected Cost After Split
After a split, a set of data points has several new sets of class supports, one
for each split. The expected cost difference can be calculated as the
difference between *E* for the original dataset, and the summed *E* over all
splits. The equation for expected cost after a split is as follows:

![Expected Cost After Split](https://raw.githubusercontent.com/mikesiers/DataCost/master/readmeImg/ExpectedCostAfterSplit.gif)

Where *k* is the number of splits, C<sub>P</sub><sup>i</sup> is the value of
C<sub>P</sub> for the *i*'th split.

### Expected Cost Per Record
The expected cost per data point is simply the expected cost for a dataset
divided by the number of data points in the dataset. It is a way of normalizing
expected cost such that logical comparisons may be made between the expected
cost of two datasets of different size.

![Expected Cost Per Data Point](https://raw.githubusercontent.com/mikesiers/DataCost/master/readmeImg/ExpectedCostPerDataPoint.gif)

Where |*D*| is the number of records in the dataset *D*. 

### Total Cost ###
The total cost for a set of records is calculated as either *C*<sub>*N*</sub>
or *C*<sub>*P*</sub>, whichever is lowest.

*C*<sub>T</sub> = min(*C*<sub>*N*</sub>, *C*<sub>*P*</sub>)
