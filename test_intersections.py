import unittest

def find_busiest_intersections(intersections):
    """
    Find the intersections with the highest number of vehicles.

    :param intersections: A dictionary where keys are intersection names and values are the number of vehicles.
    :return: A list of intersections with the highest number of vehicles.
    """
    if not intersections:
        return []

    max_vehicles = max(intersections.values())
    busiest_intersections = [intersection for intersection, vehicles in intersections.items() if vehicles == max_vehicles]

    return busiest_intersections

class TestFindBusiestIntersections(unittest.TestCase):

    def test_single_busiest_intersection(self):
        intersections = {'A&B': 10, 'C&D': 20, 'E&F': 15}
        self.assertEqual(find_busiest_intersections(intersections), ['C&D'])

    def test_multiple_busiest_intersections(self):
        intersections = {'A&B': 20, 'C&D': 20, 'E&F': 15}
        self.assertEqual(find_busiest_intersections(intersections), ['A&B', 'C&D'])

    def test_no_intersections(self):
        intersections = {}
        self.assertEqual(find_busiest_intersections(intersections), [])

    def test_all_intersections_with_same_vehicles(self):
        intersections = {'A&B': 10, 'C&D': 10, 'E&F': 10}
        self.assertEqual(find_busiest_intersections(intersections), ['A&B', 'C&D', 'E&F'])

if __name__ == '__main__':
    unittest.main()
