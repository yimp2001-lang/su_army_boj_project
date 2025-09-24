#!/data/data/com.termux/files/usr/bin/bash
# ↑ 이 줄은 "셰뱅(shebang)"이라고 부름.
# 이 스크립트를 실행할 때 Termux의 bash를 사용하라는 뜻이야.
# (일반 리눅스/맥에서는 보통 #!/bin/bash 를 씀)
#
#
set -e

if [ $# -lt 1 ]; then
  echo "Usage: $0 <problem_dir>   e.g. $0 gold4/1167_tree_diameter"
  exit 1
fi

target="$1"

if [ ! -f "$target/main.py" ]; then
  echo "Error: $target/main.py not found"
  exit 1
fi

if [ ! -f "$target/input.txt" ]; then
  echo "Warning: $target/input.txt not found. Running without stdin."
  python3 "$target/main.py"
else
  python3 "$target/main.py" < "$target/input.txt"
fi


"""
set -e
# 에러가 발생하면 스크립트를 바로 종료하도록 설정.
# (안 그러면 에러가 나도 뒤에 명령들이 실행될 수 있음)

target="$1"
# $1 = 스크립트를 실행할 때 넘긴 첫 번째 인자(argument).
# 예: ./scripts/run_local.sh gold4/1167_tree_diameter
#     → 그러면 target="gold4/1167_tree_diameter"

python3 "$target/main.py" < "$target/input.txt"
# 실제 실행 부분.
# target 경로 안에 있는 main.py 를 실행하면서
# input.txt 파일을 표준 입력(stdin)으로 연결해줌.
# 즉 "python3 gold4/1167_tree_diameter/main.py < gold4/1167_tree_diameter/input.txt" 와 같음.
"""
