from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import time

start_time = time.time()

record = SeqIO.read("proteina.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))
with open("salida.xml", "w") as out_handle:
	out_handle.write(result_handle.read())
result_handle.close()

print("--- %s seconds ---" % (time.time() - start_time))