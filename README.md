# Image-recognition
Devtown project
# Vision AI in One Day – CIFAR-10 (Bootcamp Submission)

An end-to-end image recognition project that compresses a 5-day curriculum into a single workflow.  
**Tech:** TensorFlow/Keras, Transfer Learning (MobileNetV2), Streamlit demo app.

## 🚀 Quick Start
### Option A — Colab (recommended)
1. Open `Vision_AI_OneDay_Colab.ipynb` in **Google Colab**.
2. **Enable GPU:** Runtime → Change runtime type → **T4 GPU**.
3. **Run all** cells. Artifacts will be saved:
   - Models: `cnn_cifar10.h5`, `aug_cnn_cifar10.h5`, `mobilenetv2_cifar10.h5`
   - Plots: `samples_grid.png`, `cnn_accuracy.png`, `cnn_loss.png`, `cnn_confusion_matrix.png`, `aug_accuracy.png`, `tl_val_acc.png`, `tl_confusion_matrix.png`

### Option B — Local Streamlit App
```bash
# 1) Create a fresh env (optional)
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\\Scripts\\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Make sure model file exists in the same directory:
#    mobilenetv2_cifar10.h5  (export it from the Colab notebook)

# 4) Run the app

streamlit run app.py

Open the local URL from Streamlit and upload any image; the app predicts one of CIFAR-10 classes.

🧪 Project Structure

.
├── Vision_AI_OneDay_Colab.ipynb
├── app.py                     # Streamlit demo
├── requirements.txt
├── README.md                  # short readme (optional)
├── README_GITHUB.md           # this file (detailed)
├── mobilenetv2_cifar10.h5     # exported from notebook (add after training)
├── plots/                     # (optional) store generated plots here
└── models/                    # (optional) store .h5 files here

📊 Results (fill with your numbers)
CNN Val Accuracy: xx.x%

Augmented CNN Val Accuracy: yy.y%

Transfer Learning Val Accuracy: zz.z% (expected best)

Notes: e.g., augmentation improved generalization; TL converged faster.

Add screenshots of tl_val_acc.png and confusion matrices to this section.

🧩 How It Works
Baseline CNN: small Conv → Pool blocks on 32×32 inputs.

Augmentation: rotation/shift/flip via ImageDataGenerator.

Transfer Learning: MobileNetV2 (Imagenet) with head replaced; resized inputs to 96×96; optional fine-tuning of last ~30 layers.

🎥 30-sec Demo (what to record)
Open final prediction cell in the notebook or the Streamlit app.

Upload an image (e.g., a car, dog, ship).

Show predicted label and confidence.

📦 Submission Pack
Notebook (.ipynb), exported models (*.h5), and plots (.png).

Slides: Vision_AI_OneDay_Slides.pptx (export to PDF if required).

GitHub repo link + Demo video link.

🛠 Requirements
See requirements.txt. Tested with Python 3.10+ and TensorFlow 2.15+.

📄 License
MIT (or add your preferred license).

👩‍💻 Author
Sakshi • Vision AI in One Day (Bootcamp: BUILD AN AI THAT SEES)


---

### Also handy (from earlier)
- Colab notebook (end-to-end): [Download `Vision_AI_OneDay_Colab.ipynb`](sandbox:/mnt/data/Vision_AI_OneDay_Colab.ipynb)  
- Slides template (5 slides): [Download PPTX](sandbox:/mnt/data/Vision_AI_OneDay_Slides.pptx)  
- Quick checklist: [Download](sandbox:/mnt/data/submission_checklist.txt)

Need me to turn the LinkedIn post into a **graphic card** or tailor the README to your **actual metrics** once you run the notebook? ​:contentReference[oaicite:0]{index=0}​




