## NLTK
# 지원 언어 : Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Italian, Norwegian, Polish, Portuguese, Russian, Slovene, Spanish, Swedish, Turkish
from nltk import sent_tokenize

text = "I wanna go to home. You too?"
sents = sent_tokenize(text, 'english')
for sent in sents:
    print(sent)


## SpaCy
# 지원 언어 : https://spacy.io/usage/models
from spacy.lang.en import English
from spacy.pipeline import Sentencizer

text = "I wanna go to home. You too?"
nlp = English()
doc = nlp(text)

sentencizer = Sentencizer()
sents = sentencizer(doc)
for sent in sents.sents:
    print(sent.text)


## Thai
from pythainlp import sent_tokenize

text = "เกิดไฟไหม้ลุกลามที่โรงไฟฟ้านิวเคลียร์ซาปอริฌเฌีย โรงไฟฟ้านิวเคลียร์ที่ใหญ่ที่สุดในยุโรป และเป็นหนึ่งในสี่ของโรงไฟฟ้านิวเคลียร์ของประเทศที่ยังเปิดใช้งาน นอกจากนี้ยังเกิดขึ้นหลังจากกองกำลังรัสเซียบุกยึดโรงไฟฟ้านิวเคลียร์เชอร์โนบิลซึ่งอยู่ชานกรุงเคียฟ เมื่อวันที่ 25 ก.พ"

# default (crfcut)
sents = sent_tokenize(text)
for sent in sents:
    print(sent)


## Vietnam
from underthesea import sent_tokenize
text = 'Taylor cho biết lúc đầu cô cảm thấy ngại với cô bạn thân Amanda nhưng rồi mọi thứ trôi qua nhanh chóng. Amanda cũng thoải mái với mối quan hệ này.'

sents = sent_tokenize(text)
for sent in sents:
    print(sent)


### 코드 체크 필요 (리서치)

## Multilingual
# multilanguage도 쓸만한거.. 같아요. 근데 확실하게 잘돌아가는지 모르겠어요.
# trained pipeline에 efficiency 버전과 accuracy 버전이 나눠져있어서 둘 다 테스트 해봤는데요.
# english-efficiency로 토크나이징하면 3개가 나오고, multilanguage-efficiency로 토크나이징하면 각 6, 5개가 나오지만, multilanguage-accuracy로 토크나이징하면 3개로 동일하게 나옵니다.

## Russian
# https://github.com/natasha/natasha

from natasha import Segmenter

segmenter = Segmenter()
text = 'Посол Израиля на Украине Йоэль Лион признался, что пришел в шок, узнав о решении властей Львовской области объявить 2019 год годом лидера запрещенной в России Организации украинских националистов (ОУН) Степана Бандеры. Свое заявление он разместил в Twitter. «Я не могу понять, как прославление тех, кто непосредственно принимал участие в ужасных антисемитских преступлениях, помогает бороться с антисемитизмом и ксенофобией. Украина не должна забывать о преступлениях, совершенных против украинских евреев, и никоим образом не отмечать их через почитание их исполнителей», — написал дипломат. 11 декабря Львовский областной совет принял решение провозгласить 2019 год в регионе годом Степана Бандеры в связи с празднованием 110-летия со дня рождения лидера ОУН (Бандера родился 1 января 1909 года). В июле аналогичное решение принял Житомирский областной совет. В начале месяца с предложением к президенту страны Петру Порошенко вернуть Бандере звание Героя Украины обратились депутаты Верховной Рады. Парламентарии уверены, что признание Бандеры национальным героем поможет в борьбе с подрывной деятельностью против Украины в информационном поле, а также остановит «распространение мифов, созданных российской пропагандой». Степан Бандера (1909-1959) был одним из лидеров Организации украинских националистов, выступающей за создание независимого государства на территориях с украиноязычным населением. В 2010 году в период президентства Виктора Ющенко Бандера был посмертно признан Героем Украины, однако впоследствии это решение было отменено судом. '
doc = Doc(text)

doc.segment(segmenter)
print(doc.tokens[:5])
print(doc.sents[:5])

## 말레이어
# https://malaya.readthedocs.io/en/latest/load-tokenizer.html

## 인도네시아어 tokenizer 는 spacy multilingual 로 대체 검토.
# 혹은 아래 링크 참고
# https://bagas.me/spacy-bahasa-indonesia.html
