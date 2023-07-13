import os
import json
import shutil

class Pipeline:
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def create_show(self, title, description, release_date, duration):
        show_dir = os.path.join(self.base_dir, 'shows', title)
        os.makedirs(show_dir, exist_ok=True)
        show_metadata = {
            'title': title,
            'description': description,
            'release_date': release_date,
            'duration': duration,
            'shots': []
        }
        with open(os.path.join(show_dir, 'metadata.json'), 'w') as f:
            json.dump(show_metadata, f)

    def get_all_shows(self):
        shows_dir = os.path.join(self.base_dir, 'shows')
        shows = []
        for show_name in os.listdir(shows_dir):
            show_dir = os.path.join(shows_dir, show_name)
            with open(os.path.join(show_dir, 'metadata.json'), 'r') as f:
                show_metadata = json.load(f)
                shows.append(show_metadata)
        return shows

    def get_show(self, title):
        show_dir = os.path.join(self.base_dir, 'shows', title)
        with open(os.path.join(show_dir, 'metadata.json'), 'r') as f:
            show_metadata = json.load(f)
        return show_metadata

    def update_show(self, title, **kwargs):
        show_dir = os.path.join(self.base_dir, 'shows', title)
        with open(os.path.join(show_dir, 'metadata.json'), 'r') as f:
            show_metadata = json.load(f)
        show_metadata.update(kwargs)
        with open(os.path.join(show_dir, 'metadata.json'), 'w') as f:
            json.dump(show_metadata, f)

    def delete_show(self, title):
        show_dir = os.path.join(self.base_dir, 'shows', title)
        shutil.rmtree(show_dir)

    def create_shot(self, show_title, shot_title, description, duration, status):
        show_dir = os.path.join(self.base_dir, 'shows', show_title)
        shot_dir = os.path.join(show_dir, 'shots', shot_title)
        os.makedirs(shot_dir, exist_ok=True)
        shot_metadata = {
            'title': shot_title,
            'description': description,
            'duration': duration,
            'status': status
        }
        with open(os.path.join(shot_dir, 'metadata.json'), 'w') as f:
            json.dump(shot_metadata, f)

    def get_all_shots(self, show_title):
        show_dir = os.path.join(self.base_dir, 'shows', show_title)
        shots_dir = os.path.join(show_dir, 'shots')
        shots = []
        for shot_name in os.listdir(shots_dir):
            shot_dir = os.path.join(shots_dir, shot_name)
            with open(os.path.join(shot_dir, 'metadata.json'), 'r') as f:
                shot_metadata = json.load(f)
                shots.append(shot_metadata)
        return shots

    def get_shot(self, show_title, shot_title):
        shot_dir = os.path.join(self.base_dir, 'shows', show_title, 'shots', shot_title)
        with open(os.path.join(shot_dir, 'metadata.json'), 'r') as f:
            shot_metadata = json.load(f)
        return shot_metadata

    def update_shot(self, show_title, shot_title, **kwargs):
        shot_dir = os.path.join(self.base_dir, 'shows', show_title, 'shots', shot_title)
        with open(os.path.join(shot_dir, 'metadata.json'), 'r') as f:
            shot_metadata = json.load(f)
        shot_metadata.update(kwargs)
        with open(os.path.join(shot_dir, 'metadata.json'), 'w') as f:
            json.dump(shot_metadata, f)

    def delete_shot(self, show_title, shot_title):
        shot_dir = os.path.join(self.base_dir, 'shows', show_title, 'shots', shot_title)
        shutil.rmtree(shot_dir)
