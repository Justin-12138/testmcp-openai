# testmcp-openai 项目

这是一个使用 FastAPI 实现的 OpenAI 兼容 API 服务，支持聊天和文本嵌入功能。

## 功能特性

- 支持 `/api/v1/chat/completions` 接口
- 支持 `/api/v1/embeddings` 接口
- 提供简单的前端聊天界面
- 支持 Docker 部署

## 技术栈

- Python 3.9
- FastAPI
- Uvicorn
- Docker

## 快速开始

### 本地运行

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动服务：
   ```bash
   uvicorn app.main:app --reload
   ```

3. 访问 http://localhost:8000

### Docker 运行

1. 构建镜像：
   ```bash
   docker build -t testmcp-openai .
   ```

2. 运行容器：
   ```bash
   docker run -p 8000:8000 testmcp-openai
   ```

3. 访问 http://localhost:8000

## API 文档

访问 http://localhost:8000/docs 查看 API 文档

## 项目结构

```
testmcp-openai/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── api.py
├── static/
│   ├── style.css
│   └── main.js
├── templates/
│   └── index.html
├── requirements.txt
├── Dockerfile
└── README.md
