class CleaningPipeline:
    """
    Runs a list of cleaning tools one by one on our data.

    Think of this as a manager that processes the data through several 
    stations (duplicates, missing values, etc.) in a specific order.
    """

    def __init__(self, initial_cleaner):
        self.main_cleaner = initial_cleaner
        self.steps = []

    def add_step(self, cleaner_class):
        """Adds a cleaning step to the pipeline."""
        self.steps.append(cleaner_class)

    def run(self):
        print(f"Starting Pipeline on {self.main_cleaner}")
        
        for CleanerClass in self.steps:
            # Create the tool using the current data
            step_instance = CleanerClass(self.main_cleaner.df)
            # Run the cleaning job
            step_instance.clean()
            # Save the clean data back to the main container for the next step
            self.main_cleaner.df = step_instance.df
            
        return self.main_cleaner
