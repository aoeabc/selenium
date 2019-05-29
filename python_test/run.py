import unittest

def disc():
    discover= unittest.defaultTestLoader.discover('./scripts/',pattern='*test.py')
    print(discover.countTestCases())

    run = unittest.TextTestRunner(verbosity=2)
    run.run(discover)

if __name__ == '__main__':
    disc()