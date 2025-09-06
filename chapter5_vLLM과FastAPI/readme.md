# FastAPI Multi-Provider Chat API

AI 채팅 서비스를 위한 FastAPI 기반 API 서버입니다. OpenAI와 RunPod 두 가지 LLM 프로바이더를 지원합니다.

## 기능

- **다중 프로바이더 지원**: OpenAI와 RunPod API 연동
- **스트리밍 지원**: OpenAI에서 실시간 응답 스트리밍
- **유연한 모델 선택**: 다양한 OpenAI 모델 지원
- **헬스체크**: 서버 상태 모니터링

## 설치 및 실행

### 1. 의존성 설치
```bash
pip install openai python-dotenv fastapi json-repair openai uvicorn fastapi
```

### 2. 환경변수 설정
env파일에서 환경변수를 입력합니다. 
OPENAI_API_KEY="your-openai-api-key"
RUNPOD_API_KEY="your-runpod-api-key"
RUNPOD_ENDPOINT_ID="your-runpod-endpoint-id"
```

### 3. 서버 실행
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API 사용법

### 헬스체크
```bash
curl -X GET http://localhost:8000/health
```

### OpenAI 채팅 (일반 응답)
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "HUG 국민·우리은행 등 표준 PF 주관금융사로 재선정 주택도시보증공사 HUG 는 주택사업자의 원활한 자금조달을 지원하는 표준 프로젝트 파이낸싱 PF 과 후분양 표준 PF 보증의 주관금융사를 새로 선정했다고 4일 밝혔다. PF 보증이란 주택 건설 사업의 미래 현금수입과 사업성을 담보로 주택 사업자가 대출받는 토 지비 등 사업비에 대한 주택사업금융의 원리금 상환을 책임지는 보증을 말한다. 후분양 PF 보증이란 주택 사업자가 주택의 일부를 후분양하는 조건으로 주택 건설  자금 대출금을 조달하는 경우에 원리금 상환을 책임지는 보증이다. HUG는 2014년 제도를 시행한 이후 표준 PF 보증 약 12조6000억원 후분양 표준 PF 보증 약 8600억원을 지원했다. 이번에 새로 선정된 주관금융사는 표준 PF의 경우 국민은행 부산은행 수협은행 우리은행 하나은행이다. 후분양 표준 PF는 부산은행 우리은행 수협은행이다. 권형택 HUG 사장은 “최근 원자재가격 급등 대출금리 인상 등 비용증가로 어려움을 겪는 주택사업자에게 저금리 금융지원을 통하여 비용을 경감시킬 수 있게 된 점을 뜻깊게 생각한다”며 “표준PF 후분양 표준PF 제도운영을 통하여 주택공급 확대를 통한 부동산 시장 안정 주거안정 지원에 큰 도움이 될 것으로 전망한다”고 밝혔다.",
    "provider": "openai",
    "model": "gpt-4o-mini",
    "streaming": false
  }'
```

### OpenAI 채팅 (스트리밍)
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "HUG 국민·우리은행 등 표준 PF 주관금융사로 재선정 주택도시보증공사 HUG 는 주택사업자의 원활한 자금조달을 지원하는 표준 프로젝트 파이낸싱 PF 과 후분양 표준 PF 보증의 주관금융사를 새로 선정했다고 4일 밝혔다. PF 보증이란 주택 건설 사업의 미래 현금수입과 사업성을 담보로 주택 사업자가 대출받는 토 지비 등 사업비에 대한 주택사업금융의 원리금 상환을 책임지는 보증을 말한다. 후분양 PF 보증이란 주택 사업자가 주택의 일부를 후분양하는 조건으로 주택 건설  자금 대출금을 조달하는 경우에 원리금 상환을 책임지는 보증이다. HUG는 2014년 제도를 시행한 이후 표준 PF 보증 약 12조6000억원 후분양 표준 PF 보증 약 8600억원을 지원했다. 이번에 새로 선정된 주관금융사는 표준 PF의 경우 국민은행 부산은행 수협은행 우리은행 하나은행이다. 후분양 표준 PF는 부산은행 우리은행 수협은행이다. 권형택 HUG 사장은 “최근 원자재가격 급등 대출금리 인상 등 비용증가로 어려움을 겪는 주택사업자에게 저금리 금융지원을 통하여 비용을 경감시킬 수 있게 된 점을 뜻깊게 생각한다”며 “표준PF 후분양 표준PF 제도운영을 통하여 주택공급 확대를 통한 부동산 시장 안정 주거안정 지원에 큰 도움이 될 것으로 전망한다”고 밝혔다.",
    "provider": "openai",
    "model": "gpt-4o-mini",
    "streaming": true
  }' \
  --no-buffer -N
