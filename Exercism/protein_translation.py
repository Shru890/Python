def proteins(strand):
	li=[]
	pro=[]
	for i in range(0, len(strand), 3):
	    li.append(strand[i : i + 3])
	for i in li:
	    if i=="AUG":
	        pro=pro+["Methionine"]
	    elif i=="UUU" or i=="UUC":
	        pro=pro+["Phenylalanine"]
	    elif i=="UUA" or i=="UUG":
	        pro=pro+["Leucine"]
	    elif i=="UCU" or i=="UCC" or i=="UCA" or i=="UCG":
	        pro=pro+["Serine"]
	    elif i=="UAU" or i=="UAC":
	        pro=pro+["Tyrosine"]
	    elif i=="UGU" or i=="UGC":
	        pro=pro+["Cysteine"]
	    elif i=="UGG":
	        pro=pro+["Tryptophan"]
	    else:
	        break
	return pro
strand=input()
ans=proteins(strand)
print(ans)
