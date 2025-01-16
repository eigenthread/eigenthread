
# Hugging Face Token Management in Google Colab

## Overview
This guide provides step-by-step instructions on generating and securely using a Hugging Face token in Google Colab for optimal interaction with Hugging Face repositories and services.

---

## 1. How to Create a Hugging Face Access Token
1. **Log In to Hugging Face**:
   - Visit [Hugging Face](https://huggingface.co/) and log in.
   - Create an account if you don’t already have one.

2. **Navigate to Settings**:
   - Go to your profile and select **"Settings"** from the dropdown menu.

3. **Generate the Token**:
   - Locate the **Access Tokens** section.
   - Click **"New Token"**, provide a name, and assign permissions.
   - Copy the token securely for use in Colab.

---

## 2. Suggested Permissions for Hugging Face Token
The following permissions depend on your use case:

### **General Use (Read Only)**:
- Enable:
  - **Read access to public repositories.**

### **Development or Contributor Use**:
- Enable:
  - **Read**
  - **Write**
  - **Upload**

### **Private Resource Access**:
- Enable:
  - **Read**
  - **Private Models**

### **Administrative Use**:
- Enable:
  - **Admin** (with caution).

---

## 3. Adding the Hugging Face Token to Google Colab

### **Option A: Using Google Drive to Store the Token Securely**
1. Authenticate and mount Google Drive:
   ```python
   from google.colab import auth
   auth.authenticate_user()

   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. Save the token securely:
   ```python
   token_path = '/content/drive/My Drive/huggingface_token.txt'
   with open(token_path, 'w') as file:
       file.write('your_hugging_face_token_here')
   ```

3. Load and set the token as an environment variable:
   ```python
   import os

   with open(token_path, 'r') as file:
       hf_token = file.read().strip()

   os.environ["HF_TOKEN"] = hf_token
   ```

4. Use the token in your Hugging Face scripts:
   ```python
   from huggingface_hub import HfApi

   api = HfApi()
   api.set_access_token(os.environ["HF_TOKEN"])
   ```

### **Option B: Setting the Token Directly in the Script**
1. Set the token directly as an environment variable:
   ```python
   import os
   os.environ["HF_TOKEN"] = "your_hugging_face_token_here"
   ```

2. Use it in your scripts as shown above.

---

## 4. Repository Permissions Overview

### Permissions for Repositories:
- **Read Access**: For accessing repository contents.
- **Write Access**: For modifying content/settings of repositories.
- **Interact with Discussions**: For opening or commenting on pull requests.

### Tips:
- If you only need access to specific repositories, specify them when creating the token.
- Use restrictive permissions to minimize security risks.

---

## 5. Security Tips
- **Avoid Hardcoding**: Do not embed tokens directly in scripts, especially for shared notebooks.
- **Use Environment Variables**: Store the token in environment variables or Google Drive for secure access.
- **Restrict Permissions**: Only enable necessary permissions to minimize potential misuse.

---

## 6. Example Usage
Here’s a simple script for interacting with Hugging Face using the token:
```python
from huggingface_hub import HfApi
import os

# Set the token as an environment variable
os.environ["HF_TOKEN"] = "your_hugging_face_token_here"

# Authenticate and interact with Hugging Face
api = HfApi()
api.set_access_token(os.environ["HF_TOKEN"])

# Example: List your repositories
repos = api.list_repos()
print(repos)
```

---

# Claim Constructor Copilot Code to by Copy-Pasted into Colab Notebook
```python
!pip install transformers datasets scikit-learn

from transformers import BertTokenizer, BertForSequenceClassification
from datasets import load_dataset
import torch
from torch.utils.data import DataLoader, Dataset
from torch.optim import AdamW
from sklearn.metrics import accuracy_score
from datetime import datetime



# Custom Dataset for HUPD Data
class HUPDDataset(Dataset):
    def __init__(self, data, tokenizer, max_length=128):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        record = self.data[idx]
        title = record.get("title", "")
        abstract = record.get("abstract", "")
        label = record.get("label", 0)  # Default to 0 if label is missing

        # Combine title and abstract
        combined_text = f"Title: {title}\nAbstract: {abstract}"

        # Tokenize the text
        encoded = self.tokenizer(
            combined_text,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )

        input_ids = encoded["input_ids"].squeeze()
        attention_mask = encoded["attention_mask"].squeeze()

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": torch.tensor(label, dtype=torch.long),
        }


# Fine-tune the Pre-trained BERT Model
def fine_tune_model(model, train_dataloader, val_dataloader, epochs=3, lr=5e-5, device="cuda"):
    optimizer = AdamW(model.parameters(), lr=lr)
    model.train()
    model.to(device)

    for epoch in range(epochs):
        total_loss = 0
        model.train()
        for batch in train_dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            # Forward pass
            outputs = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels,
            )
            loss = outputs.loss
            total_loss += loss.item()

            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss / len(train_dataloader):.4f}")

        # Validate after each epoch
        validate_model(model, val_dataloader, device)


# Validate the Model
def validate_model(model, val_dataloader, device="cuda"):
    model.eval()
    model.to(device)
    all_predictions = []
    all_labels = []

    with torch.no_grad():
        for batch in val_dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            predictions = torch.argmax(outputs.logits, dim=-1)

            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    accuracy = accuracy_score(all_labels, all_predictions)
    print(f"Validation Accuracy: {accuracy:.4f}")


# Main Function to Run the Workflow
def main():
    # Configuration
    model_name = "anferico/bert-for-patents"
    batch_size = 8
    max_length = 128
    epochs = 3
    learning_rate = 5e-5
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Specify the date ranges as required by the HUPD dataset API
    train_filing_start_date = "2016-01-01"
    train_filing_end_date = "2016-01-20"
    val_filing_start_date = "2016-01-20"
    val_filing_end_date = "2016-01-31"

    # Load the HUPD dataset with the sample data for debugging
    print("Loading HUPD dataset...")
    try:
        dataset = load_dataset(
            "HUPD/hupd",
            "sample",  # Use sample for debugging
            train_filing_start_date=train_filing_start_date,
            train_filing_end_date=train_filing_end_date,
            val_filing_start_date=val_filing_start_date,
            val_filing_end_date=val_filing_end_date,
        )
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # Perform a uniform split for training and validation
    train_dataset = dataset["train"]
    val_dataset = dataset["validation"]

    # Preprocess datasets
    tokenizer = BertTokenizer.from_pretrained(model_name)
    train_data = HUPDDataset(train_dataset, tokenizer, max_length)
    val_data = HUPDDataset(val_dataset, tokenizer, max_length)

    train_dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    val_dataloader = DataLoader(val_data, batch_size=batch_size, shuffle=True)

    # Load the pre-trained model
    print("Loading the model...")
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

    # Fine-tune the model
    print("Fine-tuning the model...")
    fine_tune_model(model, train_dataloader, val_dataloader, epochs, learning_rate, device)


if __name__ == "__main__":
    main()
```

---



## License
This document is provided for educational purposes. Use at your own discretion and follow Hugging Face’s guidelines.
