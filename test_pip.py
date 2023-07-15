import unittest
import tempfile
import os
import shutil
from datetime import datetime

from DataStructuresAPI import Pipeline

class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.base_dir = tempfile.mkdtemp()
        self.pipeline = Pipeline(self.base_dir)

    def tearDown(self):
        shutil.rmtree(self.base_dir)

    def test_create_show(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')

        show_dir = os.path.join(self.base_dir, 'shows', 'Demo Reel')
        self.assertTrue(os.path.exists(show_dir))
        
        metadata_file = os.path.join(show_dir, 'metadata.json')
        self.assertTrue(os.path.exists(metadata_file))

        metadata = self.pipeline.file_handler.read_json_file(metadata_file)
        self.assertEqual(metadata['title'], 'Demo Reel')
        self.assertEqual(metadata['description'], 'My Reel')
        self.assertEqual(metadata['release_date'], '2023-08-01')
        self.assertEqual(metadata['duration'], '1 minute')

    def test_create_shot(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')
        self.pipeline.create_shot('Demo Reel', 'Shot1010', 'The opening sequence', '100 frames', 'In progress')

        shot_dir = os.path.join(self.base_dir, 'shows', 'Demo Reel', 'shots', 'Shot1010')
        self.assertTrue(os.path.exists(shot_dir))

        metadata_file = os.path.join(shot_dir, 'metadata.json')
        self.assertTrue(os.path.exists(metadata_file))

        metadata = self.pipeline.file_handler.read_json_file(metadata_file)
        self.assertEqual(metadata['title'], 'Shot1010')
        self.assertEqual(metadata['description'], 'The opening sequence')
        self.assertEqual(metadata['duration'], '100 frames')
        self.assertEqual(metadata['status'], 'In progress')

    def test_get_show(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')

        show = self.pipeline.get_show('Demo Reel')

        self.assertEqual(show.title, 'Demo Reel')
        self.assertEqual(show.description, 'My Reel')
        self.assertEqual(show.release_date, '2023-08-01')
        self.assertEqual(show.duration, '1 minute')

    def test_get_shot(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')
        self.pipeline.create_shot('Demo Reel', 'Shot1010', 'The opening sequence', '100 frames', 'In progress')

        shot = self.pipeline.get_shot('Demo Reel', 'Shot1010')

        self.assertEqual(shot.title, 'Shot1010')
        self.assertEqual(shot.description, 'The opening sequence')
        self.assertEqual(shot.duration, '100 frames')
        self.assertEqual(shot.status, 'In progress')

    def test_update_show(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')

        self.pipeline.update_show('Demo Reel', description='My Reel')

        show = self.pipeline.get_show('Demo Reel')
        self.assertEqual(show.description, 'My Reel')

    def test_update_shot(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')
        self.pipeline.create_shot('Demo Reel', 'Shot1010', 'The opening sequence', '100 frames', 'In progress')

        self.pipeline.update_shot('Demo Reel', 'Shot1010', status='Completed')

        shot = self.pipeline.get_shot('Demo Reel', 'Shot1010')
        self.assertEqual(shot.status, 'Completed')

    def test_delete_show(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')

        self.pipeline.delete_show('Demo Reel')

        show_dir = os.path.join(self.base_dir, 'shows', 'Demo Reel')
        self.assertFalse(os.path.exists(show_dir))

    def test_delete_shot(self):
        self.pipeline.create_show('Demo Reel', 'My Reel', '2023-08-01', '1 minute')
        self.pipeline.create_shot('Demo Reel', 'Shot1010', 'The opening sequence', '100 frames', 'In progress')

        self.pipeline.delete_shot('Demo Reel', 'Shot1010')

        shot_dir = os.path.join(self.base_dir, 'shows', 'Demo Reel', 'shots', 'Shot1010')
        self.assertFalse(os.path.exists(shot_dir))

if __name__ == '__main__':
    unittest.main()
