# document_priorities.py – minimal set, no SKIP_FILES

DOCUMENT_PRIORITIES: dict[str, int] = {
    # Priority 1 – Core cyber law (always searched first)
    "TIC_Articles.pdf": 1,
    "DZ_FR_Cybercrime Law_2009.pdf": 1,
    "2018_Algeria_fr_Loi n_ 18-07 du 25 Ramadhan 1439 correspondant au 10 juin 2018 relative à la protection des personnes physiques dans le traitement des données à caractère personnel.pdf": 1,
    "Loi n° 18-07 du 25 Ramadhan 1439 correspondant au 10 juin 2018 relative à la protection des personnes physiques dans le traitement des données à caractère personnel.pdf": 1,
    "2016_Algeria_fr_Code Penal.pdf": 1,   # optional, keep if you want the full code

    # Priority 2 – Supporting / procedural
    "Law 20-06 Algeria.pdf": 2,
    "Loi n∞ 15-04 du 11 Rabie Ethani 1436 correspondant au 1er fÈvrier 2015 fixant les rËgles gÈnÈrales relatives ‡ la signature et ‡ la certification Èlectroniques.pdf": 2,
    "Penal Procedure Code 2021 Update.pdf": 2,
}

def get_priority(filename: str) -> int:
    return DOCUMENT_PRIORITIES.get(filename, 2)