```

### RunPod 채팅
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "HUG 국민·우리은행 등 표준 PF 주관금융사로 재선정 주택도시보증공사 HUG 는 주택사업자의 원활한 자금조달을 지원하는 표준 프로젝트 파이낸싱 PF 과 후분양 표준 PF 보증의 주관금융사를 새로 선정했다고 4일 밝혔다. PF 보증이란 주택 건설 사업의 미래 현금수입과 사업성을 담보로 주택 사업자가 대출받는 토 지비 등 사업비에 대한 주택사업금융의 원리금 상환을 책임지는 보증을 말한다. 후분양 PF 보증이란 주택 사업자가 주택의 일부를 후분양하는 조건으로 주택 건설  자금 대출금을 조달하는 경우에 원리금 상환을 책임지는 보증이다. HUG는 2014년 제도를 시행한 이후 표준 PF 보증 약 12조6000억원 후분양 표준 PF 보증 약 8600억원을 지원했다. 이번에 새로 선정된 주관금융사는 표준 PF의 경우 국민은행 부산은행 수협은행 우리은행 하나은행이다. 후분양 표준 PF는 부산은행 우리은행 수협은행이다. 권형택 HUG 사장은 “최근 원자재가격 급등 대출금리 인상 등 비용증가로 어려움을 겪는 주택사업자에게 저금리 금융지원을 통하여 비용을 경감시킬 수 있게 된 점을 뜻깊게 생각한다”며 “표준PF 후분양 표준PF 제도운영을 통하여 주택공급 확대를 통한 부동산 시장 안정 주거안정 지원에 큰 도움이 될 것으로 전망한다”고 밝혔다.",
    "provider": "runpod"
  }'
```

## API 파라미터

### ChatRequest 모델
| 파라미터 | 타입 | 기본값 | 설명 |
|---------|------|--------|------|
| `query` | string | - | 사용자 질문 (필수) |
| `provider` | string | "openai" | "openai" 또는 "runpod" |
| `model` | string | "gpt-4o-mini" | OpenAI 모델명 |
| `streaming` | boolean | false | 스트리밍 응답 여부 |

### 지원 모델 (OpenAI)
- `gpt-4o-mini`
- `gpt-4o`
- `gpt-3.5-turbo`
- 기타 OpenAI 모델

## 프로바이더별 특징

### OpenAI
- ✅ 스트리밍 지원
- ✅ 다양한 모델 선택
- ✅ 안정적인 응답

### RunPod
- ❌ 스트리밍 미지원
- ✅ 커스텀 모델 사용 가능
- ⚡ 빠른 응답 (동기식)

## 실시간 스트리밍 확인

스트리밍 응답을 실시간으로 보려면:

```bash
# curl 사용시
curl ... --no-buffer -N

# httpie 사용시
http --stream POST localhost:8000/chat ...

# 브라우저에서
http://localhost:8000/docs
```

## API 문서

서버 실행 후 다음 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 파일 구조

```
.
├── main.py           # FastAPI 앱 및 라우터
├── llm_service.py    # LLM 프로바이더 서비스
└── README.md         # 이 파일
```

## 에러 처리

- **400**: 알 수 없는 프로바이더
- **500**: 내부 서버 오류 (API 키 오류, 네트워크 오류 등)

## 주의사항

1. **환경변수**: API 키들이 올바르게 설정되어 있는지 확인
2. **스트리밍**: RunPod는 스트리밍을 지원하지 않음
3. **타임아웃**: 긴 응답의 경우 타임아웃 설정 확인