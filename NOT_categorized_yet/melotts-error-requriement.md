# pip3 install 
```
  File "/home/amrrobot/.local/lib/python3.10/site-packages/numba/core/pythonapi.py", line 12, in <module>
    from numba.core import (
  File "/home/amrrobot/.local/lib/python3.10/site-packages/numba/core/lowering.py", line 19, in <module>
    from numba.misc.coverage_support import get_registered_loc_notify
  File "/home/amrrobot/.local/lib/python3.10/site-packages/numba/misc/coverage_support.py", line 114, in <module>
    class NumbaTracer(coverage.types.Tracer):
AttributeError: module 'coverage' has no attribute 'types'
```

melo 패키지를 만드는 과정에서 뭔가 꼬여서 numba 패키지가 꼬여버렸다.;;
```
pip3 install --upgrade pip setuptools wheel
```

coverage 에서 문제가 발생하는데,   

`python3.10 기준으로 numba >= 0.57.1` 이어야 하는데  

먼저 numba llvmlite coverage 등을 삭제한 후 
```
pip3 uninstall -y numba llvmlite coverage
```

다시 인스톨
```
pip3 install "numba==0.57.1" "llvmlite==0.40.1" coverage
```

테스트 버전 확인
```
python3 -c "import numba; print(numba.__version__)"
```

버전이 나오면 정상 작동하는 것임

