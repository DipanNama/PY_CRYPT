import unittest, json, ast
from pathlib import Path
from PY_CRYP7 import encode, decode, HASH_CODE
class CodecTests(unittest.TestCase):
    def test_roundtrip(self):
        for text in ['', '  Hello  world!  ', '\tA\r\n B\n', ''.join(HASH_CODE), 'a'*1000]:
            self.assertEqual(decode(encode(text)), text)
    def test_original(self):
        original=ast.literal_eval(ast.parse(Path('legacy/PY_CRYP7.py').read_text()).body[0].value)
        self.assertEqual(HASH_CODE,original)
        self.assertEqual(json.loads(Path('site/alphabet.json').read_text()), original)
    def test_bad_text(self):
        for text in [None, '🙂', "'", 'a'*1001]:
            with self.assertRaises(ValueError): encode(text)
    def test_bad_envelopes(self):
        for x in ['', '{}', '[]', 'null', '{', json.dumps({'format':'wrong','tokens':[]}), json.dumps({'format':'pycrypt-toy-v1','tokens':[None]}), json.dumps({'format':'pycrypt-toy-v1','tokens':['unknown']}), 'x'*50001]:
            with self.assertRaises(ValueError): decode(x)
    def test_repetition(self):
        x=json.loads(encode('aa'))
        self.assertEqual(x['tokens'][0],x['tokens'][1])
    def test_limits(self):
        with self.assertRaises(ValueError): decode(json.dumps({'format':'pycrypt-toy-v1','tokens':[' ']*1001}))
if __name__ == '__main__': unittest.main()
