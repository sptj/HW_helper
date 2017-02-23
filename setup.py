from distutils.core import setup
import py2exe

options = {"py2exe":
               {"compressed": 1,
                "optimize": 2,
                "bundle_files": 1
                }
           }
setup(
    version="1.0.0",
    description="description for your exe",
    name="name for your exe",
    options=options,
    zipfile=None,  # 不生成zip库文件
    console=[{"script": "mian.py", "icon_resources": [(1, "Hello.ico")]}],
)