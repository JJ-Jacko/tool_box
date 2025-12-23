# 视频处理相关

## 🚀 使用方法
### 激活环境
```sh
python -m venv .venv
source .venv/bin/activate
```
### 重新编码
遍历 INPUT 文件夹的音视频文件 `mp3, wav, mp4, mov, flv, avi...`

以指定格式 `acc h264 h265 av1` 编码

放入 OUTPUT 文件夹

### 合并图片成 pdf
遍历 INPUT 文件夹的图片文件 `jpg, png...`

按名称顺序合并成一个 pdf 文件

放入 OUTPUT 文件夹

### 反色图片
遍历 INPUT 文件夹的图片文件 `jpg, png...`

反色处理

放入 OUTPUT 文件夹

### 拆分 pdf
遍历 INPUT 文件夹的 `pdf` 文件

拆分成图片

放入 OUTPUT 文件夹

### 凌乱文件重命名
遍历 INPUT 文件夹指定格式的文件

以指定命名格式重命名

放入 OUTPUT 文件夹

报告重复文件的次数和对应路径及哈希值

### 统计文件
遍历 INPUT 文件夹及子文件夹

报告不同类型文件出现的次数

### 批量解压文件
遍历 INPUT 文件夹的压缩包 `zip, 7z, rar, gz, tar, xz...`

解压缩

放入 OUTPUT 文件夹

### 提取指定格式的文件
遍历 INPUT 文件夹及子文件夹

提取指定格式的文件

去重

按排序重命名

放入 OUTPUT 文件夹

报告重复文件的次数和对应路径及哈希值

