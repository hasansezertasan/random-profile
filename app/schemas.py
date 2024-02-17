import datetime

from pydantic import BaseModel, Field, computed_field


class Profile(BaseModel):
    first_name: str
    last_name: str
    biography: str
    username: str
    password: str
    email: str
    address: str
    profession: str
    date_of_birth: datetime.date
    phone_number: str
    domain: str
    profile_picture: str
    website: str

    @computed_field
    def age(self) -> int:
        today = datetime.date.today()
        age = (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )
        return age

    @computed_field
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
