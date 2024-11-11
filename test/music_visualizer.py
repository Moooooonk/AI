# 필요한 라이브러리 설치 (터미널에서 실행)
# pip install pygame librosa numpy

import pygame
import numpy as np
import librosa
import time

# 음악 파일 로드 및 분석
audio_file = 'path/to/your/music/file.wav'  # 음악 파일 경로를 입력하세요
y, sr = librosa.load(audio_file)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
volume = librosa.feature.rms(y=y)[0]  # Root Mean Square (RMS) 값으로 볼륨 추출

# Pygame 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

# 비주얼 반응 루프
running = True
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 현재 재생 시간에 따른 볼륨 값 계산
    elapsed_time = time.time() - start_time
    current_frame = int(elapsed_time * sr)  # 재생 시간에 해당하는 프레임 계산
    
    if current_frame < len(volume):
        current_volume = volume[current_frame]  # 현재 볼륨 값
    else:
        current_volume = 0

    # 볼륨에 따른 색상 변화
    color_intensity = int(current_volume * 255 * 10)  # 볼륨에 비례하여 색상 강도 조절
    color_intensity = max(0, min(color_intensity, 255))  # 0에서 255 사이로 값 제한
    screen.fill((color_intensity, 100, 150))  # 색상 변경

    pygame.display.flip()
    clock.tick(30)  # 화면 갱신 속도 조절

pygame.quit()
