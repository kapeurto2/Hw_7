"""간단한 통계적 추론 함수를 제공한다."""

from typing import Iterable, Tuple
import math
from .descriptive import 평균, 분산


_Z_값 = {
    0.80: 1.2816,
    0.85: 1.4395,
    0.90: 1.6449,
    0.95: 1.96,
    0.99: 2.5758,
}


def 표본평균_신뢰구간(data: Iterable[float], 신뢰수준: float = 0.95) -> Tuple[float, float]:
    """정규분포를 가정하고 표본평균의 신뢰구간을 계산한다.

    신뢰수준은 0.80, 0.85, 0.90, 0.95, 0.99 중에서 선택한다.
    Z-값을 사용하며, 표본 분산을 모분산의 추정치로 사용한다.
    """

    if 신뢰수준 not in _Z_값:
        raise ValueError("지원하지 않는 신뢰수준입니다. 0.80, 0.85, 0.90, 0.95, 0.99 중 하나를 사용하세요.")

    숫자들 = list(data)
    n = len(숫자들)
    if n == 0:
        raise ValueError("신뢰구간을 계산하려면 최소 1개의 숫자가 필요합니다.")

    평균값 = 평균(숫자들)
    분산값 = 분산(숫자들, sample=True)
    표준오차 = math.sqrt(분산값 / n)
    z = _Z_값[신뢰수준]

    하한 = 평균값 - z * 표준오차
    상한 = 평균값 + z * 표준오차
    return 하한, 상한
