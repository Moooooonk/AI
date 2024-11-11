# 필요한 라이브러리 설치 (주석 해제 후 터미널에서 실행)
# pip install magenta tensorflow mido

import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.protobuf import generator_pb2
from magenta.protobuf import music_pb2
import tensorflow as tf
from mido import MidiFile

# 모델 종류 및 체크포인트 위치 지정
model_name = 'attention_rnn'
bundle_name = model_name + '.mag'
bundle = mm.sequence_generator_bundle.read_bundle_file(bundle_name)

# Melody RNN 모델 생성
generator_map = melody_rnn_sequence_generator.get_generator_map()
melody_rnn = generator_map[model_name](checkpoint=None, bundle=bundle)
melody_rnn.initialize()

# 생성할 시퀀스의 기본 정보 설정
total_seconds = 30  # 음악 길이 (초)
tempo = 120  # 템포 (BPM)

# 기본 노트 시퀀스 정의
primer_sequence = music_pb2.NoteSequence()
primer_sequence.tempos.add(qpm=tempo)

# 생성 요청 파라미터 설정
generator_options = generator_pb2.GeneratorOptions()
generator_options.generate_sections.add(
    start_time=0,
    end_time=total_seconds
)

# 음악 생성
sequence = melody_rnn.generate(primer_sequence, generator_options)

# 생성된 음악을 MIDI 파일로 저장
output_file = 'generated_music.mid'
mm.sequence_proto_to_midi_file(sequence, output_file)
print(f"Generated music saved as {output_file}")

# MIDI 파일 재생
midi_file = MidiFile(output_file)
for msg in midi_file.play():
    print(msg)
