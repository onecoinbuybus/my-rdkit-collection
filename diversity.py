from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

'''
Code for calculating molecular diversity based on tanimoto similarity
'''

def tanimoto_similarity(fp1, fp2):
    return DataStructs.TanimotoSimilarity(fp1, fp2)

def average_tanimoto_similarity(fingerprints):
    total_similarity = 0
    num_comparisons = 0

    for i in range(len(fingerprints)):
        for j in range(i+1, len(fingerprints)):
            total_similarity += tanimoto_similarity(fingerprints[i], fingerprints[j])
            num_comparisons += 1

    if num_comparisons == 0:
        return 0

    return total_similarity / num_comparisons

def generate_fingerprints(mols):
    fingerprints = [AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024) for mol in mols]
    return fingerprints

def main():
    mols = [Chem.MolFromSmiles('CCO'), Chem.MolFromSmiles('CCCSC'), Chem.MolFromSmiles('CCCOCCCC')]
    fingerprints = generate_fingerprints(mols)
    average_similarity = average_tanimoto_similarity(fingerprints)
    diversity = 1 - average_similarity
    print("Molecular diversity:", diversity)

if __name__ == '__main__':
    main()