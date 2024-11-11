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
spectrogram = np.abs(librosa.stft(y))  # 주파수 스펙트럼 분석

# Pygame 초기화
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
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

    # 현재 재생 시간에 따른 볼륨과 주파수 값 계산
    elapsed_time = time.time() - start_time
    current_frame = int(elapsed_time * sr)  # 재생 시간에 해당하는 프레임 계산
    
    if current_frame < len(volume):
        current_volume = volume[current_frame]  # 현재 볼륨 값
    else:
        current_volume = 0

    # 주파수 대역별 반응 계산 (주파수 대역을 5개로 나눔)
    if current_frame < spectrogram.shape[1]:
        low_freq = np.mean(spectrogram[:10, current_frame])  # 저주파
        mid_low_freq = np.mean(spectrogram[10:30, current_frame])  # 중저주파
        mid_freq = np.mean(spectrogram[30:60, current_frame])  # 중간 주파수
        mid_high_freq = np.mean(spectrogram[60:100, current_frame])  # 중고주파
        high_freq = np.mean(spectrogram[100:, current_frame])  # 고주파
    else:
        low_freq = mid_low_freq = mid_freq = mid_high_freq = high_freq = 0

    # 볼륨에 따른 배경 색상 변화
    color_intensity = int(current_volume * 255 * 10)  # 볼륨에 비례하여 색상 강도 조절
    color_intensity = max(0, min(color_intensity, 255))  # 0에서 255 사이로 값 제한
    screen.fill((color_intensity, 100, 150))  # 배경 색상 변경

    # 주파수 대역에 따라 원을 화면에 그리기
    pygame.draw.circle(screen, (255, 50, 50), (screen_width // 2, screen_height // 2), int(low_freq / 50), 5)  # 저주파
    pygame.draw.circle(screen, (50, 255, 50), (screen_width // 2, screen_height // 2 - 50), int(mid_low_freq / 50), 5)  # 중저주파
    pygame.draw.circle(screen, (50, 50, 255), (screen_width // 2, screen_height // 2 - 100), int(mid_freq / 50), 5)  # 중간 주파수
    pygame.draw.circle(screen, (255, 255, 50), (screen_width // 2, screen_height // 2 - 150), int(mid_high_freq / 50), 5)  # 중고주파
    pygame.draw.circle(screen, (255, 50, 255), (screen_width // 2, screen_height // 2 - 200), int(high_freq / 50), 5)  # 고주파

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(30)  # 화면 갱신 속도 조절

pygame.quit()
