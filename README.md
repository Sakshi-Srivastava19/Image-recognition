# Image-recognition
Devtown project
# Vision AI in One Day: CIFAR-10 Image Recognition

A compressed end-to-end project: dataset → CNN → augmentation/evaluation → transfer learning (MobileNetV2) → demo.

## Quick Start (Google Colab)
1. Open **Vision_AI_OneDay_Colab.ipynb** in Google Colab.
2. Enable GPU: *Runtime → Change runtime type → T4 GPU*.
3. Run all cells. Keep epochs small if you’re rushing (8–10 for CNN, 5–8 for TL).

## Project Structure
- **Simple CNN** on CIFAR-10
- **Data Augmentation** and metrics: accuracy, precision, recall, F1, confusion matrix
- **Transfer Learning** with MobileNetV2 (fine-tune last ~30 layers)
- **Demo**: Single image prediction

## Results (Example Template)
- CNN Val Accuracy: ~X%
- Augmented CNN Val Accuracy: ~Y%
- Transfer Learning Val Accuracy: ~Z%
- Key Insights: (write 2–3 bullets)

## How to Record the 30-sec Demo
- Use a screen recorder while running the last prediction cell.
- Show one image upload and the predicted label.

## Add to Portfolio
- Add plots saved by the notebook to this README.
- Upload `*.h5` models and key images:
  - `samples_grid.png`, `cnn_accuracy.png`, `cnn_loss.png`, `cnn_confusion_matrix.png`
  - `aug_accuracy.png`, `tl_val_acc.png`, `tl_confusion_matrix.png`

## Environment
- Python 3.x, TensorFlow 2.x, scikit-learn

## Author
Sakshi – Vision AI in a Day (Bootcamp Submission, 2025-08-13)

