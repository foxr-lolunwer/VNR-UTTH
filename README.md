## 本地部署指南 / Local Deployment Guide

### 中文说明
这是一个 **Hearts of Iron IV** 的模组仓库。若要在本地部署本项目，请参考以下步骤：

1. **放置项目**：将本项目文件夹放置在你的游戏文档目录下：
   `<盘符>:\Users\<用户名>\Documents\Paradox Interactive\Hearts of Iron IV\mod\`
2. **新建引导文件**：在上述 `mod` 文件夹中新建一个文本文件，命名为 `xxx.mod`。
3. **同步描述信息**：将本项目中 `descriptor.mod` 的全部内容复制到该 `xxx.mod` 文件中。
4. **添加绝对路径**：在 `xxx.mod` 文件中另起一行，添加本项目文件夹的绝对路径：
   `path="<盘符>:/Users/<用户名>/Documents/Paradox Interactive/Hearts of Iron IV/mod/VNR+UTTH"`

完成后，游戏启动器即可识别此本地模组。

---

### English Instructions
This is a mod repository for **Hearts of Iron IV**. To deploy this project locally, follow these steps:

1. **File Location**: Place the project folder in your game's Documents directory:
   `<Drive>:\Users\<Username>\Documents\Paradox Interactive\Hearts of Iron IV\mod\`
2. **Create .mod File**: Create a new text file named `xxx.mod` in the directory mentioned above.
3. **Copy Contents**: Copy the entire contents of `descriptor.mod` from this repository into the new `xxx.mod` file.
4. **Add Absolute Path**: Add a new line to the `xxx.mod` file specifying the absolute path to the project folder:
   `path="<Drive>:/Users/<Username>/Documents/Paradox Interactive/Hearts of Iron IV/mod/VNR+UTTH"`

Once configured, the Paradox Launcher will recognize the local mod.
