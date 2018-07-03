import lemoncheesecake.api as lcc
from lemoncheesecake.matching import check_that, equal_to, greater_than

from components.user import User, create_user, get_user
from core.common.init import Base

SUITE = {
    "description": "Users API tests",
    "rank": 1
}


@lcc.test("verify get all users")
def verify_get_all_users():
    response = get_user(base_url=Base.USER_BASE_URL)
    num_users = len(response.json())
    check_that("value", response.status_code, equal_to(200))
    check_that("number of users", num_users, greater_than(0))


@lcc.test("verify get user details")
def verify_get_user_details():
    my_user_id = 1
    response = get_user(base_url=Base.USER_BASE_URL, user_id=my_user_id)
    check_that("value", response.status_code, equal_to(200))
    check_that("user_id", response.json()['id'], equal_to(my_user_id))


@lcc.test("verify create user")
def verify_create_user():
    user = User(user_name="Some User", email="someuser@xyz.com")
    response = create_user(base_url=Base.USER_BASE_URL, payload=user.get_create_user_payload())
    check_that("value", response.status_code, equal_to(200))
