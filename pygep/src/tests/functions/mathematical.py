from pygep.functions.mathematical import arithmetic
from pygep.functions.mathematical import comparison
from pygep.functions.mathematical import constants
from pygep.functions.mathematical import hyperbolic
from pygep.functions.mathematical import power
from pygep.functions.mathematical import rounding
from pygep.functions.mathematical import trigonometry
import math, unittest


class MathNonterminalTest(unittest.TestCase):
    '''Tests the mathematical non-terminals'''
    def testArithmetic(self):
        self.assertEqual(5,  arithmetic.add_op(2, 3))
        self.assertEqual(-5, arithmetic.subtract_op(5, 10))
        self.assertEqual(10, arithmetic.multiply_op(2, 5))
        self.assertEqual(2,  arithmetic.divide_op(4, 2))
        self.assertEqual(5,  arithmetic.modulus_op(15, 10))


    def testComparison(self):
        self.assertEqual(1, comparison.equal_op(1, 1))
        self.assertEqual(2, comparison.equal_op(1, 2))
        self.assertEqual(1, comparison.unequal_op(1, 2))
        self.assertEqual(2, comparison.unequal_op(2, 2))
        self.assertEqual(1, comparison.less_op(1, 2))
        self.assertEqual(2, comparison.less_op(3, 2))
        self.assertEqual(2, comparison.greater_op(1, 2))
        self.assertEqual(3, comparison.greater_op(3, 2))
        self.assertEqual(1, comparison.less_or_equal_op(1,2))
        self.assertEqual(1, comparison.less_or_equal_op(1,1))
        self.assertEqual(2, comparison.less_or_equal_op(3,2))
        self.assertEqual(2, comparison.greater_or_equal_op(2,1))
        self.assertEqual(2, comparison.greater_or_equal_op(2,2))
        self.assertEqual(3, comparison.greater_or_equal_op(2,3))


    def testConstants(self):
        self.assertEqual(0, constants.zero_op())
        self.assertEqual(1, constants.one_op())
        self.assertEqual(math.pi, constants.pi_op())
        self.assertEqual(math.e, constants.e_op())
        
    
    def testHyperbolic(self):
        self.assertEqual(math.sinh(5), hyperbolic.sineh_op(5))
        self.assertEqual(math.cosh(5), hyperbolic.cosineh_op(5))
        self.assertEqual(math.tanh(5), hyperbolic.tangenth_op(5))
        self.assertEqual(1. / math.sinh(5), hyperbolic.cosecanth_op(5))
        self.assertEqual(1. / math.cosh(5), hyperbolic.secanth_op(5))
        self.assertEqual(1. / math.tanh(5), hyperbolic.cotangenth_op(5))
    

    def testPower(self):
        self.assertEqual(math.log(5), power.ln_op(5))
        self.assertEqual(math.log10(5), power.log10_op(5))
        self.assertEqual(8, power.power_op(2,3))
        self.assertEqual(math.exp(2), power.exp_op(2))
        self.assertEqual(10 ** 2, power.pow10_op(2))
        self.assertEqual(10 ** 2, power.square_op(10))
        self.assertEqual(10 ** 3, power.cube_op(10))
        self.assertEqual(5, power.root_op(25))
        self.assertEqual(10 ** (1./3), power.cube_root_op(10))
        self.assertEqual(1. / 5, power.inverse_op(5))


    def testRounding(self):
        self.assertEqual(5, rounding.floor_op(5.9))
        self.assertEqual(5, rounding.ceil_op(4.1))
        self.assertEqual(5, rounding.round_op(5.2))
        self.assertEqual(1, rounding.abs_op(-1))


    def testTrigonometry(self):
        self.assertEqual(math.sin(5), trigonometry.sine_op(5))
        self.assertEqual(math.cos(5), trigonometry.cosine_op(5))
        self.assertEqual(math.tan(5), trigonometry.tangent_op(5))
        self.assertEqual(1. / math.sin(5), trigonometry.cosecant_op(5))
        self.assertEqual(1. / math.cos(5), trigonometry.secant_op(5))
        self.assertEqual(1. / math.tan(5), trigonometry.cotangent_op(5))
        self.assertEqual(math.asin(1), trigonometry.arcsine_op(1))
        self.assertEqual(math.acos(1), trigonometry.arccosine_op(1))
        self.assertEqual(math.atan(1), trigonometry.arctangent_op(1))
        self.assertEqual(1. / math.asin(1), trigonometry.arccosecant_op(1))
        self.assertEqual(1. / math.acos(0), trigonometry.arcsecant_op(0))
        self.assertEqual(1. / math.atan(1), trigonometry.arccotangent_op(1))


if __name__ == '__main__':
    unittest.main()
