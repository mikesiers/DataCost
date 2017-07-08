# DataCost
Calculate cost based metrics about data based on the number of positive and negative data points.

These cost metrics are used at the core of the classification algorithms CSTree, CSForest, BCSForest, and BCF.
The functions have been carefully implemented following a TDD style and auto-generated documentation is available in the
documentation folder.

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

*C*<sub>*N*</sub> = *N*<sub>*TN*</sub> X *C*<sub>*TN*</sub> + *N*<sub>*FN*</sub> X *C*<sub>*FN*</sub>

The cost incurred by labelling as positive is calculated as:

*C*<sub>*P*</sub> = *N*<sub>*TP*</sub> X *C*<sub>*TP*</sub> + *N*<sub>*FP*</sub> X *C*<sub>*FP*</sub>

### Expected Cost
The expected cost is typically a representation of how much a set of data points can be expected to cost a business. It is represented by the symbol *E*. The equation for *E* is as follows:

![Expected Cost](https://raw.githubusercontent.com/mikesiers/DataCost.py/master/readmeImg/ExpectedCost.gif)

### Expected Cost After Split
After a split, a set of data points has several new sets of class supports, one for each split. The expected cost difference can be calculated as the difference between *E* for the original dataset, and the summed *E* over all splits. The equation for expected cost after a split is as follows:

![Expected Cost After Split](https://raw.githubusercontent.com/mikesiers/DataCost.py/master/readmeImg/ExpectedCostAfterSplit.gif)

Where *k* is the number of splits, C<sub>P</sub><sup>i</sup> is the value of C<sub>P</sub> for the *i*'th split.

### Expected Cost Per Record
The expected cost per data point is simply the expected cost for a dataset divided by the number of data points in the dataset. It is a way of normalizing expected cost such that logical comparisons may be made between the expected cost of two datasets of different size.

![Expected Cost Per Data Point](https://raw.githubusercontent.com/mikesiers/DataCost.py/master/readmeImg/ExpectedCostPerDataPoint.gif)

Where |*D*| is the number of records in the dataset *D*. 
