# Demo_Python
> echo "# Demo_Python" >> README.md</br>
git init</br>
git add README.md</br>
git commit -m "first commit"</br>
git remote add origin git@github.com:Forever-3197/Demo_Python.git</br>
git push -u origin master</br>

## 解决为什么不能正常编译解释问题：缺少main主函数
> 在终端执行py文件时，从主文件main.py文件开始，被解释器作为主函数，所以一般在这个文件里编程相关工作<br/>如果任然无法正常编译，在所要执行的文件加：
```python
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
os.putenv("PYTHONPATH", cur_path)
```
也就是将当前文件加入到解释器的工作路径里