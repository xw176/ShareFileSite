### check命令
启动 Django 项目,在启动 django 项目之前，我们应该有一个良好的习惯,使用 check 命令

`python3 manage.py check`

没出错的话,说明我们的 Django 项目可以正常启动。


### 遇到的问题（编码的问题）
`'utf-8' codec can't decode byte 0xd7 in position 206: invalid continu`

- 解决:
templates 下的文件编码改成utf-8