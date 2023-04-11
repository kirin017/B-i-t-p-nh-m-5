import pytest
from src.index import is_valid_triangle
import os



# Một hàm test sử dụng cho nhiều test case
# Dùng một hàm test nhưng cho nhiều test case khác nhau
# pytest.mark.parametrize có tác dụng truyền lần lượt các test case vào hàm test của mình
# ta sẽ truyền đối số đầu tiên là các tham số cho hàm test
# đối số thứ 2 là một mảng các test case, với mỗi test case, chương trình sẽ truyền lần lượt các giá trị vào các tham số đã ghi ở đối số thứ nhất
# Về cơ bản, hàm test sẽ chạy n lần, với n là số test case, ở đây ta có 3 test case
# Giá trị của a, expected_result sẽ lần lượt được gán bằng giá trị của từng test case và sau đó được truyền vào hàm test
@pytest.mark.parametrize(
    "a, b, c, expect_result",
    [
    (1, 2, 3, False), # Testcase1
    (5, 3, 2, False), #Testcase2
    (3, 7, 2, False), #Testcase3
    (3, 4, 5, True),  #Testcase4
    (4, 6, 9, True),   #Testcase5
    ],
)
def test_checkTriangle_Funct(a, b, c, expect_result):
    assert is_valid_triangle(a, b, c) == expect_result


