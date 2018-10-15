class Task:
    def __init__(self, processing_time, too_early_penalty, too_late_penalty):
        self.processing_time = processing_time
        self.too_early_penalty = too_early_penalty
        self.too_late_penalty = too_late_penalty
