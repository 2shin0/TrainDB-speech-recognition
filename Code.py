# 1. (원천 데이터 폴더)/034
# (원천 데이터 폴더)/034/파일명.wav -> (결과물 폴더)/034/wav
import os
import shutil

def copy_wav_files(source_dir, target_dir):
    # source_dir에서 .wav 파일들을 찾습니다.
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.wav'):
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir, file)

                # 파일을 target_dir로 복사합니다.
                shutil.copy2(source_file_path, target_file_path)
                print(f'Copied: {source_file_path} to {target_file_path}')

# 소스 디렉토리와 타겟 디렉토리 경로를 정의합니다.
source_dir = '(결과물 폴더)/034/'
target_dir = r'(원천 데이터 폴더)/034/wav'

# 함수를 호출하여 파일을 복사합니다.
copy_wav_files(source_dir, target_dir)



# (원천 데이터 폴더)/034/파일명.json에서 "length"의 value를 붙인 내용 
# -> (결과물 폴더)/034/DURINFO

# (결과물 폴더)/034/DURINFO 파일 생성

# (결과물 폴더)/034/DURINFO 파일에 내용 작성 시작
# broadcast_00033001.json -> 34/wav/00033001     6.78
# 00033001 ~ 00034000
import json
base_dir = '(결과물 폴더)/034/etc/'
json_dir = '(원천 데이터 폴더)/034/'
durinfo_path = os.path.join(base_dir, "DURINFO")

