
---

### 5. `flatness_calculator.spec`

```python
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['flatness_gui.py'],
    pathex=[],
    datas=[('assets/logo.png', 'assets')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz, a.scripts, [],
    name='flatness_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)
