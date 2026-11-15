import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import uncensored
from uncensored import api_config


class ConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.saved_key = uncensored.api_key
        self.saved_url = uncensored.base_url
        self.addCleanup(setattr, uncensored, 'api_key', self.saved_key)
        self.addCleanup(setattr, uncensored, 'base_url', self.saved_url)
        self.environment = patch.dict(os.environ)
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.config_dir = Path(self.temp.name) / 'uncensored'
        for name, value in [('_CONFIG_DIR', self.config_dir),
                            ('_CONFIG_FILE', self.config_dir / 'config.json')]:
            p = patch.object(api_config, name, value)
            p.start()
            self.addCleanup(p.stop)

    def test_set_base_url_updates_exported_configuration(self):
        uncensored.set_base_url('https://example.invalid/v1')
        self.assertEqual(uncensored.base_url, 'https://example.invalid/v1')
        self.assertEqual(uncensored.get_base_url(), 'https://example.invalid/v1')
        client = uncensored.Client(api_key='test-key')
        self.assertEqual(client.base_url, 'https://example.invalid/v1')

    def test_set_api_key_replaces_previous_global_key(self):
        uncensored.api_key = 'old-key'
        uncensored.set_api_key('new-key')
        self.assertEqual(uncensored.api_key, 'new-key')
        self.assertEqual(uncensored.get_api_key(), 'new-key')
        self.assertEqual(uncensored.Client().api_key, 'new-key')

    def test_key_persists_and_environment_is_updated(self):
        uncensored.api_key = None
        uncensored.set_api_key('new-key')
        self.assertEqual(os.environ['UNCENSORED_API_KEY'], 'new-key')
        uncensored.api_key = None
        del os.environ['UNCENSORED_API_KEY']
        self.assertEqual(uncensored.get_api_key(), 'new-key')

    def test_global_key_still_has_priority(self):
        uncensored.api_key = 'direct-key'
        os.environ['UNCENSORED_API_KEY'] = 'env-key'
        self.assertEqual(uncensored.get_api_key(), 'direct-key')


if __name__ == '__main__':
    unittest.main()
