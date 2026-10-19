# Learn

深度学习学习笔记：d2l 教程 notebook + PyTorch 练习代码。

## 目录结构

```
Learn/
├─ d2l/                    d2l 教程 notebook
├─ pytorch/                PyTorch 练习脚本
│  ├─ Dataset.py           自定义 Dataset
│  ├─ TensorBoard.py       TensorBoard 试用
│  ├─ ClassTest.py
│  ├─ data/                ants/bees 图片（不入库，需本地准备）
│  └─ dataset/             同上（不入库）
├─ logs/                   TensorBoard 事件文件（不入库）
├─ LoadDataset.py
└─ requirements.txt
```

## 环境准备（新设备首次）

需要 Python 3.11。用 conda：

```bash
conda create -n pytorch python=3.11
conda activate pytorch
pip install -r requirements.txt
```

当前 `requirements.txt` 里的 `torch` 是 **CPU 版**。若新设备有 NVIDIA 显卡，改用 CUDA 版：

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

然后在 VS Code 里 `Ctrl+Shift+P` → `Python: Select Interpreter` 选中该 conda 环境。

## 数据集

图片数据集（约 90MB）**不在仓库里**，需要在新设备上自行准备，并保持相同相对路径：

```
pytorch/data/train/ants_image/*.jpg
pytorch/data/train/bees_image/*.jpg
pytorch/data/val/ants/*.jpg
pytorch/data/val/bees/*.jpg
```

从旧设备拷贝，或重新下载 [hymenoptera_data](https://download.pytorch.org/tutorial/hymenoptera_data.zip)。

## 跨设备同步流程

### 日常三步

```bash
git pull                                  # 开始学习前：先拿最新
git add -A && git commit -m "说明改了什么"  # 学完：存档
git push                                  # 上传
```

> commit 只存到本机，push 才上云。**关机/换设备前一定要 push。**

### 新设备第一次

```bash
git clone https://github.com/makesisisi/Learn.git
```

然后按上面「环境准备」「数据集」两步配好环境。

### 状态速查

| `git status -sb` 输出 | 含义 | 该做什么 |
|---|---|---|
| `## main...origin/main` | 已同步 | 直接开始 |
| `## main...origin/main [behind 3]` | 远程有更新 | `git pull` |
| `## main...origin/main [ahead 1]` | 本地有未推送提交 | `git push` |
| `## main...origin/main [ahead 1, behind 1]` | 两边都有新提交 | `git pull` 合并后再 push |

VS Code 左侧「源代码管理」面板（`Ctrl+Shift+G`）等价操作：文件旁 **+** 暂存 → 输入框写消息点 **✓** 提交 → 状态栏 **同步**按钮拉取/推送。

### 避免冲突

- **一台设备开始前 pull，结束后 push**；
- **不要在两台设备上同时编辑同一个 `.ipynb`** —— notebook 是 JSON，冲突后难以手工修复。

真撞上了：

```bash
git pull                 # 提示 CONFLICT
# VS Code 里打开冲突文件，选 Accept Current / Incoming / Both
git add <冲突文件>
git commit
git push
```

### 不同步的内容

`data/`、`dataset/`、`logs/`、conda 环境都不会进仓库（见 `.gitignore`）。
`.vscode/launch.json` 与 `.vscode/settings.json` 会同步，所以调试配置（F5）在每台设备上一致。
