# tests/test_member_manager.py

# 테스트 실행 및 예외 검증을 위한 라이브러리
import pytest

# ==============================================
# 회원이 없는 상태에서 회원 조회 테스트
# ==============================================
def test_get_nonexist_member(empty_manager):        # 회원이 비어있는 상태
    with pytest.raises(KeyError) as info:           # KeyError 발생
        empty_manager.get_member("user")            # 존재하지 않는 회원 조회
    assert 'member not found' in str(info.value)    # 에러 메시지에 not found 포함 여부


# ==============================================
# 회원이 없는 상태에서 잘못된 입력값으로 회원 추가 테스트 
# ==============================================

# 잘못된 입력값 목록
case = [
    ("ab", "Alice", "alice@gmail.com"),   # user_id 길이 부족 (3 미만)
    ("user1", "", " user1@gmail.com"),    # name이 빈 문자열
    ("user2", " ", "user2@gmail.com"),    # name이 공백
    ("user3", "tom", "user3@"),           # email 형식 오류
]

# 여러 입력값을 반복해서 테스트
@pytest.mark.parametrize("user_id, name, email", case)
def test_add_member_invalid_inputs(empty_manager, user_id, name, email):
    with pytest.raises(ValueError):                             # ValueError 발생
        empty_manager.add_member(user_id, name, email)          # 잘못된 입력값으로 회원 추가


# ==============================================
# 회원이 1명 있는 상태에서 회원 삭제 테스트 
# ==============================================
def test_remove_members(manager_with_one_members):              # 회원 1명 존재
    result = manager_with_one_members.remove_member("user1")    # user1 회원 삭제 실행
    assert result == True                                       # 삭제 성공 여부
    assert manager_with_one_members.count_members() == 0        # 삭제 후 회원 수 == 0인지 확인


# ==============================================
# 회원이 여러명 있는 상태에서 회원 추가 테스트
# ==============================================
def test_add_members(manager_with_many_members):                                        # 회원 3명 존재
    cnt_mem = manager_with_many_members.count_members()                                 # 추가 전, 현재 회원 수 저장
    result = manager_with_many_members.add_member("user4", "herny", "user4@gmail.com")  # 회원 추가
    assert result == True                                                               # 추가 성공
#   assert manager_with_many_members.count_members() == 4                               # 회원 수 == 4인지 확인
    assert manager_with_many_members.count_members() == cnt_mem + 1                     # 회원 수가 1 증가했는지 확인


# ==============================================
# 회원이 1명있는 상태에서 회원 조회 테스트
# ==============================================
def test_get_member(manager_with_one_members):               # 회원 1명 존재
    result = manager_with_one_members.get_member("user1")    # user1 회원 정보 조회
    assert result["name"] == "홍길동"                         # 이름이 정확한지 확인
    assert result["email"] == "user1@gmail.com"              # 이메일이 정확한지 확인


# ==============================================
# 회원이 1명인 상태에서 잘못된 입력값으로 회원 추가 테스트
# ==============================================
def test_add_invalid_input2(manager_with_one_members):       # 회원 1명 존재
    with pytest.raises(ValueError):                         # ValueError 발생
        manager_with_one_members.add_member("a", "홍길동", "user1@gmail.com")   # user_id 길이 부족 상태로 회원 추가 시도

