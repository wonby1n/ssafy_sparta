# 정처기 실기 준비 day-1

## C 언어 기초 정리

### 기본 프로그램 구조

```
#include <stdio.h>   // 표준 입출력 헤더 파일

int main(void) {
    // 코드 작성
    return 0;        // 프로그램 정상 종료
}
```

#include <stdio.h>
- 표준 입력/출력 함수(printf, scanf) 사용을 위해 필요.

int main(void)
- 프로그램 시작점. 운영체제에 정수(int) 값을 반환.

return 0;
- 정상 종료를 의미. (안 써도 되지만 쓰는 게 정석)


### 출력 (printf)

```
#include <stdio.h>

int main(void) {
    printf("Hello World\n");       // 문자열 출력
    printf("%d\n", 10);            // 정수 출력
    printf("%f\n", 3.14);          // 실수 출력
    printf("%c\n", 'A');           // 문자 출력
    printf("%s\n", "Hello C");     // 문자열 출력
    return 0;
}
```

%d : 정수 (int)

%f : 실수 (float)

%c : 문자 (char)

%s : 문자열 (char[])

\n : 줄바꿈

### 입력 (scanf)

```
#include <stdio.h>

int main(void) {
    int a;
    scanf("%d", &a);   // 정수 입력
    printf("입력값: %d\n", a);

    return 0;
}
```

scanf("형식지정자", &변수); → &는 변수의 메모리 주소를 의미.

문자열 입력은 & 필요 없음 (char 배열 자체가 주소임).

### 정수 배열 (리스트 개념)


```
#include <stdio.h>

int main(void) {
    int arr[5];  // 크기 5인 배열 선언

    // 입력 받기
    for (int i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }

    // 출력하기
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
```

📌 실행 예시:

입력: 1 2 3 4 5
출력: 1 2 3 4 5


✅ 요약

printf : 출력 (형식 지정자 필요)

scanf : 입력 (&변수 필수)

배열 = 파이썬의 리스트 개념 → int arr[크기];


### 파이썬 vs C 차이

| 파이썬

a = int(input())


파이썬은 변수가 객체를 자동으로 가리키고, input() 값이 알아서 변수에 저장돼.
👉 내부에서 메모리 주소를 알아서 처리해줌.

| C

int a;
scanf("%d", &a);


C에서는 컴퓨터한테 "이 값(a)을 어디에 저장할지" 직접 알려줘야 함.
👉 &a는 변수 a의 메모리 주소를 의미.


### 문제

다음은 C 언어 코드이다. 출력 결과를 쓰시오.

```
#include <stdio.h>

int t = 0;

void fn(int x[], int y) {
    int z = t;
    t++;
    printf("A: %d\n", z);

    if (y <= 0) return;

    printf("B: %d\n", x[--y]);
    fn(x, y);
    printf("C: %d\n", z);
}

int main() {
    int x[4] = {2, 1, 3, 7};
    int y = 4;
    fn(x, y);
    return 0;
}
```

📌 코드 분석

전역 변수

int t = 0;


t는 전역 변수, 모든 함수에서 공유됨.

fn 함수 동작

```
void fn(int x[], int y) {
    int z = t;          // z에 현재 t값 저장
    t++;                // t 증가
    printf("A: %d\n", z);

    if (y <= 0) return; // y가 0 이하면 종료

    printf("B: %d\n", x[--y]);  // y 감소시키고, x[y] 출력
    fn(x, y);                   // 재귀 호출
    printf("C: %d\n", z);       // 함수 끝날 때 z 출력
}
```

```
main
int main() {
    int x[4] = {2, 1, 3, 7};
    int y = 4;
    fn(x, y);
    return 0;
}
```

배열 x = {2, 1, 3, 7}

(즉, x[0]=2, x[1]=1, x[2]=3, x[3]=7)

y = 4


📌 함수 실행 과정

첫 호출: fn(x, 4)

z = 0, t=1

출력: A: 0

y=4 → 0보다 큼

--y → 3 → x[3]=7

출력: B: 7

재귀 호출: fn(x, 3)

두 번째 호출: fn(x, 3)

z = 1, t=2

출력: A: 1

--y → 2 → x[2]=3

출력: B: 3

재귀 호출: fn(x, 2)

세 번째 호출: fn(x, 2)

z = 2, t=3

출력: A: 2

--y → 1 → x[1]=1

출력: B: 1

재귀 호출: fn(x, 1)

네 번째 호출: fn(x, 1)

z = 3, t=4

출력: A: 3

--y → 0 → x[0]=2

출력: B: 2

재귀 호출: fn(x, 0)

다섯 번째 호출: fn(x, 0)

z = 4, t=5

출력: A: 4

y <= 0 → return

이후 실행 X

📌 재귀 복귀하면서 C 출력

네 번째 호출 끝: C: 3

세 번째 호출 끝: C: 2

두 번째 호출 끝: C: 1

첫 호출 끝: C: 0

✅ 최종 출력 결과
```
A: 0
B: 7
A: 1
B: 3
A: 2
B: 1
A: 3
B: 2
A: 4
C: 3
C: 2
C: 1
C: 0
```