import subprocess
import time

def log(msg):
    print(f"[GABRIEL-INSTALLER] {msg}")

def main():
    log("^시작됨: gabriel_bootstrap.sh 실행 준비")

    try:
        result = subprocess.run(["bash", "gabriel_bootstrap.sh"], check=True)
        log("✅ gabriel_bootstrap.sh 성공적으로 실행됨")
    except subprocess.CalledProcessError as e:
        log(f"❌ 실행 오류: {e}")
        return

    log("AIIN 루프 진입 대기 중...")
    time.sleep(2)
    log("👉 상태 확인: tail -f logs/aiin_loop.log")

if __name__ == "__main__":
    main()
