class User:
    def __init__(
        self,
        id,
        email,
        password_hash,
        role,
        first_name,
        last_name,
        is_active,
        organization_id,
        employee_id
    ):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.organization_id = organization_id
        self.employee_id = employee_id

    @staticmethod
    def from_db(row):
        return User(
            id=row[0],
            email=row[1],
            password_hash=row[2],
            role=row[3],
            first_name=row[4],
            last_name=row[5],
            is_active=row[6],
            organization_id=row[7],
            employee_id=row[8],
        )
