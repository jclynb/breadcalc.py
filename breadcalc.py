import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets6.lottiefiles.com/packages/lf20_HKkJc2.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json, speed=1, height=200, key="initial")

#st.set_page_config(layout="wide")

st.title("Baker's Percentage Calculator")
st.subheader('A Web App by [Jaclyn Baughman](http://jclyn.info)')


st.markdown(":bread: Let's make bread! All we need is four ingredients and some arithmetic. To use this calculator, choose how much flour you want to use, your hydration target, and your amount of starter/yeast.")

st.markdown("First time user? Read below! :arrow_down: ")

st.header("Sourdough Calculator")

st.markdown("First time making sourdough? Tartine’s recipe is 1000g flour (900g white + 100g whole wheat), 200g leaven, and 75% hydration. This recipe makes two loaves.")

def sourmath(flour, hydration, leaven):
    starter = leaven/2 #leaven is equal parts water and flour
    flour_total = flour + starter
    salt = round(flour_total * .02)
    water = round((flour_total)*(hydration) - starter)
    total_water = round((flour_total)*hydration)


    flour_percent = flour/flour
    salt_percent = salt/flour_total
    leaven_perecent = starter/flour_total
    water_percent = water/flour_total
    total_water_percent = total_water/flour_total

    weights = "{ingredient:.0f}g"
    percents = "{ingredient:.0%}"

    data_table = {'Total Flour': [weights.format(ingredient=flour_total), percents.format(ingredient=flour_percent)], 'Salt': [weights.format(ingredient=salt), percents.format(ingredient=salt_percent)], 'Leaven': [weights.format(ingredient=leaven), percents.format(ingredient=leaven_perecent)], 'Water': [weights.format(ingredient=water), percents.format(ingredient=water_percent)], 'Total Water': [weights.format(ingredient=total_water), percents.format(ingredient=total_water_percent)]}
    dataframe = pd.DataFrame(data_table, index=['Weight', "Percent"])
    return dataframe
    #return "Flour: " + str(flour) + "g", "Salt: " + str(salt) + "g",  "Leaven: " + str(leaven) + "g",  "Water: " + str(water) + "g"



flour = st.slider("Flour (g)", 200, 1000, 200, 25)
hydration = st.slider("Hydration Precentage", .5, 1.20, .5, .01)
leaven = st.slider("Leaven/Starter (g) (half water half flour blend)", 100, 500, 100, 10)

st.table(sourmath(flour, hydration, leaven))
st.markdown(
    """
    - The percentage for the leaven is the amount of flour in the leaven divided by the total flour in the recipe.
    """
    )

st.header("Instant Yeast Bread Calculator")
st.markdown("By adding commerical yeast to flour, water, and salt, you can make a wide variety of doughs! Pizza, focaccia, white and whole wheat breads--you name it!")
#wwheat = st.radio("Adding Whole Wheat?", ("No Whole Wheat", "Less than 50% Whole Wheat", "More than 50% Whole Wheat"))

def breadmath(flour2, hydration2, yeast):
    salt = round(flour2 * .02)
    water = round(flour2*hydration2)   

    flour_percent = (flour2/flour2)
    salt_percent = (salt/flour2)
    yeast_percent = (yeast/flour2)
    water_percent = (water/flour2)

    weights = "{ingredient:.0f}g"
    percents = "{ingredient:.0%}"

    data_table2 = {'Flour': [weights.format(ingredient=flour2), percents.format(ingredient=flour_percent)], 'Salt': [weights.format(ingredient=salt), percents.format(ingredient=salt_percent)], 'Yeast': [weights.format(ingredient=yeast), percents.format(ingredient=yeast_percent)], 'Water': [weights.format(ingredient=water), percents.format(ingredient=water_percent)]}
    dataframe2 = pd.DataFrame(data_table2, index=['Weight', "Percent"])
    return dataframe2

