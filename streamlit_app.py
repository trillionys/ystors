import random
import streamlit as st

st.set_page_config(page_title="통합 오라클 리딩", page_icon="🔮", layout="wide")

DICE = {
    1: "시작, 단순함, 씨앗, 의지",
    2: "균형, 관계, 선택, 반응",
    3: "확장, 표현, 창조성, 연결",
    4: "구조, 안정, 현실화, 질서",
    5: "변화, 이동, 실험, 흔들림",
    6: "조화, 돌봄, 회복, 완성감",
}

ZODIACS = {
    "양자리": "시작, 직진, 용기, 충동",
    "황소자리": "감각, 안정, 소유, 지속",
    "쌍둥이자리": "호기심, 언어, 정보, 변주",
    "게자리": "보호, 가족성, 감정, 내면",
    "사자자리": "창조성, 자기표현, 자부심, 빛",
    "처녀자리": "분석, 정리, 개선, 실용",
    "천칭자리": "균형, 관계, 미학, 조율",
    "전갈자리": "심층성, 집착, 변형, 비밀",
    "사수자리": "탐험, 철학, 확장, 낙관",
    "염소자리": "목표, 책임, 성취, 체계",
    "물병자리": "독립성, 미래성, 공동체, 혁신",
    "물고기자리": "공감, 상상, 영성, 해체",
}

PLANETS = {
    "태양": "정체성, 생명력, 중심성, 드러남",
    "달": "감정, 무의식, 리듬, 보호",
    "수성": "사고, 언어, 정보, 연결",
    "금성": "사랑, 미감, 관계, 끌림",
    "화성": "행동, 욕망, 추진력, 충돌",
    "목성": "확장, 행운, 신념, 성장",
    "토성": "책임, 한계, 시간, 구조",
    "천왕성": "해방, 돌파, 혁신, 예측불가",
    "해왕성": "꿈, 영감, 환상, 경계의 흐림",
    "명왕성": "심층 변화, 권력, 죽음과 재생",
}

TAROT_MAJOR = [
    ("바보", "새로운 여정, 가능성, 무모함"),
    ("마법사", "의지, 기술, 현실화"),
    ("여사제", "직관, 비밀, 내면의 지혜"),
    ("여제", "풍요, 돌봄, 창조성"),
    ("황제", "질서, 권위, 구조"),
    ("교황", "전통, 가르침, 신념 체계"),
    ("연인", "선택, 결합, 가치관"),
    ("전차", "승리, 통제, 추진력"),
    ("힘", "용기, 인내, 부드러운 힘"),
    ("은둔자", "성찰, 고독, 탐구"),
    ("운명의 수레바퀴", "전환점, 순환, 운"),
    ("정의", "균형, 책임, 판단"),
    ("매달린 사람", "멈춤, 관점 전환, 희생"),
    ("죽음", "끝맺음, 변형, 재생"),
    ("절제", "조화, 중용, 통합"),
    ("악마", "집착, 욕망, 속박"),
    ("탑", "붕괴, 해방, 충격적 진실"),
    ("별", "희망, 치유, 비전"),
    ("달", "불안, 무의식, 환상"),
    ("태양", "명료함, 기쁨, 생명력"),
    ("심판", "각성, 부름, 재평가"),
    ("세계", "완성, 통합, 성취"),
]

SUITS = {
    "완드": "열정, 행동, 창의적 에너지",
    "컵": "감정, 관계, 공감",
    "소드": "사고, 갈등, 언어, 결단",
    "펜타클": "현실, 몸, 돈, 안정",
}

RANKS = [
    ("에이스", "씨앗, 시작, 가능성"),
    ("2", "선택, 균형, 상호작용"),
    ("3", "성장, 협력, 표현"),
    ("4", "안정, 기반, 정체"),
    ("5", "갈등, 변화, 균열"),
    ("6", "회복, 조화, 주고받음"),
    ("7", "평가, 인내, 전략"),
    ("8", "숙련, 반복, 속도"),
    ("9", "성취 직전, 내적 완성"),
    ("10", "완성, 부담, 다음 단계"),
    ("페이지", "배움, 메시지, 호기심"),
    ("나이트", "움직임, 추구, 돌진"),
    ("퀸", "수용, 성숙, 내면화"),
    ("킹", "통제, 책임, 외적 완성"),
]

