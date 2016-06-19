from mofu import Mofu

import unittest

class TestMofu(unittest.TestCase):
    def test_say(self):
        m = Mofu()
        self.assertEqual('mofu', m.say())

    def test_sing(self):
        m = Mofu()
        self.assertEqual('mofu mofu', m.sing())

if __name__ == '__main__':
    unittest.main()
