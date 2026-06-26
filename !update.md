可参照如下步骤更新

# common
## ai_equipment
用空文件来替换UTTNH或其他模组的海军内容（fleet/naval...）
**随UTTNH更新**
## defines
**直接将VNR的文件粘贴过来**
## on_actions
拓展内容，**不需要更新**
## scripted_effects
拓展内容，**不需要更新**
## scripted_guis
### 00_navy_rework_welcome_splash_gui
如果VNR更改了ui文件，需要同步更新
ui内容属于稍微高级一点的功能，如果没有相关知识：
如果影响到了游戏（比如崩溃，布局错误，重要内容显示不全），直接删除本文件
如果没有，就不要管
如果有相关知识：
注意新添加的tab页逻辑就好
### VUCE_niche_intro_container
用来显示舰船设计器中舰船类别按钮右下方的问号按钮的，不需要更新，除非舰船设计器布局发生了很大变化
## scripted_localisation
拓展内容，**不需要更新**
## special_projects
**直接替换为VNR文件**
## technologies
### MTG_naval
**直接换成VNR的**
仅用于提供跨模组兼容，覆盖UTTNH的海军科技为VNR的，如果有一天VNR将UTTNH添加到了依赖，可以删除该文件
### MTG_naval_Support
**逐个比对**
需要仔细比对，修改项目已经用VUC(E)注释标注
应用VNR的更新内容，保留桥接内容（主要是路径属性）
如果科技位置发生变化，需要额外检查嫁接的科技树位置
### naval
男人大炮DLC已并入本体游戏，但UTTNH或VNR或原版依旧保留了文件
这个文件不是必要的，也**不需要更新**
为了兼容性，保留了科技id，但清空了所有效果
### VUC_replace_tech
兼容模组替换的UTTNH科技
比如雷达科技。UTTNH和VNR都提供了更高级的雷达，UTTNH写在了电子科技树里。为了最大兼容性，没有覆盖电子科技树，而是覆写了科技（去除了重合的雷达科技，部分科技有额外效果）
**如果UTTNH没有更新电子科技树，这个文件就不需要更新**
### VUCE_naval
**只有在UTTNH更新海军科技的情况下才可能需要更新**
冷战拓展科技的船体科技（还有其他的）使用的是UTTNH的id。同时，它们的纹理也是引用的UTTNH的纹理
如果原版发生了对海军内容做了重大更新，也需要检查额外内容
### VUCE_ex_tech
废弃的文件，原本是用于冷战战力跃升的，目前可以删除
## technology_tags
一般不需要更新
更新时需要参照UTTNH，记得保留VUCE的海军界面
## units
对于覆盖的**单位类别**，直接**用VNR文件覆盖**即可
对于**装备**，需要**仔细比对**（特殊位置有标记）
对于**模块**，VNR更新时一般**不需要处理**，UTTNH更新海军模块时需要具体分析
## script_enums
基本不影响游戏，**可跳过更新**
根据运行时log更新，提示缺什么就加什么
# gfx
**一般不需要更新**
# interface
主要关注：
- countrytechtreeview
- equipmentdesignerview
## countrytechtreeview
大多数情况下VNR或UTTNH更新时必须同步更新
VNR提供海军的两个部分
UTTNH的文件作为基底
VNR更新时，将VNR的海军内容标签页复制到一个临时文件中，再将原来的海军内容标签页复制到另一个临时文件中。比对这两个文件的异同，将比对完成后的文件覆盖到本模组中（有标记）
UTTNH更新时，将除了海军标签页的内容直接替换
注意不要遗漏VUCE的海军标签页
也就是mtgnavalfolder和mtgnavalsupportfolder
**mtgnavalfolder可以直接用VNR的覆盖**
**mtgnavalsupportfolder需要仔细比对**
## equipmentdesignerview
用来拓展舰船类别选择窗口，使其能够装得下VUCE添加的新类别
**一般只有钢四本体和VNR偶尔会动这个文件**，注意比对
## equipmentdesigner
如果VNR更新了，**直接覆盖**
# localisation
需要运行python脚本，负责需要逐个重命名
分别将VNR的中文和英文文件分别全部拷贝到对应文件夹中（也可以只选更新的文件），然后在localisation目录下运行src_copy.py
一般而言，命令为：
`python src_copy.py`
# descriptor.mod
更新完毕后进入游戏检查没问题后，加一下版本号后上传github
然后运行release.py生成发行版（去掉非必要文件，节省订阅者磁盘空间）
把发行版上传到steam工坊和github release

# VSCode 工作区配置参考
可以相对方便地进行维护
```json
{
	"folders": [
		{
			"name": "VNR+UTTH",
			"path": "."
		},
		{
			"name": "A VNR+UTTH",
			"path": "../A VNR+UTTH"
		},
		{
			"name": "VNR + UTTNH + RT56",
			"path": "../VNR + UTTNH + RT56"
		},
		{
			"name": "KNR + UTTNH",
			"path": "../KNR + UTTNH"
		},
		{
			"name": "VNR-RO",
			"path": "../../../../../SteamLibrary/steamapps/workshop/content/394360/2993772482"
		},
		{
			"name": "KNR-RO",
			"path": "../../../../../SteamLibrary/steamapps/workshop/content/394360/2860531377"
		},
		{
			"name": "UTTNH-RO",
			"path": "../../../../../SteamLibrary/steamapps/workshop/content/394360/3413890094"
		},
		{
			"name": "RT56-RO",
			"path": "../../../../../SteamLibrary/steamapps/workshop/content/394360/820260968"
		}
	],
	"settings": {
		"files.readonlyInclude": {
            "E:/SteamLibrary/steamapps/workshop/content/394360/**": true
        },
		"workbench.editor.enablePreview": false,
		"workbench.editor.enablePreviewFromQuickOpen": false
	}
}
```
# 推荐的VSCode插件
- tboby.cwtools-vscode https://marketplace.visualstudio.com/items?itemName=tboby.cwtools-vscode
- chaofan.hoi4modutilities https://marketplace.visualstudio.com/items?itemName=Chaofan.hoi4modutilities
- dragon-archer.paradox-highlight https://marketplace.visualstudio.com/items?itemName=dragon-archer.paradox-highlight