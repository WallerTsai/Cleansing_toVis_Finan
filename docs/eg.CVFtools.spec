# 示例，注意修改datas中的文件路径
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py','Function_define.py','Files_writing.py','Files_reading.py','Files_preparation.py','Files_define.py','Clean.py','Charts_show.py'],
    pathex=[],
    binaries=[],
    datas=[(':path\\to\\Lib\\site-packages\\pyecharts\\','.\\pyecharts\\')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CVFtools',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
