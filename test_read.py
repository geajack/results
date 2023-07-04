from results import create_results_directory, load_results_directory

results = load_results_directory("results/test-04-07-23@18:09:06")

print(results.json("output.json"))