# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

a.binaries += [('hira2.bin', '.\\hira2.bin', 'DATA')]
a.binaries += [('kata.bin', '.\\kata.bin', 'DATA')]
a.binaries += [('alp.bin', '.\\alp.bin', 'DATA')]
a.binaries += [('human.bin', '.\\human.bin', 'DATA')]
a.binaries += [('hrkt.bin', '.\\hrkt.bin', 'DATA')]
a.binaries += [('mld.pickle','.\\mld.pickle','DATA')]

a.binaries += [('voc.csv', '.\\voc.csv', 'DATA')]
a.binaries += [('test1.csv', '.\\test1.csv', 'DATA')]
a.binaries += [('namelist.csv', '.\\namelist.csv', 'DATA')]
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
