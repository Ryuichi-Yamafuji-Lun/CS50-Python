#unit test twitter
from twttr import shorten

def test_shorten():
    assert shorten('aeiouAEIOU') == ''
    assert shorten('UnIvErSiTy') == 'nvrSTy'