flour2 = st.slider("Flour (g)", 100, 1000, 100, 25)
hydration2 = st.slider("Hydration Precentage", .5, 1.0, .5, .1)
yeast = st.slider("Instant Dried Yeast (g) (genearlly around 1/2-1tsp)", 1.0, 5.0, 1.0, .5)

st.table(breadmath(flour2, hydration2, yeast))

st.header("Pre-ferment Bread Calculator")
st.markdown("Want to make baguettes? Make a poolish by combining flour, water, and instant dried yeast and let sit overnight.")

def poolmath(flour3, hydration3, poolish):
    halfpool = poolish/2
    total_flour3 = flour3 + halfpool
    salt = round(total_flour3 * .02)
    water = round((total_flour3*hydration3) - halfpool)  
    total_water = round(total_flour3*hydration3) 

    flour_percent = (flour3/flour3)
    salt_percent = (salt/total_flour3)
    poolish_percent = (halfpool/total_flour3)
    water_percent = (water/total_flour3)
    total_water_percent = (total_water/total_flour3)

    weights = "{ingredient:.0f}g"
    percents = "{ingredient:.0%}"

    data_table3 = {'Total Flour': [weights.format(ingredient=total_flour3), percents.format(ingredient=flour_percent)], 'Salt': [weights.format(ingredient=salt), percents.format(ingredient=salt_percent)], 'Poolish': [weights.format(ingredient=poolish), percents.format(ingredient=poolish_percent)], 'Water': [weights.format(ingredient=water), percents.format(ingredient=water_percent)], 'Total Water': [weights.format(ingredient=total_water), percents.format(ingredient=total_water_percent)]}
    dataframe3 = pd.DataFrame(data_table3, index=['Weight', "Percent"])
    return dataframe3

flour3 = st.slider("Flour (g)", 100, 1000, 100, 10)
hydration3 = st.slider("Hydration Precentage", .55, 1.0, .55, .01)
poolish = st.slider("Poolish (g)", 100, 1000, 100, 10)

st.table(poolmath(flour3, hydration3, poolish))
st.markdown(
    """
    - The percentage for the poolish is the amount of flour in the poolish divided by the total flour in the recipe.
    """
    )

st.subheader('Bread Notes')
st.markdown(
    """
     - **Hydration + flour types:** whole wheat flour is very absorbant. Rye flours are genearlly less absorbant, but with a wide variety of white/medium/dark rye (& pumpernickle!) it's best to learn how your flours affect hydration and fermentaion before incorporating into your breads.  Higher ratios of whole wheat to white flour will need closer to 80% hydration. For pure white flour breads, start around 70% and add about 5-10% hydration when starting to incorporate whole wheat.
    """
    )

st.markdown(
    """
    - **Hydration outcomes:** the higher the hydration of the dough, the more air bubbles, rise, and chewiness you'll see (though the dough will also be sticky-er and wetter). But add too much water and you'll end up with a soupy mess. Then again, add too little and you’ll end up with a dense flying saucer...
    Setting your hydration will depend on what kind of end result you're looking for and what kind of flours you are using. Having a lower hydration means a stiffer and easier to work with dough, which might be great for shaping pizza, but may not produce those big airy bubbles you typically look for in sourdough.
    """
)

st.markdown(
    """
    - **Salt choice:** I set the default salt percentage to 2%. You can add a little over or a little under, but don't stray too far from the 2% mark or you'll end up hurting the yeast activity/rise of your bread (yeasts hate salt!)
    """
)

st.markdown(
    """
    - **Why is flour always 100%?:** Bakers use flour as the standard weight to divide our other ingredients against. This means our total flour will always be 100%, and we will always divide by that number. So a bread with 600g of water and 1000g of flour will be 60% hydration. With sourdough and pre-fermented doughs, we add a mixture that has a 50/50 water-to-flour ratio (starter/leaven/poolish). This ingredient affects our hydration percentage, and needs to be added to our total water and total flour calculation.)
    """
)