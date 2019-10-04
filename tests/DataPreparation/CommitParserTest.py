import unittest

class CommitParserTest(unittest.TestCase):
    def setUp(self):
        self.commits = [
            ["7c6a067c065deb3ac95bbdc24805d36dc63d3587 36605 - Connection status of digital sensors is shown in sensor pool (#1707)"],
            ["f2727eab8292dfeaf77562af8d5e9b92394389c6 33568 - Command: Move to Rack with autosampler (#1661)"],
            ["dc787f41584a5b7ef7616572c50f416e7fc4b79b 45756 - Define activity to acquire reference spectrum (#1734)"],
            ["09c79ca6ba409db3dd3808e81da3c2fac9dbe619 31713 - Update Lightning Chart Control to latest version 8.3 (#1735)"],
        ]

        self.expected_results = [
            [36605, "Connection status of digital sensors is shown in sensor pool", 1707],
            [33568, "Command: Move to Rack with autosampler", 1661],
            [45756, "Define activity to acquire reference spectrum", 1734],
            [31713, "Update Lightning Chart Control to latest version 8.3", 1735],
            ]

    def test_init_createHistWithProperElements(self):
        for i, x in enumerate(self.commits):

            result = p.Parse(str(x))
            self.assertEqual(result[0], self.expected_results[i][0])
            self.assertEqual(result[1], self.expected_results[i][1])
            self.assertEqual(result[2], self.expected_results[i][2])
