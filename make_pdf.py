import sys
import nbconvert
import nbformat

Complex_Networks = [
    "leggi_pdb",
    "PCM_permute",
    "ER_networks",
    "real_net_analysis",
    "laplacian_lab_07",
    "open_network_growth_models",
]

Pattern_Recognition = [
    "Pat_Rec_Lab_1",
    "SwissRoll_PCA_MDS_LLE_IsoMap_tSNE_UMAP",
    "clustering_examples",
    "simple_perceptron",
    "neuron_class",
    "scikit_intro",
]

Models = [
    "bigrams",
    "trigrams",
    "concatenated_network",
    "convolutional_network",
    "min-char-rnn",
    "GPT",
    "gpt_source",
    'GAN',
]

Quantum_Computing = [
    "prerequisites",
]

out_notebook = nbformat.v4.new_notebook()
subject = sys.argv[1].lower()
outext = ".pdf"
if subject == 'cn':
    files = Complex_Networks
    outfile = 'Complex_Networks'
elif subject == 'pr':
    files = Pattern_Recognition
    outfile = 'Pattern_Recognition'
elif subject == 'mnm':
    files = Models
    outfile = 'Models_and_Numerical_Methods'
    outext = "-LAB.pdf"
elif subject == 'qc':
    files = Quantum_Computing
    outfile = 'Quantum_Computing'
    outext = "-LAB.pdf"

for file in files:
    temp_notebook = nbformat.read('./src/{}/{}.ipynb'.format(outfile, file), as_version=4)
    out_notebook.cells.extend(temp_notebook.cells)

out_pdf = nbconvert.PDFExporter().from_notebook_node(out_notebook)[0]
with open(outfile+outext, 'wb') as f:
    f.write(out_pdf)