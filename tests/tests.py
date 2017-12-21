def dictn(keys, values):
    try:
        if type(keys) and type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result


print(dictn([1,2,3],['a','b','c','d']))


if __name__ == '__main__':
    import unittest

    class TestFactorialMethods(unittest.TestCase):
        def test_list(self):
            self.assertEqual(dictn([1,2,3],['a','b','c']),{1: 'a', 2: 'b', 3: 'c'})
            self.assertEqual(dictn([1,2,3,4],['a','b','c']),{1: 'a', 2: 'b', 3: 'c', 4: None})

        def test_float(self):
            self.assertTrue(dictn(1,1) is None)
            self.assertTrue(dictn(2,[2]) is None)

        def test_bool(self):
            self.assertIsNone(dictn(False,True), None)

        def test_negative(self):
            self.assertEqual(dictn(-1,-2), None)
            self.assertEqual(dictn(-10,-100), None)

        def test_iter(self):
            self.assertIs(dictn('bad','good'), None )

    unittest.main(verbosity=2)
