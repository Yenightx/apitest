# 说明文档

## 1 目录结构

- apiCall：存放接口封装方法
- config：存放配置文件
- data_struct：存放数据结构
- result：执行过程中生成的文件夹，里面存放每次测试的结果
- runner：启动程序
- testCase：存放具体的测试case
- testFile：存放测试过程中用到的文件，包括上传的文件，测试用例以及数据库的sql语句

## 2 搭建环境

### 2.1 安装Anaconda

> 下载地址：https://www.anaconda.com/products/individual#Downloads

**注意事项**：安装时，请将<u>Register Anaconda as the system Python 3.x</u>都勾选上

### 2.2 安装Pycharm

> 下载地址：https://www.jetbrains.com/pycharm/download/#section=windows

#### 2.2.1 获取激活码
xxx

### 2.3 安装Allure

> 下载地址：https://github.com/allure-framework/allure2/releases

- 将下载好的文件解压存放
- 配置环境变量
  - 找到变量PATH，编辑PATH
  - 添加新的一行，添加内容为Allure的存放目录\bin，如D:\allure-2.13.2\bin

### 2.4 安装依赖库

打开命令行窗口，输入

```commandline
pip install D:\Zlib-0.2.8-py3-none-any.whl
```
