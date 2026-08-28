import time
from datetime import datetime

class TimeCore:
    def __init__(self):
        self.last_cycle_start = None
        self.last_cycle_end = None
        self.last_pause_start = None
        self.last_pause_end = None
        self.last_runtime_start = None
        self.last_runtime_end = None

    def timestamp(self):
        return datetime.now().isoformat()

    def cycle_start(self):
        self.last_cycle_start = time.monotonic()

    def cycle_end(self):
        self.last_cycle_end = time.monotonic()

    def cycle_delta(self):
        if self.last_cycle_start is not None and self.last_cycle_end is not None:
            return self.last_cycle_end - self.last_cycle_start
        return None

    def pause_start(self):
        self.last_pause_start = time.monotonic()

    def pause_end(self):
        self.last_pause_end = time.monotonic()

    def pause_duration(self):
        if self.last_pause_start is not None and self.last_pause_end is not None:
            return self.last_pause_end - self.last_pause_start
        return None

    def is_short_pause(self):
        duration = self.pause_duration()
        return duration is not None and duration < 300

    def is_long_pause(self):
        duration = self.pause_duration()
        return duration is not None and duration >= 300

    def runtime_start(self):
        self.last_runtime_start = time.monotonic()

    def runtime_end(self):
        self.last_runtime_end = time.monotonic()

    def runtime_gap(self):
        if self.last_runtime_start is not None and self.last_runtime_end is not None:
            return self.last_runtime_end - self.last_runtime_start
        return None

    def is_new_day(self):
        gap = self.runtime_gap()
        return gap is not None and gap > 3600 * 6
