import os.path
import zipfile

homedir = os.path.expanduser("~")
print('\nInstalando REA-Snake...')
print('\tNa pasta: '+homedir+'/REA-Snake/')

print('\tMovendo REA.zip...')
fantasy_zip = zipfile.ZipFile('REA.zip')
fantasy_zip.extractall(homedir)
fantasy_zip.close()

print('\tMovendo Game_sounds.zip...')
fantasy_zip = zipfile.ZipFile('gameSounds.zip')
fantasy_zip.extractall(homedir+'/REA/SNAKE/sounds/')
fantasy_zip.close()

print('\tCriando atalho: SnakeMath.desktop...')
arqDesktop = open('SnakeMath.desktop', 'w')
arqDesktop.write('#!/usr/bin/env xdg-open\n')
arqDesktop.write('[Desktop Entry]\n')
arqDesktop.write('Name=Snake\n')
arqDesktop.write('Comment=Rea - Snake\n')
arqDesktop.write('Exec='+homedir+'/REA/Snake.sh\n')
arqDesktop.write('Icon='+homedir+'/REA/snake.ico\n')
arqDesktop.write('Type=Application\n')
arqDesktop.write('Terminal=0')
arqDesktop.close()

print('\tObtendo permissão de execução...')
os.chmod('ServerSnake.jar', 0o777)
os.chmod(homedir+'/REA', 0o777)
os.chmod(homedir+'/REA/snake.ico', 0o777)
os.chmod(homedir+'/REA/Snake.sh', 0o777)
os.chmod('SnakeMath.desktop', 0o777)

print('\tFim')