# VNR+UTTNH Compatch Expand (VUCE)

[![Steam Workshop](https://img.shields.io/badge/Steam-Workshop-blue?logo=steam)](https://steamcommunity.com/sharedfiles/filedetails/?id=3164741523)
[![GitHub Releases](https://img.shields.io/badge/GitHub-Releases-orange?logo=github)](https://github.com/foxr-lolunwer/VNR-UTTH/releases)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)

🌐 [English Version / 英文版](README.md)

## 当前版本信息
* **MOD 版本:** `Neo 1.8.4`
* **VNR 版本:** `v2.11 - "Tokyo Bay Finale"` (2026.6.22)
* **UTTNH 版本:** `Jan 11, 2026`

## 🔗 快速链接
* **Steam 工作坊:** [点击订阅](https://steamcommunity.com/sharedfiles/filedetails/?id=3164741523)
* **GitHub Releases:** [下载手动安装包](https://github.com/foxr-lolunwer/VNR-UTTH/releases) (适合手动安装或回滚旧版本)

---

## 🛠 功能介绍

通过本模组可以使 [原版海军重置(VNR)](https://steamcommunity.com/sharedfiles/filedetails/?id=2993772482) 和 [UTTNH](https://steamcommunity.com/sharedfiles/filedetails/?id=3413890094) 兼容。

该模组将 VNR 的体验扩展到了 20 世纪 90 年代，沿用 VNR 的海军设计器与 AI 逻辑，并将科技树补全至现代。

> [!WARNING]
> **注意：** 目前冷战海军部分内容尚未完成，游玩 VUCE 制作的冷战内容可能会影响您的游戏体验。

---

## 📅 计划路线图
* [ ] 寻找潜在冲突
* [ ] 添加额外冷战舰船部件
* [ ] 统一配件数值风格

---

## ⚠️ 注意事项
* **加载顺序**: 请将本模组放置在 VNR 和 UTTNH **之后**。
* **兼容包**:
    * [VNR + ETT 1960 Compatch](https://steamcommunity.com/sharedfiles/filedetails/?id=3167054950)
    * [VNR + UTTNH + RT56 Compatch](https://steamcommunity.com/sharedfiles/filedetails/?id=3457591333)
    * [KNR + UTTNH Compatch](https://steamcommunity.com/sharedfiles/filedetails/?id=3663581410)

---

## 💻 本地部署指南
若要从 GitHub 下载并进行本地部署，请参考以下步骤：

> [!WARNING]
> 不要下载源码后直接启用本模组，至少需要确保删除 interface 下的 src 文件夹及其子文件夹下的所有 .gfx 文件。

1. **放置项目**：将本项目文件夹放置在：
   `你的游戏文档路径（不是安装路径，一般是 C:\Users\<用户名>\Documents\Paradox Interactive\Hearts of Iron IV）\mod\`
2. **新建引导文件**：在上述文件夹中新建一个名为 `xxx.mod` 的文本文件。
3. **同步描述信息**：将本项目中 `descriptor.mod` 的内容全部复制到该文件中。
4. **添加绝对路径**：在文件末尾添加一行：
   `path="<盘符>:/Users/<用户名>/Documents/Paradox Interactive/Hearts of Iron IV/mod/VNR-UTTH"`
5. **删除文件**：删除 interface/src 下的所有 .gfx 文件。

运行 `release.py` 可以快速生成一个发行版 mod（删除了绝大部分非必要文件），通过编辑 `release.ignore`（规则和 `.gitignore` 类似）实现黑名单过滤。

> [!NOTE]
> 运行 `release.py` 时记得更改导出文件夹路径，**每次导出前会删除导出文件夹里的所有内容**。
