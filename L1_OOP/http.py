from typing import Optional

from L1_OOP.types import DataType


class Request:
    """
    Mocks request object
    """
    method: str
    data: DataType

    def __init__(self, method: str, data: DataType):
        self.method = method
        self.data = data


class Response:
    """
    Mocks response object
    """
    data: DataType
    html_template: str
    status: int

    def __init__(self, html_template: str, status: int, data: Optional[DataType] = None):
        self.html_template = html_template
        self.data = data
        self.status = status
