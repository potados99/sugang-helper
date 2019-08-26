# sugang-helper

수강신청 망했을 때에 사용할 수 있는 매크로입니다.

I모 대학 재학중이시고 파이썬 좋아하시나요? 여기로 오세요.


## 환경 설정

*sugang-helper* 는 Python3 기반의 `Selenuim`과 `ChromeDriver`를 사용합니다.

파이썬이 설치되어있지 않다면 먼저 설치해주세요. 이 프로젝트에서는 Python3을 사용합니다.

- [Python](https://www.python.org/downloads/)

`Selenium`은 `pip`를 사용해 설치합니다.

~~~
pip install selenium
~~~

`Chrome`을 설치하고 `ChromeDriver`를 내려받아주세요. 같은 버전을 사용해야 합니다.

- [Google Chrome](https://www.google.com/intl/ko/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads)


## 사용법

`private_template.py` 파일의 이름을 `private.py`로 바꾼 뒤 함수를 완성해주세요.

- `get_chromedriver_path`: 내려받은 `ChromeDriver`의 경로입니다.
- `get_url`: 수강신청 사이트의 주소입니다.
- `get_id`: 학번입니다.
- `get_password`: 비밀번호입니다.
- `get_target`: 잡고자 하는 과목입니다.
- `get_target_index`: 검색 결과 중 잡고자 하는 과목의 인덱스입니다.

> 이곳에 입력한 학번과 비밀번호는 로그인할 때에만 사용됩니다(`worker.py`의 88번, 89번 줄).
비밀번호를 평문으로 보관해놓는 것은 위험하니, 사용이 끝나면 꼭 삭제해주세요.

`worker.py`를 실행합니다.

~~~
python3 worker.py
~~~

또는(Linux/Mac 환경)

~~~
./run
~~~


## 동작

### 루틴

4개의 큰 루틴으로 이루어져 있습니다.

- `init`: WebDriver를 초기화하고 사이트에 접속합니다.
- `login`: 학번과 비밀번호를 사용해 로그인합니다.
- `search`: 원하는 과목을 검색합니다.
- `loop`: 해당 과목 신청을 반복해서 시도합니다.

이 루틴들은 차례대로 실행됩니다.

`loop` 루틴에서 키보드 인터럽트가 발생하거나(`Ctrl + C`) 처리되지 않은 예외가 연속 100번 이상 발생하면 프로그램이 종료됩니다.

### 출력

10번 클릭당 한 번씩 `.`이 출력됩니다.    
예외가 발생하면 `!`가 출력됩니다.


## 프로젝트 목적

모두가 편법을 사용하지 않는 것이 가장 이상적입니다.    
그 다음의 차선은 모두가 편법을 사용하는 것입니다.    
가장 나쁜 것은 소수만 편법을 사용해 기회를 독점하는 것입니다.

수강신청 망해보신 적 있으신가요? 많은 사람들이 매크로의 힘을 빌려 이를 극복하고자 합니다.    
매크로 사용을 근절할 수는 없습니다. 그렇다면 모두가 매크로를 사용하는 것이 공정합니다.  

우리가 수강신청하는 기계가 될 필요는 없습니다.    
기계에게 맡기고 그 시간에 더욱 즐거운 일을 하면 됩니다.


## 나아갈 방향

아직은 하나의 사이트와 하나의 흐름만을 지원합니다.

각 사이트에 맞는 다양한 흐름을 쉽게 스크립트로 작성하여 사용할 수 있도록 개선하고자 합니다.
