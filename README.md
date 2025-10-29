# Multi-Person Detection and Re-identification

This project implements a state-of-the-art multi-object tracking system that combines motion and appearance information with camera-motion compensation and accurate Kalman filtering.

## Key Features

  * Multi-person detection and tracking
  * Person re-identification (ReID)
  * YOLOX & YOLOv7 support
  * Multi-class object tracking
  * Camera motion compensation
  * Real-time video processing

## 📖 Performance Highlights

  * **MOT17 Dataset:** 80.5 MOTA, 80.2 IDF1, 65.0 HOTA
  * **MOT20 Dataset:** 77.8 MOTA, 77.5 IDF1, 63.3 HOTA

## 💻 System Requirements

  * **Operating System:** Ubuntu 20.04 (tested) or Windows 10/11
  * **Python:** 3.7
  * **CPU:** Multi-core processor (Intel i5 or better recommended)
  * **RAM:** 8GB minimum, 16GB recommended
  * **Storage:** 5GB free space for models and dependencies

## 🚀 Installation Guide

### Step 1: Install Anaconda/Miniconda

If you don't have Conda installed, download and install Miniconda from: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

### Step 2: Create Conda Environment

Open your terminal/command prompt and run:

```bash
conda create -n botsort_env python=3.7
conda activate botsort_env
```

### Step 3: Install PyTorch (CPU Version)

Install PyTorch for CPU-only usage via Conda:

```bash
conda install pytorch torchvision cpuonly -c pytorch
```

Or using pip:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Step 4: Clone the Repository

```bash
git clone https://github.com/KraitOPP/Multi-Person-Detection-and-Reidentification.git
cd Multi-Person-Detection-and-Reidentification
```

### Step 5: Install Required Dependencies

```bash
pip install -r requirements.txt
python setup.py develop
```

### Step 6: Install Additional Packages

```bash
# Install pycocotools
pip install cython
pip install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

# Install Cython-bbox
pip install cython_bbox

# Install faiss for CPU
pip install faiss-cpu
```

## 📥 Download Pretrained Models

### Model Files Required

Create a `pretrained` folder in the project root directory:

```bash
mkdir pretrained
```

### Download Models from Google Drive

Download the following pretrained models and extract them to the `pretrained` folder:

**Google Drive Link:** [https://drive.google.com/file/d/1rCEIYGc2kC2qbiT6XggOPbV3DELpwDLf/view?usp=sharing](https://drive.google.com/file/d/1rCEIYGc2kC2qbiT6XggOPbV3DELpwDLf/view?usp=sharing)

The `pretrained` folder should contain these files:

  * `bytetrack_x_mot20.tar`
  * `mot20_sbs_S50.pth`
  * `yolox_x.pth`

### Folder Structure

After extraction, your project structure should look like:

```plaintext
Multi-Person-Detection-and-Reidentification/
│
├── pretrained/
│   ├── bytetrack_x_mot20.tar
│   ├── mot20_sbs_S50.pth
│   └── yolox_x.pth
│
├── tools/
├── yolox/
├── fast_reid/
├── requirements.txt
└── setup.py
```

## ▶️ Running the Project (CPU Mode)

### Basic Demo with Video File

To run person detection and tracking on a video file (make sure to add `--device cpu`):

```bash
python tools/demo.py video --path videos/cam1_street_trim.mp4 -f exps/example/mot/bytetrack_x_mot20.py -c pretrained/bytetrack_x_mot20.tar --with-reid --fast-reid-config fast_reid/configs/MOT20/sbs_S50.yml --fast-reid-weights pretrained/mot20_sbs_S50.pth --fuse-score --save_result --device cpu
```

**Note:** The original command was missing `--device cpu` and included `--fp16`. The command above is corrected for a CPU-only setup as per the guide's recommendations.

## ⚙️ Important Parameters

### Commonly Used Flags

  * `--path`: Path to video file, image folder, or webcam ID
  * `--with-reid`: Enable re-identification module
  * `--fuse-score`: Use fused detection and ReID scores
  * `--save_result`: Save output video/images
  * `--device cpu`: **Force CPU usage** (important for CPU-only setup)
  * `-c`: Path to checkpoint/model file
  * `-f`: Path to experiment configuration file

### View All Available Options

```bash
python tools/demo.py -h
```

## ⚠️ Performance Notes for CPU Mode

When running on CPU without GPU acceleration:

  * **Processing Speed:** Expect slower frame rates compared to GPU (approximately 5-15 FPS depending on your CPU).
  * **Video Resolution:** Lower resolution videos will process faster.
  * **Optimization Tips:**
      * Use smaller input resolution with the `--input-size` parameter.
      * **Disable** the `--fp16` flag (it is not beneficial on CPU).
      * Remove `--fuse-score` if ReID fusion is not critical.

## 📂 Output

Results will be saved in the following locations:

  * **Tracked Videos:** `YOLOX_outputs/yolox_x_mix_det/track_vis/`
  * **Tracking Results (TXT):** `YOLOX_outputs/yolox_x_mix_det/track_results/`
  * **Detection Visualizations:** Output folder specified in command

## 🔍 Troubleshooting

### Common Issues

**Issue 1: `ImportError` for torch**

  * **Solution:** Ensure PyTorch is properly installed for CPU. Re-run the installation command:
    ```bash
    conda install pytorch torchvision cpuonly -c pytorch
    ```

**Issue 2: CUDA errors on a CPU-only machine**

  * **Solution:** You must always add the `--device cpu` flag to your `demo.py` command.

**Issue 3: Out of memory errors**

  * **Solution:** Process lower resolution videos or reduce the batch size (if applicable).

**Issue 4: Slow processing**

  * **Solution:** This is expected for CPU mode. Consider:
      * Reducing the input video resolution.
      * Processing shorter video clips.
      * Using lighter model variants (if available).

## 📁 Project Structure

```plaintext
Multi-Person-Detection-and-Reidentification/
│
├── pretrained/         # Pretrained model weights
├── tools/              # Main execution scripts
│   ├── demo.py         # Demo script for single-class
│   ├── mc_demo.py      # Multi-class demo script
│   └── track.py        # Tracking evaluation script
├── yolox/              # YOLOX detector implementation
├── fast_reid/          # ReID module
├── tracker/            # Tracking algorithms
├── requirements.txt    # Python dependencies
└── setup.py            # Installation script
```

## 🙏 Acknowledgments

This project builds upon:

  * ByteTrack
  * FastReID
  * YOLOX
  * YOLOv7
