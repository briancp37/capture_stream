import os
import tempfile
import shutil
import unittest
from utils.path_utils import ensure_dir


class TestPathUtils(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.test_dir)
        
    def test_ensure_dir_existing_directory(self):
        """Test ensure_dir with an existing directory"""
        # Create a directory first
        existing_dir = os.path.join(self.test_dir, "existing")
        os.makedirs(existing_dir)
        
        # Call ensure_dir - should not raise an error
        ensure_dir(existing_dir)
        
        # Directory should still exist
        self.assertTrue(os.path.exists(existing_dir))
        self.assertTrue(os.path.isdir(existing_dir))
        
    def test_ensure_dir_new_directory(self):
        """Test ensure_dir with a new directory"""
        new_dir = os.path.join(self.test_dir, "new_directory")
        
        # Directory should not exist initially
        self.assertFalse(os.path.exists(new_dir))
        
        # Call ensure_dir
        ensure_dir(new_dir)
        
        # Directory should now exist
        self.assertTrue(os.path.exists(new_dir))
        self.assertTrue(os.path.isdir(new_dir))
        
    def test_ensure_dir_nested_directory(self):
        """Test ensure_dir with a nested directory path"""
        nested_dir = os.path.join(self.test_dir, "level1", "level2", "level3")
        
        # Directory should not exist initially
        self.assertFalse(os.path.exists(nested_dir))
        
        # Call ensure_dir
        ensure_dir(nested_dir)
        
        # Directory should now exist
        self.assertTrue(os.path.exists(nested_dir))
        self.assertTrue(os.path.isdir(nested_dir))
        
        # Parent directories should also exist
        parent1 = os.path.join(self.test_dir, "level1")
        parent2 = os.path.join(parent1, "level2")
        self.assertTrue(os.path.exists(parent1))
        self.assertTrue(os.path.exists(parent2))


if __name__ == '__main__':
    unittest.main() 