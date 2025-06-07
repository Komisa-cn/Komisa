import streamlit as st
from components.interactive import display_interactive_chart
import os # 确保导入 os
from PIL import Image # 确保导入 Image

def 七人传奇():
    st.markdown("## 初始核心团队")
    left_col, right_col = st.columns([3, 1])
    
    with left_col: # 将“逗比的雀巢”的文本和下方图片放入左列
        st.markdown("""
        ### 逗比的雀巢
        **工作室创立者、灵魂人物** | *公司老板* | *导演 & 编剧* 
        
        商务合作（备注品牌）：加微信51947303 | 微博：@逗比的雀大巢

        - 从高中时期开始创作游戏、动画向搞笑配音视频，于2019年正式在上海组建工作室
        - 担任雀巢工作室大部分视频的导演、编剧及配音，其账号在B站的总播放量已逼近15亿，总获赞数8500w+
        - 用幽默诙谐、兼具自夸和自嘲的风格，为自己执导了一期传记类纪录片，记录工作室成立6年来的发展
        - 个人纪录片：【万字解析】我，为什么是B站最帅的博主 
        
        https://www.bilibili.com/video/BV1VEqoYmEKi/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        # 在下方添加图片
        image_below_path = os.path.join("static", "images", "B站最帅.png") 
        if os.path.exists(image_below_path):
            st.image(image_below_path, width=300) 
        else:
            st.warning(f"Image not found at {image_below_path}")

    with right_col: # 将头像图片放入右列
        image_path = os.path.join("static", "images", "雀巢单人.jpg") # 注意：文件夹中似乎是 .webp 格式
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=200) # 直接在 st 对象上调用 image，而不是 right_col.image
        else:
            st.warning(f"Profile image not found at {image_path}")

    st.markdown("---") 
    
    # 为“机智的碎月”创建新的列
    left_col_suiyue, right_col_suiyue = st.columns([3, 1])

    with left_col_suiyue:
        st.markdown("""
        ### 机智的碎月
        **工作室元老人物、搞笑短剧主创 & 主演** | *B站粉丝量：140w+* | 个人主页：https://space.bilibili.com/2063605
        
        商务合作（备注品牌）：加微信745889559 | 微博：@机智的碎月

        - 最早加入工作室的成员，常和雀巢一起在搞笑短剧中演对手戏，演技成熟
        - 在雀巢的风格影响下，他也开始创作自己的搞笑短剧视频，其账号在B站的总播放量已达1.4亿，总获赞数近800w
        - 在视频中常以时而严厉、时而不着调的警长或医生形象出现，生活中却温柔腼腆，被粉丝亲切地称呼为“碎月妈咪”
        - 代表作：FBI：监控里看到了奇怪的人... 
        
        https://www.bilibili.com/video/BV1XB4y1W7KZ/?spm_id_from=333.1387.upload.video_card.click
        """)
    # 在下方添加图片
        image_below_path_suiyue = os.path.join("static", "images", "碎月代表作.png") 
        if os.path.exists(image_below_path_suiyue):
            st.image(image_below_path_suiyue, width=300) # 您可以调整width
        else:
            st.warning(f"Image not found at {image_below_path_suiyue}")
 
    with right_col_suiyue: # 将头像图片放入右列
        image_path_suiyue = os.path.join("static", "images", "碎月.jpg")
        if os.path.exists(image_path_suiyue):
            image_suiyue = Image.open(image_path_suiyue)
            st.image(image_suiyue, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_suiyue}")

    st.markdown("---") # 在“机智的碎月”板块后添加分隔线

    # 为“良心发作的chunchun”创建新的列
    left_col_chun, right_col_chun = st.columns([3, 1])

    with left_col_chun:
        st.markdown("""
        ### 良心发作的chunchun
        **工作室元老人物、搞笑短剧主创 & 主演** | *B站粉丝量：150w+* | 个人主页：https://space.bilibili.com/1590705
        
        商务合作（备注品牌）：加微信745889559 | 微博：@失眠的chunchun

        - 早期在雀巢的视频中配音、出镜，中后期开始独立创作自己的搞笑短剧
        - 得益于他日益成熟的编导水平和演技，他的大部分视频的播放量都稳定在100w以上，账号总播放量达到2.1亿，总获赞数1300w+
        - 他创作的视频往往有着吸引人的主题（如校园、课堂、犯罪等），以及丰富的剧情，有时还蕴含对社会/人性阴暗面的批判，因此总给人留下很深刻的记忆点
        - 代表作：这是最棒的新年礼物！ 
        
        https://www.bilibili.com/video/BV1aD4y1j7P3/?spm_id_from=333.1387.upload.video_card.click
        """)
        # 在下方添加图片
        image_below_path_chun = os.path.join("static", "images", "chun代表作.png") 
        if os.path.exists(image_below_path_chun):
            st.image(image_below_path_chun, width=300) # 您可以调整width
        else:
            st.warning(f"Image not found at {image_below_path_chun}")

    with right_col_chun: # 将头像图片放入右列
        image_path_chun = os.path.join("static", "images", "chun.jpg")
        if os.path.exists(image_path_chun):
            image_chun = Image.open(image_path_chun)
            st.image(image_chun, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_chun}")

    st.markdown("---")

    # 为“炎辰大鸽子”创建新的列
    left_col_yanchen, right_col_yanchen = st.columns([3, 1])

    with left_col_yanchen:
        st.markdown("""
        ### 炎辰大鸽子
        **工作室元老人物、搞笑短剧主创 & 主演** | *B站粉丝量：180w+* | 个人主页：https://space.bilibili.com/170088482
        
        商务合作（备注品牌）：加微信51947303 | 微博：@炎辰大鸽子

        - 早期负责雀巢视频的文案创作、剪辑制作等，中后期开始参演视频，并着手创作自己的搞笑短剧，其账号总播放量已达2.9亿，总获赞数近1800w
        - 在自己的视频中，他常常以主角的身份出现，经历一系列线性的无厘头搞笑事件
        - “5G冲浪”的他，总是能把时下最新最热的梗融进视频中：deepseek、MVP、来财...,因此在各平台（B站、抖音、小红书）都有不错的热度
        - 代表作：老师：我也要拿人头！！ 
        
        https://www.bilibili.com/video/BV1Fe4y1o7Ex/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        # 在下方添加图片
        image_below_path_yanchen = os.path.join("static", "images", "炎辰代表作.png")
        if os.path.exists(image_below_path_yanchen):
            st.image(image_below_path_yanchen, width=300)
        else:
            st.warning(f"Image not found at {image_below_path_yanchen}")    

    with right_col_yanchen:
        image_path_yanchen = os.path.join("static", "images", "炎辰.jpg")
        if os.path.exists(image_path_yanchen):
            image_yanchen = Image.open(image_path_yanchen)
            st.image(image_yanchen, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_yanchen}")    

    st.markdown("---")

    # 为“7鲸尾”创建新的列
    left_col_jingwei, right_col_jingwei = st.columns([3, 1])

    with left_col_jingwei:
        st.markdown("""
        ### 7鲸尾
        **搞笑短剧主创 & 主演** | *粉丝向内容（拍摄花絮、工作室介绍）创作者* | *B站粉丝量：80w+* 
        
        个人主页：https://space.bilibili.com/20841379
        
        商务合作（备注品牌）：加微信Pr020713 | 微博：@不是鲸尾

        - 早期用自己画的小纸人讲述雀巢工作室幕后的故事，并发布雀巢视频的拍摄花絮，受众主要是对工作室成员较为熟悉、有一定忠诚度的粉丝
        - 中后期开始独立创作自己的搞笑短剧，创作能力由青涩逐渐走向成熟，其账号总播放量已达6800w+，总获赞数480w+
        - 2025年，得益于他在雀巢的视频“陪伴我10年的员工离开了”中出色的演出，他被更多人认可，粉丝量迎来高速增长，几乎翻了一番
        - 代表作：看了就得罪雀巢工作室所有人 
        
        https://www.bilibili.com/video/BV1U99QYKEGJ/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        # 在下方添加图片
        image_below_path_jingwei = os.path.join("static", "images", "鲸尾代表作.png")
        if os.path.exists(image_below_path_jingwei):
            st.image(image_below_path_jingwei, width=300)
        else:
            st.warning(f"Image not found at {image_below_path_jingwei}")

    with right_col_jingwei:
        image_path_jingwei = os.path.join("static", "images", "鲸尾.jpg")
        if os.path.exists(image_path_jingwei):
            image_jingwei = Image.open(image_path_jingwei)
            st.image(image_jingwei, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_jingwei}")
    
    st.markdown("---")

    # 为“超正经的小李”创建新的列
    left_col_xiaoli, right_col_xiaoli = st.columns([3, 1])

    with left_col_xiaoli:
        st.markdown("""
        ### 超正经的小李
        **搞笑短剧主创 & 主演** | *生活向内容（vlog、综艺）创作者* | *B站粉丝量：90w+* 
        
        个人主页：https://space.bilibili.com/317783104
        
        商务合作（备注品牌）：加微信Pr020713 | 微博：@风雨尘的十月

        - 较晚加入工作室，常以性感或变态的角色形象出现在视频中，其独特的人设迅速博得了大量观众的关注
        - 由于拥有青涩的外貌和健美的身材，他很快吸引了一批粉丝，并开始发布雀巢庆生、粉丝礼物开箱、工作室趣味运动会等回馈粉丝的生活向内容
        - 中后期，在吸取雀巢等人的拍摄经验后，他也开始独立创作自己的搞笑短剧、承接商单，账号总播放量已达8400w+，总获赞数620w+
        - 代表作：老板：看我戳爆气球！！ 
        
        https://www.bilibili.com/video/BV19m4y1K7qA/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        # 在下方添加图片
        image_below_path_xiaoli = os.path.join("static", "images", "小李代表作.png")
        if os.path.exists(image_below_path_xiaoli):
            st.image(image_below_path_xiaoli, width=300)
        else:
            st.warning(f"Image not found at {image_below_path_xiaoli}")

    with right_col_xiaoli:
        image_path_xiaoli = os.path.join("static", "images", "小李.jpg")
        if os.path.exists(image_path_xiaoli):
            image_xiaoli = Image.open(image_path_xiaoli)
            st.image(image_xiaoli, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_xiaoli}")

    st.markdown("---")

    # 为“蛋水饿”创建新的列
    left_col_danshui, right_col_danshui = st.columns([3, 1])

    with left_col_danshui:
        st.markdown("""
        ### 蛋水饿
        **搞笑短剧主创 & 主演** | *B站粉丝量：40w+* | 个人主页：https://space.bilibili.com/276562678
        
        商务合作（备注品牌）：加微信Pr020713 | 微博：@蛋水饿

        - 较晚加入工作室，常以二次元、小丑等滑稽的形象出现在视频中，演技逐渐从青涩走向成熟
        - 初期，他的账号主要发布基于美食和雀巢吃播的搞笑视频，后期也开始创作自己的搞笑短剧，账号总播放量近6400w+，总获赞数380w+
        - 代表作：雀巢：公司倒闭了（喜 
        
        https://www.bilibili.com/video/BV17w4m1X7Ey/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        # 在下方添加图片
        image_below_path_danshui = os.path.join("static", "images", "蛋水饿代表作.png")
        if os.path.exists(image_below_path_danshui):
            st.image(image_below_path_danshui, width=300)
        else:
            st.warning(f"Image not found at {image_below_path_danshui}")

    with right_col_danshui:
        image_path_danshui = os.path.join("static", "images", "蛋水饿.jpg")
        if os.path.exists(image_path_danshui):
            image_danshui = Image.open(image_path_danshui)
            st.image(image_danshui, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_danshui}")

    st.markdown("---")
    
    st.markdown("## 团队介绍视频")
    
    st.markdown("""
    ### "领导说干不了就滚"
    **介绍了七人传奇组合的每个人的小故事** 
    
    *链接: https://www.bilibili.com/video/BV1nC4y1G7qx/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28*
    """)
# 在下方添加图片
    image_below_path = os.path.join("static", "images", "七人传奇.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")
    
    st.markdown("""
    ### "这工作室能开5年！！！！？？？"
    **讲述了雀巢工作室五年来逐渐发展壮大的历程** 
    
    *链接: https://www.bilibili.com/video/BV1nMcuepERe/?spm_id_from=333.1387.homepage.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28*
    """)
# 在下方添加图片
    image_below_path = os.path.join("static", "images", "工作室介绍.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")
    