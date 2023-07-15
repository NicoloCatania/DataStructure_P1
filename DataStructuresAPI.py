import os
import json
import shutil
from typing import List, Dict

class Show:
    def __init__(self, title: str, description: str, release_date: str, duration: str) -> None:
        self.title = title
        self.description = description
        self.release_date = release_date
        self.duration = duration
        self.shots: List[Shot] = []

    def to_dict(self) -> Dict[str, any]:
        return {
            'title': self.title,
            'description': self.description,
            'release_date': self.release_date,
            'duration': self.duration,
            'shots': [shot.to_dict() for shot in self.shots]
        }

    @classmethod
    def from_dict(cls, show_dict: Dict[str, any]) -> 'Show':
        show = cls(show_dict['title'], show_dict['description'], show_dict['release_date'], show_dict['duration'])
        shots = show_dict['shots']
        show.shots = [Shot.from_dict(shot) for shot in shots]
        return show

class Shot:
    def __init__(self, title: str, description: str, duration: str, status: str) -> None:
        self.title = title
        self.description = description
        self.duration = duration
        self.status = status

    def to_dict(self) -> Dict[str, any]:
        return {
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, shot_dict: Dict[str, any]) -> 'Shot':
        return cls(shot_dict['title'], shot_dict['description'], shot_dict['duration'], shot_dict['status'])

class FileHandler:
    @staticmethod
    def create_directory(directory: str) -> None:
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    def read_json_file(file_path: str) -> Dict[str, any]:
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json_file(file_path: str, data: Dict[str, any]) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def delete_directory(directory: str) -> None:
        shutil.rmtree(directory)

class Pipeline:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = base_dir
        self.file_handler = FileHandler()

    def get_show_directory(self, title: str) -> str:
        return os.path.join(self.base_dir, 'shows', title)

    def create_show(self, title: str, description: str, release_date: str, duration: str) -> None:
        show_dir = self.get_show_directory(title)
        self.file_handler.create_directory(show_dir)
        show_metadata = Show(title, description, release_date, duration)
        metadata_file = os.path.join(show_dir, 'metadata.json')
        self.file_handler.write_json_file(metadata_file, show_metadata.to_dict())

    def get_all_shows(self) -> List[Show]:
        shows_dir = os.path.join(self.base_dir, 'shows')
        shows = []
        for show_name in os.listdir(shows_dir):
            show_dir = os.path.join(shows_dir, show_name)
            metadata_file = os.path.join(show_dir, 'metadata.json')
            show_dict = self.file_handler.read_json_file(metadata_file)
            show = Show.from_dict(show_dict)
            shows.append(show)
        return shows

    def get_show(self, title: str) -> Show:
        show_dir = self.get_show_directory(title)
        metadata_file = os.path.join(show_dir, 'metadata.json')
        show_dict = self.file_handler.read_json_file(metadata_file)
        return Show.from_dict(show_dict)

    def update_show(self, title: str, **kwargs: any) -> None:
        show = self.get_show(title)
        for key, value in kwargs.items():
            setattr(show, key, value)
        metadata_file = os.path.join(self.get_show_directory(title), 'metadata.json')
        self.file_handler.write_json_file(metadata_file, show.to_dict())

    def delete_show(self, title: str) -> None:
        show_dir = self.get_show_directory(title)
        self.file_handler.delete_directory(show_dir)

    def create_shot(self, show_title: str, shot_title: str, description: str, duration: str, status: str) -> None:
        show_dir = self.get_show_directory(show_title)
        shot_dir = os.path.join(show_dir, 'shots', shot_title)
        self.file_handler.create_directory(shot_dir)
        shot_metadata = Shot(shot_title, description, duration, status)
        metadata_file = os.path.join(shot_dir, 'metadata.json')
        self.file_handler.write_json_file(metadata_file, shot_metadata.to_dict())

    def get_all_shots(self, show_title: str) -> List[Shot]:
        show_dir = self.get_show_directory(show_title)
        shots_dir = os.path.join(show_dir, 'shots')
        shots = []
        for shot_name in os.listdir(shots_dir):
            shot_dir = os.path.join(shots_dir, shot_name)
            metadata_file = os.path.join(shot_dir, 'metadata.json')
            shot_dict = self.file_handler.read_json_file(metadata_file)
            shot = Shot.from_dict(shot_dict)
            shots.append(shot)
        return shots

    def get_shot(self, show_title: str, shot_title: str) -> Shot:
        shot_dir = os.path.join(self.get_show_directory(show_title), 'shots', shot_title)
        metadata_file = os.path.join(shot_dir, 'metadata.json')
        shot_dict = self.file_handler.read_json_file(metadata_file)
        return Shot.from_dict(shot_dict)

    def update_shot(self, show_title: str, shot_title: str, **kwargs: any) -> None:
        shot = self.get_shot(show_title, shot_title)
        for key, value in kwargs.items():
            setattr(shot, key, value)
        metadata_file = os.path.join(self.get_show_directory(show_title), 'shots', shot_title, 'metadata.json')
        self.file_handler.write_json_file(metadata_file, shot.to_dict())

    def delete_shot(self, show_title: str, shot_title: str) -> None:
        shot_dir = os.path.join(self.get_show_directory(show_title), 'shots', shot_title)
        self.file_handler.delete_directory(shot_dir)