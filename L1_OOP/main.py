from L1_OOP.controllers import RegisterViewController
from L1_OOP.fixtures import user1
from L1_OOP.http import Request

if __name__ == '__main__':
    controller = RegisterViewController()
    # Get
    get_request = Request(method='GET', data={'pk': 2})
    response1 = controller.dispatch(get_request)
    assert response1.status == 200
    # Post
    post_request = Request(method='POST', data=user1)
    response2 = controller.dispatch(post_request)
    assert response2.status == 201
