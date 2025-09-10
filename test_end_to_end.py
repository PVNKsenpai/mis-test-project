from src.sample_mis_code import MIS

def test_order_flow():
    system = MIS()
    # Đăng nhập
    assert system.login("admin", "123456")
    # Tạo đơn hàng
    assert system.create_order("Steel", 10)
    # Kiểm tra số đơn
    assert len(system.orders) == 1
