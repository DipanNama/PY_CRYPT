const t=require('node:test'),a=require('node:assert/strict'),{execFileSync}=require('node:child_process'),map=require('./site/alphabet.json'),c=require('./site/codec').create(map);
t('roundtrip whitespace, empty and whole alphabet',()=>{for(const s of ['', '  Hello  world!  ','\tA\r\n B\n',Object.keys(map).join(''),'a'.repeat(1000)])a.equal(c.decode(JSON.stringify(c.encode(s))),s);});
t('Python parity',()=>{for(const s of ['', '  Hello  world!  ','\tA\r\n B\n',Object.keys(map).join('')]){const py=execFileSync('python3',['PY_CRYP7.py','encode',s],{encoding:'utf8'}).trim();a.deepEqual(JSON.parse(py),c.encode(s));a.equal(execFileSync('python3',['PY_CRYP7.py','decode',JSON.stringify(c.encode(s))],{encoding:'utf8'}).slice(0,-1),s);}});
t('reject unsupported text',()=>{for(const s of [null,'🙂',"'",'a'.repeat(1001)])a.throws(()=>c.encode(s));});
t('reject malformed tokens',()=>{for(const s of ['', '{}','[]','null','{',JSON.stringify({format:'wrong',tokens:[]}),JSON.stringify({format:'pycrypt-toy-v1',tokens:[null]}),JSON.stringify({format:'pycrypt-toy-v1',tokens:['__proto__']}),'x'.repeat(50001)])a.throws(()=>c.decode(s));});
t('limit tokens',()=>a.throws(()=>c.decode(JSON.stringify({format:'pycrypt-toy-v1',tokens:Array(1001).fill(' ')}))));
t('repeated characters reveal pattern',()=>a.equal(c.encode('aa').tokens[0],c.encode('aa').tokens[1]));
t('safe text data',()=>a.equal(c.decode(JSON.stringify(c.encode('<script>'))),'<script>'));
t('main-only workflow',()=>{const s=require('fs').readFileSync('.github/workflows/pages.yml','utf8');a.ok(s.includes('branches: [main]'));a.ok(!s.includes('workflow_dispatch'));});
