from results import create_results_directory, load_results_directory

results = create_results_directory("test")

results.json("output.json", [1, 2, 3])