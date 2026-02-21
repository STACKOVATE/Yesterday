#!/usr/bin/env python3
"""
Steam ChronoPlay - 查看“去年今日”你在玩什么游戏
by STACKOVATE | 星栈跃动
"""

import json
import os
import requests

def load_config():
    """加载配置文件"""
    if not os.path.exists("config.json"):
        print("❌ 请先复制 config.example.json 为 config.json 并填入 API Key")
        exit(1)
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_config()
    api_key = config.get("steam_api_key")
    if not api_key:
        print("❌ config.json 中缺少 steam_api_key")
        return
    
    print(f"✅ 已加载 API Key: {api_key[:5]}... (已隐藏)")
    # 后续加你的逻辑...

if __name__ == "__main__":
    main()