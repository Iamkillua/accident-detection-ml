import os

os.system("aria2c " + "https://mediacenter.harshdeepsfiles.workers.dev/0:/accident-detection.rar")
				
import patoolib
patoolib.extract_archive("accident-detection.rar", outdir=".")

