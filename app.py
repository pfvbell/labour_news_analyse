import streamlit as st
import pandas as pd
import numpy as np
from youtube_transcript_api import YouTubeTranscriptApi

#### User puts in youtube link, downloads video and then transcribes? ####
### Use this library: https://pypi.org/project/youtube-transcript-api/ ###

### Key Q: Can we download channel 4 and/ or iplayer content? ###

st.title('Campaign Lab Broadcast News Analyser')
st.header('Prototype - July 2022')


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
            ('Full Transcript', 'Sentences with Labour', 'search'))
            # Other options: 'Sentences with other parties', 'Sentences with other parties', Sentences with politicians or SEARCH FOR KEYWORD
            if text_output == 'Full Transcript':
                for sentence in text_chunks:
                    st.text(sentence)
            elif text_output == 'Sentences with Labour': # Get 3 chunk sequence containing 'labour'
                labour_indices = [i for i, s in enumerate(text_chunks) if 'labour' in s]
                for i, text in enumerate(text_chunks):
                    if i in labour_indices:
                        st.subheader(f'Labour Mention context:')
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



