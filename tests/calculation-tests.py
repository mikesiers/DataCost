import sys
sys.path.append('../')
from src.datacost import cost_labelling_positive, cost_labelling_negative,\
  expected_cost, expected_cost_after_split
import unittest

class test_calculations(unittest.TestCase):

  # Initialize a cost matrix which can be used in testing.
  cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1, 'FN' : 5}

  def test_cost_labelling_positive(self):
    # Test that if <3 or >3 arguments are passed, a TypeError is raised.
    with self.assertRaises(TypeError):
      cost_labelling_positive(2, 3)
      cost_labelling_positive(2, 3, 7, self.cost_matrix)
    # Test a simple case with 2 positive and 3 negative data points.
    self.assertEqual(cost_labelling_positive(2, 3, self.cost_matrix), 5)
    # Test that a KeyError is raised when the passed cost_matrix doesn't
    # contain the required costs.
    with self.assertRaises(KeyError):
      bad_cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1}
      cost_labelling_positive(2, 3, bad_cost_matrix)

  def test_cost_labelling_negative(self):
    # Test that if <3 or >3 arguments are passed, a TypeError is raised.
    with self.assertRaises(TypeError):
      cost_labelling_negative(2, 3)
      cost_labelling_negative(2, 3, 7, self.cost_matrix)
    # Test a simple case with 2 positive and 3 negative data points.
    self.assertEqual(cost_labelling_negative(2, 3, self.cost_matrix), 10)
    # Test that a KeyError is raised when the passed cost_matrix doesn't
    # contain the required costs.
    with self.assertRaises(KeyError):
      bad_cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1}
      cost_labelling_negative(2, 3, bad_cost_matrix)

  def test_expected_cost(self):
    # Test that if <3 or >3 arguments are passed, a TypeError is raised.
    with self.assertRaises(TypeError):
      expected_cost(2, 3)
      expected_cost(2, 3, 7, self.cost_matrix)
    # Test a simple case with 2 positive and 3 negative data points.
    cost = expected_cost(2, 3, self.cost_matrix)
    self.assertEqual(round(cost, 5), 6.66667)
    # Test that a KeyError is raised when the passed cost_matrix doesn't
    # contain the required costs.
    with self.assertRaises(KeyError):
      bad_cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1}
      expected_cost(2, 3, bad_cost_matrix)

  def test_expected_cost_after_split(self):
    # Test that if <2 or >2 arguments are passed, a TypeError is raised.
    with self.assertRaises(TypeError):
      expected_cost_after_split('one')
      expected_cost_after_split('one', 'two', 'three')
    # Test a simple case with 2 splits. The first split has 2 positive, and 3
    # negative. The second split has 4 positive and 6 negative.
    class_supports = [{'positive' : 2, 'negative' : 3,},\
      {'positive' : 4, 'negative': 6}]
    cost = expected_cost_after_split(class_supports, self.cost_matrix)
    self.assertEqual(round(cost, 5), 20.00000)
    # Test that a KeyError is raised when the passed cost_matrix doesn't
    # contain the required costs.
    with self.assertRaises(KeyError):
      bad_cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1}
      expected_cost_after_split([{'positive' : 4, 'negative' : 3}],\
        bad_cost_matrix)
    # Test that a KeyError is raised when the passed class supports don't
    # contain the required classes ('positive', and 'negative').
    with self.assertRaises(KeyError):
      bad_class_supports = [{'positive' : 4, 'negative' : 3},\
        {'Y' : 3, 'N' : 1}]
      expected_cost_after_split(class_supports, bad_cost_matrix)

if __name__ == '__main__':
    unittest.main(exit=False)
