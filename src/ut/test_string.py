def test_string():
    s = "hello"
    assert len(s) == 5
    assert s.upper() == "HELLO"
    assert s.lower() == "hello"
    assert s.startswith("he")
    assert s.endswith("lo")
    assert s.find("ll") == 2
    assert s.find("xx") == -1
    assert s.replace("ll", "xx") == "hexxo"
    assert "hello" == "hello"
    assert "hello" != "world"
    assert "hello" in "hello world"
    assert "hello" not in "world"
    assert "hello" + "world" == "helloworld"
    assert "hello" * 3 == "hellohellohello"
    assert "hello"[0] == "h"
    assert "hello"[1] == "e"