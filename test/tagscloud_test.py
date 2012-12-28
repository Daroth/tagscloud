import unittest

import tagscloud

class TagCloudTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_withoutFilter(self):
        """
        Test if all tags are returned with relevant count values.
        """
        pass

    def test_withOneTag(self):
        """
        Test if all tag are returned when it asked to be filtered by one tag.
        """
        self.assertEqual(tagscloud.process_tag_count([{'count': 1}]), [{'count': 1, 'size': 75}])

    def test_withTwoTags(self):
        """
        Same as withOneTag test but with two tags.
        """
        self.assertEqual(tagscloud.process_tag_count([{'count': 1}, {'count': 10}]), [{'count': 1, 'size': 75}, {'count': 10, 'size': 120}])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
