from rdkit import Chem

def read_smiles_from_file(file_path):
    with open(file_path, "r") as f:
        smiles_list = [line.strip() for line in f.readlines()]
    return smiles_list

file_path = "xxx.smi"  # Change this to the path of your file
smiles_list = read_smiles_from_file(file_path)

def write_smiles_to_file(smiles_list, file_path):
    with open(file_path, "w") as f:
        for smiles in smiles_list:
            f.write(smiles + "\n")

output_file_path = "xxx.smi"  # Change this to the desired output file path
write_smiles_to_file(smiles_list, output_file_path)