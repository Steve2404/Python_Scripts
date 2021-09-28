from pathlib import Path
"""mp3, wav, flac : Musique
    avi, mp4, gif : Videos
    bmp, png, jpg : Images
    txt, pptx, csv, xls, odp, pages : Documents
    autres : Divers
"""

EXTENSION = {".mp3": "Musique",
             ".wav": "Musique",
             ".flac": "Musique",
             ".avi": "Videos",
             ".mp4": "Videos",
             ".mkv": "Videos",
             ".gif": "Images",
             ".bmp": "Images",
             ".png": "Images",
             ".jpg": "Images",
             ".webp": "Images",
             ".exe" : "Setup",
             ".zip": "Archives",
             ".rar": "Archives",
             ".py" : "Python_Prog",
             ".ipynb":"Python_Prog",
             ".txt": "Documents",
             ".pptx": "Documents",
             ".csv": "Documents", 
             ".xls": "Documents", 
             ".odp": "Documents",
             ".pdf": "Documents",
             ".pages": "Documents"
            }
chemin = Path.home() / "Downloads"
file = [f for f in chemin.iterdir() if f.is_file()]
for f in file:
    dossier = EXTENSION.get(f.suffix, "Divers")
    new_chemin = chemin / dossier
    new_chemin.mkdir(parents= True, exist_ok= True)
    f.rename(new_chemin/f.name)
