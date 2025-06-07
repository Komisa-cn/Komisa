import streamlit as st

def 联系我们():
    st.markdown("## 联系我们")
    
    st.markdown("""
    您可以通过以下方式与雀巢工作室联系：
    
    ### 商务合作（请备注品牌或来意）
    - **公共邮箱**: [NESTLEHOUSE@163.com](mailto:NESTLEHOUSE@163.com)
    - **商务微信**: 51947303（B站） | fqsw0015（抖音）
    ### 粉丝交流
    - 微博群/抖音群热聊中，欢迎加入！
    """)
    
    st.markdown("### 有什么话想对我们说吗？")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("尊姓大名")
            email = st.text_input("您的邮箱/手机号/微信号")
            
        with col2:
            subject = st.text_input("主题")
            
        message = st.text_area("内容", height=150)
        
        submitted = st.form_submit_button("发送")
        
        if submitted:
            st.success("谢谢你的留言！送你一朵雀巢的小花【亲亲】")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
    
    st.markdown("""
    ### 加入我们
    官方招聘网站：[https://julingshen.jobs.feishu.cn/nestlehouse](https://julingshen.jobs.feishu.cn/nestlehouse)
    
    目前有以下职位空缺：
    - 小红书官方账号运营（7-12k/月）
    - 剪辑师（长期招聘，8-16k/月）
    - 编导（长期招聘，12-25k/月）
    - 导演（6-15k/月）
    - 编导实习生（150-200/天）
    - 摄像实习生（150-200/天）
    
    工作地点：成都   欢迎你的加入！
    """)
