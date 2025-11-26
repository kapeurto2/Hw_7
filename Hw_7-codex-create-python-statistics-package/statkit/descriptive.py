"""기술 통계 함수를 제공한다."""

from typing import Iterable, List
import math


def _정제된_수치들(data: Iterable[float]) -> List[float]:
    """반복 가능한 자료에서 숫자만 추출하여 정렬된 리스트로 반환한다.

    잘못된 값이 섞인 경우를 대비해 float 변환에 실패하면 건너뛴다.
    빈 데이터는 ValueError를 발생시킨다.
    """

    숫자들 = []
    for 값 in data:
        try:
            숫자들.append(float(값))
        except (TypeError, ValueError):
            # 숫자로 변환되지 않는 값은 무시한다.
            continue

    if not 숫자들:
        raise ValueError("계산할 수 있는 숫자가 없습니다.")

    숫자들.sort()
    return 숫자들


def 평균(data: Iterable[float]) -> float:
    """산술평균을 계산한다."""

    숫자들 = _정제된_수치들(data)
    return sum(숫자들) / len(숫자들)


def 중앙값(data: Iterable[float]) -> float:
    """중앙값을 계산한다."""

    숫자들 = _정제된_수치들(data)
    길이 = len(숫자들)
    중간 = 길이 // 2

    if 길이 % 2 == 1:
        return 숫자들[중간]

    return (숫자들[중간 - 1] + 숫자들[중간]) / 2


def 분산(data: Iterable[float], sample: bool = True) -> float:
    """표본 또는 모분산을 계산한다.

    sample=True이면 자유도 n-1을 사용하고, False이면 n을 사용한다.
    """

    숫자들 = _정제된_수치들(data)
    n = len(숫자들)
    if n < 2:
        raise ValueError("분산을 계산하려면 최소 2개의 숫자가 필요합니다.")

    평균값 = 평균(숫자들)
    제곱합 = sum((x - 평균값) ** 2 for x in 숫자들)
    자유도 = n - 1 if sample else n
    return 제곱합 / 자유도


def 표준편차(data: Iterable[float], sample: bool = True) -> float:
    """표본 또는 모표준편차를 계산한다."""

    return math.sqrt(분산(data, sample=sample))


def 요약(data: Iterable[float], sample: bool = True) -> dict:
    """기본적인 기술 통계량을 묶어서 반환한다."""

    숫자들 = _정제된_수치들(data)
    return {
        "개수": len(숫자들),
        "평균": 평균(숫자들),
        "중앙값": 중앙값(숫자들),
        "분산": 분산(숫자들, sample=sample),
        "표준편차": 표준편차(숫자들, sample=sample),
        "최솟값": 숫자들[0],
        "최댓값": 숫자들[-1],
    }
