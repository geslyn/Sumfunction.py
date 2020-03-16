import unittest

def sum(a,b):
    return a + b

class SumTest(unittest.TestCase):

  def test_func_1(self):
      # Arrange
      a = 20
      b = 20
      # Act
      result = sum(a,b)
      #assert
      self.assertEqual(result, a + b)

if __name__ == '__main__':
    unittest.main()
