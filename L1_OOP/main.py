from L1_OOP.controllers import RegisterViewController
from L1_OOP.fixtures import user3
from L1_OOP.http import Request

if __name__ == '__main__':
    print('-------------------------')
    print('Creating controller')
    print('-------------------------')
    controller = RegisterViewController()
    # Get
    print('Dispatching GET request')
    print('-------------------------')
    get_request = Request(method='GET', data={'pk': 2})
    response1 = controller.dispatch(get_request)
    assert response1.status == 200
    print('GET request success')
    print('-------------------------')
    # Post
    print('Dispatching POST request')
    print('-------------------------')
    post_request = Request(method='POST', data=user3)
    response2 = controller.dispatch(post_request)
    assert response2.status == 201
    print('POST request success')
    print('-------------------------')
