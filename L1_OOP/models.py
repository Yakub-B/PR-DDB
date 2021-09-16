from dataclasses import dataclass, asdict


@dataclass
class UserModel:
    pk: int
    email: str
    first_name: str
    last_name: str

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    @property
    def as_dict(self) -> dict:
        return asdict(self)

    def __str__(self) -> str:
        return f'User: {self.email}'
