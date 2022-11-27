import pytest
from services import rules_modules

class TestRulesClass:
    
    @pytest.mark.parametrize("test_input,expected", [("ABC123456#%",11), ("123456",6)])
    def test_count_size(self,test_input,expected):
        assert rules_modules.count_size(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [("ABC123456#%",2), ("123456",0),("!@#$%^&*()-+\/{}[]",18),("a!@#B123$Hello\/",6)])
    def test_count_special(self,test_input,expected):
        assert rules_modules.count_special(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [("ABC123456#%",3), ("123456",0),("AaBbCc12345T",4)])
    def test_count_uppercase(self,test_input,expected):
        assert rules_modules.count_uppercase(test_input) == expected
        
    @pytest.mark.parametrize("test_input,expected", [("ABC123456#%",0), ("123456",0),("AaBbCc12345T",3),("#iAaBbCc12345T",4)])
    def test_count_lowercase(self,test_input,expected):
        assert rules_modules.count_lowercase(test_input) == expected
        
    @pytest.mark.parametrize("test_input,expected", [("ABC12345#%",5), ("123456",6),("7A6aBbCc12345T",7),("#iAaBbT",0)])
    def test_count_numerical(self,test_input,expected):
        assert rules_modules.count_numerical(test_input) == expected
        
    @pytest.mark.parametrize("test_input,expected", [("a123bcd2vv",True), ("123456",False),("7A6aBbCc12345T",False),("#iAaBbCC",True),
                                                ("##12345abc",True)])
    def test_is_repeated(self,test_input,expected):
        assert rules_modules.is_repeated(test_input) == expected
        
    
    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            True),
            ("12345&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            False),
            ("12345&",
             [
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            True)
             ]
    )
    def test_verify_minsize_data(self,password,data,expected):
        assert rules_modules.verify_minsize_data(password,data) == expected

    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            True),
            ("12345&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            False),
            ("12345&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            True)
             ]
    )
    def test_verify_min_special_char_data(self,password,data,expected):
        assert rules_modules.verify_min_special_char_data(password,data) == expected

    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4},
            {"rule": "minUppercase", "value":2}
            ],
            True),
            ("12345&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            True),
            ("12345&T",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4},
            {"rule": "minUppercase", "value":2}
            ],
            False)
             ]
    )
    def test_verify_min_uppercase_data(self,password,data,expected):
        assert rules_modules.verify_min_uppercase_data(password,data) == expected


    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True),
            ("12345&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4}
            ],
            True),
            ("12345&T",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 4},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            False)
             ]
    )
    def test_verify_min_lowercase_data(self,password,data,expected):
        assert rules_modules.verify_min_lowercase_data(password,data) == expected

    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 3},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True),
            ("12345&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 6}
            ],
            False),
            ("12345&T",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True)
             ]
    )
    def test_verify_min_digit_data(self,password,data,expected):
        assert rules_modules.verify_min_digit_data(password,data) == expected

    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 3},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True),
            ("12345&DD",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 6}
            ],
            False),
            ("12345&T",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True)
             ]
    )
    def test_verify_no_repeated_data(self,password,data,expected):
        assert rules_modules.verify_no_repeated_data(password,data) == expected

    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 3},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True),
            ("12345&DD",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 6}
            ],
            False),
            ("ABC12345678#&Tabc",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            True)
             ]
    )
    def test_verify_is_valid_password(self,password,data,expected):
        assert rules_modules.verify_is_valid_password(password,data) == expected

    @pytest.mark.parametrize(
            "password,data,expected",
             [("TesteSenhaForte!123&",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 3},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            {"verify": True,"noMatch":[]}),
            ("12345&DD",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 6}
            ],
            {"verify": False,"noMatch":["minSpecialChars","minDigit","noRepeted"]}),
            ("ABC12345678#&Tabc",
             [
            {"rule": "minSize","value": 8},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "minUppercase", "value":2},
            {"rule": "minLowercase", "value":2}
            ],
            {"verify": True,"noMatch":[]}),
            ("12345&DD",
             [
            {"rule": "minSize","value": 10},
            {"rule": "minSpecialChars","value": 2},
            {"rule": "noRepeted","value": 0},
            {"rule": "minDigit","value": 6},
            {"rule": "minLowercase", "value":2}
            ],
            {"verify": False,"noMatch":["minSize","minSpecialChars","minLowercase","minDigit","noRepeted"]})
            
             ]
    )
    def test_return_verify(self,password,data,expected):
        assert rules_modules.return_verify(password,data) == expected
