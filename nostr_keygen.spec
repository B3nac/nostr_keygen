# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['nostr_keygen.py'],
    pathex=[],
    binaries=[('_cffi_backend.cpython-310-x86_64-linux-gnu.so', '.')],
    datas=[('bech32', 'bech32')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='nostr_keygen',
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
