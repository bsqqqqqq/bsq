import json
title='我们 love 你们'
with open('title.json','w',encoding='utf-8') as f:
    json.dump([title],f)