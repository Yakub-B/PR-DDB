from abc import ABC, abstractmethod

from L1_OOP.db import DataBase
from L1_OOP.exceprions import HTTP404
from L1_OOP.types import DataType
from L1_OOP.http import Request, Response


HOME_PAGE = 'path/to/root.html'


class BaseViewController(ABC):
    html_template: str

    @abstractmethod
    def _get(self, request: Request) -> Response:
        raise NotImplementedError()

    @abstractmethod
    def _post(self, request: Request) -> Response:
        raise NotImplementedError()

    def dispatch(self, request: Request) -> Response:
        methods_map = {
            'GET': self._get,
            'POST': self._post,
        }
        try:
            return methods_map[request.method](request)
        except KeyError:
            raise HTTP404(f'{request.method} is not supported')


class RegisterViewController(BaseViewController):
    html_template = '/path/to/register.html'
    _db: DataBase

    def __init__(self):
        self._db = DataBase()
        super(RegisterViewController, self).__init__()

    def _register_user(self, data: DataType):
        self._db.create_user(data)

    def _get(self, request: Request) -> Response:
        pk = request.data['pk']
        user = self._db.get_user(pk)
        return Response(html_template=self.html_template, data=user.as_dict, status=200)

    def _post(self, request: Request) -> Response:
        self._register_user(request.data)
        return Response(html_template=HOME_PAGE, status=201)
