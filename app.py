import streamlit as st
import pandas as pd
import numpy as np

# Broadcast/ News libraries
from youtube_transcript_api import YouTubeTranscriptApi
from newsapi import NewsApiClient

#### User puts in youtube link, downloads video and then transcribes? ####
### Use this library: https://pypi.org/project/youtube-transcript-api/ ###

### Key Q: Can we download channel 4 and/ or iplayer content? ###

st.title('Political News Scanner')
st.header('Campaign Lab Prototype - July 2022')

news_type = st.radio('Which news do you want to scan?', ['None', 'Print', 'Broadcast - Video'])

if news_type == 'None':
    pass
elif news_type == 'Print':
    st.text('Not yet built! Could scan news for mentions and return sentiment + topic visuals?')
    # News API
    # Init
    # newsapi = NewsApiClient(api_key='API_KEY')

    # news_option = st.radio('What headlines do you want?', ['Labour', 'Keir Starmer'])
    # if news_option == 'Labour':
    #     top_headlines = newsapi.get_top_headlines(q='labour',
    #                                         sources='bbc-news,the-verge',
    #                                         category='business',
    #                                         language='en',
    #                                         country='uk')
                                        
    # else: 

    #     top_headlines = newsapi.get_top_headlines(q='labour',
    #                                         sources='bbc-news,the-verge',
    #                                         category='business',
    #                                         language='en',
    #                                         country='uk')

    # print(top_headlines)
    
else:
    upload_format = st.radio(
        'How do you want to select video to analyse?',
        ('Youtube Link', 'Upload Video'))

    if upload_format == 'Upload Video':
        st.file_uploader('Upload video to transcribe ⬇')

        # Video File Analyser

    else:
        st.text('Transcripts should be available for most but not all C4 and BBC videos on Youtube.')
        try:
            video_id = st.text_input('Youtube Video ID (the bit after v= in the url). E.g. VkKmPQ1AFks')
            if video_id:
                video_data = YouTubeTranscriptApi.get_transcript(video_id)
                text_chunks = []
                for chunk in video_data:
                    text_chunks.append(chunk['text'])
                text_output = st.radio(
                'What analysis do you want?',
                ('Full Transcript', 'Labour Mentions', 'Search'))
                # Other options: 'Sentences with other parties', 'Sentences with other parties', Sentences with politicians or SEARCH FOR KEYWORD
                if text_output == 'Full Transcript':
                    for sentence in text_chunks:
                        st.text(sentence)
                elif text_output == 'Sentences with Labour': # Get 3 chunk sequence containing 'labour'
                    labour_indices = [i for i, s in enumerate(text_chunks) if 'labour' in s]
                    for i, text in enumerate(text_chunks):
                        if i in labour_indices:
                            st.subheader(f'Labour Mention Context:')
                            # labour_context_string = ' '.join(text_chunks[i-1:i+6])
                            labour_context_sequence = text_chunks[i-1:i+6]
                            for labour_str in labour_context_sequence:
                                st.text(labour_str)
                else: 
                    search_word = st.text_input('word to search')
                    if search_word:
                        search_word_indices = [i for i, s in enumerate(text_chunks) if search_word in s]
                        for i, text in enumerate(text_chunks):
                            if i in search_word_indices:
                                st.subheader(f'Search Word Mention context:')
                                # labour_context_string = ' '.join(text_chunks[i-1:i+6])
                                search_context_sequence = text_chunks[i-1:i+6]
                                for search_str in search_context_sequence:
                                    st.text(search_str)

        except:
            st.text('There are no transcripts available for this youtube video')


# st.text('Product Qs')
# st.text('Q1: Do you want aggregate visuals on Topics?')
# st.text('Q2: Do you want aggregate visuals sentiment?')
# st.text('Q3: Do you want aggregate visuals on num times Labour was mentioned?')
# st.text('Q3: Do you want aggregate visuals on Labour mps mentioned?')