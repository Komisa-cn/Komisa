import streamlit as st
from PIL import Image
import os

def 组织头目():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>逗比的雀巢</h4>
        <p>B站知名搞笑组织头目 | B站粉丝量：930w+ | 抖音粉丝量：200w+<br>
        - 26岁, 坐拥3个百大奖杯<br>
        - 毕业于美国雪城大学导演系<br>
        - 每年亲吻一次陈睿<br>
        - 个人主页：<a href="https://space.bilibili.com/5294454" target="_blank">https://space.bilibili.com/5294454</a><br></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "雀巢.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### 关于雀巢
        做搞笑视频，雀巢是认真的。

        2015年，还是一名高中生的雀巢开始了他在B站的创作之路。最初，他通过动画（《哆啦A梦》、《福尔摩斯》等）及游戏（锈湖系列）的搞笑配音，迅速得到人们的关注，并于2019年成功建立自己的工作室。

        随后，导演系出身的他不满足于对动画的“二创”，带领团队向原创真人短剧转型。他不断打磨视频质量，编导并出演了一系列“不按套路出牌”的创意搞笑内容。在这些视频中，他时而是欺诈师，时则是大侦探，还当过纽约警察局的警员……无论是旅行vlog、热血漫画还是悬疑烧脑的风格，都能成为他创作喜剧的载体。
        
        他的视频梗多而密集，荒诞的剧情搭配着意想不到的反转和呼应，令观众大呼“过瘾”。沉浸在这些爆笑情节中，无论你是谁，都可以从或繁忙或疲惫的生活中短暂抽离出来，获得几分钟的欢笑和放松。有人说，雀巢的搞笑短剧就像快节奏时代的一剂“布洛芬”，人们服用了，便不痛了。
        
        目前，雀巢已经成立小有规模的传媒公司，坐落于成都。他和他的团队，在喜剧创作这条路上，还有很长的路要走。
        """
    )
    st.markdown("---")
    st.markdown(
        """
        ### 发展历程
        - 2015年：美国高中留学期间，在Bilibili平台发布自己的第一条视频；
        - 2019年：招募初始核心成员，组建动画配音工作室；
        - 2020年：动画配音二创视频“警察：你这推理是要把我笑死吗”爆火，至今已获得3800w+播放量；
        - 2021年：正式于上海成立公司，后转移业务至成都，公司规模不断扩大。同年，工作室的内容创作开始从“动画配音”向“真人短剧”转型；
        - 2020、2023、2024年：获得Bilibili“年度百大UP主”荣誉；
        - 2024年: 真人短剧视频“FBI：奇怪？犯人怎么消失了？”获得第十三届北京国际电影节短视频单元娱乐类二等奖。
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page