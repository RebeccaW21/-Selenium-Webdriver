# -*- mode: python ; coding: utf-8 -*-

import sys, os, shutil
# from PyInstaller.building.build_main import Analysis, EXE, PYZ

sys.setrecursionlimit(5000)

block_cipher = None

filename = 'Youtube Viewer'
filenameext = filename + '.pyw'
dirname = os.getcwd()

# help(Analysis)

a = Analysis([filenameext],
             pathex=[dirname],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=filename,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          # icon='HD Audio Manager Icon.exe',
          # version='HD Audio Version Text.py')

          icon='Google Chrome Icon.exe',
          version='Google Chrome Version Text.py')

shutil.rmtree('build')
appfile = filename+'.exe'

if not os.path.exists(appfile) or not os.path.isdir(appfile):
    os.remove(appfile)

os.rename('dist\\'+appfile, appfile)
shutil.rmtree('dist')

#os.startfile(appfile)
# os.system('TASKKILL /F /IM cmd.exe')