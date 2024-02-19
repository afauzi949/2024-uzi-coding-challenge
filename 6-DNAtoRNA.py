# UZI Coding Challenge
# 6/366
# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python


#DNA to RNA structure
def dna_to_rna(dna):  
    rna = ""  # string kosong
    for i in dna:
        if i == "T":
            rna += "U"  #tambah karakter dari perulangan ke rna 
        else:
            rna += i    #tambah karakter jika bukan T ke rna    
    return rna          #mengembalikan nilai fungsi ke dna

print(dna_to_rna("GCAT"))
print(dna_to_rna("TTTT"))
print(dna_to_rna("GACCGCCGCC"))

