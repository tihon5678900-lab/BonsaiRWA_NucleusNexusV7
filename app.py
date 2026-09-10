import streamlit as st
from ai_appraiser import appraise_bonsai
from blockchain import mint_rwa_nft
import json, os

st.set_page_config(page_title="BonsaiRWA V7", page_icon="🌳", layout="wide")
st.title("🌳 BonsaiRWA Nucleus Nexus V7")
st.caption("127 Mai Vang RWA on Base 8453 - AI Nebius + NVIDIA Nemotron")

uploaded = st.file_uploader("Upload Mai Vang", type=["jpg","png"])
if uploaded:
    st.image(uploaded, use_container_width=True)
    if st.button("🚀 Appraise", type="primary"):
        with st.spinner("Nebius AI dang dinh gia..."):
            result = appraise_bonsai(uploaded, "Mai Vang")
        st.success("✅ Done!")
        col1,col2,col3 = st.columns(3)
        col1.metric("Value", f"${result['value_usd']:,}")
        col2.metric("Age", f"{result['age_years']} years")
        col3.metric("Rarity", f"{result['rarity']}/100")
        st.json(result)

if st.button("⛓️ Mint on Base 8453"):
    tx = mint_rwa_nft("0xDemo", {"value":15000})
    st.success(f"Minted! {tx}")