# -*- mode: python -*-

import PyInstaller.config
PyInstaller.config.CONF['distpath'] = '.'

block_cipher=None

a = Analysis(['..\\BridgeShapeTool.py'],
             pathex=['C:\\Users\\Ender\\Desktop\\University\\MATH3808\\BridgeShapeTool\\dist'],
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

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='BridgeShapeTool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False)

coll = COLLECT(exe,
               a.binaries,
               a.scripts,
               a.datas,
               strip=False,
               upx=False,
               name='app')