# DURINFO 파일 생성 및 열기
with open(durinfo_path, "w", encoding="utf-8") as durinfo_file:
    # broadcast_00033001.json부터 broadcast_00034000.json까지 순회
    for i in range(33001, 34001):
        json_file_name = f"broadcast_{i:08d}.json"
        json_path = os.path.join(json_dir, json_file_name)
        
        # JSON 파일 로드
        try:
            with open(json_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
                # 파일명에서 마지막 3자리 추출 및 length 값 추출
                file_number = json_file_name[-13:-5]
                length = data.get("length", "N/A")

                # DURINFO 파일에 기록
                durinfo_file.write(f"34/wav/{file_number}     {length}\n")
        except FileNotFoundError:
            print(f"{json_file_name} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {json_file_name}.")

print("DURINFO 파일 생성 및 데이터 기록 완료")



# (원천 데이터 폴더)/034/파일명.txt에서 다른 내용 동일, 괄호 첫 번째 선택 내용 
# -> (결과물 폴더)/00033001/LANG
# 034/wav/파일구분번호 tab (문장 기호 제외하고 괄호가 있다면 첫 번째 내용)
import re

base_dir = '(결과물 폴더)/034/etc/'
txt_dir = '(원천 데이터 폴더)/034/'
lang_file_path = os.path.join(base_dir, "LANG")

# LANG 파일 생성 및 열기
with open(lang_file_path, "w", encoding="utf-8") as lang_file:
    # broadcast_00033001.txt부터 broadcast_00034000.txt까지 순회
    for i in range(33001, 34001):
        txt_file_name = f"broadcast_{i:08d}.txt"
        txt_path = os.path.join(txt_dir, txt_file_name)

        # TXT 파일 로드
        try:
            with open(txt_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
                
                # 괄호와 괄호 내용 제거
                # '/' 문자를 공백으로 대체하고 양쪽 공백 제거
                content = content.replace('/', '').strip()

                # 첫 번째 괄호 내용을 찾아 저장
                first_bracket_content = re.search(r'\((.*?)\)', content)

                if first_bracket_content:
                    first_bracket_content = first_bracket_content.group(1)
                    # 모든 괄호와 그 안의 내용 삭제
                    content = re.sub(r'\(.*?\)', '', content)
                    # 첫 번째 괄호 내용을 원래 위치에 다시 삽입
                    # 이 경우, 첫 번째 괄호 위치를 대략적으로 추정하여 삽입
                    content_parts = content.split(maxsplit=2)  # 최대 분할을 2로 제한하여 세 부분으로 나눔
                    if len(content_parts) >= 3:
                        content = f"{content_parts[0]} {content_parts[1]} {first_bracket_content} {content_parts[2]}"
                                
                # LANG 파일에 기록
                lang_file.write(f"034/wav/{i:08d}     {content}\n")
        except FileNotFoundError:
            print(f"{txt_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while processing {txt_file_name}: {e}")

print("LANG 파일 생성 및 데이터 기록 완료")



# (원천 데이터 폴더)/034/파일명.json에서 다른 내용 동일, 괄호 두 번째 선택 내용 
# -> (결과물 폴더)/034/PROMPT
# 034/wav/파일구분번호 tab (문장 기호 제외하고 괄호가 있다면 두 번째 내용)
base_dir = '(결과물 폴더)/034/etc/'
txt_dir = '(원천 데이터 폴더)/034/'
prompt_file_path = os.path.join(base_dir, "prompt")

# prompt 파일 생성 및 열기
with open(prompt_file_path, "w", encoding="utf-8") as prompt_file:
    # broadcast_00033001.txt부터 broadcast_00034000.txt까지 순회
    for i in range(33001, 34001):
        txt_file_name = f"broadcast_{i:08d}.txt"
        txt_path = os.path.join(txt_dir, txt_file_name)

        # TXT 파일 로드
        try:
            with open(txt_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
                
                # 괄호와 괄호 내용 제거
                # '/' 문자를 공백으로 대체하고 양쪽 공백 제거
                content = content.replace('/', '').strip()

                # 두 번째 괄호 내용을 찾아 저장
                second_bracket_content = re.search(r'\(.*?\)\s*\((.*?)\)', content)

                if second_bracket_content:
                    second_bracket_content = second_bracket_content.group(1)
                    # 모든 괄호와 그 안의 내용 삭제
                    content = re.sub(r'\(.*?\)', '', content)
                    # 두 번째 괄호 내용을 원래 위치에 다시 삽입
                    # 이 경우, 두 번째 괄호 위치를 대략적으로 추정하여 삽입
                    content_parts = content.split(maxsplit=2)  # 최대 분할을 2로 제한하여 세 부분으로 나눔
                    if len(content_parts) >= 3:
                        content = f"{content_parts[0]} {content_parts[1]} {second_bracket_content} {content_parts[2]}"
                                
                # prompt 파일에 기록
                prompt_file.write(f"034/wav/{i:08d}     {content}\n")
        except FileNotFoundError:
            print(f"{txt_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while processing {txt_file_name}: {e}")

print("PROMPT 파일 생성 및 데이터 기록 완료")



# 2. (원천 데이터 폴더)/035

# 이 폴더에는 없는 파일이 몇 개 있었다.
# broadcast_00034123.json not found.
# broadcast_00034403.json not found.
# broadcast_00034404.json not found.
# broadcast_00034671.json not found.
# broadcast_00034831.json not found.
# broadcast_00034123.txt not found.
# broadcast_00034403.txt not found.
# broadcast_00034404.txt not found.
# broadcast_00034671.txt not found.
# broadcast_00034831.txt not found.

# (원천 데이터 폴더)/035/파일명.wav -> (결과물 폴더)/035/wav
def copy_wav_files(source_dir, target_dir):
    # source_dir에서 .wav 파일들을 찾습니다.
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.wav'):
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir, file)

                # 파일을 target_dir로 복사합니다.
                shutil.copy2(source_file_path, target_file_path)
                print(f'Copied: {source_file_path} to {target_file_path}')

# 소스 디렉토리와 타겟 디렉토리 경로를 정의합니다.
source_dir = '(원천 데이터 폴더)/035/'
target_dir = r'(결과물 폴더)/035/wav'

# 함수를 호출하여 파일을 복사합니다.
copy_wav_files(source_dir, target_dir)

# 함수를 호출하여 파일을 복사합니다.
copy_wav_files(source_dir, target_dir)



# (원천 데이터 폴더)/035/파일명.json에서 "length"의 value를 붙인 내용 
# -> (결과물 폴더)/035/DURINFO
import json
base_dir = '(결과물 폴더)/035/etc/'
json_dir = '(원천 데이터 폴더)/035/'
durinfo_path = os.path.join(base_dir, "DURINFO")

# DURINFO 파일 생성 및 열기
with open(durinfo_path, "w", encoding="utf-8") as durinfo_file:
    # broadcast_00034001.json부터 broadcast_00035000.json까지 순회
    for i in range(34001, 35001):
        json_file_name = f"broadcast_{i:08d}.json"
        json_path = os.path.join(json_dir, json_file_name)
        
        # JSON 파일 로드
        try:
            with open(json_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                
                # 파일명에서 마지막 3자리 추출 및 length 값 추출
                file_number = json_file_name[-13:-5]
                length = data.get("length", "N/A")

                # DURINFO 파일에 기록
                durinfo_file.write(f"35/wav/{file_number}     {length}\n")
        except FileNotFoundError:
            print(f"{json_file_name} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {json_file_name}.")

print("DURINFO 파일 생성 및 데이터 기록 완료")



# (원천 데이터 폴더)/035/파일명.txt에서 다른 내용 동일, 괄호 첫 번째 선택 내용 
# -> (결과물 폴더)/035/LANG
# 035/wav/파일구분번호 tab (문장 기호 제외하고 괄호가 있다면 첫 번째 내용)
import re

base_dir = '(결과물 폴더)/035/etc/'
txt_dir = '(원천 데이터 폴더)/035/'
lang_file_path = os.path.join(base_dir, "LANG")

# LANG 파일 생성 및 열기
with open(lang_file_path, "w", encoding="utf-8") as lang_file:
    # broadcast_00034001.txt부터 broadcast_00035000.txt까지 순회
    for i in range(34001, 35001):
        txt_file_name = f"broadcast_{i:08d}.txt"
        txt_path = os.path.join(txt_dir, txt_file_name)

        # TXT 파일 로드
        try:
            with open(txt_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
                
                # 괄호와 괄호 내용 제거
                # '/' 문자를 공백으로 대체하고 양쪽 공백 제거
                content = content.replace('/', '').strip()

                # 첫 번째 괄호 내용을 찾아 저장
                first_bracket_content = re.search(r'\((.*?)\)', content)

                if first_bracket_content:
                    first_bracket_content = first_bracket_content.group(1)
                    # 모든 괄호와 그 안의 내용 삭제
                    content = re.sub(r'\(.*?\)', '', content)
                    # 첫 번째 괄호 내용을 원래 위치에 다시 삽입
                    # 이 경우, 첫 번째 괄호 위치를 대략적으로 추정하여 삽입
                    content_parts = content.split(maxsplit=2)  # 최대 분할을 2로 제한하여 세 부분으로 나눔
                    if len(content_parts) >= 3:
                        content = f"{content_parts[0]} {content_parts[1]} {first_bracket_content} {content_parts[2]}"
                                
                # LANG 파일에 기록
                lang_file.write(f"035/wav/{i:08d}     {content}\n")
        except FileNotFoundError:
            print(f"{txt_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while processing {txt_file_name}: {e}")

print("LANG 파일 생성 및 데이터 기록 완료")



# (원천 데이터 폴더)/035/파일명.json에서 다른 내용 동일, 괄호 두 번째 선택 내용 
# -> (결과물 폴더)/035/PROMPT
# 035/wav/파일구분번호 tab (문장 기호 제외하고 괄호가 있다면 두 번째 내용)
base_dir = '(결과물 폴더)/035/etc/'
txt_dir = '(원천 데이터 폴더)/035/'
prompt_file_path = os.path.join(base_dir, "prompt")

# prompt 파일 생성 및 열기
with open(prompt_file_path, "w", encoding="utf-8") as prompt_file:
    # broadcast_00034001.txt부터 broadcast_00035000.txt까지 순회
    for i in range(34001, 35001):
        txt_file_name = f"broadcast_{i:08d}.txt"
        txt_path = os.path.join(txt_dir, txt_file_name)

        # TXT 파일 로드
        try:
            with open(txt_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()
                
                # 괄호와 괄호 내용 제거
                # '/' 문자를 공백으로 대체하고 양쪽 공백 제거
                content = content.replace('/', '').strip()

                # 두 번째 괄호 내용을 찾아 저장
                second_bracket_content = re.search(r'\(.*?\)\s*\((.*?)\)', content)

                if second_bracket_content:
                    second_bracket_content = second_bracket_content.group(1)
                    # 모든 괄호와 그 안의 내용 삭제
                    content = re.sub(r'\(.*?\)', '', content)
                    # 두 번째 괄호 내용을 원래 위치에 다시 삽입
                    # 이 경우, 두 번째 괄호 위치를 대략적으로 추정하여 삽입
                    content_parts = content.split(maxsplit=2)  # 최대 분할을 2로 제한하여 세 부분으로 나눔
                    if len(content_parts) >= 3:
                        content = f"{content_parts[0]} {content_parts[1]} {second_bracket_content} {content_parts[2]}"
                                
                # prompt 파일에 기록
                prompt_file.write(f"035/wav/{i:08d}     {content}\n")
        except FileNotFoundError:
            print(f"{txt_file_name} not found.")
        except Exception as e:
            print(f"An error occurred while processing {txt_file_name}: {e}")

print("PROMPT 파일 생성 및 데이터 기록 완료")