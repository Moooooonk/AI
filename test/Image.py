# 필요한 라이브러리 설치 (터미널에서 아래 명령어 실행 필요)
# pip install diffusers transformers torch accelerate

import torch
from diffusers import StableDiffusionPipeline
import os

# 1. 모델 ID 설정 및 환경 확인
model_id = "CompVis/stable-diffusion-v1-4"

# CUDA 사용 가능 여부 확인
if torch.cuda.is_available():
    device = "cuda"
    print("CUDA GPU를 사용하여 실행합니다.")
else:
    device = "cpu"
    print("CPU를 사용하여 실행합니다. 속도가 느릴 수 있습니다.")

# 2. Stable Diffusion 파이프라인 설정 및 모델 로드
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
pipe = pipe.to(device)

# 3. 텍스트 프롬프트 입력 (사용자가 원하는 스타일 입력 가능)
prompt = "a surrealist painting in the style of Salvador Dali"

# 4. 이미지 생성
print(f"'{prompt}'에 따라 이미지를 생성 중입니다...")
image = pipe(prompt).images[0]

# 5. 결과 이미지 저장 및 표시
output_path = "generated_art.png"
image.save(output_path)
print(f"이미지가 '{output_path}'로 저장되었습니다.")

# 이미지 보기 (선택 사항)
image.show()
