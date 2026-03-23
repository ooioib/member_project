# tests/conftest.py
import pytest
from apps.member_manager import MemberManager


@pytest.fixture
# 회원이 없는 상태
def empty_manager():
    manager = MemberManager()

    return manager
    pass


@pytest.fixture
# 회원이 1명 있는 상태
# add_member(user_id, name, email) 메서드를 이용해서 회원 추가
def manager_with_one_members():
    manager = MemberManager()
    manager.add_member("user1", "홍길동", "user1@gmail.com")
    return manager
    pass


@pytest.fixture
# 회원이 여러명 있는 상태
def manager_with_many_members():
    manager = MemberManager()
    manager.add_member("user1", "홍길동", "user1@gmail.com")
    manager.add_member("user2", "홍길순", "user2@gmail.com")
    manager.add_member("user3", "홍길자", "user3@gmail.com")
    return manager
    pass
