# -*- mode: python -*-

block_cipher = None


a = Analysis(['pytalian.py'],
             pathex=['/Users/SantiGuillenGar/Documents/Uni/Y2S2/pytalian'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pytalian',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='pytalian.app',
             icon=None,
             bundle_identifier=None)
