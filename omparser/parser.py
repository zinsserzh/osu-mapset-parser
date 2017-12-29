import glob
import os
import weakref
from .file import File

class OsuMapsetParser:
    """A parser to group files in an osu mapset directory."""
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)

        self.core_files = set()
        self.music_files = set()
        self.background_files = set()
        self.skin_image_files = set()
        self.skin_sound_files = set()
        self.video_files = set()
        self.storyboard_files = set()

        self.parse()

    def has_core(self):
        return bool(self.core_files)

    def has_music(self):
        return bool(self.music_files)

    def has_background(self):
        return bool(self.background_files)

    def has_skin_image(self):
        return bool(self.skin_image_files)

    def has_skin_sound(self):
        return bool(self.skin_sound_files)

    def has_video(self):
        return bool(self.video_files)

    def has_storyboard(self):
        return bool(self.storyboard_files)

    def parse(self):
        """Parse .osu .osb files and generate results"""
        self.parse_core()
        self.walk_through()

    def parse_core(self):
        for file in glob.glob(os.path.join(self.directory, "*.osu")):
            # TODO parse music, background, video
            self.core_files.add(self._file_factory(os.path.basename(file)))

        for file in glob.glob(os.path.join(self.directory, "*.osb")):
            # TODO parse background, video
            self.core_files.add(self._file_factory(os.path.basename(file)))

    def walk_through(self):
        for dir_name, _, file_name in os.walk(self.directory):
            # TODO For each file:
            # 1. check which group it belongs to
            # 2. create File object with self._file_factory
            # 3. add the File object to proper group

    def _file_factory(self, rel_path):
        proxy = weakref.proxy(self)
        return File(proxy, rel_path)
