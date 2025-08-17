# 쿠버네티스 연구원 개발 환경 매니페스트

이 디렉토리에는 100명의 연구원을 위한 쿠버네티스 기반 개발 환경 구성을 위한 매니페스트 파일들이 포함되어 있습니다.

## 파일 구조

```
k8s-manifests/
├── namespace.yaml              # 네임스페이스 정의
├── resource-quota.yaml         # 리소스 할당 정책
├── priority-class.yaml         # 작업 우선순위 클래스
├── researcher-pod-template.yaml # 연구원용 Pod 템플릿
├── simulation-job.yaml         # Simulation 작업 Job
├── monitoring.yaml             # 모니터링 구성
└── README.md                   # 이 파일
```

## 배포 순서

1. **네임스페이스 생성**
   ```bash
   kubectl apply -f namespace.yaml
   ```

2. **리소스 할당 정책 설정**
   ```bash
   kubectl apply -f resource-quota.yaml
   ```

3. **우선순위 클래스 생성**
   ```bash
   kubectl apply -f priority-class.yaml
   ```

4. **모니터링 구성**
   ```bash
   kubectl apply -f monitoring.yaml
   ```

5. **연구원 Pod 생성 (예시)**
   ```bash
   kubectl apply -f researcher-pod-template.yaml
   ```

6. **Simulation 작업 실행 (예시)**
   ```bash
   kubectl apply -f simulation-job.yaml
   ```

## 주요 구성 요소

### 1. 네임스페이스
- `researcher-dev`: 연구원 개발 환경
- `monitoring`: 모니터링 도구

### 2. 리소스 할당
- 연구원당 최대: 20 Core CPU, 64GB Memory
- 저장공간: 7TiB
- 자동 리소스 제한 적용

### 3. 우선순위 시스템
- `simulation-priority-high`: 높은 우선순위 Simulation (1000)
- `simulation-priority-normal`: 일반 Simulation (500)
- `compile-priority`: Compile 작업 (300)
- `development-priority`: 일반 개발 (100)

### 4. 모니터링
- **Prometheus**: 메트릭 수집
- **Grafana**: 대시보드 및 시각화
- 클러스터 상태 및 작업 진행 상황 모니터링

## 사용법

### 연구원 Pod 생성
```bash
# 연구원별 Pod 생성
kubectl run researcher-001 --image=ubuntu:20.04 \
  --namespace=researcher-dev \
  --requests=cpu=10,memory=32Gi \
  --limits=cpu=20,memory=64Gi
```

### Simulation 작업 실행
```bash
# Simulation Job 생성
kubectl apply -f simulation-job.yaml

# 작업 상태 확인
kubectl get jobs -n researcher-dev

# 로그 확인
kubectl logs job/simulation-job -n researcher-dev
```

### 모니터링 접근
```bash
# Grafana 접근
kubectl port-forward svc/grafana-service 3000:3000 -n monitoring

# Prometheus 접근
kubectl port-forward svc/prometheus-service 9090:9090 -n monitoring
```

## 대기열 관리

### Pending 작업 확인
```bash
# 대기 중인 Pod 확인
kubectl get pods -n researcher-dev --field-selector=status.phase=Pending

# 대기열 길이 확인
kubectl get pods -n researcher-dev | grep Pending | wc -l
```

### 우선순위 조정
```bash
# 작업 우선순위 변경
kubectl patch job simulation-job -n researcher-dev \
  -p '{"spec":{"template":{"spec":{"priorityClassName":"simulation-priority-high"}}}}'
```

## 확장 및 유지보수

### 노드 추가
```bash
# 새 Work Node 추가 후
kubectl label node new-work-node node-type=work-node
```

### 백업
```bash
# 클러스터 설정 백업
kubectl get all -n researcher-dev -o yaml > backup.yaml
```

### 업데이트
```bash
# Rolling Update
kubectl rollout restart deployment/prometheus -n monitoring
```

## 문제 해결

### 리소스 부족
```bash
# 노드별 리소스 사용량 확인
kubectl top nodes

# Pod별 리소스 사용량 확인
kubectl top pods -n researcher-dev
```

### 네트워크 문제
```bash
# 서비스 연결 확인
kubectl get svc -n researcher-dev
kubectl describe svc <service-name> -n researcher-dev
```

### 저장공간 문제
```bash
# PVC 상태 확인
kubectl get pvc -n researcher-dev
kubectl describe pvc <pvc-name> -n researcher-dev
```

## 보안 고려사항

1. **RBAC 설정**: 연구원별 접근 권한 제한
2. **네트워크 정책**: Pod 간 통신 제한
3. **시크릿 관리**: 민감한 정보 암호화
4. **정기 감사**: 접근 로그 모니터링

## 성능 최적화

1. **노드 선택**: 작업 유형에 따른 노드 배치
2. **리소스 예약**: 중요한 작업을 위한 리소스 예약
3. **자동 스케일링**: 필요에 따른 자동 확장
4. **캐싱**: 자주 사용되는 데이터 캐싱

이 매니페스트들을 사용하여 효율적이고 안정적인 연구원 개발 환경을 구축할 수 있습니다. 