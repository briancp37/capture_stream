import unittest
import tempfile
import os
import yaml
from utils.config_loader import load_config


class TestConfigLoader(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        # Clean up temporary files
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_load_config_with_default_path(self):
        """Test loading config from default config.yaml path"""
        # This test will fail initially since config_loader doesn't exist yet
        config = load_config()
        self.assertIsInstance(config, dict)
        self.assertIn('stream', config)
        self.assertIn('capture', config)
        self.assertIn('paths', config)
    
    def test_load_config_with_custom_path(self):
        """Test loading config from a custom path"""
        # Create a test config file
        test_config = {
            'stream': {'source_type': 'twitch'},
            'capture': {'mode': 'fps'},
            'paths': {'output_dir': '/test/path'}
        }
        
        test_config_path = os.path.join(self.test_dir, 'test_config.yaml')
        with open(test_config_path, 'w') as f:
            yaml.dump(test_config, f)
        
        config = load_config(test_config_path)
        self.assertEqual(config['stream']['source_type'], 'twitch')
        self.assertEqual(config['capture']['mode'], 'fps')
        self.assertEqual(config['paths']['output_dir'], '/test/path')
    
    def test_load_config_file_not_found(self):
        """Test that load_config raises an error when file doesn't exist"""
        non_existent_path = os.path.join(self.test_dir, 'nonexistent.yaml')
        with self.assertRaises(FileNotFoundError):
            load_config(non_existent_path)
    
    def test_load_config_invalid_yaml(self):
        """Test that load_config raises an error for invalid YAML"""
        invalid_yaml_path = os.path.join(self.test_dir, 'invalid.yaml')
        with open(invalid_yaml_path, 'w') as f:
            f.write("invalid: yaml: content: [")
        
        with self.assertRaises(yaml.YAMLError):
            load_config(invalid_yaml_path)
    
    def test_load_actual_config_file(self):
        """Test loading the actual config.yaml file"""
        if os.path.exists('config.yaml'):
            config = load_config('config.yaml')
            self.assertIsInstance(config, dict)
            self.assertIn('stream', config)
            self.assertIn('capture', config)
            self.assertIn('paths', config)
            
            # Test specific values from the actual config
            self.assertEqual(config['stream']['source_type'], 'twitch')
            self.assertEqual(config['capture']['mode'], 'fps')
            self.assertEqual(config['capture']['fps'], 1)
            self.assertEqual(config['paths']['output_dir'], '/mnt/cfb_shared/screenshots')


if __name__ == '__main__':
    unittest.main() 