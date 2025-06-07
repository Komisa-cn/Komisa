import streamlit as st
import base64
import os
from components.interactive import display_interactive_chart
from PIL import Image

def 开枝散叶():

    st.title("团队其他up主")

    # --- 生姜蛋包饭 ---
    left_col_danbaofan, right_col_danbaofan = st.columns([3, 1])
    with left_col_danbaofan:
        st.markdown("""
        ### 生姜蛋包饭
        **B站粉丝量：180w+** | *商务合作（备注品牌）：加微信Pr020713* | 个人主页：https://space.bilibili.com/475304452
        - 个人风格突出的纸板动画创作者，较早加入雀巢工作室，常作为演员在工作室其他up主的搞笑短剧中出境
        - 账号总播放量达9300w+，总获赞数770w+
        - 代表作：警长：再不投降我就击毙人质！ 
        
        https://www.bilibili.com/video/BV17C4y1A7mg/?spm_id_from=333.1387.homepage.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path_danbaofan = os.path.join("static", "images", "蛋包饭代表作.png")
        if os.path.exists(image_below_path_danbaofan):
            st.image(image_below_path_danbaofan, width=300) 
        else:
            st.warning(f"Image not found at {image_below_path_danbaofan}")

    with right_col_danbaofan:
        image_path_danbaofan = os.path.join("static", "images", "蛋包饭.jpg")
        if os.path.exists(image_path_danbaofan):
            image_danbaofan = Image.open(image_path_danbaofan)
            st.image(image_danbaofan, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_danbaofan}")
    st.markdown("---")

    # --- 鹤吱菌 ---
    left_col_hezhijun, right_col_hezhijun = st.columns([3, 1])
    with left_col_hezhijun:
        st.markdown("""
        ### 鹤吱菌
        **B站粉丝量；270w+** | *商务合作（备注品牌）：加微信Pr020713* | 个人主页：https://space.bilibili.com/3353026
        - 2020年百大up主，其创作的【师生对线】系列搞笑配音视频曾红极一时，后于2024年加入雀巢工作室，转型真人搞笑短剧创作者
        - 账号总播放量达3.3亿，总获赞数2200w+
        - 代表作：考试时最害怕的一集 
        
        https://www.bilibili.com/video/BV1qE9RYoEpa/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path_hezhijun = os.path.join("static", "images", "何志军代表作.png")
        if os.path.exists(image_below_path_hezhijun):
            st.image(image_below_path_hezhijun, width=300)
        else:
            st.warning(f"Image not found at {image_below_path_hezhijun}")

    with right_col_hezhijun:
        image_path_hezhijun = os.path.join("static", "images", "何志军.jpg")
        if os.path.exists(image_path_hezhijun):
            image_hezhijun = Image.open(image_path_hezhijun)
            st.image(image_hezhijun, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_hezhijun}")
    st.markdown("---")

    # --- 善良的诚哥 & 滑稽的康康 ---
    left_col_chengkang, right_col_chengkang = st.columns([3, 1])
    with left_col_chengkang:
        st.markdown("""
        ### 善良的诚哥 & 滑稽的康康
        **B站粉丝量: 诚哥：110w+ | 康康：20w+** | *商务合作（备注品牌）：加微信745889559* 
        
        账号主页：https://space.bilibili.com/1835967 (诚哥)
        - 酷似“一个逗哏+一个捧哏”的双人搞笑组合，其中诚哥以独特的东北口音与总是穿着二次元痛衣的形象而被网友熟知
        - 于2024年共同加入雀巢工作室，开启办公室搞笑段子创作之路
        - 账号总播放量：诚哥2.9亿，康康；3400w+ | 获赞数：诚哥2400w+，康康210w+
        - 代表作：甲方满足了我的幻想♥ 
        
        https://www.bilibili.com/video/BV1pKRPYoEaw/?spm_id_from=333.1387.homepage.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path_chengkang = os.path.join("static", "images", "诚哥代表作.png")
        if os.path.exists(image_below_path_chengkang):
            st.image(image_below_path_chengkang, width=300)
        else:
            st.warning(f"Image not found at {image_below_path_chengkang}")

    with right_col_chengkang:
        # 注意：这里可能需要为诚哥和康康分别展示头像，或者选择一个代表性的头像
        image_path_chengkang = os.path.join("static", "images", "诚哥.jpg") # 假设使用诚哥的头像
        if os.path.exists(image_path_chengkang):
            image_chengkang = Image.open(image_path_chengkang)
            st.image(image_chengkang, width=200)
        else:
            st.warning(f"Profile image not found at {image_path_chengkang}")
    st.markdown("---")

    st.header("养胃的霖冬")
    left_col, right_col = st.columns([3, 1])
    with left_col:
        st.markdown("""
        - **B站粉丝量：80w+** | *商务合作（备注品牌）：加微信LD35888636* | 个人主页：https://space.bilibili.com/35888636
        - 用雀巢和霖冬手偶配音、演绎搞笑小剧场的up主，较早加入雀巢工作室，常作为演员在工作室其他up主的搞笑短剧中出境
        - 账号总播放量达1.1亿，总获赞数770w+
        - 代表作：老师：不想学习就滚回家去！（谢谢老师 
        
        https://www.bilibili.com/video/BV1Yw4m1a7G1/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path = os.path.join("static", "images", "霖冬代表作.png")
        if os.path.exists(image_below_path):
            st.image(image_below_path, width=300)
        else:
            st.warning(f"Image not found at {image_below_path}")

    with right_col:
        image_path = os.path.join("static", "images", "霖冬.jpg")
        if os.path.exists(image_path):
            st.image(image_path, width=200)
        else:
            st.warning("Profile image not found")
    st.markdown("---")

    st.header("在下乌鸦有何贵干")
    left_col, right_col = st.columns([3, 1])
    with left_col:
        st.markdown("""
        - **B站粉丝量：50w+** | *商务合作（备注品牌）：加微信745889559* | 个人主页：https://space.bilibili.com/456782283
        - 于2023年末加入雀巢工作室的游戏区up主，通过3D建模、制作小游戏等方式创作搞笑视频，常作为演员在工作室其他up主的搞笑短剧中出境
        - 账号总播放量达6200w+，总获赞数280w+
        - 代表作：一秒速通了老板做的游戏！ 
        
        https://www.bilibili.com/video/BV15H4y1c7Ud/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path = os.path.join("static", "images", "乌鸦代表作.png")
        if os.path.exists(image_below_path):
            st.image(image_below_path, width=300) 
        else:
            st.warning(f"Image not found at {image_below_path}")

    with right_col:
        image_path = os.path.join("static", "images", "乌鸦.jpg")
        if os.path.exists(image_path):
            st.image(image_path, width=200)
        else:
            st.warning("Profile image not found")
    st.markdown("---")

    st.header("刘拖地")
    left_col, right_col = st.columns([3, 1])
    with left_col:
        st.markdown("""
        - **B站粉丝量：40w+** | *商务合作（备注品牌）：加微信Pr020713* | 个人主页：https://space.bilibili.com/341069816
        - 于2023年加入雀巢工作室的科技区up主，基于科技产品改造、科技实验创作搞笑或硬核视频，常作为演员在工作室其他up主的搞笑短剧中出境
        - 账号总播放量达7700w+，总获赞数530w+
        - 代表作：我爸对移动办公有些误解 
        
        https://www.bilibili.com/video/BV1wb4y157wr/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path = os.path.join("static", "images", "刘拖地代表作.png")
        if os.path.exists(image_below_path):
            st.image(image_below_path, width=300)
        else:
            st.warning(f"Image not found at {image_below_path}")

    with right_col:
        image_path = os.path.join("static", "images", "刘拖地.jpg")
        if os.path.exists(image_path):
            st.image(image_path, width=200)
        else:
            st.warning("Profile image not found")
    st.markdown("---")

    st.header("林肯DK")
    left_col, right_col = st.columns([3, 1])
    with left_col:
        st.markdown("""
        - **B站粉丝量：10w+** | *商务合作（备注品牌）：加微信745889559* | 个人主页：https://space.bilibili.com/2354138
        - 搞笑短剧创作者及演员，频繁出演雀巢工作室其他up主的视频，于2023年加入雀巢工作室
        - 账号总播放量达1800w+，总获赞数70w+
        - 代表作：被人跟踪了！救救我！ 
        
        https://www.bilibili.com/video/BV1WdfqYTEoQ/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
        """)
        image_below_path = os.path.join("static", "images", "林肯代表作.png")
        if os.path.exists(image_below_path):
            st.image(image_below_path, width=300)
        else:
            st.warning(f"Image not found at {image_below_path}")

    with right_col:
        image_path = os.path.join("static", "images", "林肯.jpg")
        if os.path.exists(image_path):
            st.image(image_path, width=200)
        else:
            st.warning("Profile image not found")
    st.markdown("---")