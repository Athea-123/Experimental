from pyclense import BaseCleaner, DuplicateCleaner, MissingDataCleaner, FormatStandardizer, CleaningPipeline

base = BaseCleaner("data/dataset.csv")
print(f"Loaded: {base}")        
print(f"Row count: {len(base)}") 

pipeline = CleaningPipeline(base)

pipeline.add_step(DuplicateCleaner)
pipeline.add_step(MissingDataCleaner)
pipeline.add_step(FormatStandardizer)

final_result = pipeline.run()

final_result.save_data("data/cleaned_dataset.csv")