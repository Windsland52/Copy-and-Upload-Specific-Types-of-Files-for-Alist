# Copy-and-Upload-Specific-Types-of-Files-for-Alist
适用于需要挑选特定后缀文件，复制时保持目录结构，后续通过alist挂载路径上传网盘的Windows用户

## 适用系统

Windows 64位

## 下载

程序结构：

```
|──current work directory
    ├─upload.py
    │
    └─config.json
```

## 配置文件

默认设置如下：

```json
{
  "save_directory_name": "data",
  "alist_path": "C:\\",
  "save_file_type": [
    "xml"
  ],
  "uploaded_list": [
  ]
}
```

前3项根据个人需求填写,最后一项不用管。

### "save_directory_name"

保存到本地的目录名称。修改引号中间的内容，例如`"save_directory_name": "dirname"`

### "alist_path"

alist本地挂载的路径。通过alist可实现文件上传。这里注意windows下路径的'\\'要写成'\\\\',防止程序报错。本程序支持含中文路径。

### "save_file_type"

需要保存的文件后缀，本程序默认上传xml文件，如需上传其它类型，修改双引号内的内容即可。特别地，如有多种类型，各个类型需要用英文逗号隔开，例如

```json
"save_file_type": [
    "xml",
    "mp3",
    "txt"
  ]
```

其它可选项后面再做，可提建议。

## 任务计划

通过定时启动程序，实现文件的自动上传。

现在来介绍Windows平台下的任务计划程序的使用。

下文参考[Windows 运行任务](https://www.kancloud.cn/xuwenyang/php_standard/2071664)

### 步骤

1. `Win+R`弹出运行，输入`taskschd.msc`后回车，进入程序。
2. 操作->创建基本任务，填写名称与描述。
3. 触发器选择一次，开始时间选0:00:00.
4. 操作选启动程序。
5. 程序或脚本选将下载并放好位置的upload.py，参数不填，这里注意一定要将下面的起始于填上，填程序所在文件夹的路径（C:\upload.py这里就填C:\），不然程序无法正常运行。
6. 完成后保存，点进属性->触发器，选中一次并点击编辑。在高级设置中选中重复任务间隔，根据个人需求选择时间，我这里选1小时。后面的持续时间选无限期。下面的已启用选中。
7. 后面的条件根据自己的情况自行设置，我用的是服务器就全不勾选了。
8. 设置完毕，后续根据实际应用再找找问题吧。

## Contact me

Bilibili:[追忆惘然_星梦](https://space.bilibili.com/166729477)

E-mail:[wind_land@foxmail.com](
