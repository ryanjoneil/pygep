from pygep.util import cache, memoize
import unittest


class Foo(object):
    '''A dummy class for testing the cache & memoize'''
    x = y = 0

    @cache
    def bar(self):
        Foo.x += 1
        return 'baz'
    
    @memoize
    def baz(self, z):
        Foo.y += 1
        return Foo.y + z


class CacheTest(unittest.TestCase):
    '''Verifies that caching works on an instance level'''
    def testCache(self):
        f = Foo()
        self.assertEqual('baz', f.bar())
        self.assertEqual(1, f.x)
        self.assertEqual('baz', f.bar())
        self.assertEqual(1, f.x)

        f = Foo()
        self.assertEqual('baz', f.bar())
        self.assertEqual(2, f.x)
        self.assertEqual('baz', f.bar())
        self.assertEqual(2, f.x)


    def testMemoize(self):
        f1 = Foo()
        self.assertEqual(2, f1.baz(1))
        self.assertEqual(2, f1.baz(1))
        self.assertEqual(1, f1.y)
        self.assertEqual(2, f1.baz(0))
        self.assertEqual(2, f1.y)
        
        f2 = Foo()
        self.assertEqual(3, f2.baz(0))
        self.assertEqual(3, f2.baz(0))
        
        mn = '_baz_memo'
        self.assertEqual(mn, f2.baz.memo)
        self.assertNotEqual(getattr(f1, mn), getattr(f2, mn))


if __name__ == '__main__':
    unittest.main()

