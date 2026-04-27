# ☁️ Azure HTTP API - File Metadata Service

A REST API built on Azure Functions that queries and returns metadata about files stored in Azure Blob Storage.

This is my second cloud project, building on serverless architecture to create an API service that connects to cloud storage. 🚀

---

## What it does

Upload files to Azure Blob Storage, then hit the API endpoint to get file information back.

**GET /files** → Returns list of all files with metadata (name, size, upload date, status) 📋

Think: Invoice uploaded → API endpoint tells you file size, when it was uploaded, processing status. ✅

---

## Why it matters

Most companies have data in cloud storage. They need ways to **query that data**. This API shows how to:
- Connect services together (storage + compute) 🔗
- Build REST endpoints on serverless 📡
- Query cloud resources from code 💻

---

## Tech stack

- Azure Functions v4 (HTTP trigger)
- Python 3.11 🐍
- Azure Blob Storage SDK
- Git for version control 📦

---

## Running it locally

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Create local.settings.json**
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

**3. Start Azurite** 
`Cmd+Shift+P` → `Azurite: Start`

**4. Run the function**
```bash
func start
```

**5. Test the API** 🧪
```bash
curl http://localhost:7071/api/files
```

---

## The API

**GET /files**
- Returns all files in Blob Storage 📁
- Response: `[{name, size, upload_date, status}, ...]`

---

## What I'm learning

Building this second project teaches:
- How to build REST APIs on serverless 🔨
- How cloud services communicate with each other 🤝
- Querying cloud resources from code 📊
- Real-world file metadata patterns 🎯

---

## Next steps

- Add error handling for connection failures ⚠️
- Add unit tests 🧪
- Add filtering/search to API 🔍
- Connect this to blob-trigger-function (full pipeline) 🔗
- Deploy to Azure ☁️

---

## Deployment status

🚧 In development - Local testing complete, deploying to Azure soon

---

## Author

**Cecilia | @cecilialabs** — [github.com/cecilialabs](https://github.com/cecilialabs)

Building cloud systems, one project at a time. 🚀

Always building, always learning. 🧠 🌷
