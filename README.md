# VNR+UTTNH Compatch Expand (VUCE)

[![Steam Workshop](https://img.shields.io/badge/Steam-Workshop-blue?logo=steam)](https://steamcommunity.com/sharedfiles/filedetails/?id=3164741523)
[![GitHub Releases](https://img.shields.io/badge/GitHub-Releases-orange?logo=github)](https://github.com/foxr-lolunwer/VNR-UTTH/releases)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)

🌐 [Chinese Version / 中文版](README_zh.md)

## Version Info
* **MOD Ver:** `Neo 1.8.4`
* **VNR Ver:** `v2.11 - "Tokyo Bay Finale"` (2026.6.22)
* **UTTNH Ver:** `Jan 11, 2026`

## 🔗 Quick Links
* **Steam Workshop:** [Subscribe Here](https://steamcommunity.com/sharedfiles/filedetails/?id=3164741523)
* **GitHub Releases:** [Download Manual Version](https://github.com/foxr-lolunwer/VNR-UTTH/releases) (Suitable for manual installation or rolling back to older versions)

---

## 🛠 Features

This mod makes [VNR](https://steamcommunity.com/sharedfiles/filedetails/?id=2993766165) and [UTTNH](https://steamcommunity.com/sharedfiles/filedetails/?id=3413890094) compatible, expanding your VNR experience into the 1990s!

It bridges the gap between UTTNH's vanilla-style designer and VNR's advanced systems, guiding the technology tree from 1955 up to the 90s.

> [!WARNING]
> **Notice:** Some Cold War naval content is currently unfinished. Playing VUCE-produced Cold War content may result in an incomplete experience.

---

## 📅 Roadmap
* [ ] Look for potential conflict issues
* [ ] Add additional Cold War ship parts
* [ ] Align UTTNH accessory values with VNR style

---

## ⚠️ Notes
* **Load Order**: Place this mod **AFTER** VNR and UTTNH.
* **Compatibility Pack**:
    * [VNR + ETT 1960 Compatch](https://steamcommunity.com/sharedfiles/filedetails/?id=3167054950)
    * [VNR + UTTNH + RT56 Compatch](https://steamcommunity.com/sharedfiles/filedetails/?id=3457591333)
    * [KNR + UTTNH Compatch](https://steamcommunity.com/sharedfiles/filedetails/?id=3663581410)

---

## 💻 Local Deployment Guide
If you want to download from GitHub and deploy locally, please follow these steps:

> [!WARNING]
> DO NOT enable this mod directly after downloading the source code. You must at least ensure that all `.gfx` files under the `interface/src` folder and its subfolders are deleted.

1. **Place the Project**: Place the project folder into:
   `Your Game Documents Path (NOT the installation path, usually C:\Users\<Username>\Documents\Paradox Interactive\Hearts of Iron IV)\mod\`
2. **Create Boot File**: Create a new text file named `xxx.mod` in the above folder.
3. **Sync Description**: Copy all content from `descriptor.mod` in the project into this new file.
4. **Add Absolute Path**: Add a new line at the end of the file:
   `path="<Drive>:/Users/<Username>/Documents/Paradox Interactive/Hearts of Iron IV/mod/VNR-UTTH"`
5. **Delete Files**: Delete all `.gfx` files under `interface/src`.

You can run `release.py` to quickly generate a production release of the mod (which removes most non-essential files). Blacklist filtering can be configured by editing `release.ignore` (rules are similar to `.gitignore`).

> [!NOTE]
> Remember to change the export folder path when running `release.py`. **Every export will completely delete all existing contents in the target export folder.**
