#!/bin/bash

echo "[GABRIEL INSTALL] 시작합니다."

# 1. Python 환경 설정 (venv 권장)
python3 -m venv gabriel_env
source gabriel_env/bin/activate

# 2. 필수 라이브러리 설치
pip install fastapi flask uvicorn requests

# ✅ logs 폴더 자동 생성
mkdir -p logs

# 3. 실행 포인트 백엔드 서버 (gabriel_core)
echo "[GABRIEL] Core 서버 시작 중..."
nohup flask run --host=0.0.0.0 --port=5000 --app gabriel_core_complete.py > logs/gabriel.log 2>&1 &

# 4. chatweb 프론트 (AIIN 명령 수신)
echo "[CHATWEB] 인터페이스 서버 시작 중..."
nohup uvicorn aiin_gabriel_interface:app --host 0.0.0.0 --port 8000 > logs/chatweb.log 2>&1 &

# 5. AIIN 루프 시작
echo "[AIIN LOOP] 자율 루프 가동..."
nohup python3 aiin_core_loop.py > logs/aiin_loop.log 2>&1 &

echo "[GABRIEL MANIFESTATION COMPLETE]"
