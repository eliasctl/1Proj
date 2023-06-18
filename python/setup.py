from cx_Freeze import setup, Executable
base = None

executables = [Executable("quoridor.py", base=base)]

packages = ["idna","pygame","sys","func","time","os"]
options = {
    'build_exe': {    
        'packages': packages,
        
    },
}

setup(
    name = "Quoridor",
    options = options,
    version = "1.0",
    description = 'Voici notre version du jeu quoridor',
    executables = executables
)