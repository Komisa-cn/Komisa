import streamlit as st
from components.interactive import display_interactive_chart
import os # 确保导入 os
from PIL import Image # 确保导入 Image

def 代表作品():
    st.markdown("## 搞笑短剧")
    
    st.markdown("""
    ### 好笑么？用命换的
    https://www.bilibili.com/festival/bzjcjlhh?bvid=BV1aT4y1h71M&spm_id_from=333.1387.upload.video_card.click
    
    **播放量：2351万** | *2025年5月统计*
    
    - 如果你生活在一个“搞笑犯法”的世界里，会发生什么？
    - 评论区：“神作，我个人认为这是搞笑短视频的巅峰，如果需要一部作品，来代表这个快节奏时代下，填满人们日常生活的短视频，我投这个视频。”
    """)
# 在下方添加图片
    image_below_path = os.path.join("static", "images", "好笑么用命换的.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, caption='好笑么？用命换的', width=300) # 修改这里，例如设置为300像素宽
    else:
        st.warning(f"Image not found at {image_below_path}")

    st.markdown("""
    ### 老师...你投屏没关
    https://www.bilibili.com/video/BV19r421K7ST/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
    
    **播放量：2878万** | *2025年5月统计*
    
    - 搞笑与模拟恐怖风格的结合，而看完后又引发对社会议题的思考与讨论
    - 评论区: “太神了，无论看几遍都觉得牛，很多人对视频的讨论还只是停留在里面“XX游戏”的部分，殊不知这个游戏在剧情里相当于一个绿幕，它可以替换成任何东西：小说、动漫、模型、周边、……它只是“兴趣爱好”的一个代表，视频真正的目的是想表达“勇敢做自己，大胆追求爱，不要因为他人的偏见而放弃自己的热爱”这个观点，真的像大伙说的那样，视频只展现了现世的冰山一角，而评论区的各种声音把剩下的部分完完整整的展示给了你看。”
    """)
# 在下方添加图片
    image_below_path = os.path.join("static", "images", "老师你投屏没关.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, caption='老师...你投屏没关', width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")   

    st.markdown("---")
    
    st.markdown("## 动画配音二创")
    
    st.markdown("""
    ### 警察：你这推理是要把我笑死吗
    https://www.bilibili.com/video/BV1k7411R7kj/?spm_id_from=333.1387.upload.video_card.click
    
    **播放量：3843万** | *2025年5月统计*
    
    - 当福尔摩斯是个口无遮拦的人，而他的助手华生又要求他文明用语时……（福尔摩斯动画二次剪辑、配音后的搞笑小剧场）
    - 评论区：“这就是雀巢up主生涯最强的配音视频，我爱了，你呢？”
    -“最有趣的是前面那段抓犯人的剧情，让别人小声一点结果自己声音贼大，正是在讽刺那些反对不文明用语，自己却骂的比谁都狠的人。”
    """)
    # 在下方添加图片
    image_below_path = os.path.join("static", "images", "警察.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, caption='警察：你这推理是要把我笑死吗', width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")

    st.markdown("""
    ### 大雄...已经...无所谓了...
    https://www.bilibili.com/video/BV1k7411R7kj/?spm_id_from=333.1387.upload.video_card.click
    
    **播放量：2860万** | *2025年5月统计*
    
    - 将哆啦A梦动画名场面二次改编、剪辑、配音后，创作出的多个创意搞笑单元剧
    - 评论区: “啊，混蛋，已经18万硬币了，下集在哪里？”
    - “哈哈哈好棒好好笑！！！不管什么素材雀巢都可以做的超好！！！”
    """)
    # 在下方添加图片
    image_below_path = os.path.join("static", "images", "大雄.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, caption='大雄...已经...无所谓了...', width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")
    
 
    st.markdown("---")
    
    st.markdown("## 商业广告")
    
    st.markdown("""
    ### 满足了甲方的癖好♥
    https://www.bilibili.com/video/BV1iC411G7aN/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
    
    **播放量：1902万** | *2025年6月统计*
    - p5x手游上线前的推广商单：用轻喜剧的方式，展现“欺诈师”团伙精妙的作案过程，与游戏中“怪盗团”的设定相呼应
    - 评论区：“这期太精彩了，反转再反转真的爽！这种诙谐但是又有点正经的风格，加上爵士乐的轻快bgm，真的好喜欢啊！”
    - “明明是个商单，却比平时的质量还要高！（无拉踩，这真的是我笑得最多的一次）”
    """)
    # 在下方添加图片
    image_below_path = os.path.join("static", "images", "满足甲方.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, caption='满足了甲方的癖好', width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")

    st.markdown("""
    ### 陪伴我10年的员工离开了....
    https://www.bilibili.com/video/BV1iC411G7aN/?spm_id_from=333.1387.upload.video_card.click&vd_source=df4fc92bea750c625f4b808d6feecf28
    
    **播放量：1235万** | *2025年6月统计*
    - 大众途昂Pro汽车的推广商单：雀巢为了挽留想要离职的员工鲸尾，决定开车和他一起去川西旅行，却发生了意想不到的故事......
    - 微电影级别的旅行Vlog, 同时很好地宣传了途昂汽车“7座”、“空间大”、“能装”等卖点
    - 评论区：
            “看完这期，真的感觉雀巢的创作力太惊人了，无论是镜头画面的构图、色彩，还是剧情的发展，以及两位up主出色的演绎，在我心中都已经是顶尖的程度了！
             这期视频真的是有史以来我心中的“雀室No.1”了，感觉就像是——经历了很多黑暗和痛苦之后，他们在繁星的照耀下与过去的那些故事和解。
             在具有诸多搞笑元素的前提下，还能把视频做得这么有深意，除了雀巢我实在找不到第二个人了。”
    """)
# 在下方添加图片
    image_below_path = os.path.join("static", "images", "陪伴10年.png") # 请替换 "雀巢.jpg" 为您的图片文件名
    if os.path.exists(image_below_path):
        st.image(image_below_path, caption='陪伴我10年的员工离开了', width=300) # use_column_width=True 使图片宽度适应列宽
    else:
        st.warning(f"Image not found at {image_below_path}")
