import random
from pypinyin import pinyin, lazy_pinyin, Style

#下面是常用汉字表
common_words = "乙一乃丁卜刀九了七八厂儿二几力人入十又久丸丈乞乡勺刃亏凡卫亿亡叉川寸弓巾女尸士夕么万三上下与习也之义于个千及大飞干工广己已口马门山才土小子丰乏乌丹予丑勾勿匀厅允互井云匹凤冈劝凶仓介仇仅仆仁仍升午订双友艺屯夫巨币尺扎巴忆幻尤孔贝父户斤木牛欠犬氏瓦牙止爪中书无不专为公六历切元五区队内办从今以化什计认反太天引开少比长车斗方风火见毛片气日手水王文心月支分卡册乎乐丘丙丛丝匆占厉刊兄兰印功击令付仙仪仔仗让讨讯训辽失央巧左归帅叨叼叮句古另叶司台叹右召闪宁奶奴犯尼饥扒扑扔汉汇汁纠圣幼冬孕轧灭斥末未旦旧礼永甘瓜禾矛母鸟皮甲申田穴甩玉业东且世主包北加务写出代们他半去记议发节边对头平布市号叫可史只它打四外处本术民必正白立龙目生石示电由用乓乒乔丢买兴冰冲厌创刚刘刑兆亚匠防邪阳阴阵网劣企伞仰伐仿伏伙伤似伟伪伍休优协充亦访讽讲延芒芝巡州迈迁迅寺寻夺夹夸巩异庆庄帆师吃吊吓吉吗吐吸驰闭闯守宇宅妇奸妈妄岂岁屿尽壮扛扣扩扫托扬执池汗汤污纪纤圾尘尖忙孙字负贞毕轨死危爷戏灯灰考朵朴杀朽杂朱欢旬早旨曲肌臣虫耳齐肉舌羽舟竹页衣血羊份共决压争划列则光先阶那关再动军农会众传价件任全华产交论设许达过导并年当合各后名同向问安好如她江红级约场地在回团因多式存成观老机权收次有此百而米色西行至自串丽乱兵冻冷冶初免龟判删医阿陈附邻陆邮阻卵助劫劲励努余伯伴佛估伶伸佣亩词评诉译诊苍芳芦芹苏芽彻役迟返违迎远寿弟弄弃床库序希帐吧吵呈吹呆吨否告含吼君启吞呜吴呀驳驴驱闷闲宏宋妨妙妥妖狂犹岔岛岗尿尾饭饮壳扮抄扯抖扶抚护拒抗扭抛批抢扰折投找抓沉泛沟汽沙沈汪沃纯纺纲纳纽纱纹纸纵坝坊坏坚均坑块坛址坐困围园怀忧孝财贡歼戒灿灵灾灶材村杜杆杠李束杏杨牢攻旱旷忌忍忘肠肚肝皂私秃秀钉针盯疗鸡男穷补良辰赤豆谷麦辛言足吩坟纷芬两严况别利际即却劳但低何你体位住作克县识证花还进近连运这张应听员间完形层局声把报技没快我极来条改状时社求志更步每究系角里身走乖丧乳典净卧厕券兔刺刮剂刻刷降郊郎陕限郑凯凭势侧供佳佩侨侍依侦侄卖享诚诞诗试详询叔范苦茄茎茅茂苗苹若英彼径征迫述奔奉奇幸弦底店废庙录帘帖帜咐呼呢味咏驾驶驼驻闹闸宝官审宜宙宗姑姐妹妻姓狗狐岸岭岩届居屈饱饰饲拔拌抱拨拆抽担抵拐拣拘拦拢抹拍披抬拖押拥择招波泊沸河浅泪沫泥泡泼泄泻沿泳泽沾注练绍终垂垃垄坡坦固夜尚怖怪怜怕孤季孟败贩贯货贫贪贤责购轰轮软卷爸房炒炊炕炉炎视斧斩板杯柜杰枪松析枣枕枝牧版欧欣昂昌昏昆旺承环玩忽念态忠肥肺肤服股肩肯朋肾胁胀肢肿武爬秆钓盲鸣码罗畅画衬衫艰虎虏舍肃齿隶鱼雨顶顷奋事其具到制些例使单参京该话建变取受往府和命周定实始委拉法油治经细线织组国图性备学质转或所规现者构果林物放明易育的直矿知空采非金青表临举厚厘剑剃削陡险卸冒勉勇冠促俘俭俊俩侵俗侮修亮亭诵误诱语叛叙草茶荡荒茧荐茫荣药待迹迷逆送逃退追封奖奏差弯庭帮帝哀哈咳哄哗哪咸哑咽咬咱骄骆骂阀阁闻宫客室宪宣姜娇姥娃威姨姻姿独狠狡狮狭狱峡屋饼饺饶挡挂挥挤挎括挠挪拼拾拴挑挺挖挣测洞洪浑浇洁津浓洽洒洗洋洲浊绑绘绞绝络绕绒巷城垫垦垮垒尝恨恒恢恼恰孩贷费贵贺贱贸贴轻残殃施扁炮烂炼炭炸既觉览柏柄栋架枯栏柳某染柔柿树柱牵牲故春显星映昼昨神祝祖拜泉玻珍怠急怒怨怎胞背胆胡脉胖胜胃歪皇皆甚秒秋钞钢钩钥钟竖盆盈毒盾眉盼眨疤疮疯疫鸦砍砌砖矩罚畏穿窃突袄虾虹蚂蚀虽蚁耐耍缸竿赴赵趴食骨鬼首香项顺美前除院养保便信南亲说很律适选将度带品响按持指活济派给结统型复点战标查政是段思总种科看省相研界类要重革面音须乘羞凉剥剧剖匪陵陪陶陷兼冤倍倡倘倒俯健借俱倦倾倚债读课谅请谁谊诸谈荷获莲莫徒徐递逗逢逝透途逐射套弱座席啊唉唇哥唤哭哨唐哲阅宾害宽宵宴宰娘娱狼狸峰屑饿壶挨捕换捡捐捆捞捏捎损挽振捉涌浮浩浸浪涝润涉涛涂浴涨浙继绢绣埋恭悔悄悟悦夏贿贼毙烈轿载殊旁旅爹扇烦烘烤烧烫烟烛笔案柴档桂核桨校框栗桥桑桃桐栽株桌牺敌氧晃晋晒晌晓晕祥拿拳浆泰瓶班珠恶恩恳恐恋息脆胳脊胶朗脑胸脏脂爱秘秤秧秩租铃铅钱钳钻竞站监盐益盏眠病疾疲疼症鸭皱础破罢畜留窄袜袍袖蚕蚊耻耽缺虑耕耗紧索艳翅翁致舱航舰笋笑臭辱躬酒配赶顾顽顿预衰粉准原党部都候值调速通造验家容展海流消圆离资热较料格根样特效能称积铁真被素般起难高匙凑减剪副隆随隐兽勒偿假偶偏停偷谎谜谋菠菜菊菌萝萌萍萄营著逮弹康廊庸唱啦售唯啄骑寄寇密宿婚婆婶猜猎猫猛猪崇崖崭彩屠馆馅掉捷掘控掠描排捧授探掏推掀掩淡混渐淋渠渗淘添淹液渔绸绩绿绵绳绪续堵堆培堂域圈够惭惨悼惯惊惧惕惜辅辆斜旋戚毫检梨梁梅梦梢梳梯桶械犁敢救敏欲晨晚祸球患您悉悬悠爽脖脚脸脱望甜移铲铜银竟章笼盛盗盖盒盘眯睁痕痒鸽票略窑蛋蛇聋职虚粗粒粘累衔船笨笛符野距跃雪雀黄鹿麻颈袭袋做得常商接据清深维基情族断教理眼着率第象领羡厨厦割剩隔隙傲傍储傅博谦谢谣葱董葛葵落葡葬循御逼遍遗遇尊奥幅帽喘喊喝喉喇喷善喂喜骗阔富寒嫂猴猾屡馋插搭搁搅揭揪搂揉搜握援渡溉港湖滑渴湿湾游渣滋编缎缓缘堡塔堤堪悲惰慌慨愧禽愉赌赔赏焦煮辈辉殖焰毯棒棍椒棵棉棚棋森椅植棕牌敞敬散款欺晶景普晴暑暂智掌琴斑惩惠惑惹曾替朝腊脾腔登稍税稀锄锋锅链铺锐锁销锈铸童痛鹅硬短番窗窜窝疏裤裙裕蛮蜓蛙蛛粥絮紫舒艇策答筋筐筛筒筝筑释辜超趁趋跌践跑鲁雄雅雁黑颂街裁裂愤粪道强属提温就然斯最期程确联等量越集题装鄙障勤催傻像谨叠蓝蒙蓬蒜蓄蒸微遣遥廉幕嗓嫁嫌摆搬搏搞摸摄摊携摇滨滚滥溜滤漠滩滔溪源缠缝墓塞塑塌塘填慎赖煎输煌煤楚概槐楼榆歇献暗暖福殿毁瑞愁慈愚愈腹腾腿腥腰稠锤错键锦锯锣锡盟睬督睛睡痰鹊碍碑碌碰碎碗矮禁罩罪蛾蜂舅粮粱肆筹简签触躲辟辞誉酬酱跟跪跨跳龄鉴雹雷零雾魂韵鼓鼠满照新数感想意置解路群凳僚谱蔽蔑遭遮弊嘉嗽骡察寨嫩馒摧撇摔摘滴漏漫漂漆演缩境墙舞慕慢赛赚熊旗截熔熄榜榴模榨敲歌歉暮璃愿膀膊膏膜稳锻锹端竭瘦碧磁疑蜡蜜蜻蝇蜘聚腐裳裹翠箩豪辣誓酷酿貌静鲜魄鼻颗精管算酸需劈僵僻蕉蔬德遵嘱播撤撑撒撕撞潮潜墨懂熟飘槽横橡樱暴摩毅慧慰膛膝稻稿镇瞒瞎蝶蝴聪糊艘箭篇箱躺醋醉趣趟踩踏踢踪靠霉震鞋黎额颜影增凝薄薯薪避邀嘴操激澡缴壁懒赞赠燕燃橘膨稼镜磨融糕糖篮辨辩醒蹄餐雕默衡颠器整藏骤擦赢戴燥臂穗瞧螺糠糟繁翼辫蹈霜霞鞠镰鹰覆翻蹦鞭爆攀瓣疆警蹲颤嚼嚷灌壤耀籍躁魔蠢霸露囊罐匕刁丐邓冗仑讥夭歹戈乍冯卢凹凸艾夯叭叽囚尔皿矢玄匈邦阱邢凫伦伊仲亥讹讳诀讼讶廷芍芋迄迂夷弛吏吕吁吆驮驯妆屹汛纫旭肋臼卤刨匣兑罕伺佃佑诈诅芭芙芥苇芜芯巫庇庐吠吭吝呐呕呛吮吻吟吱闰妒妓姊狈岖彤屁扳扼抠抡拟抒抑沧沪沥沦沐沛汰汹纬坎坞坠囱囤忱轩灸灼杈杉杖牡汞玖玛韧肛肖肘鸠甸甫邑卦刹刽陌陋郁函侈侥侣侠卑卒卓叁诡苞苟苛茉苫苔茁奈奄弧弥庞帕帚呵哎咖咕咙咆呻咒驹宠宛姆狞岳屉拗拂拇拧拓拄拙泌沽沮泞泣沼绊绅绎坷坤坯坪怯怔贬账贮炬觅枫杭枚枢枉玫昙昔氓祈殴瓮肮肪肴歧秉疙疚矾衩虱疟忿氛陨勃勋俄侯俐俏诲诫诬茬茴荤荠荚荆荔荞茸茵荧徊逊契奕哆咧咪哟咨骇闺闽宦娄娜姚狰峦屏屎饵拱拷拭挟拯洛洼涎垛垢恍恃恬恤幽贰轴飒烁炫毡柑枷柬柠柒栅栈氢昧昵昭祠泵玷玲珊胧胚胎秕钝钙钧钠钮钦盅盹鸥砂砚蚤虐籽衍韭凌凄剔匿郭卿俺倔诽诺谆荸莱莉莽莺莹逞逛哺哼唧唠哩唆哮唁骏娩峻峭馁捌挫捣捍捅捂涤涡涣涧浦涩涕埃埂圃悍悯贾赁赂赃羔殉烙梆桦栖栓桅桩氨挚殷瓷斋恕胯脓脐胰秦秫钾铆疹鸵鸯鸳砾砰砸祟畔窍袒蚌蚪蚣蚜蚓耿聂耸舀耙耘紊笆酌豹豺颁袁衷乾厢兜匾隅凰冕勘傀偎谍谓谐谚谒菲菇菱菩萨萎萧萤徘徙巢逻逸尉奢庵庶啡唬啃啰啤啥唾啸阐阎寂娶婉婴猖崩崔崎彪彬掺捶措掸掂捺捻掐掖掷淳淀涵淮淑涮淌淆涯淫淤渊绷绰综绽缀埠堕悴惦惋赊烹焊焕梗梭梧敛晦晤祷琅琉琐曹曼脯秽秸铛铐铝铭铣铡盔眷眶痊鸿硅硕矫祭畦窒裆袱蛆蛉蚯蛀聊翎舶舵舷笙笤赦麸躯酗酝趾颅颇衅隘募凿谤蒂葫蒋遏遂逾奠喳啼喧喻骚寓媒媚婿猬猩嵌彭壹搀揣搓揩揽搔揖揍渤溅溃渺湃湘滞缔缆缕缅堰愕惶赐赋赎焙椎棺棘榔棱棠椭椰犀牍敦氮氯晾晰掰琳琼琢韩惫腌腕腋锉锌竣痘痪痢鹃甥硫硝畴窖窘蛤蛔蜒粟粤翘翔筏酣酥跋跛雳雇鼎黍颊焚剿谬蓖蒿蒲蓉廓幌嗤嗜嗦嗡嗅寞寝嫉媳猿馏馍搪漓溺溶溯溢滓缤缚煞辐辑斟椿楷榄楞楣楔暇瑰瑟腻腮腺稚锭锚锰锨锥睹瞄睦痹痴鹏鹉碘碉硼禀署畸窟窥褂裸蜀蜕蜗蜈蛹聘肄筷誊酪跺跷靖雏靶靴魁颓颖频衙兢隧僧谭蔼蔓蔫蔚箫蔗幔嘀嘁寡寥嫡彰漱漩漾缨墅慷孵赘熬熙熏辖辕榕榛摹镀瘩瘟碴碟碱碳褐褪蝉舆粹舔箍箕赫酵踊雌凛谴蕊蕴幢嘲嘿嘹嘶嬉履撮撩撵撬擒撰澳澈澄澜潦潘澎潭缭墩懊憔憎樊橄樟敷憋憨膘稽镐镊瘪瘤瘫鹤磅磕碾褥蝙蝠蝗蝌蝎褒翩篓豌豫醇鲫鲤鞍冀儒蕾薇薛噩噪撼擂擅濒缰憾懈辙燎橙橱擎膳瓢穆瘸瘾鹦窿蟆螟螃糙翰篡篙篱篷踱蹂鲸霍霎黔儡藐徽嚎壕懦赡檩檬檀檐曙朦臊臀爵镣瞪瞭瞬瞳癌礁磷蟥蟀蟋糜簇豁蹋鳄魏藕藤嚣瀑戳瞻癞襟璧鳍蘑藻攒孽癣蟹簸簿蹭蹬靡鳖羹巍攘蠕糯譬鳞鬓躏霹髓蘸瓤镶矗"

