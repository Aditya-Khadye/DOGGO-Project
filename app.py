mchl
mchl_mndz
Playing Visual Studio Code

Nightfall — 4/27/2025 1:25 PM
I'm idle until classes start again 🧍‍♀️ so i need this final to fill the void
mchl — 4/27/2025 1:26 PM
southern nights on thursday
Nightfall — 4/27/2025 1:40 PM
southern nights is a gay bar
mchl — 4/27/2025 1:44 PM
i’m aware
Nightfall — 4/27/2025 1:44 PM
just making sure lol
mchl — 4/27/2025 1:45 PM
i haven’t been but have heard good things
Nightfall — 4/27/2025 1:45 PM
same, all my girlies love to go
mchl — 4/27/2025 1:45 PM
my straight friend loves that place
i suppose as a straight man i should’ve just said “my boy loves that place”
Nightfall — 4/27/2025 1:46 PM
homeboys love southern nights 💯
Nightfall — 4/27/2025 3:40 PM
@TitanXLord you down? 👀
TitanXLord — 4/27/2025 8:26 PM
myb i just saw this was submitting the final lol why there i thought yall were thinkin lib
mchl — 4/27/2025 8:26 PM
southern nights etter
TitanXLord — 4/27/2025 8:29 PM
what time you thinking
mchl — 4/27/2025 8:29 PM
night time
TitanXLord — 4/27/2025 8:30 PM
like aroudn 10 pm?
mchl — 4/27/2025 8:30 PM
ye like 9/10 type shit
Nightfall — 4/27/2025 8:31 PM
my bedtime is 10:30
mchl — 4/27/2025 8:32 PM
whatever you say buddy
Nightfall — 4/27/2025 8:32 PM
I'll ask my mommy if I can stay out later 🙏
Nightfall — 4/27/2025 8:32 PM
how was the final btw, I'm on the last couple of questions
TitanXLord — 4/27/2025 8:33 PM
not too bad but I think some of the questions were confusing we'll see how he grades it
Nightfall — 4/27/2025 8:34 PM
I almost emailed him asking for clarification but through my email I realized the answer
mchl — 4/27/2025 8:35 PM
thats actually deep as fuck to me i cant lie
writing that down
Nightfall — 4/27/2025 8:38 PM
you might be more drunk than you realize 😅
mchl — 4/27/2025 8:39 PM
nah that shit deep regardless of how inebriated i am
i didnt use autocorrect at all for that btw so how drunk can i possibly be truly
Nightfall — 4/27/2025 8:42 PM
that's true, I couldn't spell ts sober
Nightfall — 4/27/2025 8:51 PM
I think the dataset in the final is the one Beamlak and Jania used for data mining 💀
mchl — 4/27/2025 8:57 PM
mfs just be stealin
TitanXLord — 5/12/2025 7:58 PM
Y’all ready for assignments due before class at midnight lmao
mchl — 5/12/2025 7:59 PM
until i see this man in real life i will NOT be doing work for him 
mchl — 5/14/2025 4:57 PM
hey lauren if you can slide me your laptop at some point so i can try to make a pr and get our code onto the public github so we can put it on our resumes
i lowkey gotta figure out why you cant push stuff
Nightfall — 5/14/2025 9:18 PM
okay yeah, I've been meaning to do that as well
I'll bring it tomorrow
Aditya we're gonna miss you 💔
TitanXLord — 5/14/2025 9:19 PM
I’m gonna be on campus tomorrow lol
Nightfall — 5/14/2025 9:20 PM
i thought u weren't taking the second class
TitanXLord — 5/14/2025 9:30 PM
I’m not but I have some other things to do around
I’ll come over after I’m finished lol
Nightfall — 5/14/2025 10:09 PM
perfect
Nightfall — Yesterday at 10:39 AM
import streamlit as st
from PIL import Image
from doggy import load_model, predict
import asyncio
import sys
Expand
app.py
1 KB
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

# Load the Dog-Breed-120 model and processor
def load_model(model_name="prithivMLmods/Dog-Breed-120"):
Expand
doggy.py
1 KB
Attachment file type: unknown
final_report.ipynb
44.54 KB
Attachment file type: unknown
LICENSE
1.07 KB
Attachment file type: document
Machine Learning Project Proposal.docx
14.82 KB
Machine Learning Project Proposal

Group 70
Team Members:
• Aditya Khadye
• Michael Mendez
Expand
Machine Learning Project Proposal.md
2 KB
Attachment file type: unknown
Project Proposal.ipynb
2.79 KB
# Machine-Learning-Project
Machine Learning project for our course CAP5610. Developed collaboratively by Lauren Suarez, Aditya Khadye, and Michael Mendez. This repository will contain our datasets, models, code implementations, and documentation as we work through our project.
README.md
1 KB
it wouldn't let me send as one big file so here is everything inside of the project
mchl — Yesterday at 10:40 AM
gracias
Nightfall — Yesterday at 10:40 AM
de nada
﻿
import streamlit as st
from PIL import Image
from doggy import load_model, predict
import asyncio
import sys

if sys.platform == "darwin":
    try:
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
    except Exception as e:
        print(f"Failed to set event loop policy: {e}")

# Load model once
def get_model():
    return load_model()

st.title("🐶 Dog Breed Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image')

    processor, model, labels = get_model()
    label, is_dog = predict(img, processor, model, labels)

    if is_dog:
        st.success(f"✅ This is a dog! Breed: {label}")
    else:
        st.warning(f"❌ This does not appear to be a dog. Predicted: {label}")
app.py
1 KB