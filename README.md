# TestMCP OpenAI 项目

这是一个使用 FastAPI 实现的 OpenAI 兼容接口项目，提供 chat/completions 和 embeddings 两个主要功能。

## 功能特性

- **Chat Completion**: 使用 qwen2.5:0.5b 模型生成文本回复
- **Text Embedding**: 使用 nomic-embed-text:latest 模型计算文本向量
- **API 鉴权**: 使用 API Key 进行接口访问控制
- **Web 界面**: 提供美观的 Web 界面进行功能测试

## 快速开始

1. 安装依赖
```bash
pip install -r requirements.txt
```

2. 启动服务
```bash
python main.py
```

3. 访问 Web 界面
打开浏览器访问 http://localhost:8000

## API 使用

### Chat Completion
```bash
curl -X POST http://localhost:8000/chat/completions \
  -H "API-Key: your-secret-api-key" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "你好", "max_tokens": 100}'
```

### Text Embedding
```bash
curl -X POST http://localhost:8000/embeddings \
  -H "API-Key: your-secret-api-key" \
  -H "Content-Type: application/json" \
  -d '{"text": "这是一个测试文本"}'
```

## 项目结构
```
testmcp-openai/
├── main.py              # 主程序
├── requirements.txt     # 依赖文件
├── README.md            # 项目说明
├── static/              # 静态文件
│   ├── style.css        # 样式表
│   └── script.js        # JavaScript
└── templates/           # 模板文件
    └── index.html       # 主页面
```

## 注意事项

1. 请确保本地 http://localhost:11434/v1 服务已启动
2. 生产环境请修改默认的 API Key
3. 建议使用环境变量管理敏感信息
