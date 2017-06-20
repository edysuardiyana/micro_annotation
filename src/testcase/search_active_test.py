__author__ = 'ArseneLupin'

import searchActive
import unittest

class search_active_test(unittest.TestCase):

    def search_active_test(self):

        source_list = [[2.0, 0.6, 0.7, 0.8, 1.4, 1.6, 0.9, 1.0 ], [0.5, 0.6, 0.7, 0.8, 1.4, 1.0, 1.9, 1.5 ], [0.5, 0.6, 0.7, 0.8, 1.4, 0.8, 0.9, 1.6 ],
                      [0.5, 2.6, 0.7, 0.8, 1.4, 1.1, 0.9, 1.9 ] ]

        target_list = [[2.0, 0.6, 0.7, 0.8, 1.4, 1.6, 0.9, 1.0, 0 ], [0.5, 0.6, 0.7, 0.8, 1.4, 1.0, 1.9, 1.5, 1], [0.5, 0.6, 0.7, 0.8, 1.4, 0.8, 0.9, 1.6, 0 ],
                      [0.5, 2.6, 0.7, 0.8, 1.4, 1.1, 0.9, 1.9, 0 ] ]

        output = searchActive.activeFeat(source_list)

        for i in range(len(target_list)):
            for j in range(len(target_list[0])):


                self.assertAlmostEqual(target_list[i][j], output[i][j])

