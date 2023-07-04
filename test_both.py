from results import create_results_directory, load_results_directory

results = create_results_directory("test2")
inputs = load_results_directory("test-04-07-23@18:09:06")

results.json("output2.json", inputs.json("output.json"))