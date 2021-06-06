import glob
import threading
import time
import schedule
import os

# 최초 파일 리스트
past_file_list = glob.glob(os.getcwd()+"/*.csv")

def new_file():
    global past_file_list
    file_list = glob.glob(os.getcwd()+"/*.csv")
    # past(과거) file list와 현재 시점의 file list의 크기가 다를 경우
    # (파일이 추가되는 경우만 생각하였음)
    if len(file_list)!=len(past_file_list):
        for i in file_list:
            # 현재 파일 리스트의 파일 중에서
            # 과거 파일 리스트에 없는 파일을 추출
            if i not in past_file_list:
                file = i
                # / 단위로 구분하고 확장자를 제거
                file = file.split("/")[-1].replace('.csv','')
                break
        # kafka topic을 생성할 명령어에 topic 이름으로 위에서 추출한 file 이름 삽입
        topic = "/usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic "+file
        # logstash conf 파일 실행 명령어에 위에서 추출한 file 이름 삽입
        logstash = "/usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/"+file+".conf"
        
        # os.system 명령어를 사용해 파이썬에서 시스템 명령어 사용
        os.system(topic)
        time.sleep(60)
        # kafka에 적재하는데 시간이 오래 소요될 수 있으니 넉넉하게 딜레이 5분
        os.system(logstash)
        time.sleep(300)
    # past_file_list에 현재 시점의 파일 리스트를  저장
    past_file_list = file_list
    # 해당 함수를 10초 단위로 반복 실행
    threading.Timer(10,new_file).start()

new_file()
