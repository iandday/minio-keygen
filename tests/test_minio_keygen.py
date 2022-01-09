

import minio_keygen.minio_keygen as minio_keygen
import unittest
from minio_keygen.minio_keygen import main
import sys




class TestMinioKeyGen(unittest.TestCase):
    """
    Test the compute_keys function from the minio_keygen library
    """

    def test_compute_keys_integers(self):
        result = minio_keygen.compute_keys(14, 30)
        self.assertEqual(len(result[0]), 19) and self.assertEqual(len(result[1]), 40)
    
    def test_compute_keys_float(self):
        result = minio_keygen.compute_keys(14.5, 30.2)
        self.assertEqual(len(result[0]), 19) and self.assertEqual(len(result[1]), 40)

    def test_compute_keys_key_string(self):
        with self.assertRaises(SystemExit):
                minio_keygen.compute_keys('g', 30)

    def test_compute_keys_token_string(self):
        with self.assertRaises(SystemExit):
                minio_keygen.compute_keys(30, 'z')
    
    def test_main(self):
        sys.argv=['']
        self.assertEqual(main(), None)

        