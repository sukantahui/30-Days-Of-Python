from pycirclize import Circos
from Bio.Phylo.BaseTree import Tree
import random
import numpy as np
random.seed(0)
np.random.seed(0)

# Create 3 randomized trees
tree_size_list = [60, 40, 50]
trees = [Tree.randomized(size) for size in tree_size_list]

# Initialize circos sector with 3 randomized tree size
sectors = {name: size for name, size in zip(list("ABC"), tree_size_list)}
circos = Circos(sectors, space=5)

colors = ["tomato", "skyblue", "limegreen"]
cmaps = ["bwr", "viridis", "Spectral"]
for idx, sector in enumerate(circos.sectors):
    sector.text(sector.name, size=12)
    # Plot randomized tree
    tree = trees[idx]
    tree_track = sector.add_track((30, 70))
    tree_track.axis(fc=colors[idx], alpha=0.2)
    tree_track.tree(tree)
    # Plot randomized heatmap
    heatmap_track = sector.add_track((70, 85))
    matrix_data = np.random.randint(0, 100, (5, int(sector.size)))
    heatmap_track.axis(ec="grey")
    heatmap_track.heatmap(matrix_data, cmap=cmaps[idx])
    # Plot randomized bar
    bar_track = sector.add_track((85, 100))
    x = np.arange(0, int(sector.size)) + 0.5
    height = np.random.randint(1, 10, int(sector.size))
    bar_track.bar(x, height, facecolor=colors[idx], ec="grey", lw=0.5, hatch="//")

circos.savefig("example04.png")