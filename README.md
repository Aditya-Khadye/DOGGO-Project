# Vision Transformer (ViT) – Scalable Image Classification

Machine Learning project implementing the **Vision Transformer (ViT)** architecture, based on Google Research’s paper:  
> _“An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale”_  
> [[arXiv:2010.11929]](https://arxiv.org/abs/2010.11929)

This repository extends the original ViT approach and includes training on both **standard datasets** (CIFAR-10, CIFAR-100) and **custom datasets** (e.g., dog breeds). Developed as part of a Machine Learning course project (CAP5610), this implementation demonstrates how ViTs can scale across datasets and be adapted for real-world image classification tasks.

---

## 🚀 Key Features

- 🧠 Built from scratch based on Google's ViT model
- 📦 Modular architecture: patch sizes, attention heads, layers, embedding sizes
- 🧪 Training pipeline with CLI, evaluation scripts, and experiment tracking
- 🐶 Specialized training on custom dog breed dataset
- 📊 Visualization support (attention maps, training curves via TensorBoard)
- 🖥️ Streamlit interface (experimental)

---

## 📁 Project Structure

```bash
├── vit.py                 # Vision Transformer model
├── train.py               # Training pipeline
├── data_loader.py         # Dataset handling and augmentations
├── final_report.ipynb     # Final experiment results and analysis
├── doggy.py               # Dog breed-specific ViT model
├── app.py                 # Streamlit interface (WIP)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🧪 Example Training Command

```bash
python train.py --dataset custom --data_path ./data --epochs 100 --batch_size 32
```

Supports training from scratch or fine-tuning. Logs are saved for TensorBoard visualization.

---

## 🔧 Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/vision-transformer.git
cd vision-transformer
pip install -r requirements.txt
```

**Dependencies**:  
- Python 3.8+  
- PyTorch, torchvision  
- NumPy, matplotlib, tqdm

---

## 📚 Reference

If you use or build upon this work, please cite the original ViT paper:

```bibtex
@article{dosovitskiy2020image,
  title={An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale},
  author={Dosovitskiy, Alexey and et al.},
  journal={arXiv preprint arXiv:2010.11929},
  year={2020}
}
```

---

## 👥 Contributors

Developed collaboratively for CAP5610 by:

- **Aditya Khadye**  
- **Michael Mendez**  
- **Lauren Suarez**

---

## 📌 Future Enhancements

- [ ] Add pretrained model weights
- [ ] HuggingFace Transformers integration
- [ ] Export to ONNX for deployment
- [ ] Model interpretability tools (e.g., Grad-CAM)

---

## 📄 License

This project is licensed under the MIT License.
