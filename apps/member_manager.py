# app.member_manager.py

class MemberManager:

    # 회원 정보를 저장하는 딕셔너리
    def __init__(self):
        self.members = {}

    def add_member(self, user_id, name, email):

        # user_id는 최소 3자 이상이어야 함
        if not user_id or len(user_id) < 3:
            raise ValueError("user_id must be at least 3 characters long")

        # name은 공백이면 안 됨
        if not name or not name.strip():
            raise ValueError("name cannot be empty")

        # 이메일 형식 간단 검증 (@, . 포함 여부)
        if "@" not in email or "." not in email:
            raise ValueError("invalid email format")

        # 이미 존재하는 user_id인지 확인
        if user_id in self.members:
            raise ValueError("user_id already exists")

        self.members[user_id] = {
            "name": name,
            "email": email,
        }
        return True  # 성공 시 True

    def get_member(self, user_id):

        # 회원이 존재하지 않으면 에러
        if user_id not in self.members:
            raise KeyError("member not found")
        # 회원 정보 반환
        return self.members[user_id]

    def remove_member(self, user_id):

        # 회원이 없으면 에러
        if user_id not in self.members:
            raise KeyError("member not found")

        # 회원 삭제
        del self.members[user_id]
        return True

    def count_members(self):
        # 현재 회원 수 반환
        return len(self.members)
