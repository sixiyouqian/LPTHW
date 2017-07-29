# 使用ssh连接github repository
## 什么是SSH
## 创建SSH步骤
1. cd ~/.ssh
2. ssh-keygen -t rsa -C "wangluzhou@aliyun.com"
3. 将公匙id_rsa.pub上的内容复制到github中的ssh配置中去
4. 开始测试：
```shell
# 在git上配置你的用户名和邮箱地址
$ git config --global user.name "wangluzhou"
$ git config --global user.email "wangluzhou@aliyun.com"
# 测试ssh
ssh -T git@github.com
```
## git版本管理步骤
### 1. 初始化你的本地仓库
```shell
git init
```
这一步是将你当前所在的本地目录改造成一个git仓库的格式
### 2. 将内容添加
```
git add .
```
### 3. 将本地内容提交到本地
```
git commit -m "XXXXX"
```
### 4. 添加远程库
```
git remote add origin "git@github.com:wangluzhou/your-repository-name"
```
### 5. 上传到远程库
```
git push -u origin master
```
### 跟新
```
git pull
```
