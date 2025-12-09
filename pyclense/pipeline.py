class CleaningPipeline:

    def __init__(self, initial_cleaner):
        self.main_cleaner = initial_cleaner
        self.steps = []

    def add_step(self, cleaner_class):
        """Adds a cleaning step to the pipeline."""
        self.steps.append(cleaner_class)

    def run(self):
        print(f"Starting Pipeline on {self.main_cleaner}")
        
        for CleanerClass in self.steps:
            step_instance = CleanerClass(self.main_cleaner.df)
            step_instance.clean()
            
            self.main_cleaner.df = step_instance.df
            
        return self.main_cleaner