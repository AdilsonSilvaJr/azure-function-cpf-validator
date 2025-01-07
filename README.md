# 🔗 Azure Function CPF Validator

This project contains an Azure Function that validates Brazilian CPF numbers. 🇧🇷

## 🚀 Getting Started

### ✅ Prerequisites

- [🔧 Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)  
- [📘 Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)

### 🛠️ Setup

1. **📂 Clone the repository**:  
   ```bash
   git clone <repository-url>  
   cd azure-function-cpf-validator
   ```

2. **⚙️ Configure the Function App**: Update the `local.settings.json` file with your Azure Function App settings.

3. **☁️ Deploy the Function**: Navigate to the project directory and deploy the function:  
   ```bash
   func azure functionapp publish <your-function-app-name>
   ```

## 📡 Usage

Once deployed, you can validate a CPF number by sending an HTTP request to the function's endpoint.

### 🔍 Example Request
```bash
curl -X POST "https://<your-function-app-name>.azurewebsites.net/api/validacpf" \
-H "Content-Type: application/json" -d '{"cpf": "12345678909"}'
```

### 📋 Example Response
- ✅ **Valid CPF**:  
   ```json
   {
     "valid": true
   }
   ```
- ❌ **Invalid CPF**:  
   ```json
   {
     "valid": false
   }
   ```

## 📜 License

This project is licensed under the MIT License.
