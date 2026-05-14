# 🔐 Password Vault 4.0 – Secure Offline Credential Storage

Password Vault 4.0 is a **fully offline**, **AES‑256‑GCM encrypted**,  
**identity‑aware** credential storage module for **SIRIUS LOCAL AI Runtime 4.0**.

It provides deterministic, safe, and OWNER‑controlled password management  
without cloud sync, telemetry, or external dependencies.

---

# 1. 🎯 Purpose

Password Vault 4.0 enables SIRIUS to:

- store credentials securely  
- retrieve them deterministically  
- enforce identity‑aware access  
- integrate with workflows and NL commands  
- operate fully offline  
- protect sensitive data with modern cryptography  

The vault is designed for **local‑only**, **tamper‑resistant**,  
**family‑safe** credential management.

---

# 2. 🧱 Architecture Overview

Password Vault 4.0 consists of four internal layers:

### **1. vault_api.py**  
Public interface for all vault operations.

### **2. vault_core.py**  
Implements logic for storing, retrieving, updating, and deleting entries.

### **3. vault_storage.py**  
Handles encrypted JSON container on disk.

### **4. vault_crypto.py**  
AES‑256‑GCM encryption + PBKDF2‑HMAC‑SHA256 key derivation.

---

# 3. 🔐 Cryptography

### **Encryption:**  
- AES‑256‑GCM  
- 12‑byte IV  
- authentication tag included in ciphertext  

### **Key Derivation:**  
- PBKDF2‑HMAC‑SHA256  
- 200,000 iterations  
- deterministic salt for stable vault key  

### **Storage Format:**  
Encrypted JSON file containing:

```json
{
  "entries": {
    "example.com": {
      "username": "user123",
      "password": "encrypted",
      "meta": {}
    }
  }
}
```

---

# 4. 🛡 Identity Enforcement (Security Family 4.0)

Password Vault strictly follows identity rules:

| Identity | Permissions |
|---------|-------------|
| **OWNER** | full read/write/delete |
| **FAMILY** | read‑only |
| **STRANGER** | denied |

All access is routed through:

- Security Family 4.0  
- NL Router 4.0  
- Runtime Core 4.0  

No module may bypass these rules.

---

# 5. 🧠 NL Router Integration

Password Vault adds natural language commands:

- “ulož heslo pre …”  
- “zobraz heslo pre …”  
- “vymaž heslo pre …”  
- “čo mám uložené vo vaulte?”  

NL Router → RuntimeManager → vault_api → vault_core → vault_storage → vault_crypto

---

# 6. ⚙️ RuntimeManager Tasks

RuntimeManager exposes deterministic tasks:

- `vault.store_credential`  
- `vault.get_credential`  
- `vault.delete_credential`  
- `vault.list_credentials`  

All tasks enforce identity and capability boundaries.

---

# 7. 📁 File Location

Vault file is stored locally:

```
/sirius_data/vault/password_vault.json.enc
```

- encrypted  
- tamper‑resistant  
- OWNER‑protected  

---

# 8. 🧪 Testing Requirements

Password Vault must pass:

- encryption/decryption tests  
- identity enforcement tests  
- tamper detection tests  
- workflow integration tests  
- NL routing tests  
- deterministic behavior tests  

---

# 9. 🚫 Non‑Goals

Password Vault does **not**:

- sync to cloud  
- send telemetry  
- store plaintext  
- auto‑fill browser fields  
- integrate with external password managers  

These features are intentionally excluded for security.

---

# 10. 📌 Module Status

**Version:** 4.0.0 (Stable)  
Password Vault is a **finalized**, **frozen**, **production‑ready** module.  
No further structural changes are planned.

