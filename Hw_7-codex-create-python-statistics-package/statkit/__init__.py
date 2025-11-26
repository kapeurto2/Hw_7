"""간단한 통계 처리 패키지."""

from .descriptive import 평균, 중앙값, 분산, 표준편차, 요약
from .inference import 표본평균_신뢰구간

__all__ = [
    "평균",
    "중앙값",
    "분산",
    "표준편차",
    "요약",
    "표본평균_신뢰구간",
]