HEXAGRAMS = {
    "111111": ("건", "창조성, 추진력, 강한 시작, 주도권"),
    "000000": ("곤", "수용성, 기반, 돌봄, 기다림"),
    "100010": ("준", "시작의 혼란, 어려운 출발, 씨앗"),
    "010001": ("몽", "미숙함, 배움, 안내, 성장 전 단계"),
    "111010": ("수", "기다림, 준비, 때를 살핌"),
    "010111": ("송", "갈등, 논쟁, 원칙의 충돌"),
    "010000": ("사", "조직, 전략, 집단적 움직임"),
    "000010": ("비", "협력, 결합, 서로 기대는 힘"),
    "111011": ("소축", "작은 축적, 섬세한 조율"),
    "110111": ("리", "조심스러운 전진, 예의, 균형"),
    "111000": ("태", "평화, 소통, 조화로운 흐름"),
    "000111": ("비괘", "막힘, 단절, 흐름의 정체"),
    "101111": ("동인", "사람들과의 연대, 공동의 뜻"),
    "111101": ("대유", "큰 소유, 풍요, 자원의 확장"),
    "001000": ("겸", "겸손, 낮춤, 안정된 성장"),
    "000100": ("예", "기쁨, 준비된 움직임, 활력"),
    "100110": ("수", "따름, 흐름을 받아들임"),
    "011001": ("고", "오래된 문제의 수리, 정비"),
    "110000": ("임", "다가옴, 기회, 성장의 접근"),
    "000011": ("관", "관찰, 통찰, 거리를 둔 이해"),
    "100101": ("서합", "막힌 것을 깨물어 통과함, 결단"),
    "101001": ("비", "꾸밈, 형식, 아름답게 드러남"),
    "000001": ("박", "벗겨짐, 약화, 구조의 붕괴"),
    "100000": ("복", "돌아옴, 회복, 새로운 주기"),
    "100111": ("무망", "순수함, 억지 없는 흐름"),
    "111001": ("대축", "큰 축적, 힘의 저장"),
    "100001": ("이", "기름, 돌봄, 말과 음식의 상징"),
    "011110": ("대과", "큰 과잉, 무게, 압박"),
    "010010": ("감", "깊은 물, 위험, 반복되는 시험"),
    "101101": ("리", "불, 명료함, 의식의 밝음"),
    "001110": ("함", "감응, 끌림, 마음의 움직임"),
    "011100": ("항", "지속, 꾸준함, 관계의 유지"),
    "001111": ("돈", "물러남, 후퇴, 거리두기"),
    "111100": ("대장", "큰 힘, 강한 추진력"),
    "000101": ("진", "나아감, 상승, 인정받음"),
    "101000": ("명이", "상처 입은 빛, 숨겨진 지혜"),
    "101011": ("가인", "가족, 내부 질서, 가까운 관계"),
    "110101": ("규", "어긋남, 차이, 다른 시선"),
    "001010": ("건", "험난함, 장애, 넘기 어려운 고비"),
    "010100": ("해", "풀림, 해방, 긴장의 완화"),
    "110001": ("손", "덜어냄, 비움, 절제"),
    "100011": ("익", "더함, 성장, 보탬"),
    "111110": ("쾌", "결단, 터뜨림, 분명한 선택"),
    "011111": ("구", "마주침, 유혹, 갑작스러운 만남"),
    "000110": ("췌", "모임, 집중, 집단의 힘"),
    "011000": ("승", "상승, 점진적 성장"),
    "010110": ("곤", "갇힘, 압박, 제한"),
    "011010": ("정", "우물, 근원, 공동의 자원"),
    "101110": ("혁", "혁명, 변화, 낡은 틀의 교체"),
    "011101": ("정", "솥, 변형, 새롭게 익힘"),
    "100100": ("진", "우레, 충격, 각성"),
    "001001": ("간", "멈춤, 산, 고요한 집중"),
    "001011": ("점", "점진적 진행, 천천히 자리잡음"),
    "110100": ("귀매", "불균형한 결합, 성급한 연결"),
    "101100": ("풍", "풍성함, 절정, 밝은 순간"),
    "001101": ("여", "나그네, 임시성, 이동"),
    "011011": ("손", "바람, 스며듦, 부드러운 영향력"),
    "110110": ("태", "기쁨, 말, 즐거운 교류"),
    "010011": ("환", "흩어짐, 분산, 풀어냄"),
    "110010": ("절", "절제, 한계 설정, 규칙"),
    "110011": ("중부", "진실한 마음, 내적 신뢰"),
    "001100": ("소과", "작은 지나침, 세밀함, 조심"),
    "101010": ("기제", "이미 이룸, 완성 후 관리"),
    "010101": ("미제", "아직 이루지 못함, 전환 직전"),
}


