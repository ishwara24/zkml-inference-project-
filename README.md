# zkML Inference with TinyNet Model (Privacy-Preserving AI on Blockchain)

This project demonstrates how to perform privacy-preserving AI inference using a simple PyTorch model (TinyNet) and generate zero-knowledge proofs with the EZKL framework.

The goal is to ensure that:
- The model runs inference off-chain
- A zero-knowledge proof is generated
- The proof is verified on-chain without revealing the input or model internals

---

## 🔧 Project Structure

| File | Purpose |
|------|---------|
| `export_to_onnx.py` | Python script to convert the PyTorch model to ONNX format |
| `model.onnx`        | ONNX version of the TinyNet model |
| `model.compiled`    | Compiled circuit version for EZKL (may need regeneration) |
| `input.json`        | Example input to test inference |
| `settings.json`     | EZKL compile configuration (can be adjusted if needed) |
| `commands.txt`      | Full command history to repeat or debug this setup |

---

## 📌 Requirements

- EZKL version: `v7.2.0`
- Python version: 3.12+
- Rust & Cargo installed
- ONNX and PyTorch libraries installed (see Python script)

---

## 🛠 Setup Instructions (High-Level)

1. Clone EZKL:

```bash
git clone --branch v7.2.0 https://github.com/zkonduit/ezkl.git
cd ezkl
cargo build --release
