import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 & 포켓몬 추천", page_icon="🎮")

# MBTI 데이터 정의 (포켓몬 도감 번호를 활용해 공식 이미지 URL 생성)
mbti_pokemon_data = {
    "INTJ": {
        "job": "과학자 / 전략가 / 시스템 아키텍트",
        "pokemon": "후딘 (Alakazam)",
        "id": 65,
        "desc": "높은 지능과 분석력으로 완벽한 전략을 세우는 모습이 INTJ의 이성적인 성격과 똑 닮았습니다."
    },
    "INTP": {
        "job": "연구원 / 소프트웨어 개발자 / 분석가",
        "pokemon": "폴리곤 (Porygon)",
        "id": 137,
        "desc": "인공적으로 만들어진 데이터 포켓몬으로, 끊임없이 정보를 탐구하고 분석하는 INTP 개발자에게 딱 어울립니다."
    },
    "ENTJ": {
        "job": "경영자 / 프로젝트 매니저 / 리더",
        "pokemon": "망나뇽 (Dragonite)",
        "id": 149,
        "desc": "강력한 힘과 지적 능력을 겸비하고 집단을 이끄는 든든한 대장부의 면모가 ENTJ 리더와 어울립니다."
    },
    "ENTP": {
        "job": "창업가 / 발명가 / 기획자",
        "pokemon": "팬텀 (Gengar)",
        "id": 94,
        "desc": "창의적이고 장난기 넘치며, 늘 새로운 방식으로 판을 흔드는 것을 즐기는 ENTP와 환상의 케미를 자랑합니다."
    },
    "INFJ": {
        "job": "상담사 / 작가 / 교사",
        "pokemon": "뮤 (Mew)",
        "id": 151,
        "desc": "깊은 통찰력과 따뜻한 마음으로 세상의 조화를 바라는 신비로운 존재감이 INFJ와 닮았습니다."
    },
    "INFP": {
        "job": "예술가 / 시인 / 소설가",
        "pokemon": "이브이 (Eevee)",
        "id": 133,
        "desc": "무한한 가능성을 품고 있으며 자신만의 독특한 자아(진화)를 찾아 나서는 감성적인 모습이 INFP 그 자체입니다."
    },
    "ENFJ": {
        "job": "사회활동가 / 외교관 / 비영리 단체 리더",
        "pokemon": "토게키스 (Togekiss)",
        "id": 468,
        "desc": "사람들에게 기쁨과 평화를 나누어 주며, 화합을 이끌어내는 따뜻한 마음씨가 ENFJ와 매칭됩니다."
    },
    "ENFP": {
        "job": "크리에이터 / 마케터 / 이벤트 플래너",
        "pokemon": "피카츄 (Pikachu)",
        "id": 25,
        "desc": "통통 튀는 에너지와 밝은 매력으로 어디서나 분위기 메이커 역할을 톡톡히 해내는 ENFP의 정석입니다."
    },
    "ISTJ": {
        "job": "회계사 / 공무원 / 기록 보관원",
        "pokemon": "메타그로스 (Metagross)",
        "id": 376,
        "desc": "정확하고 빈틈없는 계산 능력과 규칙을 철저히 준수하는 신뢰감이 ISTJ의 성격과 어울립니다."
    },
    "ISFJ": {
        "job": "간호사 / 초등 교사 / 사회복지사",
        "pokemon": "해피너스 (Blissey)",
        "id": 242,
        "desc": "아프고 다친 이들을 헌신적으로 보살피며 평화와 안정을 주는 모습이 ISFJ 수호자형과 완벽히 일치합니다."
    },
    "ESTJ": {
        "job": "경찰관 / 군인 / 관리자",
        "pokemon": "윈디 (Arcanine)",
        "id": 59,
        "desc": "충성심이 강하고 체계적이며, 강한 책임감으로 질서를 수호하는 모습이 ESTJ의 면모를 보여줍니다."
    },
    "ESFJ": {
        "job": "호텔리어 / 홍보 담당자 / 상담 전문가",
        "pokemon": "푸린 (Jigglypuff)",
        "id": 39,
        "desc": "타인의 감정에 깊이 공감하고 주변 사람들을 조화롭게 챙겨주는 친근한 매력이 ESFJ와 닮았습니다."
    },
    "ISTP": {
        "job": "엔지니어 / 파일럿 / 기술 전문가",
        "pokemon": "루카리오 (Lucario)",
        "id": 448,
        "desc": "도구를 다루는 데 능숙하고 침착하며, 뛰어난 피지컬과 실용적인 판단력을 가진 ISTP의 카리스마와 어울립니다."
    },
    "ISFP": {
        "job": "디자이너 / 화가 / 사진작가",
        "pokemon": "루브도 (Smeargle)",
        "id": 235,
        "desc": "꼬리 끝의 물감으로 세상을 자유롭게 캔버스 삼아 그리는 예술가적인 기질이 ISFP와 꼭 맞습니다."
    },
    "ESTP": {
        "job": "소방관 / 운동선수 / 영업 대표",
        "pokemon": "초염몽 (Infernape)",
        "id": 392,
        "desc": "행동이 먼저 앞서는 열정적인 파이터로, 스릴을 즐기고 실전에서 강한 능력을 발휘하는 ESTP와 같습니다."
    },
    "ESFP": {
        "job": "연예인 / 레크리에이션 강사 / 승무원",
        "pokemon": "에레키드 (Elekid)",
        "id": 239,
        "desc": "한순간도 지루할 틈 없이 주변을 유쾌한 에너지와 웃음으로 가득 채우는 스타성이 ESFP와 판박이입니다."
    }
}

# UI 구성
st.title("🔮 MBTI 직업 맞춤형 포켓몬 추천기")
st.write("본인의 MBTI를 선택하면 어울리는 직업군과 파트너 포켓몬을 추천해 드립니다.")

# MBTI 선택 박스
mbti_list = list(mbti_pokemon_data.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

if selected_mbti:
    data = mbti_pokemon_data[selected_mbti]
    
    # 구분선
    st.markdown("---")
    
    # 2열 레이아웃 구성
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(f"✨ {selected_mbti}의 추천 직업")
        st.info(f"👉 **{data['job']}**")
        
        st.subheader(f"🐉 추천 파트너 포켓몬")
        st.success(f"**{data['pokemon']}**")
        st.write(data['desc'])
        
    with col2:
        # 공식 포켓몬 고화질 이미지 URL (Official Artwork 사용)
        img_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{data['id']}.png"
        st.image(img_url, caption=data['pokemon'], use_container_width=True)
