import matplotlib.pyplot as plt

size = 10  # Starting size
max_iterations = 100
best_structure = generate_initial_structure(size)

for iteration in range(max_iterations):
    new_structure = evolve_structure(best_structure)
    if evaluate_structure(new_structure):
        best_structure = new_structure
        # Save the structure as an image
        plt.imshow(best_structure)  # This will need to be adapted to visualize the structure
        plt.savefig(f"structure_{iteration}.jpg")
