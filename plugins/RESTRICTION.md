# plugins编写规范
## 1. 接口规范
### 1.1. 接口命名
- 接口命名应该具有描述性，能够清晰表达接口的功能。
- 接口只能接受一个参数，即args,args是一个列表
- 接口必须只返回一个字符串，或者一个列表，列表的格式必须是[字符串，url，字符串,url...]
- 接口首个单词必须是interface

### 1.2 介绍内容接口
每个插件必须写一个名为interface_get_introduction的函数
这个函数接受0个参数，返回一个字符串，简单介绍自己的功能

### 1.3 获取名称接口
每个插件必须写一个名为interface_get_name的函数
这个函数接受0个参数，返回一个字符串，简单介绍本插件名称，也即命令名称