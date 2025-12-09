from pyclense.base import BaseCleaner
from pyclense.duplicate import DuplicateCleaner
from pyclense.missing import MissingDataCleaner
from pyclense.standardizer import FormatStandardizer
from pyclense.pipeline import CleaningPipeline

base = BaseCleaner("data/dataset.csv")
print(f"Loaded: {base}")        
print(f"Row count: {len(base)}") 

# Set up the Pipeline
pipeline = CleaningPipeline(base)

#Register the specific tools to be used. Note that the class names are passed directly, not instances
pipeline.add_step(DuplicateCleaner)
pipeline.add_step(MissingDataCleaner)
pipeline.add_step(FormatStandardizer)

final_result = pipeline.run()

final_result.save_data("data/cleaned_dataset.csv")
