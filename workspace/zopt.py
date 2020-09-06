

from typing import Optional

def test(a: str) -> Optional[str]:
    #print(a) ==> {'a': 1234}
    #or
    #print(a) ==> None
    if a == "dog": return None
    else: return a


if __name__ == "__main__":
    print(str(test("dog")))
    print(type(str(test("dog"))))
    print(str(test("doga")))
    print(str(test("dog")) + str(test("doga")))

