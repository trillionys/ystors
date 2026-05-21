import random
import time
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
    "111111": ("건", "하늘. 창조, 추진력, 강한 양의 에너지"),
    "000000": ("곤", "땅. 수용, 돌봄, 기반, 음의 에너지"),
    "100010": ("준", "시작의 어려움, 혼돈 속의 싹"),
    "010001": ("몽", "미숙함, 배움, 안내가 필요한 상태"),
    "111010": ("수", "기다림, 때를 살핌, 준비"),
    "010111": ("송", "논쟁, 긴장, 원칙의 충돌"),
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
        "tarot_deck": build_tarot_deck(),
        "tarot": None,
        "iching": None,
        "zodiac": None,
        "planet": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def dice_face(n):
    return ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"][n - 1]


def draw_iching():
    lines = [random.choice([0, 1]) for _ in range(6)]
    key = "".join(map(str, lines))
    name, meaning = HEXAGRAMS.get(
        key,
        ("미정괘", "서로 다른 힘이 섞이며 새로운 균형을 찾는 중입니다.")
    )
    return {"lines": lines, "key": key, "name": name, "meaning": meaning}


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


def keywords():
    pool = ["시작", "균형", "전환", "회복", "확장", "통찰", "용기", "수용", "구조", "해방"]
    random.shuffle(pool)
    return pool[:3]


def integrated_reading():
    a, b = st.session_state.dice
    tarot = st.session_state.tarot
    iching = st.session_state.iching
    zodiac = st.session_state.zodiac
    planet = st.session_state.planet
    keys = keywords()

    return f"""
이번 조합은 **{keys[0]}**, **{keys[1]}**, **{keys[2]}**의 흐름으로 읽힙니다.

주사위의 숫자 **{a}와 {b}**는 현재 에너지의 기본 리듬을 보여줍니다.  
타로의 **{tarot["name"]} {tarot["orientation"]}**은 심리적 상징과 내면의 방향을 드러냅니다.  
주역의 **{iching["name"]}**은 상황의 구조와 변화 가능성을 보여줍니다.  
별자리 **{zodiac}**는 이 에너지가 어떤 태도로 표현되는지를 말하고,  
행성 **{planet}**은 가장 강하게 작동하는 원리를 나타냅니다.

통합적으로 보면, 지금은 하나의 정답을 찾기보다는 여러 상징이 가리키는 공통된 패턴을 읽는 시기입니다.  
겉으로는 우연처럼 보이는 요소들이 모여 현재 흐름의 상징적 지도를 만들고 있습니다.
"""


init()

st.title("🔮 통합 오라클 리딩")
st.write("주사위, 타로, 주역, 별자리, 행성을 뽑고 하나의 상징 리딩으로 통합합니다.")

if st.button("전체 초기화"):
    for key in ["dice", "tarot", "iching", "zodiac", "planet"]:
        st.session_state[key] = None
    st.session_state.tarot_deck = build_tarot_deck()
    st.rerun()

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("🎲 주사위")

    if st.button("주사위 굴리고 멈추기"):
        box = st.empty()
        for _ in range(12):
            a, b = random.randint(1, 6), random.randint(1, 6)
            box.markdown(f"# {dice_face(a)} {dice_face(b)}")
            time.sleep(0.05)

        st.session_state.dice = (random.randint(1, 6), random.randint(1, 6))
        st.rerun()

    if st.session_state.dice:
        a, b = st.session_state.dice
        st.markdown(f"## {dice_face(a)} {dice_face(b)}")
        st.write(f"**결과:** {a} + {b} = {a + b}")
        st.write(f"{a}: {DICE[a]}")
        st.write(f"{b}: {DICE[b]}")

with col2:
    st.header("🃏 타로카드")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("덱 섞기"):
            st.session_state.tarot_deck = build_tarot_deck()
            st.session_state.tarot = None
            st.rerun()

    with c2:
        if st.button("랜덤 1장 뽑기"):
            st.session_state.tarot = random.choice(st.session_state.tarot_deck)
            st.rerun()

    if st.session_state.tarot:
        t = st.session_state.tarot
        st.write(f"**{t['name']} · {t['orientation']}**")
        st.write(t["meaning"])

    with st.expander("156장 랜덤 배열 보기"):
        cols = st.columns(6)
        for i, card in enumerate(st.session_state.tarot_deck):
            mark = "↕" if card["orientation"] == "역방향" else "↑"
            with cols[i % 6]:
                st.caption(f"{i + 1}. {mark} {card['name']}")

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

with col4:
    st.header("♈ 별자리")

    if st.button("별자리 굴리고 멈추기"):
        names = list(ZODIACS.keys())
        box = st.empty()
        for _ in range(14):
            box.markdown(f"## {random.choice(names)}")
            time.sleep(0.04)

        st.session_state.zodiac = random.choice(names)
        st.rerun()

    if st.session_state.zodiac:
        z = st.session_state.zodiac
        st.write(f"**{z}**")
        st.write(ZODIACS[z])

with col5:
    st.header("🪐 행성")

    if st.button("행성 굴리고 멈추기"):
        names = list(PLANETS.keys())
        box = st.empty()
        for _ in range(14):
            box.markdown(f"## {random.choice(names)}")
            time.sleep(0.04)

        st.session_state.planet = random.choice(names)
        st.rerun()

    if st.session_state.planet:
        p = st.session_state.planet
        st.write(f"**{p}**")
        st.write(PLANETS[p])

st.divider()

st.header("✨ 통합 해석")

if ready():
    ks = keywords()
    st.subheader("키워드 3개")
    st.write(", ".join(ks))

    st.subheader("리딩")
    st.markdown(integrated_reading())
else:
    st.info("5가지 결과가 모두 모이면 통합 해석이 나타납니다.")

st.caption("이 앱은 상징 해석용 엔터테인먼트 도구입니다.")