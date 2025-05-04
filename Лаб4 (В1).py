from Bio import Entrez, SeqIO

# Регистрация NCBI
Entrez.email = "andreyyaschenko07@gmail.com"

# Список с интересующими нас видами
species_names = ["Brassica oleracea", "Solanum lycopersicum"]

# Список для хранения записей
records = []

for species in species_names:
    # Поиск записи с полным кодом (complete cds) для данного вида
    search_handle = Entrez.esearch(db="nucleotide", term=f"{species} complete cds", retmax=5)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    # Получение идентификаторов записей
    id_list = search_results["IdList"]

    for seq_id in id_list:
        # Получение данных записи из GenBank
        fetch_handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="gb", retmode="text")
        records.append(SeqIO.read(fetch_handle, "genbank"))
        fetch_handle.close()

# Сохранение всех записей в один файл формата GenBank
output_file = "merged_sequences.gb"

with open(output_file, "w") as output_handle:
    SeqIO.write(records, output_handle, "genbank")

print(f"Все записи успешно сохранены в {output_file}.")
