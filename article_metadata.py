"""Per-article SEO metadata.

Add one entry per file in `templates/articles/<slug>.html`.

- `title`: search title / browser title
- `description`: meta description shown in search snippets when selected
- `keywords`: kept for editorial consistency, but Google doesn't use it for ranking
- `image`: optional override for og:image / article image
"""

ARTICLE_SEO_METADATA = {
    "avoid-stomach-cancer": {
        "title": "別讓沉默的胃癌悄悄靠近｜胃鏡檢查與保胃5招",
        "description": "胃癌是國人重要的癌症死因之一，初期症狀輕微卻危險。曜弘診所提醒高風險族群應定期做胃鏡檢查，並養成保胃5招好習慣，早期發現、早期治療，提升存活率。",
        "keywords": "胃癌衛教, 舒眠胃鏡推薦, 曜弘診所, 無痛舒眠胃鏡, 內視鏡專科團隊, 肝臟血管瘤, 肝臟超音波, 腹部超音波, 胃鏡推薦, 舒眠胃鏡, 大腸鏡檢查, 高血壓, 脂肪肝, 胃痛, 胃癌, 胰臟腫瘤, 胰臟癌, 三重, 新莊, 蘆洲, 板橋",
        "image": "/static/articlephoto/article-16-stomach-cancer.jpg",
    },
    "case-study-abdominal-ultrasound": {
        "title": "真實案例：慢性咳嗽竟是胰臟癌",
        "description": "60歲男子咳嗽兩月求診，經曜弘診所醫師仔細檢查發現為胰臟癌並已轉移。此案例說明健康檢查的重要性與醫師專業判斷的價值。",
        "keywords": "百萬腹部超音波檢查, 曜弘診所的堅持, 健康檢查的意義, 超音波檢查, 胃鏡推薦, 舒眠胃鏡推薦, 大腸鏡檢查, 大腸鏡推薦, 三重, 新莊, 蘆洲, 板橋, 疫苗, B肝, C肝, 肝硬化, 脂肪肝, 高血壓, 超音波, 肝臟超音波, 腹部超音波, 胰臟腫瘤, 胰臟癌, 肝纖維化, 肝纖維測量, 高階超音波",
        "image": "/static/articlephoto/article-11-case-study-abdominal-ultrasound.jpg",
    },
    "case-study-gastrointestinal-endoscopy": {
        "title": "真實案例：肛門疼痛竟是攝護腺癌",
        "description": "70歲男子因肛門疼痛就診，醫師憑藉專業鑑別與指診發現腫塊，最終確診為攝護腺癌。曜弘診所重視黃金治療期，守護來診者健康。",
        "keywords": "專業鑑別診斷, 曜弘診所的價值, 嚴謹的鑑別診斷與豐富的臨床經驗, 胃鏡推薦, 舒眠胃鏡推薦, 大腸鏡檢查, 大腸鏡推薦, 三重, 新莊, 蘆洲, 板橋, 脂肪肝, 高血壓, 超音波, 肝臟超音波, 腹部超音波, 胰臟腫瘤, 胰臟癌, 胃癌, 胃痛",
        "image": "/static/articlephoto/article-12-case-study-gastrointestinal-endoscopy.jpg",
    },
    "colon-polyp": {
        "title": "大腸瘜肉與大腸鏡",
        "description": "什麼是大腸瘜肉？為何需要定期檢查？了解腺瘤性瘜肉與大腸鏡檢查的重要性，預防大腸癌從早期發現開始。40歲以上或有家族病史者，建議定期檢查，守護腸道健康！。洽詢 02-29840101！",
        "keywords": "大腸瘜肉, 大腸鏡, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡, 消化系專科, 內視鏡專科, 內視鏡技術師資格, 210度可彎前鏡頭視野無死角,富士腸道內視鏡AI影像判讀設備 (CAD EYE), CAD EYE",
    },
    "colon-polyp-cancer-prevention": {
        "title": "大腸息肉 —🥊癌症的前哨站🥊",
        "description": "大腸息肉是大腸癌的前哨站！45歲以上、有家族病史者應定期檢查。曜弘診所引進高階內視鏡，助您早期發現、早期切除息肉，預防癌變。",
        "keywords": "大腸鏡, 息肉切除, 癌症預防, 早期發現早期治療, 三重, 新莊, 蘆洲, 板橋, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 健康檢查, 曜弘診所",
        "image": "/static/articlephoto/article-20-colon-polyp.jpg",
    },
    "colonoscopy-polyp-screening": {
        "title": "身體沒症狀也要查！息肉→癌的真實案例｜曜弘診所提醒",
        "description": "沒有症狀不代表沒有風險！45歲小君主動檢查大腸鏡，竟發現大腸原位癌前兆。曜弘診所提醒您：40歲以上應定期檢查，特別是有家族史者，提早預防才能守住健康！☎️ 02-29840101",
        "keywords": "大腸瘜肉, 大腸鏡, 大腸癌, 息肉切除, 大腸內視鏡, 腺瘤性瘜肉, 大腸鏡檢查, 胃鏡推薦 ,舒眠胃鏡推薦 ,大腸鏡檢查 ,大腸鏡推薦, 新北腸胃科推薦, 曜弘診所, 田名弘, 李儀鳴",
    },
    "fatty-liver": {
        "title": "脂肪肝 —【無聲的肝臟警報】外表看不出來的健康危機‼️",
        "description": "肝臟不會喊痛，但會默默變胖！台灣每三人就要一人有脂肪肝。若不理會可能惡化為肝炎、肝硬化。曜弘診所提供高階超音波檢查，助您早日發現肝臟危機。",
        "keywords": "肝癌, 早期發現早期治療, 肝臟超音波, 三重, 新莊, 蘆洲, 板橋, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 健康檢查, 癌症預防, 曜弘診所, 脂肪肝",
        "image": "/static/articlephoto/article-22-fatty-liver.jpg",
    },
    "fecal-occult-blood-negative": {
        "title": "🔍 糞便潛血陰性，腸道真的沒問題嗎⁉",
        "description": "64歲女性長期腹脹不適，糞便潛血呈陰性卻未能找到原因。來曜弘診所經問診後安排大腸鏡與內視鏡超音波檢查，當下即確診為黏膜下囊腫。糞便潛血陰性不代表腸道無礙，進階內視鏡一次檢查更完整。",
        "keywords": "胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 三重, 新莊, 蘆洲, 板橋, 五股, 黏膜下腫瘤, 內視鏡超音波, 肝臟超音波, 腹部超音波, 高血壓, 脂肪肝, 曜弘診所, 腸胃保健, 健康知識科普, 案例分享, 糞便潛血陰性不代表沒問題, 一次檢查更完整",
        "image": "/static/articlephoto/article-24-fecal-occult-blood-negative.jpg",
    },
    "fecal-occult-blood-test": {
        "title": "糞便潛血",
        "description": "糞便潛血檢查快速無痛！每20位陽性者至少1位是大腸癌患者。了解檢查好處：早期發現大腸癌、預防疾病進展。45歲以上民眾可享補助，每兩年一次。定期檢查，守護腸道健康！。洽詢 02-29840101！",
        "keywords": "糞便潛血, 線瘤性息肉, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡, 消化系專科, 內視鏡專科, 內視鏡技術師資格, 210度可彎前鏡頭視野無死角,富士腸道內視鏡AI影像判讀設備 (CAD EYE), CAD EYE",
        "image": "/static/articlephoto/article-05-fecal-occult-blood-test.jpg",
    },
    "fujifilm7000-endoscope": {
        "title": "精準的內視鏡檢查 - 胃腸異常病灶檢與胃鏡推薦",
        "description": "曜弘醫療團隊致力於提升三重基層診所之醫療照護品質，提供專業高階內視鏡檢查服務，並使用唯一通過全美FDA的AI影像判讀設備，深願提升早期病灶檢測率。",
        "keywords": "胃腸異常病灶檢, 台灣消化系內視鏡醫學會指引, 早期病灶檢測率, 胃鏡推薦, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡, 消化系專科, 內視鏡專科, 內視鏡技術師資格, 富士7000型內視鏡, 富士腸道內視鏡AI影像判讀設備 (CAD EYE), CAD EYE, 富士最新自動化內視鏡清洗設備, Canon Xario-100高階彩色杜卜勒超音波, Canon Xario-100",
        "image": "/static/articlephoto/article-01-fujifilm7000-endoscope.jpg",
    },
    "gallstones": {
        "title": "膽結石 —【小石頭，大危機】",
        "description": "右上腹悶痛、脹氣、吃油就痛？可能是膽結石！曜弘診所提供高階腹部超音波檢查，快速、無痛發現膽結石，預防大危機。",
        "keywords": "膽結石, 腹部超音波, 早期發現早期治療, 三重, 新莊, 蘆洲, 板橋, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 健康檢查, 癌症預防, 曜弘診所",
        "image": "/static/articlephoto/article-21-gallstones.jpg",
    },
    "gastroesophageal-reflux": {
        "title": "胃食道逆流，正確的就醫才能有效對症下藥解決問題",
        "description": "預防與緩解胃食道逆流不適症狀，了解飲食與生活調整技巧！曜弘診所位於新北市三重，專注於肝膽腸胃科與內視鏡檢查，提供專業舒眠胃鏡服務，確保受檢安全與診斷準確，提升生活品質。立即了解詳情！☎️ 02-29840101",
        "keywords": "胃食道逆流, 正確的就醫才能有效對症下藥解決問題, 胃鏡推薦, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡 消化系專科, 內視鏡專科, 內視鏡技術師資格",
        "image": "/static/articlephoto/article-02-gastroesophageal-reflux.png",
    },
    "gastroesophageal-reflux-disease": {
        "title": "胃食道逆流 —「火燒心」不是小事‼️",
        "description": "吃完飯就覺得胸口「火燒燒」？小心是胃食道逆流！症狀包括胸口灼熱、嘴巴有酸苦味。長期忽略可能導致食道炎甚至癌變。",
        "keywords": "肛門指診, 前列腺癌, 早期發現早期治療, 三重, 新莊, 蘆洲, 板橋, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 健康檢查, 癌症預防, 曜弘診所, 胃食道逆流, 火燒心",
        "image": "/static/articlephoto/article-19-gastroesophageal-reflux-disease.jpg",
    },
    "gastroscopy": {
        "title": "照胃鏡痛嗎？",
        "description": "胃鏡檢查很不舒服？其實醫療技術已進步許多！了解舒眠減痛、咽喉局部麻醉、不同內視鏡選擇的優劣與適用情況。曜弘診所提供專業胃鏡檢查，助您輕鬆面對不適，提升健康生活品質。洽詢 02-29840101！",
        "keywords": "照胃鏡痛嗎, 舒眠減痛, 咽喉局部麻醉, 選擇不同內視鏡, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡, 消化系專科, 內視鏡專科, 內視鏡技術師資格",
        "image": "/static/articlephoto/article-03-gastroscopy.jpg",
    },
    "hepatitis-B&C": {
        "title": "預防B型與C型肝炎的全民運動",
        "description": "B型與C型肝炎是慢性肝病、肝硬化與肝癌的重要成因。了解疫苗接種、安全性行為、避免血液接觸與定期篩檢等預防重點，及早守護肝臟健康。",
        "keywords": "肝癌, B型肝炎, C型肝炎, 保險套, 胃鏡推薦, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 胃鏡推薦, 舒眠胃鏡推薦, 三重, 新莊, 蘆洲, 板橋, 疫苗, B肝, C肝, 肝硬化, 脂肪肝, 超音波, 肝臟超音波, 腹部超音波, 肝纖維化, 肝纖維測量, 高階超音波",
        "image": "/static/articlephoto/article-08-hepatitis-B&C.jpg",
    },
    "high-quality-colonoscopy": {
        "title": "【⚠隱藏在末端的大腸腫瘤，高品質鏡檢救了她一命】",
        "description": "57歲林小姐因胃酸逆流就醫，因家族史與息肉病史安排高品質大腸鏡檢查。醫師堅持檢查至盲腸，成功揪出5公分大腸癌並及時轉診治療。提醒民眾大腸鏡應做到位，家族史是警訊，有症狀應做完整檢查。",
        "keywords": "大腸癌篩檢, 內視鏡檢查, 胃酸逆流, 腸胃鏡檢查, 預防醫學, 高品質大腸鏡, 大腸癌, 盲腸, 曜弘診所, 三重",
        "image": "/static/articlephoto/article-25-high-quality-colonoscopy.jpg",
    },
    "influenza-vaccine": {
        "title": "早說、晚說、很難過但還是曜說 - 防疫全年無休",
        "description": "根據衛生福利部疾病管制署的資料，接種流感疫苗能有效預防流感併發重症並降低死亡風險。2023-24流感季研究顯示，65歲以上長者接種疫苗後，預防流感重症保護力達75.1%，降低30天內全死因死亡風險保護力達65.7%。今年全台重症人數233人，重症熱區包括台北、新北、台中、台南及高雄。了解流感警訊，及早預防，保持健康！",
        "keywords": "流感疫苗, 克流感, 胃鏡推薦, 舒眠胃鏡推薦, 大腸鏡檢查, 大腸鏡推薦, 田名弘, 李儀鳴, 三重, 胃鏡推薦, 舒眠胃鏡推薦, 三重, 新莊, 蘆洲, 板橋, 疫苗, B肝, C肝, 肝硬化, 脂肪肝, 高血壓, 超音波, 肝臟超音波, 腹部超音波, 胰臟腫瘤, 胰臟癌, 肝纖維化, 肝纖維測量, 高階超音波",
        "image": "/static/articlephoto/article-09-influenza-vaccine.jpg",
    },
    "poop-color-health-check": {
        "title": "便便顏色與健康",
        "description": "關注便便顏色變化，識別健康隱患！鮮紅、暗紅、膿血色或極深色便便可能預示腸胃疾病。定期檢查，守護身體健康，避免大腸癌等重大病變。洽詢 02-29840101！",
        "keywords": "糞便顏色, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡, 消化系專科, 內視鏡專科, 內視鏡技術師資格, 210度可彎前鏡頭視野無死角,富士腸道內視鏡AI影像判讀設備 (CAD EYE), CAD EYE",
        "image": "/static/articlephoto/article-07-poop-color-health-check.jpg",
    },
    "stomach-cancer": {
        "title": "胃癌是全球常見的癌症之一",
        "description": "胃癌早期常無症狀，定期胃鏡檢查可早期發現、早期治療。注意飲食習慣、遠離高風險因子，降低胃癌發生機率。洽詢 02-2984-0101",
        "keywords": "胃癌, 胃鏡檢查, 消化不良, 食慾不振, 胃部不適, 幽門桿菌, 三重, 新莊, 蘆洲, 板橋, 健康檢查, 田名弘, 曜弘診所, 舒眠胃鏡推薦, 大腸鏡檢查, 大腸鏡推薦, 210度可彎前鏡頭視野無死角, 脂肪肝, 高血壓, 超音波, 肝臟超音波, 腹部超音波, 高階超音波",
        "image": "/static/articlephoto/article-10-stomach-cancer.jpg",
    },
    "stomach-pain-chronic-gastritis": {
        "title": "【胃痛不是小事】— 小心慢性胃炎正在惡化⁉️",
        "description": "吃飽胃悶痛、空腹更不舒服、常打嗝或胃酸逆流，可能不是單純消化不良，而是慢性胃炎警訊。若長期忽略，可能演變為胃潰瘍並提高胃癌風險，及早透過胃鏡檢查找出真正原因更安心。",
        "keywords": "胃痛, 慢性胃炎, 胃鏡檢查, 膽結石, 腹部超音波, 早期發現早期治療, 三重, 新莊, 蘆洲, 板橋, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 健康檢查, 癌症預防, 曜弘診所, 肚子痛",
    },
    "stomach-ulcer": {
        "title": "胃潰瘍",
        "description": "胃潰瘍不是小事！了解常見誘因如飲酒、藥物或幽門螺旋桿菌，以及如何透過專業檢查發現症狀並避免器官衰竭等嚴重後果，定期檢查守護腸胃健康。洽詢 02-29840101！",
        "keywords": "胃潰瘍, 什麼狀況下會出現胃潰瘍, 舒眠胃鏡推薦, 田名弘, 李儀鳴, 三重, 肝膽腸胃科推薦, 腸道內視鏡推薦, 新北胃鏡推薦, 照胃鏡, 消化系專科, 內視鏡專科, 內視鏡技術師資格",
        "image": "/static/articlephoto/article-04-stomach-ulcer.jpg",
    },
    "subepithelial-tumor": {
        "title": "什麼是「黏膜下腫瘤」⁉️",
        "description": "消化道內視鏡發現「隆起」？可能是黏膜下腫瘤。曜弘診所引進高頻內視鏡超音波探頭(EUS)，免轉診、免重做，一次檢查即可分辨腫瘤層次與良惡性風險。",
        "keywords": "黏膜下腫瘤, 內視鏡超音波, 肝臟超音波, 腹部超音波, 高血壓, 脂肪肝, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 三重, 新莊, 蘆洲, 板橋, 曜弘診所, 腸胃保健, 健康知識科普",
        "image": "/static/articlephoto/article-23-subepithelial-tumor.jpg",
    },
    "thyroid": {
        "title": "💔咳嗽止不住的祕密｜一位媽媽的生命故事",
        "description": "從咳嗽揭開重病真相，一位母親的信仰與醫療故事，提醒您咳嗽不是小事。曜弘診所專業團隊提供敏銳判斷與及時處置，協助民眾早期發現甲狀腺癌與相關症狀，守護家庭健康與希望。☎️ 02-29840101",
        "keywords": "真實故事, 咳嗽警訊, 甲狀腺癌, 全人照護, 用愛看見生命, 信仰與醫療同行, 未分化型甲狀腺癌, 持續性咳嗽, 肺部轉移, 甲狀腺腫瘤, 咳嗽咳血, 田名弘, 李儀鳴, 三重診所推薦, 新北內科推薦, 新北甲狀腺檢查, 內視鏡診斷, 曜弘診所, 溫柔看診, 信仰見證",
        "image": "/static/articlephoto/article-13-thyroid.jpg",
    },
    "thyroid-nodule": {
        "title": "甲狀腺結節你一定要知道的事｜脖子那顆小球是什麼？",
        "description": "摸到脖子上的小腫塊別慌張！可能是常見的甲狀腺結節。曜弘診所提供高階 ARIETTA 850 超音波與細針穿刺服務，幫您快速、安全判斷結節性質，守護健康。立即了解檢查重點與預防建議！☎️ 02-29840101",
        "keywords": "甲狀腺結節, 高階超音波, 健康檢查, 未分化型甲狀腺癌, 脖子自我檢查, 胃鏡推薦 ,舒眠胃鏡推薦 ,大腸鏡檢查 ,大腸鏡推薦 ,三重 ,新莊 ,蘆洲 ,板橋 ,脂肪肝 ,高血壓 ,超音波 ,ARIETTA 850, 富士超音波, 甲狀腺癌預防, 別讓小結節變大問題, 雙北唯一診所機型, 曜弘診所, 田名弘, 李儀鳴",
        "image": "/static/articlephoto/article-14-thyroid-nodule.jpg",
    },
    "ulcerative-colitis": {
        "title": "潰瘍性結腸炎",
        "description": "一天跑廁所三次以上？大便還帶血⁉️ 小心是潰瘍性結腸炎在作怪！這是一種腸子「自體攻擊」的慢性發炎疾病。別再以為是玻璃胃，其實是腸道在求救啦！",
        "keywords": "潰瘍性結腸炎, UC, 跑廁所不是你的錯, 胃鏡推薦, 舒眠胃鏡, 大腸鏡推薦, 三重, 新莊, 蘆洲, 板橋, 肝臟超音波, 腹部超音波, 高血壓, 脂肪肝, 曜弘診所, 腸胃保健, 健康知識科普",
        "image": "/static/articlephoto/article-17-ulcerative-colitis.jpg",
    },
}
