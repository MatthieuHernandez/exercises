import unittest
from Tree import Node

class UnitTestTree(unittest.TestCase):

    def initializeTree(self):
        return Node(["A",
                        ["B",
                            ["D", "E"]
                        ],
                        ["C",
                            ["F",
                                ["G",
                                    ["H", "I",
                                             ["J"]
                                    ]
                                ]
                             ]
                         ]
                     ], 0)
    
    def test_constructor(self):
        tree = self.initializeTree()
        self.assertIsInstance(tree, Node)

    '''def test_ComputeDeep(self):
        tree = self.initializeTree()
        deep = tree.ComputeDeep()
        self.assertEqual(deep, 6)'''


if __name__ == '__main__':
    unittest.main()
