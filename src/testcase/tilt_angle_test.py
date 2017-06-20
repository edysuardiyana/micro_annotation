__author__ = 'ArseneLupin'

import unittest
import mytilt

class tiltAngleTest(unittest.TestCase):

    def tilt_test(self):

        ax=[]
        ay=[]
        az=[]

        gx=[]
        gy=[]
        gz=[]

        ax.append(0.9562395161)
        ay.append(0.0913857527)
        az.append(0.0079153226)

        gx.append( -0.3661662395)
        gy.append(-2.5631636763)
        gz.append(-0.7323324789)

        result = mytilt.mytilt(ax, ay, az, gx, gy, gz)
        y_temp_angle = result[0]
        z_temp_angle = result[1]

        y_val = y_temp_angle[0]
        z_val = z_temp_angle[0]

        self.assertAlmostEqual(y_val,0.5465499145640936)
        self.assertAlmostEqual(z_val,0.047210333793581472)

if __name__ == '__main__':
    unittest.main()