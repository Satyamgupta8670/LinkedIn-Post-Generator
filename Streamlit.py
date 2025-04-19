import streamlit as st
import time
from few_shot import FewShotPosts
from post_generator import generate_post

# Set page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="📝",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0A66C2;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subheader {
        font-size: 1.5rem;
        color: #0077B5;
        margin-bottom: 1rem;
    }
    .highlight {
        background-color: #E7F3FF;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #0A66C2;
    }
    .fun-fact {
        background-color: #F3F2F1;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #F5AE4E;
    }
    .post-container {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #E0E0E0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Fun LinkedIn facts
linkedin_facts = [
    "LinkedIn was founded in 2002 and launched on May 5, 2003.",
    "LinkedIn has over 850 million members across more than 200 countries and territories worldwide.",
    "More than 57 million companies are listed on LinkedIn.",
    "Every week, content on LinkedIn generates 9 billion impressions.",
    "LinkedIn posts with images typically get 2x higher engagement.",
    "The best times to post on LinkedIn are Tuesday through Thursday between 10 a.m. and 1 p.m.",
    "Adding video to your LinkedIn posts can increase comment rates by 5x.",
    "The ideal length for LinkedIn posts is between 1,900 and 2,000 characters.",
    "Including 5+ relevant hashtags can increase your post reach significantly.",
    "LinkedIn's algorithm favors posts that generate quick engagement in the first hour."
]

# Post writing tips
writing_tips = [
    "Start with a hook to grab attention in the first line",
    "Break text into short, readable paragraphs",
    "Use emojis strategically to add personality 👍",
    "End with a clear call-to-action",
    "Add 3-5 relevant hashtags",
    "Include personal stories or experiences",
    "Ask questions to encourage engagement"
]

def main():
    # Header with animation effect
    st.markdown('<p class="main-header">✨ LinkedIn Post Generator ✨</p>', unsafe_allow_html=True)
    
    # Animated introduction
    with st.spinner("Loading LinkedIn magic..."):
        time.sleep(0.5)
    
    st.markdown('<p class="subheader">Create engaging LinkedIn posts with AI</p>', unsafe_allow_html=True)
    
    # Create tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Generate Post", "LinkedIn Tips", "About"])
    
    with tab1:
        # Main app functionality
        st.markdown('<div class="highlight">Fill in the options below to generate your LinkedIn post!</div>', unsafe_allow_html=True)
        
        # Create three columns for the dropdowns
        col1, col2, col3 = st.columns(3)
        
        fs = FewShotPosts()
        tags = fs.get_tags()
        
        with col1:
            # Dropdown for Topic (Tags)
            selected_tag = st.selectbox("Topic", options=tags)
            st.info(f"Posts about {selected_tag} get high engagement!")
        
        with col2:
            # Dropdown for Length
            selected_length = st.selectbox("Length", options=["Short", "Medium", "Long"])
            
            # Show appropriate message based on length
            if selected_length == "Short":
                st.info("Quick and impactful!")
            elif selected_length == "Medium":
                st.info("Perfect balance of detail and brevity!")
            else:
                st.info("In-depth content performs well with thought leadership!")
        
        with col3:
            # Dropdown for Language
            selected_language = st.selectbox("Language", options=["English", "Hinglish"])
            if selected_language == "Hinglish":
                st.info("Great for connecting with Indian professionals!")
            else:
                st.info("Classic choice for global reach!")
        
        # Random LinkedIn fact
        import random
        st.markdown(f'<div class="fun-fact">💡 <b>LinkedIn Fact:</b> {random.choice(linkedin_facts)}</div>', unsafe_allow_html=True)
        
        # Generate Button with animation
        if st.button("✨ Generate Amazing Post ✨", use_container_width=True):
            with st.spinner('Crafting your perfect LinkedIn post...'):
                # Add a small delay for animation effect
                time.sleep(1.5)
                # Generate post
                post = generate_post(selected_length, selected_language, selected_tag)
                
                # Success message with animation
                st.success("Post generated successfully!")
                
                # Display the post with styling
                st.markdown('<div class="post-container">', unsafe_allow_html=True)
                st.markdown("### Your LinkedIn Post:")
                st.markdown(post)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Add copy button
                st.text_area("Copy your post from here:", post, height=200)
                
                # Show random writing tip
                st.markdown(f'<div class="fun-fact">✏️ <b>Pro Tip:</b> {random.choice(writing_tips)}</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📊 LinkedIn Post Performance Tips")
        
        # Create expandable sections with tips
        with st.expander("Best Times to Post", expanded=True):
            st.markdown("""
            - **Tuesday - Thursday**: 10am - 1pm (highest engagement)
            - **Wednesday**: 8am - 10am, 12pm - 2pm (best overall day)
            - **Avoid**: Weekends and after 5pm
            """)
            
            # Add a fun progress bars visualization for best days
            st.write("Engagement by Day:")
            col1, col2 = st.columns(2)
            with col1:
                st.progress(0.6, "Monday")
                st.progress(0.85, "Tuesday")
                st.progress(0.95, "Wednesday")
                st.progress(0.8, "Thursday")
            with col2:
                st.progress(0.65, "Friday")
                st.progress(0.3, "Saturday")
                st.progress(0.35, "Sunday")
        
        with st.expander("Content Types That Perform Well"):
            st.markdown("""
            - **Personal stories** and achievements
            - **How-to guides** and educational content
            - **Industry insights** and trend analysis
            - **Polls** and questions that encourage engagement
            - **Carousels** for step-by-step processes
            """)
            
            # Visual performance metrics
            st.write("Content Performance:")
            col1, col2 = st.columns(2)
            with col1:
                st.progress(0.9, "Personal Stories")
                st.progress(0.85, "How-to Content")
                st.progress(0.75, "Industry Insights")
            with col2:
                st.progress(0.7, "Polls & Questions")
                st.progress(0.95, "Carousels")
        
        with st.expander("LinkedIn Algorithm Tips"):
            st.markdown("""
            - LinkedIn favors **native content** over external links
            - **First-hour engagement** is crucial for post reach
            - **Comments** are weighted higher than reactions
            - Using **relevant hashtags** (3-5) increases discoverability
            - **Consistent posting** (2-5 times per week) improves profile visibility
            """)
    
    with tab3:
        st.markdown("### About This App")
        st.markdown("""
        This LinkedIn Post Generator uses advanced AI to create engaging, professional posts tailored to your needs.
        
        **Features:**
        - Topic-specific content generation
        - Multiple length options
        - Language customization
        - Best practices implementation
        
        **How it works:**
        The generator uses few-shot learning techniques with carefully selected examples to produce relevant, engaging LinkedIn content that resonates with your audience.
        """)
        
        # Add a fun animated progress bar
        st.write("Learning more about LinkedIn every day:")
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        st.balloons()

# Run the app
if __name__ == "__main__":
    main()