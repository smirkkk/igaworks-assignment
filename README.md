# IGA Works 사전 과제 (백엔드)

## 스택
- Python 3.8
- Docker
- EC2
- RDS (MySQL)
- SQS
- Lambda (Python)

## API Endpoint
- Event Collect API
  - `[POST] http://15.164.162.135/api/collect`
- Event Search API
  - `[POST] http://15.164.162.135/api/search`

## 실행방법
1. `docker build -t [이미지 이름] .`
2. `docker run -d -p 8000:8000 --name [컨테이너 이름] [이미지 이름]`