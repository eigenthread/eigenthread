
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

## License
This document is provided for educational purposes. Use at your own discretion and follow Hugging Face’s guidelines.
