from pathlib import Path

dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".json": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"}

tri_dir = Path.home()/"Downloads" #creation du chemin
file = [f for f in tri_dir.iterdir() if f.is_file()] # liste tous les elements contenu dans notre dossier
for f in file:
    output_dir = tri_dir / dirs.get(f.suffix,"Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir/f.name)
    