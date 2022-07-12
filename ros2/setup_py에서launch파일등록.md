```py
from setuptools import setup
```

라고 되어 있는 것 외에 os, glob를 import한다 
```py
import os
from glob import glob
```

data_files= 부분에서 ('share/' + package_name, ['package.xml']), 다음에 추가 해준다  
```py
(os.path.join('share', pakcage_name, 'launch'), glob('launch/*.py'))
```

이제 launch디렉토리의 py파일은 모두 불러오게 됨