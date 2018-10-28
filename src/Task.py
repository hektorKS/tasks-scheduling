class Task:
    def __init__(self, task_id, processing_time, too_early_penalty, too_late_penalty):
        self.task_id = task_id
        self.processing_time = processing_time
        self.too_early_penalty = too_early_penalty
        self.too_late_penalty = too_late_penalty

    def __str__(self):
        return "[task_id: {}, processing_time: {}, too_early_penalty: {}, too_late_penalty: {}]".format(
            self.task_id,
            self.processing_time,
            self.too_early_penalty,
            self.too_late_penalty
        )