class three_characters:
    def get_hanzi_with_pinyin(self,target_pinyin):
        #根据汉字的拼音获取所有的汉字
        hanzi_list = []
        for char in common_words:
            if lazy_pinyin(char) == [target_pinyin]:
                hanzi_list.append(char)
        return hanzi_list

    def get_hanzi_with_pinyinHead(self,target_head):
        #根据汉字的首字母获取所有的汉字
        hanzi_list = []
        for char in common_words:
            if lazy_pinyin(char)[0][0] == target_head:
                hanzi_list.append(char)
        return hanzi_list

    def get_words_from_oneWordHead(self,input):
        #根据汉语词汇的拼音首字母获取所有的汉字组合
        ans = []
        if (len(input) > 4):
            return ans

        pinyin = []
        word_sum = []

        for word in input:
            if not ord(word) in range(0x4E00, 0x9FA5):
                return ans
            else:
                pinyin.append(lazy_pinyin(word))
        for py in pinyin:
            hanzi_list = self.get_hanzi_with_pinyinHead(py[0][0])
            word_sum.append(hanzi_list)

        def backtrack(current, curPath):
            if current == len(word_sum):
                ans.append(curPath)
                return
            for ch in word_sum[current]:
                backtrack(current + 1, curPath + ch)

        backtrack(0, "")
        return ans

    def get_words_from_oneWord(self,input):
        #根据汉语词汇的拼音获取所有的汉字组合
        ans = []
        if (len(input) > 4):
            return ans

        pinyin = []
        word_sum = []

        for word in input:
            if not ord(word) in range(0x4E00, 0x9FA5):
                return ans
            else:
                pinyin.append(lazy_pinyin(word))
        for py in pinyin:
            hanzi_list = self.get_hanzi_with_pinyin(py[0])
            word_sum.append(hanzi_list)

        def backtrack(current, curPath):
            if current == len(word_sum):
                ans.append(curPath)
                return
            for ch in word_sum[current]:
                backtrack(current + 1, curPath + ch)

        backtrack(0, "")
        return ans
    def get_specific_word_fast_full(self,input,size = 10):
        #快速获取指定拼音的汉字组合
        ans = []
        if (len(input) > 4):
            return ans

        pinyin = []
        word_sum = []

        for word in input:
            if not ord(word) in range(0x4E00, 0x9FA5):
                return ans
            else:
                pinyin.append(lazy_pinyin(word))

        for py in pinyin:
            hanzi_list = self.get_hanzi_with_pinyin(py[0])
            word_sum.append(hanzi_list)

        for s in range(0,size):
            choices = ""
            for hanzi_list in word_sum:
                choices += random.choice(hanzi_list)
            ans.append(choices)
        return ans

    def get_specific_word_fast_head(self, input, size = 10):
        #快速获取指定拼音首字母的汉字组合
        ans = []
        if (len(input) > 4):
            return ans

        pinyin = []
        word_sum = []

        for word in input:
            if not ord(word) in range(0x4E00, 0x9FA5):
                return ans
            else:
                pinyin.append(lazy_pinyin(word))

        for py in pinyin:
            hanzi_list = self.get_hanzi_with_pinyinHead(py[0][0])
            word_sum.append(hanzi_list)

        for s in range(0, size):
            choices = ""
            for hanzi_list in word_sum:
                choices += random.choice(hanzi_list)
            ans.append(choices)
        return ans

if __name__ == '__main__':
    tw = three_characters()
    wl = tw.get_specific_word_fast_full("杨振斌",20)
    cnt = 0
    for i in range(0, 20):
        word = random.choice(wl)
        wl.remove(word)
        cnt += 1
        print(word, end=' ')
        if cnt % 10 == 0:
            print()
    print()
    wl = tw.get_specific_word_fast_head("金雪",20)
    cnt = 0
    for i in range(0, 20):
        word = random.choice(wl)
        wl.remove(word)
        cnt += 1
        print(word, end=' ')
        if cnt % 10 == 0:
            print()