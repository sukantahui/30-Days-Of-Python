from pycirclize import Circos
import pandas as pd

# Create matrix dataframe (3 x 6)
row_names = ["Student", "Teacher", "Client"]
col_names = ["JAVA", "Python", "Tally", "Angulr", "PHP", "C++"]
matrix_data = [
    [4, 14, 13, 17, 5, 2],
    [7, 1, 6, 8, 12, 15],
    [9, 10, 3, 16, 11, 18],
]
matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# Initialize from matrix (Can also directly load tsv matrix file)
circos = Circos.initialize_from_matrix(
    matrix_df,
    start=-265,
    end=95,
    space=5,
    r_lim=(93, 100),
    cmap="tab10",
    label_kws=dict(r=94, size=12, color="white"),
    link_kws=dict(ec="black", lw=0.5),
)

print(matrix_df)
circos.savefig("example06.png")