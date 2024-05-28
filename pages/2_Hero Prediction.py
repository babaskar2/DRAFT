import streamlit as st
import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

st.set_page_config(
    page_title='Hero Recommendation',
    page_icon=r'C:\Users\beezl\OneDrive\Documents\Purwadhika\Modul_3\Portofolio\DRAFT_icon.png'
)

st.title('DRAFT \nDota 2 Recommendation And Feature Tool')

# Hero list
heroes = [
    'Abaddon', 'Alchemist', 'Ancient Apparition', 'Anti-Mage', 'Arc Warden', 'Axe', 'Bane', 'Batrider', 'Beastmaster',
    'Bloodseeker', 'Bounty Hunter', 'Brewmaster', 'Bristleback', 'Broodmother', 'Centaur Warrunner', 'Chaos Knight',
    'Chen', 'Clinkz', 'Clockwerk', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dawnbreaker', 'Dazzle', 'Death Prophet',
    'Disruptor', 'Doom', 'Dragon Knight', 'Drow Ranger', 'Earth Spirit', 'Earthshaker', 'Elder Titan', 'Ember Spirit',
    'Enchantress', 'Enigma', 'Faceless Void', 'Grimstroke', 'Gyrocopter', 'Hoodwink', 'Huskar', 'Invoker', 'Io', 'Jakiro',
    'Juggernaut', 'Keeper of the Light', 'Kunkka', 'Legion Commander', 'Leshrac', 'Lich', 'Lifestealer', 'Lina', 'Lion',
    'Lone Druid', 'Luna', 'Lycan', 'Magnus', 'Marci', 'Mars', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling',
    'Muerta', 'Naga Siren', "Nature's Prophet", 'Necrophos', 'Night Stalker', 'Nyx Assassin', 'Ogre Magi', 'Omniknight',
    'Oracle', 'Outworld Destroyer', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Phoenix', 'Primal Beast', 'Puck',
    'Pudge', 'Pugna', 'Queen of Pain', 'Razor', 'Riki', 'Rubick', 'Sand King', 'Shadow Demon', 'Shadow Fiend', 'Shadow Shaman',
    'Silencer', 'Skywrath Mage', 'Slardar', 'Slark', 'Snapfire', 'Sniper', 'Spectre', 'Spirit Breaker', 'Storm Spirit',
    'Sven', 'Techies', 'Templar Assassin', 'Terrorblade', 'Tidehunter', 'Timbersaw', 'Tinker', 'Tiny', 'Treant Protector',
    'Troll Warlord', 'Tusk', 'Underlord', 'Undying', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Visage', 'Void Spirit',
    'Warlock', 'Weaver', 'Windranger', 'Winter Wyvern', 'Witch Doctor', 'Wraith King', 'Zeus'
]

image_dir = r'C:/Users/beezl/OneDrive/Documents/Purwadhika/Modul_3/Portofolio/Dota 2 Portrait'

hero_images = {hero: os.path.join(image_dir, hero.replace(' ', '_').replace('\'', '').lower().replace('-', '_').lower() + '.png') for hero in heroes}

# Pilih hero
fav_hero = st.selectbox('Choose your hero', heroes)

if fav_hero:
    image_path = hero_images.get(fav_hero)
    if os.path.exists(image_path):
        st.image(image_path, caption=fav_hero)
    else:
        st.error(f"Image for {fav_hero} not found.")
        
# Load data
new_data = pd.read_csv('Portofolio/pages/dota_hero_recommendation.csv')
new_data.reset_index(drop=False, inplace=True)

with st.expander("Hero Information"):
    hero_detail = new_data.drop(columns=['Unnamed: 0', 'index'])
    hero_detail = hero_detail[hero_detail['Name']==fav_hero].T
    hero_detail.columns = ["Based on pro match in patch 7.35c"]
    st.table(hero_detail)

    
if st.button('Give Recommendation') == True:
    def vectorize_column(column):
        count_vect = CountVectorizer(tokenizer=lambda x: x.split(', '))
        count_vect.fit(new_data[column])
        dtm = count_vect.transform(new_data[column])
        return pd.DataFrame(data=dtm.toarray(), columns=count_vect.get_feature_names_out())

    item_feature_matrix_attribute = vectorize_column('Primary Attribute')
    item_feature_matrix_type = vectorize_column('Attack Type')
    item_feature_matrix_roles = vectorize_column('Roles')

    item_feature_matrix = item_feature_matrix_roles.join(item_feature_matrix_attribute).join(item_feature_matrix_type)

    index = new_data[new_data['Name'] == fav_hero].index[0] 

    hero = item_feature_matrix.iloc[index].values.reshape(1, -1)
    recommendations = new_data.copy()
    recommendations['cosine'] = cosine_similarity(hero, item_feature_matrix).reshape(-1)

    recommendations = recommendations[['Name', 'cosine', 'Tier']].sort_values('cosine', ascending=False).reset_index(drop=True)
    recommendations = recommendations[recommendations['Name'] != fav_hero]
    recommendations = recommendations.iloc[:5, [0, 2]].reset_index(drop=True)
    recommendations.index = recommendations.index + 1

    st.table(recommendations)
