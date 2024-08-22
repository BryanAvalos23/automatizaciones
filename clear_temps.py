from pathlib import Path
import shutil

user = input('digita el usuario de tu equipo')

dir_one = Path(f'C:/Users/{user}/AppData/Local/Temp')
dir_two = Path('C:/Windows/Temp')

archivos = [archivo for archivo in dir_one.iterdir() if archivo.is_file()]
directories = [directory for directory in dir_one.iterdir() if directory.is_dir() ]

archivos_two = [archivo for archivo in dir_two.iterdir() if archivo.is_file()]
directories_two = [archivo for archivo in dir_two.iterdir() if archivo.is_dir()]


response = input('Estas seguro que deseas eliminar los archivos (y / n): ').strip().lower()

while(response != 'y' and response != 'n'):
    response = input('Estas seguro que deseas eliminar los archivos (y / n): ').strip().lower()

def delete_files(files):
    for file in files:
        try:
            file.unlink()
        except Exception as er:
            print(f'Ocurrio un error: {er}')

def delete_dirs(dirs):
    for dir in dirs:
        try:
            shutil.rmtree(dir)
        except Exception as er:
            print(f'Ocurrio un error: {er}')

if response == 'y':
    print('Eliminando archivos y directorios...')

    delete_files(archivos)
    delete_files(archivos_two)

    delete_dirs(directories)
    delete_dirs(directories_two)

elif response == 'n':
    print('Proceso terminado...')