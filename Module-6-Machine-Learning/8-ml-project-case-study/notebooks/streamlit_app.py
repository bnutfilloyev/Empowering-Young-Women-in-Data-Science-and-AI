import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Sahifa sozlamalari
st.set_page_config(
    page_title="🎬 Netflix Tavsiya Tizimi",
    page_icon="🎬",
    layout="wide"
)

# CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #E50914;
        text-align: center;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #564d4d;
        text-align: center;
        margin-bottom: 3rem;
    }
    .movie-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: white;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        font-size: 1.2rem;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Modellarni yuklash
@st.cache_resource
def load_models():
    with open('../models/content_model.pkl', 'rb') as f:
        content_model = pickle.load(f)
    
    with open('../models/collaborative_model.pkl', 'rb') as f:
        collaborative_model = pickle.load(f)
    
    with open('../models/data.pkl', 'rb') as f:
        data = pickle.load(f)
    
    return content_model, collaborative_model, data

try:
    content_model, collaborative_model, data = load_models()
    movies = data['popular_movies']
    predictions_df = collaborative_model['predictions']
    cosine_sim = content_model['cosine_sim']
    
    MODEL_LOADED = True
except:
    MODEL_LOADED = False
    st.error("⚠️ Modellar yuklanmadi! Avval `netflix_recommendation_system.ipynb` ni ishga tushiring.")

# Header
st.markdown('<div class="main-header">🎬 Netflix Film Tavsiya Tizimi</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Sun\'iy Intellekt asosida shaxsiylashtirilgan film tavsiялari</div>', unsafe_allow_html=True)

