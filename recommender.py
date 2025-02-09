import polars as pl
import faiss
from sentence_transformers import SentenceTransformer
import torch
import streamlit as st


@st.cache_resource      #don't have to reload model every time, costly
def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2', 
                              device="cuda" if torch.cuda.is_available() else "cpu")
    return model.half()


def vectorization_of_input(input_df, n_matches=5):

    embedding = model.encode(
        [input_df["embedding_text"].item()], 
        convert_to_tensor=False
    ).astype('float32')


    D, I = index.search(embedding, n_matches)

    return I


# Similarity search

def similarity_search(embeddings, df):
    # Get indices from FAISS search results (I)
    closest_embeddings = embeddings.flatten().tolist()
    

    # Use Polars' gather() for index-based selection
    top_matches = df.select(
        pl.col("embedding_text").gather(closest_embeddings)
    ).to_series().to_numpy()

    return top_matches

def print_matches(top_matches):

    for match in top_matches:
        title, rest = match.split("Year:")
        year, rest = rest.split("Genre:")
        genre, rest = rest.split("Tags:")
        tags, rating = rest.split("Ratings:")

        st.markdown(f"""##### {title[7:-2]} ({year[1:-3]})  
{genre[:-3]}  
Rating: {float(rating):.2f}  
Tags: {tags[:-2]}  
  
  
        """)
        
        st.write()

###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### 

# Initialization

index = faiss.read_index("index-vdb")

model = load_model()

df = pl.read_csv("clean_data.csv")

all_genres = ['Action', 'Adventure', 'Fantasy', 
            'Mystery', 'Animation', 'Romance', 
            'Children', 'Comedy', 'Documentary', 
            'Drama', 'Western', 'Sci-Fi', 
            'Crime', 'Thriller', 'Film-Noir', 
            'War', 'Horror', 'Musical', 'IMAX']

unique_tags = pl.read_csv("normalized_tags.csv")
all_tags = unique_tags["cleaned_tags"].to_list()

###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### ###### 


# UI


st.title("Movie Recommender")


with st.form("my_form", border=False):
    title = st.text_input("Title")

    genres = st.multiselect(
        "Genres",
        all_genres,
        ["Action", "Documentary"],
    )

    tags = st.multiselect(
        "Tags",
        all_tags,
        ["unexpectedly good", "usa propaganda"],
    )
    

    left, center, right = st.columns(3)
    with left:
        year = st.number_input("Year", value=2007, min_value=1888, max_value=2024, step=1)
    with center:
        rating = st.number_input("Average rating", value=4.0, min_value=3.0, max_value=5.0, step=0.1, format="%0.1f")
    with right:
        n_recommendations = st.number_input("Amount of recommendations",step=1, value=5)


    input_df = pl.DataFrame({
        "embedding_text" : [title + "," + str(year) + "," +  ", ".join(genres) + "," +  ", ".join(tags)] #+ "," + str(rating) 
    })


    submitted = st.form_submit_button("Submit")
    st.divider()
    if submitted:
        embeddings = vectorization_of_input(input_df, n_recommendations)
        top_matches = similarity_search(embeddings, df)
        print_matches(top_matches)

