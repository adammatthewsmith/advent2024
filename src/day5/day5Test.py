import unittest
from .day5 import updateAnsestors, Node

class Day4UnitTest(unittest.TestCase):
    def testTwoLinearNodes(self):
        node1 = Node("1")
        node2 = Node("2")

        node2.parents.append(node1);

        input = [node1, node2]
        updateAnsestors(input)

        self.assertEqual(len(node2.ancestorSet), 1)
        self.assertTrue("1" in node2.ancestorSet)

    def testThreeLinearNodes(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")

        node2.parents.append(node1)
        node3.parents.append(node2)

        input = [node1, node2, node3]
        updateAnsestors(input)

        self.assertEqual(len(node2.ancestorSet), 1)
        self.assertTrue("1" in node2.ancestorSet)

        self.assertEqual(len(node3.ancestorSet), 2)
        self.assertTrue("1" in node3.ancestorSet)
        self.assertTrue("2" in node3.ancestorSet)

    def testThreeLinearNodesReverseOrder(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")

        node2.parents.append(node1)
        node3.parents.append(node2)

        input = [node3, node2, node1]
        updateAnsestors(input)

        self.assertEqual(len(node2.ancestorSet), 1)
        self.assertTrue("1" in node2.ancestorSet)

        self.assertEqual(len(node3.ancestorSet), 2)
        self.assertTrue("1" in node3.ancestorSet)
        self.assertTrue("2" in node3.ancestorSet)


    def testThreeTriangleNodes(self):
        node1 = Node("1")
        node2 = Node("2")
        node3 = Node("3")

        node2.parents.append(node1)
        node3.parents.append(node1)

        input = [node1, node2, node3]
        updateAnsestors(input)

        self.assertEqual(len(node2.ancestorSet), 1)
        self.assertTrue("1" in node2.ancestorSet)

        self.assertEqual(len(node3.ancestorSet), 1)
        self.assertTrue("1" in node3.ancestorSet)


