# exportchart.spec
# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules, collect_dynamic_libs, collect_data_files

block_cipher = None

# Thu thập tất cả module Qt6 (Core, Gui, Widgets, ...)
hiddenimports = collect_submodules('PyQt6')
binaries     = collect_dynamic_libs('PyQt6')
datas        = collect_data_files('PyQt6')

# Thêm luôn file DB của bạn
datas += [
    ('chart_topcoin.db', '.')  # file DB copy vào root của exe
]

a = Analysis(
    ['exportchart.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='exportchart',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,      # hoặc False nếu bạn muốn windowed GUI
    icon='icon.ico'    # nếu bạn có file icon.ico
)
