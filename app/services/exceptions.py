from http import HTTPStatus


class EmailError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.message = {'error': 'email does not match'}
        self.code = HTTPStatus.CONFLICT
