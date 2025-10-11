Created at : 2025-09-22 22:28
## 우선순위 큐 (priority_queue)

- - -
### 우선순위 큐란    

말 그대로 큐(queue)를 구현하는데 추가적으로 우선순위대로 정렬시켜서 큐를 구현해준다. 종류로는 내림차순과 오름차순이 있다. 이것의 장점으로는 시간복잡도가 n^2을 nlogn으로 줄여줄수 있다.  
#### 1. 우선순위 큐(priority_queue)사용법  (CPP)
- `<queue>` 헤더파일 안에 있다.  

- 기본 형태 : `priority_queue<T,Container,Compare>`  

원하는 자료형 및 클래스 T를 통해 생성. 여기서 Container는 vector와 같은 컨테이너이며 Compare는 비교함수 클래스이다.  

- 기본 생성자 형식 : `priority_queue <[Data Type]> [변수이름];`  
ex) `priority_queue<int> pq;`  
- 내부 컨테이너 변경 : `priority_queue<[Data Type],[Container Type]> [변수이름];`  
ex) `priority_queue<int,deque<int>> pq;` -> default: vector container  
- 정렬기준 변경 : `priority_queue<[Data Type],[Container Type],[정렬기준]> [변수이름];`  
ex) `priority_queue<int,vector<int>,greater<int>> pq;` -> default: 내림차순(less<>)    

```cpp
// 오름차순 정렬
struct cmp{
    bool operator()(Custom t, Custom u){
        return t.value > u.value;
    }
};
```

이런식으로 따로 비교하는 함수를 만들어 주어도 된다.  
#### 2. 우선순위 큐(priority_queue) 멤버 함수  
- bool empty() const;  //비어있을 경우 true 반환  
- size_type size() const; //원소의 개수 반환
- const value_type&top() const; //맨 위에있는 원소를 참조 및 반환
- void push (const value_type&val); //인자 삽입
- void pop(); //맨위의 있는 인자 삭제  
#### 3. 예제 코드    

```cpp
#include <iostream>
#include <functional>
#include <queue>
using namespace std;

int main(){
    // priority_queue
    priority_queue< int, vector<int>, greater<int> > pq;
    // push(element)
    pq.push(5);
    pq.push(2);
    pq.push(8);
    pq.push(9);
    pq.push(1);
    pq.push(14);  
    //queue : 1 2 5 8 9 14
    // pop()
    pq.pop(); //1 out
    pq.pop(); //2 out
    // top();
    cout << "pq top : " << pq.top() << '\n'; 

    // empty(), size()
    if(!pq.empty()) cout << "pq size : " << pq.size() << '\n';
    // pop all
    while(!pq.empty()){
        cout << pq.top() << " ";
        pq.pop();
    } 

    cout << '\n';  
    return 0; 

}

``` 

  

결과   

![priority_queue_result](https://user-images.githubusercontent.com/42687768/72158533-cdc1e400-33fd-11ea-8579-8a4e89224b5e.JPG)  

추가 구조체를 사용한 우선순위 큐 예제  

```cpp
#include<cstdio>
#include<vector>
#include<queue>

using namespace std;

struct dayScore {
    int restDay;
    int score;
    bool operator()(dayScore &a, dayScore &b) {
        return a.score < b.score;
    }
};

  

int main() {
    priority_queue<dayScore, vector<dayScore>, dayScore> pq;
    dayScore tempScore;

    for (int i = 0; i < 7; i++) {
        scanf("%d %d", &tempScore.restDay, &tempScore.score);
        pq.push(tempScore);
    }
    printf("size = %d\n", pq.size());
    while (!pq.empty()) {
        printf("%d %d\n", pq.top().restDay, pq.top().score);
        pq.pop();
    }

    return 0;
} 

```