"""datacost.py : Cost-Sensitive Data Measures

This module can be used to calculate various cost-sensitive measurements.
It is mainly intended for use in machine learning algorithms.

"""
import math

def cost_labelling_positive(num_positive, num_negative, cost_matrix):
  """Used to calculate the cost of labelling every data point as positive.

  Args:
    num_positive (int): The number of positive data points.
    num_negative (int): The number of negative data points.
    cost_matrix (dict): Every cost. e.g., {'TP':1, 'TN':0, 'FP':1, 'FN':5}

  Returns:
    (num): The cost of labelling every data point as positive.

  Raises:
    TypeError: If an incorrect number of arguments are passed.
    KeyError: If the passed cost_matrix is missing a cost.

  """
  if len(locals()) < 3:
    raise TypeError('Too few arguments.')
  elif len(locals()) > 3:
    raise TypeError('Too many arguments.')

  if any(k not in cost_matrix for k in ('TP', 'TN', 'FP', 'FN')):
    raise KeyError('A cost is missing from the passed cost matrix.')

  return num_positive * cost_matrix['TP'] + num_negative * cost_matrix['FP']

def cost_labelling_negative(num_positive, num_negative, cost_matrix):
  """Used to calculate the cost of labelling every data point as negative.

  Args:
    num_positive (int): The number of positive data points.
    num_negative (int): The number of negative data points.
    cost_matrix (dict): Every cost. e.g., {'TP':1, 'TN':0, 'FP':1, 'FN':5}

  Returns:
    (num): The cost of labelling every data point as negative.

  Raises:
    TypeError: If an incorrect number of arguments are passed.
    KeyError: If the passed cost_matrix is missing a cost.

  """
  if len(locals()) < 3:
    raise TypeError('Too few arguments.')
  elif len(locals()) > 3:
    raise TypeError('Too many arguments.')

  if any(k not in cost_matrix for k in ('TP', 'TN', 'FP', 'FN')):
    raise KeyError('A cost is missing from the passed cost matrix.')

  return num_negative * cost_matrix['TN'] + num_positive * cost_matrix['FN']