def reverse_meaning(text):
    return f"{text}의 지연, 과잉, 내면화 또는 뒤틀린 표현"


def build_tarot_deck():
    deck = []

    for name, meaning in TAROT_MAJOR:
        for orientation in ["정방향", "역방향"]:
            deck.append({
                "name": name,
                "orientation": orientation,
                "meaning": meaning if orientation == "정방향" else reverse_meaning(meaning),
            })

    for suit, suit_meaning in SUITS.items():
        for rank, rank_meaning in RANKS:
            for orientation in ["정방향", "역방향"]:
                meaning = f"{suit_meaning}; {rank_meaning}"
                deck.append({
                    "name": f"{suit} {rank}",
                    "orientation": orientation,
                    "meaning": meaning if orientation == "정방향" else reverse_meaning(meaning),
                })

    random.shuffle(deck)
    return deck


def init():
    defaults = {
        "dice": None,
        "dice_preview": (1, 1),
        "tarot_deck": build_tarot_deck(),
        "tarot": None,
        "iching": None,
        "zodiac": None,
        "zodiac_preview": "양자리",
        "planet": None,
        "planet_preview": "태양",
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def dice_face(n):
    return ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"][n - 1]


def draw_iching():
    lines = [random.choice([0, 1]) for _ in range(6)]
    key = "".join(map(str, lines))
    name, meaning = HEXAGRAMS[key]

    yin_count = lines.count(0)
    yang_count = lines.count(1)

    if yang_count > yin_count:
        balance = "양의 기운이 강해 바깥으로 움직이고 밀어붙이는 흐름이 큽니다."
    elif yin_count > yang_count:
        balance = "음의 기운이 강해 받아들이고 숙성시키는 흐름이 큽니다."
    else:
        balance = "음양이 균형을 이루어 선택과 조율이 중요한 흐름입니다."

    return {
        "lines": lines,
        "key": key,
        "name": name,
        "meaning": meaning,
        "balance": balance,
    }


def line_view(line):
    return "━━━━━━" if line == 1 else "━━  ━━"


def ready():
    return all([
        st.session_state.dice,
        st.session_state.tarot,
        st.session_state.iching,
        st.session_state.zodiac,
        st.session_state.planet,
    ])


def make_keywords_from_text(text):
    candidates = [
        "정리", "전환", "균형", "회복", "확장", "통찰", "절제", "실행",
        "기다림", "해방", "관계", "구조", "내면", "성장", "선택",
        "명료함", "수용", "변화", "집중", "재정렬"
    ]

    scored = [(word, text.count(word)) for word in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)

    picked = [word for word, score in scored if score > 0][:3]

    while len(picked) < 3:
        word = random.choice(candidates)
        if word not in picked:
            picked.append(word)

    return picked[:3]


def integrated_reading():
    a, b = st.session_state.dice
    tarot = st.session_state.tarot
    iching = st.session_state.iching
    zodiac = st.session_state.zodiac
    planet = st.session_state.planet

    dice_sum = a + b

    if dice_sum <= 4:
        rhythm = "아직 크게 펼쳐지기 전의 조심스러운 시작"
        rhythm_detail = "지금은 빠르게 결과를 만들기보다 작은 신호를 놓치지 않고 관찰하는 쪽이 좋습니다."
    elif dice_sum <= 8:
        rhythm = "현실적인 조율과 균형을 요구하는 중간 흐름"
        rhythm_detail = "어느 한쪽으로 치우치기보다 이미 놓여 있는 조건들을 정리하고 맞춰 가는 힘이 중요합니다."
    else:
        rhythm = "에너지가 바깥으로 강하게 확장되는 흐름"
        rhythm_detail = "움직임 자체는 강하지만, 방향이 정돈되지 않으면 힘이 분산될 수 있습니다."

    if tarot["orientation"] == "역방향":
        tarot_layer = (
            "심리적인 층위에서는 막힘, 지연, 과잉, 혹은 자기 안에서 아직 정리되지 않은 태도가 강조됩니다. "
            "겉으로 더 많은 행동을 취하기보다, 왜 어떤 흐름이 자연스럽게 열리지 않는지 살피는 것이 우선입니다."
        )
    else:
        tarot_layer = (
            "심리적인 층위에서는 상징이 비교적 직접적으로 드러납니다. "
            "지금 느끼는 감각이나 판단을 지나치게 의심하기보다, 그것이 어디로 향하고 있는지 차분히 확인하는 것이 좋습니다."
        )

    reading = f"""
이번 리딩의 전체 분위기는 **{rhythm}**입니다.  
{rhythm_detail}

현재의 상징들은 빠른 결론보다는, 먼저 흐름을 정리하고 방향을 가다듬으라는 쪽에 가깝습니다.  
겉으로는 단순한 우연처럼 보이지만, 여러 요소가 함께 놓였을 때 반복해서 드러나는 핵심은  
**무엇을 더할 것인가보다 무엇을 정돈해야 하는가**에 있습니다.

{tarot_layer}

구조적으로는 **{iching['name']}**의 흐름이 깔려 있습니다.  
이 괘는 `{iching['meaning']}`의 상징을 가집니다.  
{iching['balance']}  
따라서 현재의 흐름은 완전히 고정된 결론이라기보다, 작은 선택과 태도 변화에 따라 방향이 달라질 수 있는 상태입니다.

표현 방식에서는 **{zodiac}**의 성질이 드러납니다.  
`{ZODIACS[zodiac]}`의 기운은 지금의 상징을 지나치게 추상적인 예언으로 보기보다,  
실제 태도와 습관, 반응 방식 속에서 읽어야 한다는 신호로 볼 수 있습니다.

가장 강하게 작동하는 원리는 **{planet}**의 에너지입니다.  
`{PLANETS[planet]}`의 상징은 지금의 흐름이 어디에 힘을 싣고 있는지를 보여줍니다.  
이 에너지는 리딩 전체의 분위기를 결정하는 핵심 축으로 작동합니다.

종합하면, 지금은 하나의 답을 바로 고르는 시기라기보다 흩어진 신호들을 모아 패턴을 읽는 시기입니다.  
불필요한 과잉을 줄이고, 반복해서 나타나는 감각을 따라가면 방향이 더 선명해집니다.  
무리하게 결론을 앞당기기보다는, 현재 드러난 상징들이 어디에서 서로 겹치는지 보는 것이 중요합니다.
"""

    keys = make_keywords_from_text(reading)
    return reading, keys


init()

st.title("🔮 통합 오라클 리딩")
st.write("직접 굴리고, 멈추고, 선택해서 다섯 가지 상징을 모으는 오라클 리딩입니다.")

if st.button("전체 초기화"):
    st.session_state.dice = None
    st.session_state.dice_preview = (1, 1)
    st.session_state.tarot = None
    st.session_state.tarot_deck = build_tarot_deck()
    st.session_state.iching = None
    st.session_state.zodiac = None
    st.session_state.zodiac_preview = "양자리"
    st.session_state.planet = None
    st.session_state.planet_preview = "태양"
    st.rerun()

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("🎲 주사위")
    a, b = st.session_state.dice_preview
    st.markdown(f"## {dice_face(a)} {dice_face(b)}")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("굴리기", key="roll_dice"):
            st.session_state.dice_preview = (
                random.randint(1, 6),
                random.randint(1, 6),
            )
            st.rerun()

    with c2:
        if st.button("이 숫자로 멈추기", key="stop_dice"):
            st.session_state.dice = st.session_state.dice_preview
            st.rerun()

    if st.session_state.dice:
        x, y = st.session_state.dice
        st.success("주사위를 멈췄습니다.")
        st.write(f"**결과:** {x} + {y} = {x + y}")
        st.write(f"{x}: {DICE[x]}")
        st.write(f"{y}: {DICE[y]}")

with col2:
    st.header("🃏 타로카드")

    if st.button("카드 다시 섞기"):
        st.session_state.tarot_deck = build_tarot_deck()
        st.session_state.tarot = None
        st.rerun()

    if st.session_state.tarot:
        t = st.session_state.tarot
        st.success("카드를 선택했습니다.")
        st.write(f"**{t['name']} · {t['orientation']}**")
        st.write(t["meaning"])
    else:
        st.write("아래 156장의 카드 뒷면 중 하나를 직접 선택하세요.")
        cols = st.columns(12)

        for i, card in enumerate(st.session_state.tarot_deck):
            with cols[i % 12]:
                if st.button("🂠", key=f"tarot_card_{i}"):
                    st.session_state.tarot = card
                    st.rerun()

st.divider()

col3, col4, col5 = st.columns(3)

with col3:
    st.header("☯️ 주역")

    if st.button("6효 뽑기"):
        st.session_state.iching = draw_iching()
        st.rerun()

    if st.session_state.iching:
        y = st.session_state.iching

        for line in reversed(y["lines"]):
            st.markdown(f"### {line_view(line)}")

        st.write(f"**{y['name']}**")
        st.write(y["meaning"])
        st.caption(y["balance"])

with col4:
    st.header("♈ 별자리")

    st.markdown(f"## {st.session_state.zodiac_preview}")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("굴리기", key="roll_zodiac"):
            st.session_state.zodiac_preview = random.choice(list(ZODIACS.keys()))
            st.rerun()

    with c2:
        if st.button("이 별자리로 멈추기", key="stop_zodiac"):
            st.session_state.zodiac = st.session_state.zodiac_preview
            st.rerun()

    if st.session_state.zodiac:
        z = st.session_state.zodiac
        st.success("별자리를 멈췄습니다.")
        st.write(f"**{z}**")
        st.write(ZODIACS[z])

with col5:
    st.header("🪐 행성")

    st.markdown(f"## {st.session_state.planet_preview}")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("굴리기", key="roll_planet"):
            st.session_state.planet_preview = random.choice(list(PLANETS.keys()))
            st.rerun()

    with c2:
        if st.button("이 행성으로 멈추기", key="stop_planet"):
            st.session_state.planet = st.session_state.planet_preview
            st.rerun()

    if st.session_state.planet:
        p = st.session_state.planet
        st.success("행성을 멈췄습니다.")
        st.write(f"**{p}**")
        st.write(PLANETS[p])

st.divider()

st.header("✨ 통합 해석")

if ready():
    reading, ks = integrated_reading()

    st.subheader("통합 리딩")
    st.markdown(reading)

    st.subheader("키워드 3개")
    st.write(" · ".join(ks))
else:
    st.info("5가지 결과가 모두 모이면 통합 해석이 나타납니다.")

st.caption("이 앱은 상징 해석용 엔터테인먼트 도구입니다.")