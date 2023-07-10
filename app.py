import pickle
import streamlit as st
import numpy as np


# Helper function for giving the recommended books and the image url of the books
def image_fetcher(recommendation):
    book_names = []
    book_ids_index = []
    book_images = []

    # For finding the names of books from the index of book
    for book_index in range(len(recommendation)):
        book_names.append(books_pivot_table.index[recommendation[book_index]])

    # Finding the books ids from the name of the books in main table
    for name in book_names[0]:
        ids = np.where(final_books_rating['title'] == name)[0][0]
        book_ids_index.append(ids)

    # Finding the images url with the help of books ids
    for index in book_ids_index:
        img_url = final_books_rating.iloc[index]['img_url']
        book_images.append(img_url)

    return book_images


def book_recommender(name_of_book):
    recommended_book_list = []
    book_id = np.where(books_pivot_table.index == name_of_book)[0][0]
    distance, recommendation = model.kneighbors(books_pivot_table.iloc[book_id, :].values.reshape(1, -1))
    img_url = image_fetcher(recommendation)
    for i in range(len(recommendation)):
        suggested_books = books_pivot_table.index[recommendation[i]]
        for j in suggested_books:
            recommended_book_list.append(j)
    return recommended_book_list, img_url


# Loading important data using pickle.load()
model = pickle.load(open('model.pkl', 'rb'))
available_books_name_list = pickle.load(open('available_books_name_list.pkl', 'rb'))
final_books_rating = pickle.load(open('final_books_rating.pkl', 'rb'))
books_pivot_table = pickle.load(open('books_pivot_table.pkl', 'rb'))

# recommended_books, image_url = book_recommender("2nd Chance")

# All the webpage code
# st.header("Welcome to the Books Recommender System")
# book_selected_by_user = st.selectbox("Select or Type the Book Name", available_books_name_list)
#
# if st.button('Recommend Me'):
#     recommended_books, image_url = book_recommender(book_selected_by_user)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.image(image_url[1])
#         st.text(recommended_books[1])
#     with col2:
#         st.image(image_url[2])
#         st.text(recommended_books[2])
#     with col3:
#         st.image(image_url[3])
#         st.text(recommended_books[3])
#     with col4:
#         st.image(image_url[4])
#         st.text(recommended_books[4])
#     with col5:
#         st.image(image_url[5])
#         st.text(recommended_books[5])

# Define your custom color scheme
background_color = "#000000"  # black
header_footer_color = "#FFA500"  # orange
selectbox_button_color = "#FF8C00"  # orange shade
accent_color = "#FFFFFF"  # white

# Set page background color
st.markdown(
    f"""
    <style>
    body {{
        background-color: {background_color};
        color: {accent_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set header/footer background color
st.markdown(
    f"""
    <style>
    .stApp footer, .stApp header {{
        background-color: {header_footer_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Welcome to the Books Recommender System")

# Set selectbox and button color
st.markdown(
    f"""
    <style>
    .st-selectbox, .stButton button {{
        background-color: {selectbox_button_color};
        color: {accent_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

book_selected_by_user = st.selectbox("Select or Type the Book Name", available_books_name_list)

# Set button color
if st.button('Recommend Me'):
    st.markdown(
        f"""
        <style>
        .stButton button {{
            background-color: {selectbox_button_color};
            color: {accent_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    recommended_books, image_url = book_recommender(book_selected_by_user)
    col1, col2, col3, col4, col5 = st.columns(5)

    # Set image and text color
    st.markdown(
        f"""
        <style>
        .st-image img {{
            border: 3px solid {selectbox_button_color};
            border-radius: 5px;
        }}
        .st-text {{
            color: {accent_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    with col1:
        st.image(image_url[1])
        st.text(recommended_books[1])

    with col2:
        st.image(image_url[2])
        st.text(recommended_books[2])

    with col3:
        st.image(image_url[3])
        st.text(recommended_books[3])

    with col4:
        st.image(image_url[4])
        st.text(recommended_books[4])

    with col5:
        st.image(image_url[5])
        st.text(recommended_books[5])
