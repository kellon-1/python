import sys
import pickle as p     # 给模块pickle 取个别名p

sys.path   # 显示python的工作路径,自己写的代码可以放进这里，  site packages

# foo.py -> hi = 'hello'
# zip mytest.zip foo.py
# rm -rf foo.py
# python3
# >>>import foo -> error
# >>>import sys
# >>>sys.path.append('./mytest.zip')  # 把当前路径下mytest.zip添加到python工作路径
# >>>import foo