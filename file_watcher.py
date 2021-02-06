from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class File_Watcher:
    def __init__(self):
        self.observer = Observer()
        self.event_handler = FileSystemEventHandler()
        self.activated = False

    def begin_watch(self, folder_path, response=None, recursive=False):
        if not self.activated:
            self.activated = True
            if not response:
                def default_response():
                    print('file created in path:', folder_path)

                self.event_handler.on_created = default_response

            else:
                self.event_handler.on_created = response
            
            self.observer.schedule(self.event_handler, folder_path, recursive=recursive)
            self.observer.start()

    def end_watch(self):
        if self.activated:
            self.activated = False
            self.observer.stop()
            self.event_handler.on_created = None
        