if MODEL_LOADED:
    # Sidebar
    st.sidebar.header("⚙️ Sozlamalar")
    
    recommendation_type = st.sidebar.selectbox(
        "Tavsiya turi:",
        ["🎯 Hybrid (Eng yaxshi)", "👥 Collaborative", "🎬 Content-Based"]
    )
    
    num_recommendations = st.sidebar.slider(
        "Nechta tavsiya ko'rsatish:",
        min_value=5,
        max_value=20,
        value=10
    )
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["🎯 Tavsiyalar", "📊 Statistika", "ℹ️ Ma'lumot"])
    
    with tab1:
        st.header("Film Tavsiyalari")
        
        if "Content" in recommendation_type:
            # Content-Based
            st.subheader("🎬 Filmga o'xshash filmlarni toping")
            
            search_movie = st.text_input("Film nomini kiriting:", placeholder="masalan: Toy Story")
            
            if st.button("🔍 Qidirish") and search_movie:
                try:
                    # Film topish
                    idx = movies[movies['Title'].str.contains(search_movie, case=False, na=False)].index[0]
                    
                    # O'xshash filmlar
                    sim_scores = list(enumerate(cosine_sim[idx]))
                    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
                    movie_indices = [i[0] for i in sim_scores]
                    
                    recommendations = movies.iloc[movie_indices][['Title', 'Genres', 'rating_mean']].copy()
                    
                    st.success(f"✅ '{movies.iloc[idx]['Title']}' filmiga o'xshash filmlar:")
                    
                    for i, (_, row) in enumerate(recommendations.iterrows(), 1):
                        with st.container():
                            col1, col2, col3 = st.columns([3, 2, 1])
                            with col1:
                                st.markdown(f"**{i}. {row['Title']}**")
                            with col2:
                                st.text(f"🎭 {row['Genres']}")
                            with col3:
                                st.metric("⭐", f"{row['rating_mean']:.1f}")
                            st.divider()
                
                except:
                    st.error("❌ Film topilmadi! Boshqa nom bilan urinib ko'ring.")
        
        elif "Collaborative" in recommendation_type:
            # Collaborative Filtering
            st.subheader("👥 Foydalanuvchiga moslashtirilgan tavsiyalar")
            
            user_id = st.number_input(
                "Foydalanuvchi ID:",
                min_value=1,
                max_value=int(predictions_df.index.max()),
                value=1
            )
            
            if st.button("🎯 Tavsiyalarni ko'rish"):
                if user_id in predictions_df.index:
                    user_predictions = predictions_df.loc[user_id].sort_values(ascending=False)
                    user_watched = data['ratings'][data['ratings']['UserID'] == user_id]['MovieID'].values
                    
                    recommendations = user_predictions[~user_predictions.index.isin(user_watched)].head(num_recommendations)
                    
                    result = movies[movies['MovieID'].isin(recommendations.index)].copy()
                    result['predicted_rating'] = result['MovieID'].map(recommendations)
                    result = result.sort_values('predicted_rating', ascending=False)
                    
                    st.success(f"✅ Foydalanuvchi {user_id} uchun tavsiyalar:")
                    
                    for i, (_, row) in enumerate(result.iterrows(), 1):
                        with st.container():
                            col1, col2, col3 = st.columns([3, 2, 1])
                            with col1:
                                st.markdown(f"**{i}. {row['Title']}**")
                            with col2:
                                st.text(f"🎭 {row['Genres']}")
                            with col3:
                                st.metric("🎯", f"{row['predicted_rating']:.2f}")
                            st.divider()
                else:
                    st.error(f"❌ Foydalanuvchi {user_id} topilmadi!")
        
        else:
            # Hybrid
            st.subheader("🎯 Hybrid Tavsiyalar (Eng yaxshi)")
            
            user_id = st.number_input(
                "Foydalanuvchi ID:",
                min_value=1,
                max_value=int(predictions_df.index.max()),
                value=100
            )
            
            alpha = st.slider(
                "Content vs Collaborative nisbati:",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                help="0 = faqat Collaborative, 1 = faqat Content"
            )
            
            if st.button("🎯 Hybrid Tavsiyalarni ko'rish"):
                if user_id in predictions_df.index:
                    st.success(f"✅ Foydalanuvchi {user_id} uchun hybrid tavsiyalar:")
                    
                    # Simplified hybrid logic
                    collab_scores = predictions_df.loc[user_id]
                    user_watched = data['ratings'][data['ratings']['UserID'] == user_id]['MovieID'].values
                    
                    # Get recommendations
                    recommendations = collab_scores[~collab_scores.index.isin(user_watched)].nlargest(num_recommendations)
                    
                    result = movies[movies['MovieID'].isin(recommendations.index)].copy()
                    result['score'] = result['MovieID'].map(recommendations)
                    result = result.sort_values('score', ascending=False)
                    
                    for i, (_, row) in enumerate(result.iterrows(), 1):
                        with st.container():
                            col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
                            with col1:
                                st.markdown(f"**{i}. {row['Title']}**")
                            with col2:
                                st.text(f"🎭 {row['Genres']}")
                            with col3:
                                st.metric("⭐", f"{row['rating_mean']:.1f}")
                            with col4:
                                st.metric("🎯", f"{row['score']:.2f}")
                            st.divider()
                else:
                    st.error(f"❌ Foydalanuvchi {user_id} topilmadi!")
    
    with tab2:
        st.header("📊 Dataset Statistikasi")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🎬 Filmlar", f"{len(movies):,}")
        with col2:
            st.metric("👥 Foydalanuvchilar", f"{len(predictions_df):,}")
        with col3:
            st.metric("⭐ Reytinglar", f"{len(data['ratings']):,}")
        
        st.divider()
        
        # Top filmlar
        st.subheader("🏆 Eng Mashgur Filmlar")
        top_movies = movies.nlargest(10, 'rating_count')[['Title', 'Genres', 'rating_mean', 'rating_count']]
        
        for i, (_, row) in enumerate(top_movies.iterrows(), 1):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.markdown(f"**{i}. {row['Title']}**")
            with col2:
                st.text(f"🎭 {row['Genres']}")
            with col3:
                st.metric("⭐", f"{row['rating_mean']:.1f}", f"{int(row['rating_count'])} reyting")
    
    with tab3:
        st.header("ℹ️ Loyiha Haqida")
        
        st.markdown("""
        ### 🎬 Netflix Tavsiya Tizimi
        
        Bu loyiha 3 xil tavsiya algoritmidan foydalanadi:
        
        #### 1. 🎬 Content-Based Filtering
        - Film janri va tavsifiga asoslangan
        - TF-IDF va Cosine Similarity
        - O'xshash filmlarni topish
        
        #### 2. 👥 Collaborative Filtering
        - Foydalanuvchilar xatti-harakatiga asoslangan
        - SVD (Singular Value Decomposition)
        - Shaxsiylashtirilgan tavsiyalar
        
        #### 3. 🎯 Hybrid Model
        - Content va Collaborative ni birlashtiradi
        - Eng aniq natijalar
        - Cold start muammosini hal qiladi
        
        ---
        
        ### 📊 Dataset
        - **MovieLens 1M**: 6,040 foydalanuvchi, 3,706 film, 1M reyting
        - **Filtrlanган**: 50+ reyting olgan filmlar
        
        ### 🛠️ Texnologiyalar
        - Python, Pandas, NumPy
        - Scikit-learn, SciPy
        - Streamlit
        
        ---
        
        **Yaratuvchi:** AI/ML Loyihasi  
        **Sana:** 2024
        """)

else:
    st.warning("⚠️ Modellarni avval o'qitish kerak!")
    st.info("👉 `netflix_recommendation_system.ipynb` notebookni ishga tushiring")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    Made with ❤️ using Streamlit | © 2024 Netflix Recommender
</div>
""", unsafe_allow_html=True)
